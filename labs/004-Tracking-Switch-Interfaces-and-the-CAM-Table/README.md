# Lab 004 - Tracking Switch Interfaces and the CAM Table

<p class="back-link">
  <a href="../../Lab-index.html">← Back to Lab Index</a>
</p>

<table>
<tr>
<td colspan="2" valign="top">

<h1>Objective</h1>

<ul>
  <li><h3>Use switch summary commands to identify active and inactive interfaces.</h3></li>
  <li><h3>Interpret interface naming, status and protocol state from switch output.</h3></li>
  <li><h3>Check interface descriptions to map switchports to real network devices.</h3></li>
  <li><h3>Review speed, duplex and VLAN information to confirm healthy port negotiation.</h3></li>
  <li><h3>Use the MAC/CAM address table to confirm where devices are connected.</h3></li>
  <li><h3>Practise correcting command syntax when filtering or querying switch tables.</h3></li>
</ul>

</td>
</tr>

<tr>
<td colspan="2" valign="top">
<img src="Images/Topology2.png" alt="Switch interface and CAM table topology">
</td>
</tr>
</table>

---

## Scenario

This lab focuses on reading switch interface information and using it to understand what is physically and logically connected to the network.

The aim was to inspect `Switch6`, identify which interfaces were active, confirm what each port connected to, and then use the MAC/CAM table to verify the devices attached to those ports.

The practical workflow was:

```text
Check interface state → Check descriptions → Check interface status → Check CAM table → Filter for a specific MAC
```

This is a useful troubleshooting sequence because it helps answer several common questions:

* Which ports are up?
* Which ports are administratively disabled?
* What device is each port meant to connect to?
* Which VLAN is the port using?
* Is the link full duplex?
* Which MAC addresses has the switch learned on each port?

---

## Devices Used

| Device         | Role                          |
| -------------- | ----------------------------- |
| `Switch6`      | Access switch being inspected |
| `CoreSwitch`   | Upstream/core switch          |
| `AccessPoint1` | Device connected to `Et0/1`   |
| `SensorPod-A`  | Device connected to `Et0/2`   |

---

## Interface Summary

| Interface | Description            | Status          | Role              |
| --------- | ---------------------- | --------------- | ----------------- |
| `Et0/0`   | `Uplink-to-CoreSwitch` | up/up           | Uplink to core    |
| `Et0/1`   | `AccessPoint1`         | up/up           | Access point      |
| `Et0/2`   | `SensorPod-A`          | up/up           | Sensor device     |
| `Et0/3`   | `Reserved-StackLink`   | admin down/down | Reserved/disabled |

---

## VLAN and MAC Summary

| VLAN | MAC Address      | Type    | Port    | Meaning                               |
| ---: | ---------------- | ------- | ------- | ------------------------------------- |
|   10 | `5254.0058.297b` | Dynamic | `Et0/1` | Learned endpoint on AccessPoint1 port |
|   10 | `5a5a.1c1c.0d0d` | Static  | `Et0/1` | AccessPoint1 reference/static entry   |
|   20 | `5254.0036.d8d6` | Dynamic | `Et0/2` | Learned endpoint on SensorPod-A port  |
|   20 | `7c7c.b2b2.2020` | Static  | `Et0/2` | SensorPod-A reference/static entry    |
|   99 | `40a6.b77d.aa01` | Static  | `Et0/0` | Uplink/static management entry        |
|   99 | `40a6.b77d.bb02` | Static  | `Et0/0` | Uplink/static management entry        |

---

# Investigation Steps

---

