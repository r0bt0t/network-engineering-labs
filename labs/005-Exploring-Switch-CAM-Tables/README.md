# Lab 005 - Exploring Switch CAM Tables

<table>
<tr>
<td colspan="2" valign="top">

# Objective

* ### Verify the Layer 3 addressing and Layer 2 identity of two endpoints.
* ### Generate traffic between PCs on the same VLAN so the switch can learn their MAC addresses.
* ### Inspect the switch CAM/MAC address table and identify which MAC addresses appear on which ports.
* ### Clear dynamic MAC address entries and prove that the switch relearns them automatically when traffic flows again.
* ### Build confidence with the relationship between ARP, MAC addresses, switchports and traffic forwarding.

</td>
</tr>

<tr>
<td valign="top">
<img src="Images/Topology2.png">
</td>

<td valign="top">
<img src="Images/networking_image_17.png">
</td>

</tr>
</table>

---

## Scenario

This lab focuses on how a switch learns where devices are connected.

The aim was to generate traffic between two PCs, observe the resulting MAC address entries on `Switch6`, clear the dynamic entries, then generate traffic again to watch the switch relearn them.

This is one of those small labs that feels simple at first, but it is very useful because it shows what the switch is doing in the background every time hosts communicate.

The main workflow was:

```text
Verify endpoint IP/MAC details → Generate traffic → Inspect CAM table → Clear dynamic entries → Regenerate traffic → Confirm relearning
```

---

## Devices Used

| Device       | Role                                                       |
| ------------ | ---------------------------------------------------------- |
| `PC1`        | Endpoint using `192.168.1.50/24`                           |
| `PC2`        | Endpoint using `192.168.1.51/24`                           |
| `Switch6`    | Switch used to inspect, clear and repopulate the CAM table |
| `CoreSwitch` | Upstream switch/uplink neighbour                           |
| `OpsServer`  | Supporting lab device                                      |

---

## Addressing and MAC Summary

| Device                | IP Address     | MAC Address                            | Switch Port     | VLAN |
| --------------------- | -------------- | -------------------------------------- | --------------- | ---: |
| `PC1`                 | `192.168.1.50` | `52:54:00:5E:61:BD` / `5254.005e.61bd` | `Switch6 Et0/1` |   10 |
| `PC2`                 | `192.168.1.51` | `52:54:00:EB:72:52` / `5254.00eb.7252` | `Switch6 Et0/2` |   10 |
| Uplink/static entries | N/A            | `40a6.b77d.aa01`, `40a6.b77d.bb02`     | `Switch6 Et0/0` |   99 |

---

## Final Learning Topology

```text
             CoreSwitch / Uplink
                    |
                    | VLAN 99 static entries
                    |
              Switch6 Et0/0
              /           \
             /             \
   Et0/1 PC1               Et0/2 PC2
   192.168.1.50            192.168.1.51
   5254.005e.61bd          5254.00eb.7252
```

---

# Configuration and Investigation Steps

---

## Step 1 - Verify PC1 IP and MAC Details

```bash
ifconfig eth0
route -n
```

### Observed Output

```text
eth0      Link encap:Ethernet  HWaddr 52:54:00:5E:61:BD  
          inet addr:192.168.1.50  Bcast:192.168.1.255  Mask:255.255.255.0
```

```text
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 eth0
```

### Explanation

I first confirmed that `PC1` had the expected IP address and default gateway.

Important details:

| Item            | Value               |
| --------------- | ------------------- |
| IP address      | `192.168.1.50`      |
| Subnet mask     | `255.255.255.0`     |
| Default gateway | `192.168.1.1`       |
| MAC address     | `52:54:00:5E:61:BD` |

Cisco switches display MAC addresses in dotted format, so the switch would show this as:

```text
5254.005e.61bd
```

This meant I knew exactly what MAC address to look for later in the CAM table.

---

## Step 2 - Verify PC2 IP and MAC Details

```bash
ifconfig eth0
route -n
```

### Observed Output

```text
eth0      Link encap:Ethernet  HWaddr 52:54:00:EB:72:52  
          inet addr:192.168.1.51  Bcast:192.168.1.255  Mask:255.255.255.0
```

```text
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 eth0
```

### Explanation

I repeated the same checks on `PC2`.

Important details:

| Item            | Value               |
| --------------- | ------------------- |
| IP address      | `192.168.1.51`      |
| Subnet mask     | `255.255.255.0`     |
| Default gateway | `192.168.1.1`       |
| MAC address     | `52:54:00:EB:72:52` |

In Cisco dotted format, this becomes:

```text
5254.00eb.7252
```

At this point, both endpoints were confirmed to be in the same subnet and ready for local communication.

---

## Step 3 - Generate Traffic from PC1 to PC2

```bash
ping 192.168.1.51
```

### Observed Output

