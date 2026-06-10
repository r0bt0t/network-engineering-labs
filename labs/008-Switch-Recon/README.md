# Lab 008 - Switch Recon

<p class="back-link">
  <a href="../../Lab-index.html">← Back to Lab Index</a>
</p>

<table>
<tr>
<td colspan="2" valign="top">

<h1>Objective</h1>

<h4>Confirm the physical and logical relationship between <code>RW-CORE-SW</code> and <code>RW-ACC-SW</code>.</h4>

<h4>Identify the active VLAN, trunk link, management IPs and switch-to-switch uplink.</h4>

<h4>Trace each endpoint from IP address to MAC address, then from MAC address to physical switchport.</h4>

<h4>Add clear interface descriptions so the final topology can be understood quickly by another engineer.</h4>

<h4>Document the final working layout without disrupting service.</h4>

</td>
</tr>

<tr>
<td valign="top" width="60%">
<img src="Images/Packet-Tracer-Img2.png" width="100%" alt="Switch recon Packet Tracer topology">
</td>

</tr>
</table>

---

## Scenario

This lab simulates being dropped into an existing small network with limited initial information.

The task was not to redesign or reconfigure the network, but to **recon it safely**. I needed to work out:

* which switches were connected
* which VLAN was in use
* which interfaces were trunks or access ports
* which endpoint lived on which physical port
* whether the switches could reach each other
* whether the topology could be documented clearly for follow-up work

The main workflow was:

```text
CDP → Trunk table → VLAN table → ARP table → MAC address table → Interface descriptions
```

In plain English:

> Find the neighbour, confirm the path, identify the VLAN, translate IPs to MAC addresses, trace MAC addresses to ports, then document what has been proven.

---

## Devices Used

| Device             | Role                          |
| ------------------ | ----------------------------- |
| `RW-CORE-SW`       | Core switch                   |
| `RW-ACC-SW`        | Access switch                 |
| `BaristaPOS`       | Endpoint on the core switch   |
| `InventoryStation` | Endpoint on the access switch |
| `ManagerConsole`   | Endpoint on the access switch |

---

## Addressing and Endpoint Summary

| Device             | IP Address      | MAC Address      | Switch       | Interface | VLAN |
| ------------------ | --------------- | ---------------- | ------------ | --------- | ---: |
| `RW-CORE-SW`       | `192.168.42.1`  | `aabb.cc80.0200` | `RW-CORE-SW` | `Vlan42`  |   42 |
| `RW-ACC-SW`        | `192.168.42.2`  | `aabb.cc80.0100` | `RW-ACC-SW`  | `Vlan42`  |   42 |
| `BaristaPOS`       | `192.168.42.37` | `5254.0024.1d40` | `RW-CORE-SW` | `Et0/1`   |   42 |
| `InventoryStation` | `192.168.42.38` | `5254.0048.eef9` | `RW-ACC-SW`  | `Et0/1`   |   42 |
| `ManagerConsole`   | `192.168.42.39` | `5254.0083.1986` | `RW-ACC-SW`  | `Et0/2`   |   42 |

---

## Final Topology

```text
                    VLAN 42 trunk
RW-CORE-SW Et0/0 ======================= Et0/0 RW-ACC-SW
     |                                          |
     |                                          |-- Et0/1 InventoryStation
     |                                          |   192.168.42.38
     |                                          |   5254.0048.eef9
     |                                          |
     |                                          |-- Et0/2 ManagerConsole
     |                                              192.168.42.39
     |                                              5254.0083.1986
     |
     |-- Et0/1 BaristaPOS
         192.168.42.37
         5254.0024.1d40
```

---

# Configuration and Recon Steps

---

## Step 1 - Confirm the Core Switch Identity

```bash
enable
show run | include hostname
```

### Observed Output

```text
hostname RW-CORE-SW
```

### Explanation

Before making any assumptions, I confirmed the hostname of the first switch. This matters because it is easy to misread a topology if the device role is not confirmed first.

At this stage, I knew I was working on:

```text
RW-CORE-SW
```

---

## Step 2 - Check Core Switch Interface Status

```bash
show ip interface brief
```

### Observed Output

```text
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.1    YES TFTP   up                    up
```

### Explanation

This showed that:

* `Et0/0` was active
* `Et0/1` was active
* `Et0/2` and `Et0/3` were administratively shut down
* the switch had a management SVI on VLAN 42
* the core switch management IP was `192.168.42.1`