## Step 1 - Check the Basic Interface State

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
```

### Explanation

This command gave a quick health check of the switch interfaces.

The key points were:

| Interface | Status                     | Meaning           |
| --------- | -------------------------- | ----------------- |
| `Et0/0`   | up/up                      | Active link       |
| `Et0/1`   | up/up                      | Active link       |
| `Et0/2`   | up/up                      | Active link       |
| `Et0/3`   | administratively down/down | Manually disabled |

This immediately showed that three ports were live and one port was intentionally disabled.

The difference between `down` and `administratively down` is important:

* `down` usually means no active physical link.
* `administratively down` means the interface has been shut down in configuration.

---

## Step 2 - Check Interface Descriptions

```bash
show interfaces description
```

### Observed Output

```text
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink-to-CoreSwitch
Et0/1                          up             up       AccessPoint1
Et0/2                          up             up       SensorPod-A
Et0/3                          admin down     down     Reserved-StackLink
```

### Explanation

The descriptions made the topology much easier to understand.

Instead of just seeing interface names, I could map each port to its intended purpose:

```text
Et0/0 → CoreSwitch uplink
Et0/1 → AccessPoint1
Et0/2 → SensorPod-A
Et0/3 → Reserved stack link
```

This is a good example of why interface descriptions are valuable. They reduce guesswork and make support work faster.

---

## Step 3 - Check VLAN, Speed and Duplex

```bash
show interface status
```

### Observed Output

```text
Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        Uplink-to-CoreSwit connected    trunk        full   auto 10/100/1000BaseTX
Et0/1        AccessPoint1       connected    10           full   auto 10/100/1000BaseTX
Et0/2        SensorPod-A        connected    20           full   auto 10/100/1000BaseTX
Et0/3        Reserved-StackLink disabled     1            full   auto 10/100/1000BaseTX
```

### Explanation

This command provided a more detailed operational view.

Important findings:

| Interface | VLAN / Mode | Duplex | Speed | Interpretation                   |
| --------- | ----------- | ------ | ----- | -------------------------------- |
| `Et0/0`   | trunk       | full   | auto  | Uplink is connected and trunking |
| `Et0/1`   | VLAN 10     | full   | auto  | AccessPoint1 link looks healthy  |
| `Et0/2`   | VLAN 20     | full   | auto  | SensorPod-A link looks healthy   |
| `Et0/3`   | VLAN 1      | full   | auto  | Disabled/reserved port           |

This confirmed that the active links were connected, full duplex and auto-negotiated. There were no obvious speed or duplex problems.

---

## Step 4 - Attempt to View the MAC Table

```bash
show mac address table
```

### Observed Output

```text
                         ^
% Invalid input detected at '^' marker.
```

### Explanation

This command failed because the syntax was slightly wrong.

I entered:

```bash
show mac address table
```

but Cisco IOS expects:

```bash
show mac address-table
```

The hyphen matters here.

This was a useful reminder that IOS command syntax can be quite specific, especially with compound command names.

---

## Step 5 - View the MAC/CAM Table Correctly

```bash
show mac address-table
```

### Observed Output

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.0058.297b    DYNAMIC     Et0/1
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  20    5254.0036.d8d6    DYNAMIC     Et0/2
  20    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0
```

### Explanation

The MAC table showed which MAC addresses were associated with which ports.

The key findings were:

| Port    | VLAN | MAC Evidence               | Interpretation           |
| ------- | ---: | -------------------------- | ------------------------ |
| `Et0/0` |   99 | Static MACs                | Uplink/core-side entries |
| `Et0/1` |   10 | Dynamic and static entries | AccessPoint1-side device |
| `Et0/2` |   20 | Dynamic and static entries | SensorPod-A-side device  |

This confirmed that the switch was learning MAC addresses on the expected interfaces.

---

## Step 6 - Attempt to Filter the MAC Table

```bash
show mac address-table|5a5a.1c1c.0d0d
show mac address-table | 5a5a.1c1c.0d0d
```

### Observed Output

```text
                              ^
% Invalid input detected at '^' marker.
```

```text
                                 ^
% Invalid input detected at '^' marker.
```

### Explanation

I attempted to filter the MAC table using pipe-style syntax, but this was not accepted in this environment.

The issue was that I tried to filter directly by the MAC address after the pipe. IOS filtering normally needs a keyword such as `include`, but for this specific task there was a cleaner built-in option.

---

## Step 7 - Use the Correct MAC Address Filter

```bash
show mac address-table address 5a5a.1c1c.0d0d
```

### Observed Output

```text
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
Total Mac Addresses for this criterion: 1
```

### Explanation

This was the correct way to search for one specific MAC address in the MAC address table.

It confirmed:

```text
5a5a.1c1c.0d0d → VLAN 10 → Et0/1
```

That matched the expected AccessPoint1 port.

---

# Verification

## Interface State Verification

```bash
show ip interface brief
```

Confirmed:

| Interface | State                      |
| --------- | -------------------------- |
| `Et0/0`   | up/up                      |
| `Et0/1`   | up/up                      |
| `Et0/2`   | up/up                      |
| `Et0/3`   | administratively down/down |