```text
PING 192.168.1.51 (192.168.1.51): 56 data bytes
64 bytes from 192.168.1.51: seq=25 ttl=64 time=0.844 ms
64 bytes from 192.168.1.51: seq=26 ttl=64 time=0.923 ms
64 bytes from 192.168.1.51: seq=27 ttl=64 time=0.862 ms
64 bytes from 192.168.1.51: seq=28 ttl=64 time=0.830 ms
64 bytes from 192.168.1.51: seq=29 ttl=64 time=0.914 ms
^C
--- 192.168.1.51 ping statistics ---
30 packets transmitted, 30 packets received, 0% packet loss
round-trip min/avg/max = 0.811/0.909/1.541 ms
```

### Explanation

The ping from `PC1` to `PC2` proved that the two hosts could communicate.

It also forced ARP resolution to occur. Before `PC1` can send traffic to `PC2`, it needs to know the destination MAC address for `192.168.1.51`.

This is useful because the ARP exchange and ICMP traffic give the switch something to learn from.

---

## Step 4 - Confirm PC1 Learned PC2’s MAC Address

```bash
arp -a
```

### Observed Output

```text
? (192.168.1.51) at 52:54:00:eb:72:52 [ether] on eth0
```

### Explanation

This confirmed that `PC1` had learned the MAC address for `PC2`.

```text
192.168.1.51 → 52:54:00:eb:72:52
```

This matched the MAC address seen earlier on `PC2`.

So at the endpoint level, ARP was working correctly.

---

## Step 5 - Access Switch6 and Attempt to View the MAC Table

```bash
Switch6>enable
Switch6#configure terminal
Switch6(config)#show mac address-table
```

### Observed Output

```text
                  ^
% Invalid input detected at '^' marker.
```

### Explanation

I accidentally tried to run a `show` command while in global configuration mode.

Most `show` commands need to be run from privileged EXEC mode:

```text
Switch6#
```

not from:

```text
Switch6(config)#
```

The fix was simply to exit back to privileged EXEC mode.

---

## Step 6 - View the Switch6 CAM Table

```bash
end
show mac address-table
```

### Observed Output

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.005e.61bd    DYNAMIC     Et0/1
  10    5254.00eb.7252    DYNAMIC     Et0/2
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  10    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0
```

### Explanation

This showed the expected dynamic MAC entries:

| MAC Address      | Type    | Port    | Meaning |
| ---------------- | ------- | ------- | ------- |
| `5254.005e.61bd` | Dynamic | `Et0/1` | `PC1`   |
| `5254.00eb.7252` | Dynamic | `Et0/2` | `PC2`   |

This proved that `Switch6` had learned the two endpoint MAC addresses from traffic arriving on the relevant ports.

The table also included static MAC entries, which were not removed by clearing dynamic entries later.

---

## Step 7 - Clear Dynamic CAM Table Entries

```bash
clear mac address-table dynamic
```

### Explanation

This command clears dynamically learned MAC addresses from the switch CAM table.

Dynamic entries are learned automatically from traffic. Static entries are manually configured or pre-existing and are not removed by this command.

This is a useful way to demonstrate that the switch is not “magically” aware of devices. It learns where they are based on source MAC addresses in frames it receives.

---

## Step 8 - Confirm Dynamic Entries Were Removed

```bash
show mac address-table
```

### Observed Output

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  10    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0
```

### Explanation

The dynamic entries for PC1 and PC2 were gone.

Before clearing, the table included:

```text
5254.005e.61bd
5254.00eb.7252
```

After clearing, only static entries remained.

That confirmed the `clear mac address-table dynamic` command worked as expected.

---

## Step 9 - Regenerate Traffic with a Controlled Ping

```bash
ping -c 5 192.168.1.51
```

### Observed Output

```text
PING 192.168.1.51 (192.168.1.51): 56 data bytes
64 bytes from 192.168.1.51: seq=0 ttl=64 time=0.823 ms
64 bytes from 192.168.1.51: seq=1 ttl=64 time=0.927 ms
64 bytes from 192.168.1.51: seq=2 ttl=64 time=0.786 ms
64 bytes from 192.168.1.51: seq=3 ttl=64 time=0.871 ms
64 bytes from 192.168.1.51: seq=4 ttl=64 time=0.827 ms

--- 192.168.1.51 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.786/0.846/0.927 ms
```

### Explanation

This ping was limited to 5 packets using:

```bash
-c 5
```

That was a cleaner test than the earlier continuous ping, which had to be manually stopped with `Ctrl+C`.

The successful result proved that PC1 and PC2 could still communicate after the switch CAM table was cleared.

---

## Step 10 - Confirm the Switch Relearned the Dynamic Entries

```bash
show mac address-table
```