This gave the first useful clue: VLAN 42 was likely the main operational VLAN in this lab.

---

## Step 3 - Check the Core Switch Trunk

```bash
show interfaces trunk
```

### Observed Output

```text
Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          42

Port           Vlans allowed and active in management domain
Et0/0          42

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          42
```

### Explanation

This confirmed that `Et0/0` on `RW-CORE-SW` was a trunk port.

Important findings:

| Item                   | Result   |
| ---------------------- | -------- |
| Trunk port             | `Et0/0`  |
| Encapsulation          | `802.1Q` |
| Native VLAN            | 1        |
| Allowed VLAN           | 42       |
| Active forwarding VLAN | 42       |

This told me that the core switch was carrying VLAN 42 across `Et0/0`, most likely towards another switch.

---

## Step 4 - Check VLAN Membership on the Core Switch

```bash
show vlan brief
```

### Observed Output

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/2, Et0/3
42   VLAN0042                         active    Et0/1
```

### Explanation

This confirmed that `Et0/1` was an access port in VLAN 42.

At this point, the likely layout was:

| Interface | Likely Role          |
| --------- | -------------------- |
| `Et0/0`   | Trunk/uplink         |
| `Et0/1`   | Endpoint access port |
| `Et0/2`   | Unused/admin down    |
| `Et0/3`   | Unused/admin down    |

I still needed to prove what was connected to `Et0/0` and `Et0/1`.

---

## Step 5 - Use CDP to Identify the Neighbour Switch

```bash
show cdp neighbors
```

### Observed Output

```text
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
RW-ACC-SW        Eth 0/0           136             R S I  Linux Uni Eth 0/0
```

### Explanation

CDP confirmed that:

```text
RW-CORE-SW Et0/0 connects to RW-ACC-SW Et0/0
```

This proved the switch-to-switch link and confirmed that the trunk on `RW-CORE-SW Et0/0` led to the access switch.

---

## Step 6 - Document the Core Switch Uplink

```bash
configure terminal
interface ethernet0/0
description Uplink-To-RW-ACC-SW-ET0/0
end
write memory
```

### Explanation

Once the uplink had been proven with CDP and the trunk table, I added a description to make the topology clearer for anyone inspecting the switch later.

This is a small change, but a useful one. It turns an unknown interface into a documented link.

---

## Step 7 - Verify Core Switch Management Details

```bash
show run interface vlan 42
show ip route
show run | include default gateway
```

### Observed Output

```text
interface Vlan42
 ip address 192.168.42.1 255.255.255.0
```

```text
Gateway of last resort is not set