---

## Interface Description Verification

```bash
show interfaces description
```

Confirmed:

| Interface | Description            |
| --------- | ---------------------- |
| `Et0/0`   | `Uplink-to-CoreSwitch` |
| `Et0/1`   | `AccessPoint1`         |
| `Et0/2`   | `SensorPod-A`          |
| `Et0/3`   | `Reserved-StackLink`   |

---

## Interface Status Verification

```bash
show interface status
```

Confirmed:

| Interface | Status    | VLAN / Mode | Duplex | Speed |
| --------- | --------- | ----------- | ------ | ----- |
| `Et0/0`   | connected | trunk       | full   | auto  |
| `Et0/1`   | connected | 10          | full   | auto  |
| `Et0/2`   | connected | 20          | full   | auto  |
| `Et0/3`   | disabled  | 1           | full   | auto  |

---

## MAC Table Verification

```bash
show mac address-table
```

Confirmed:

| MAC Address      | VLAN | Type    | Port    |
| ---------------- | ---: | ------- | ------- |
| `5254.0058.297b` |   10 | Dynamic | `Et0/1` |
| `5a5a.1c1c.0d0d` |   10 | Static  | `Et0/1` |
| `5254.0036.d8d6` |   20 | Dynamic | `Et0/2` |
| `7c7c.b2b2.2020` |   20 | Static  | `Et0/2` |
| `40a6.b77d.aa01` |   99 | Static  | `Et0/0` |
| `40a6.b77d.bb02` |   99 | Static  | `Et0/0` |

---

# Troubleshooting

## Issue 1 - Incorrect MAC address table command

### What happened

I entered:

```bash
show mac address table
```

The switch returned an invalid input error.

### Diagnosis

The command needed a hyphen between `address` and `table`.

### Fix

The correct command was:

```bash
show mac address-table
```

### Lesson

Cisco IOS command syntax can be very specific. When a command fails, the caret marker helps identify where IOS stopped understanding the input.

---

## Issue 2 - Incorrect filtering attempt

### What happened

I tried to filter the MAC table using:

```bash
show mac address-table|5a5a.1c1c.0d0d
show mac address-table | 5a5a.1c1c.0d0d
```

Both attempts failed.

### Diagnosis

The switch did not accept this pipe/filter syntax. I needed to use the MAC address table’s built-in address lookup option instead.

### Fix

The correct command was:

```bash
show mac address-table address 5a5a.1c1c.0d0d
```

### Lesson

When searching the MAC table for one address, the `address` keyword is often cleaner and more precise than general output filtering.

---

# Key Learnings

* `show ip interface brief` is useful for a quick port state overview.
* `show interfaces description` maps interfaces to real-world labels.
* `show interface status` shows VLAN, duplex and speed information in a compact format.
* `show mac address-table` reveals which MAC addresses are associated with which switchports.
* Static and dynamic MAC entries can appear in the same table.
* A port with several remote/static MACs may indicate an uplink or infrastructure-facing interface.
* Cisco syntax matters; small differences such as hyphens can change whether a command works.
* The most useful workflow was:

```text
Interface brief → Interface descriptions → Interface status → MAC address table → Targeted MAC lookup
```

---

# Improvements for Next Time

* Use the exact IOS command syntax for MAC table lookups.
* Use `show mac address-table address <mac>` when searching for a single MAC address.
* Record interface status, VLAN and MAC table results in a table from the start.
* Capture screenshots of both the full MAC table and the targeted MAC lookup.
* Pay attention to whether the switch is showing a dynamic endpoint MAC or a static lab/reference MAC.
* Add notes explaining why full duplex and expected VLAN membership matter for troubleshooting.

---

# Final Result

This lab successfully identified active and inactive switch interfaces, verified interface descriptions, confirmed VLAN/speed/duplex status and used the MAC/CAM table to associate devices with switchports.

The final confirmed mapping was:

```text
Et0/0 → Uplink-to-CoreSwitch / trunk / VLAN 99 static entries
Et0/1 → AccessPoint1 / VLAN 10 / MAC 5a5a.1c1c.0d0d
Et0/2 → SensorPod-A / VLAN 20 / MAC 7c7c.b2b2.2020
Et0/3 → Reserved-StackLink / administratively down
```

The lab reinforced how much can be learned from basic switch show commands before making any configuration changes.