### Observed Output

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.005e.61bd    DYNAMIC     Et0/1
  10    5254.00eb.7252    DYNAMIC     Et0/2
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  10    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0
```

### Explanation

The dynamic entries returned after traffic was generated again.

This proved the main learning point of the lab:

```text
A switch learns MAC addresses dynamically by inspecting the source MAC address of frames entering each port.
```

After clearing the table, the switch had to relearn PC1 and PC2 when traffic flowed again.

---

# Verification

## Endpoint Verification

| Device | IP Address        | MAC Address         | Default Gateway |
| ------ | ----------------- | ------------------- | --------------- |
| `PC1`  | `192.168.1.50/24` | `52:54:00:5E:61:BD` | `192.168.1.1`   |
| `PC2`  | `192.168.1.51/24` | `52:54:00:EB:72:52` | `192.168.1.1`   |

---

## CAM Table Verification

### Before Clearing

| MAC Address      | Type    | Port    | Device                  |
| ---------------- | ------- | ------- | ----------------------- |
| `5254.005e.61bd` | Dynamic | `Et0/1` | `PC1`                   |
| `5254.00eb.7252` | Dynamic | `Et0/2` | `PC2`                   |
| `5a5a.1c1c.0d0d` | Static  | `Et0/1` | Static lab entry        |
| `7c7c.b2b2.2020` | Static  | `Et0/2` | Static lab entry        |
| `40a6.b77d.aa01` | Static  | `Et0/0` | Uplink/static lab entry |
| `40a6.b77d.bb02` | Static  | `Et0/0` | Uplink/static lab entry |

### After Clearing Dynamic Entries

| MAC Address      | Type   | Port    |
| ---------------- | ------ | ------- |
| `5a5a.1c1c.0d0d` | Static | `Et0/1` |
| `7c7c.b2b2.2020` | Static | `Et0/2` |
| `40a6.b77d.aa01` | Static | `Et0/0` |
| `40a6.b77d.bb02` | Static | `Et0/0` |

### After Regenerating Traffic

| MAC Address      | Type    | Port    | Device |
| ---------------- | ------- | ------- | ------ |
| `5254.005e.61bd` | Dynamic | `Et0/1` | `PC1`  |
| `5254.00eb.7252` | Dynamic | `Et0/2` | `PC2`  |

---

## Verification Commands Used

```bash
ifconfig eth0
route -n
ping 192.168.1.51
ping -c 5 192.168.1.51
arp -a
show mac address-table
clear mac address-table dynamic
```

---

# Troubleshooting

## Issue 1 - Ping kept running longer than intended

### What happened

The first Linux ping ran until it was manually stopped, resulting in:

```text
30 packets transmitted, 30 packets received
```

### Diagnosis

On Linux, `ping` continues until stopped unless a count is specified.

### Fix

I stopped the running ping with `Ctrl+C`, then used:

```bash
ping -c 5 192.168.1.51
```

### Lesson

On Linux, use `-c` to specify the number of packets. This keeps testing neat and makes the output easier to include in a lab write-up.

---

## Issue 2 - Tried to run a show command in configuration mode

### What happened

I entered:

```bash
show mac address-table
```

from global configuration mode:

```text
Switch6(config)#
```

The switch returned:

```text
% Invalid input detected at '^' marker.
```

### Diagnosis

Most `show` commands are run from privileged EXEC mode.

### Fix

I exited configuration mode and ran the command from:

```text
Switch6#
```

### Lesson

Pay attention to the prompt. It tells you which mode you are in:

| Prompt            | Mode                 |
| ----------------- | -------------------- |
| `Switch>`         | User EXEC            |
| `Switch#`         | Privileged EXEC      |
| `Switch(config)#` | Global configuration |

---

# Key Learnings

* Switches learn MAC addresses dynamically from the source MAC address of incoming frames.
* ARP allows hosts to learn each other’s MAC addresses before sending traffic.
* The CAM/MAC address table maps MAC addresses to switchports.
* Clearing dynamic MAC entries does not remove static entries.
* After the dynamic table is cleared, normal traffic will repopulate it.
* Linux `ping` continues until stopped unless a packet count is supplied.
* The CLI prompt is important because it shows whether commands are being entered in the correct mode.

---

# Improvements for Next Time

* Use `ping -c <number>` from the start when testing from Linux hosts.
* Capture before-and-after CAM table outputs side by side.
* Use a small table to track endpoint IP, MAC and switchport mappings.
* Be more deliberate about checking the CLI prompt before entering commands.
* Add a short diagram showing PC1 on `Et0/1`, PC2 on `Et0/2`, and the uplink on `Et0/0`.

---

# Final Result

This lab successfully demonstrated how a switch learns MAC addresses dynamically.

`PC1` and `PC2` were verified with correct IP addresses, default gateways and MAC addresses. After traffic was generated between them, `Switch6` learned their MAC addresses on the correct ports. Clearing the dynamic CAM table removed the learned entries, and a controlled ping caused the switch to relearn them.

The key practical takeaway was:

```text
Traffic creates learning opportunities for the switch. Clear the dynamic table, generate new traffic, and the CAM table rebuilds itself from what the switch sees entering each port.
```