C        192.168.42.0/24 is directly connected, Vlan42
L        192.168.42.1/32 is directly connected, Vlan42
```

### Explanation

This confirmed that `RW-CORE-SW` was managed through VLAN 42 using:

```text
192.168.42.1/24
```

No default gateway or default route was configured. That was acceptable within this lab because the switch only needed local VLAN 42 reachability.

---

## Step 8 - Confirm Core-to-Access Switch Reachability

```bash
ping 192.168.42.2
```

### Observed Output

```text
.!!!!
Success rate is 80 percent (4/5)
```

### Explanation

The first ping failed while ARP resolved the destination MAC address. The following replies succeeded.

This confirmed that the core switch could reach the access switch management IP:

```text
RW-CORE-SW 192.168.42.1 → RW-ACC-SW 192.168.42.2
```

---

## Step 9 - Confirm the Access Switch Identity

```bash
enable
show run | include hostname
```

### Observed Output

```text
hostname RW-ACC-SW
```

### Explanation

After moving to the second switch, I confirmed the hostname before continuing. This avoided mixing up outputs from the core and access switches.

I initially tried:

```bash
show run | hostname
```

That produced an error because `hostname` needs to be used with `include` when filtering command output:

```bash
show run | include hostname
```

---

## Step 10 - Check Access Switch Interface Status

```bash
show ip interface brief
```

### Observed Output

```text
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.2    YES TFTP   up                    up
```

### Explanation

This showed:

* `Et0/0`, `Et0/1` and `Et0/2` were active
* `Et0/3` was administratively down
* the access switch management IP was `192.168.42.2`
* VLAN 42 was active on the switch

This suggested that `Et0/0` was likely the uplink, while `Et0/1` and `Et0/2` were endpoint-facing access ports.

---

## Step 11 - Check the Access Switch Trunk

```bash
show interfaces trunk
```

### Observed Output

```text
Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          42
```

### Explanation

This matched the core switch. Both sides showed:

| Switch       | Trunk Port | Allowed VLAN |
| ------------ | ---------- | -----------: |
| `RW-CORE-SW` | `Et0/0`    |           42 |
| `RW-ACC-SW`  | `Et0/0`    |           42 |

This confirmed that VLAN 42 was being carried correctly between the switches.

---

## Step 12 - Check Access Switch VLAN Membership

```bash
show vlan brief
```

### Observed Output

```text
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3
42   VLAN0042                         active    Et0/1, Et0/2
```

### Explanation

This confirmed that the access switch endpoint ports were:

| Interface | VLAN |
| --------- | ---: |
| `Et0/1`   |   42 |
| `Et0/2`   |   42 |

The unused/admin-down port `Et0/3` remained in VLAN 1.

---

## Step 13 - Use CDP from the Access Switch

```bash
show cdp neighbors
```

### Observed Output

```text
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
RW-CORE-SW       Eth 0/0           128             R S I  Linux Uni Eth 0/0
```

### Explanation

This confirmed the same link from the access switch side:

```text
RW-ACC-SW Et0/0 connects to RW-CORE-SW Et0/0
```

Checking both sides helped confirm that the physical and logical topology matched.

---

## Step 14 - Document the Access Switch Uplink

```bash
configure terminal
interface ethernet0/0
description Uplink To RW-CORE-SW Et0/0
end
write memory
```

### Verification

```bash
show interfaces description
```

### Observed Output

```text
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink To RW-CORE-SW Et0/0
Et0/1                          up             up       
Et0/2                          up             up       
Et0/3                          admin down     down     
Vl42                           up             up
```

### Explanation

The uplink had now been documented on both switches. That makes the topology much easier to understand during later troubleshooting or handover.

---

## Step 15 - Confirm Endpoint Reachability from the Core Switch

```bash
ping 192.168.42.37
ping 192.168.42.38
ping 192.168.42.39
```

### Observed Output

```text
ping 192.168.42.37
!!!!!
Success rate is 100 percent (5/5)
```

```text
ping 192.168.42.38
!!!!!
Success rate is 100 percent (5/5)
```

```text
ping 192.168.42.39
!!!!!
Success rate is 100 percent (5/5)
```

### Explanation

All three endpoints responded from the core switch. This confirmed that the devices were online and reachable in VLAN 42.

The next task was to work out where each endpoint was physically connected.

---

## Step 16 - Use ARP to Convert Endpoint IPs to MAC Addresses

```bash
show ip arp
```

### Observed Output

```text
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.42.1            -   aabb.cc80.0200  ARPA   Vlan42
Internet  192.168.42.2           20   aabb.cc80.0100  ARPA   Vlan42
Internet  192.168.42.37           0   5254.0024.1d40  ARPA   Vlan42
Internet  192.168.42.38           0   5254.0048.eef9  ARPA   Vlan42
Internet  192.168.42.39           0   5254.0083.1986  ARPA   Vlan42
```

### Explanation

ARP allowed me to translate each known endpoint IP address into a MAC address.

| IP Address      | MAC Address      |
| --------------- | ---------------- |
| `192.168.42.37` | `5254.0024.1d40` |
| `192.168.42.38` | `5254.0048.eef9` |
| `192.168.42.39` | `5254.0083.1986` |

This is an important step because the MAC address table is searched by MAC, not by IP.

---

## Step 17 - Trace BaristaPOS on the Core Switch

```bash
show mac address-table address 5254.0024.1d40
```

### Observed Output

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0024.1d40    DYNAMIC     Et0/1
```

### Explanation

This confirmed that:

```text
BaristaPOS = 192.168.42.37 = 5254.0024.1d40 = RW-CORE-SW Et0/1
```

Because the MAC was learned directly on `Et0/1`, the endpoint was connected directly to the core switch rather than beyond the trunk.

---

## Step 18 - Document BaristaPOS on the Core Switch

```bash
configure terminal
interface ethernet0/1
description BaristaPOS 192.168.42.37
end
write memory
```

### Verification

```bash
show interfaces description
```

### Observed Output

```text
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink-To-RW-ACC-SW-ET0/0
Et0/1                          up             up       BaristaPOS 192.168.42.37
Et0/2                          admin down     down     
Et0/3                          admin down     down     
Vl42                           up             up
```

### Explanation

The first endpoint was now identified and documented directly on the switch interface.

---

## Step 19 - Trace Remaining Endpoint MACs from the Core Switch

```bash
show mac address-table address 5254.0048.eef9
show mac address-table address 5254.0083.1986
```

### Observed Output

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0048.eef9    DYNAMIC     Et0/0
```

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0083.1986    DYNAMIC     Et0/0
```

### Explanation

Both MAC addresses were learned by the core switch through `Et0/0`.

Since `Et0/0` was already proven to be the trunk to `RW-ACC-SW`, this showed that both remaining endpoints were somewhere beyond the access switch.

At this stage:

| Endpoint        | Core Switch MAC Table Result | Meaning              |
| --------------- | ---------------------------- | -------------------- |
| `192.168.42.38` | Learned via `Et0/0`          | Behind access switch |
| `192.168.42.39` | Learned via `Et0/0`          | Behind access switch |

---

## Step 20 - Trace InventoryStation and ManagerConsole on the Access Switch

```bash
show mac address-table address 5254.0048.eef9
show mac address-table address 5254.0083.1986
```

### Observed Output

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0048.eef9    DYNAMIC     Et0/1
```

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0083.1986    DYNAMIC     Et0/2
```

### Explanation

This confirmed the final two endpoint locations:

```text
InventoryStation = 192.168.42.38 = 5254.0048.eef9 = RW-ACC-SW Et0/1
```

```text
ManagerConsole = 192.168.42.39 = 5254.0083.1986 = RW-ACC-SW Et0/2
```

The workflow was:

```text
IP address → ARP table → MAC address → MAC table → physical switchport
```

This is the key practical skill demonstrated by the lab.

---

## Step 21 - Document the Access Switch Endpoint Ports

```bash
configure terminal
interface ethernet0/1
description InventoryStation 192.168.42.38
interface ethernet0/2
description ManagerConsole 192.168.42.39
end
write memory
```

### Verification

```bash
show interfaces description
```

### Observed Output

```text
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink To RW-CORE-SW Et0/0
Et0/1                          up             up       InventoryStation 192.168.42.38
Et0/2                          up             up       ManagerConsole 192.168.42.39
Et0/3                          admin down     down     
Vl42                           up             up
```

### Explanation

The access switch now had clear descriptions for both endpoint-facing ports and its uplink.

This completed the documentation task without changing any VLAN membership or disrupting service.

---

# Verification

## Final Core Switch Verification

```bash
show interfaces description
show interfaces trunk
show mac address-table address 5254.0024.1d40
show mac address-table address 5254.0048.eef9
show mac address-table address 5254.0083.1986
```

### Confirmed Results

| Check                | Result                           |
| -------------------- | -------------------------------- |
| `Et0/0`              | Uplink to `RW-ACC-SW Et0/0`      |
| `Et0/1`              | `BaristaPOS 192.168.42.37`       |
| VLAN 42 trunk        | Active and forwarding on `Et0/0` |
| BaristaPOS MAC       | Learned directly on `Et0/1`      |
| InventoryStation MAC | Learned via trunk `Et0/0`        |
| ManagerConsole MAC   | Learned via trunk `Et0/0`        |

---

## Final Access Switch Verification

```bash
show interfaces description
show interfaces trunk
show mac address-table address 5254.0048.eef9
show mac address-table address 5254.0083.1986
```

### Confirmed Results

| Check                | Result                           |
| -------------------- | -------------------------------- |
| `Et0/0`              | Uplink to `RW-CORE-SW Et0/0`     |
| `Et0/1`              | `InventoryStation 192.168.42.38` |
| `Et0/2`              | `ManagerConsole 192.168.42.39`   |
| VLAN 42 trunk        | Active and forwarding on `Et0/0` |
| InventoryStation MAC | Learned directly on `Et0/1`      |
| ManagerConsole MAC   | Learned directly on `Et0/2`      |

---

## Verification Summary

| Device       | Interface | Description                      | Status |
| ------------ | --------- | -------------------------------- | ------ |
| `RW-CORE-SW` | `Et0/0`   | `Uplink-To-RW-ACC-SW-ET0/0`      | up/up  |
| `RW-CORE-SW` | `Et0/1`   | `BaristaPOS 192.168.42.37`       | up/up  |
| `RW-ACC-SW`  | `Et0/0`   | `Uplink To RW-CORE-SW Et0/0`     | up/up  |
| `RW-ACC-SW`  | `Et0/1`   | `InventoryStation 192.168.42.38` | up/up  |
| `RW-ACC-SW`  | `Et0/2`   | `ManagerConsole 192.168.42.39`   | up/up  |

---

## Final Findings

* `RW-CORE-SW` and `RW-ACC-SW` are connected through `Et0/0` on both switches.
* The switch-to-switch link is an 802.1Q trunk.
* VLAN 42 is the active VLAN carried over the trunk.
* `RW-CORE-SW` is managed on `192.168.42.1/24`.
* `RW-ACC-SW` is managed on `192.168.42.2/24`.
* No default gateway or default route is configured on either switch.
* `BaristaPOS` is connected directly to `RW-CORE-SW Et0/1`.
* `InventoryStation` is connected to `RW-ACC-SW Et0/1`.
* `ManagerConsole` is connected to `RW-ACC-SW Et0/2`.
* All active interfaces were documented with descriptions.
* The final topology was confirmed without interrupting service.

---

# Troubleshooting

## Issue 1 - Incorrect command filter

### What happened

I initially entered:

```bash
show run | hostname
```

This produced an invalid input error.

### Diagnosis

The pipe operator needs a filtering action such as `include`.

### Fix

The correct command was:

```bash
show run | include hostname
```

### Lesson

When filtering command output, use the correct pipe syntax:

```bash
show running-config | include <text>
```

---

## Issue 2 - First ping to the access switch only returned 80 percent

### What happened

The first ping from `RW-CORE-SW` to `192.168.42.2` returned:

```text
.!!!!
Success rate is 80 percent
```

### Diagnosis

The first ICMP request likely timed out while ARP resolved the destination MAC address.

### Fix

No configuration change was needed. The following replies succeeded, confirming reachability.

### Lesson

A first ping sometimes loses the first packet while ARP completes. Repeating the test can confirm whether there is a real connectivity problem.

---

## Issue 3 - Endpoint MACs appeared on the core trunk

### What happened

The MAC addresses for `InventoryStation` and `ManagerConsole` appeared on `RW-CORE-SW Et0/0`.

### Diagnosis

`Et0/0` was already confirmed as the trunk to `RW-ACC-SW`, so this meant the endpoints were not directly connected to the core switch. They were behind the access switch.

### Fix

I moved to `RW-ACC-SW` and searched for the same MAC addresses there.

### Lesson

When a MAC address appears on a trunk, follow the trunk to the neighbouring switch and continue tracing.

---

# Key Learnings

* A safe recon workflow avoids guesswork.
* CDP is useful for confirming directly connected neighbours.
* `show interfaces trunk` confirms whether VLANs are being carried between switches.
* `show vlan brief` identifies access ports and VLAN membership.
* ARP translates IP addresses to MAC addresses.
* The MAC address table maps MAC addresses to switchports.
* If a MAC address is learned over a trunk, the endpoint is likely behind another switch.
* Interface descriptions are a simple but valuable form of documentation.
* Verification should be performed from both sides of an uplink where possible.
* Small command syntax mistakes are normal and can be corrected with careful use of IOS help and filtering.

---

# Improvements for Next Time

* Start by sketching a quick working topology as evidence is gathered.
* Capture command outputs in smaller sections rather than one long CLI block.
* Use a table from the beginning to track IP, MAC, switch, interface and VLAN mappings.
* Repeat important pings after ARP resolution to confirm stable reachability.
* Save final command outputs separately in a `configs/` or `evidence/` folder.
* Work slightly more independently through the recon process before asking for hints, while still checking assumptions before making changes.

---

# Final Result

This lab successfully identified and documented the existing switch topology.

The final confirmed layout was:

* `RW-CORE-SW Et0/0` trunks to `RW-ACC-SW Et0/0`
* VLAN 42 is carried across the trunk
* `BaristaPOS` is connected to `RW-CORE-SW Et0/1`
* `InventoryStation` is connected to `RW-ACC-SW Et0/1`
* `ManagerConsole` is connected to `RW-ACC-SW Et0/2`

The lab reinforced a practical network recon method:

```text
Confirm device identity → Check interfaces → Confirm trunks → Use CDP → Ping endpoints → Check ARP → Trace MAC table → Document interfaces
```

This is a useful workflow for understanding an unfamiliar network without making unnecessary changes.
