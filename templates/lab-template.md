# Lab XXX - TITLE

<table>
<tr>
<td colspan="2" valign="top">

# Objective

* ### Describe the main technical goal of the lab.
* ### Explain what network skill or concept is being demonstrated.
* ### State what the final working outcome should prove.
* ### Include any troubleshooting, security, routing, switching, or verification objective if relevant.

</td>
</tr>

<tr>
<td valign="top">
<img src="Images/example-topology.png">
</td>

<td valign="bottom">
<img src="Images/example-supporting-image.png">
</td>

</tr>
</table>

---

## Scenario

Briefly describe the situation this lab represents.

Example:

This lab simulates a small office network where several devices need to be configured, verified and documented. The goal was to build the network methodically, test each stage, and confirm the final behaviour using Cisco IOS verification commands.

The main workflow was:

```text
Step 1 concept → Step 2 concept → Step 3 concept → Verification → Documentation
```

In plain English:

> Explain what you were trying to achieve as if another learner or junior engineer was reading your notes.

---

## Devices Used

| Device    | Role                                   |
| --------- | -------------------------------------- |
| `R1`      | Router / default gateway / DHCP server |
| `S1`      | Core/access switch                     |
| `S2`      | Access switch                          |
| `PC1`     | Test client                            |
| `PC2`     | Test client                            |
| `Server1` | Server / target device                 |

---

## Addressing and VLAN Plan

Delete this section if the lab does not use IP addressing or VLANs.

| VLAN | Name    | Purpose         | Subnet            | Gateway        |
| ---: | ------- | --------------- | ----------------- | -------------- |
|   10 | `MAIN`  | Trusted devices | `192.168.10.0/24` | `192.168.10.1` |
|   20 | `GUEST` | Guest devices   | `192.168.20.0/24` | `192.168.20.1` |
|   99 | `MGMT`  | Management      | `192.168.99.0/24` | `192.168.99.1` |

---

## Interface / Port Plan

Delete this section if it is not needed.

| Device | Interface | Connected To | VLAN / Role    |
| ------ | --------- | ------------ | -------------- |
| `S1`   | `Fa0/1`   | `PC1`        | VLAN 10        |
| `S1`   | `Gi0/1`   | `R1`         | Trunk / uplink |
| `S2`   | `Fa0/1`   | `PC2`        | VLAN 20        |
| `S2`   | `Gi0/1`   | `S1`         | Trunk / uplink |

---

## Final Topology

Use whichever format suits the lab. This can be a simple text diagram, a screenshot, or both.

```text
R1
 |
S1
 |\
 | \ 
PC1 S2
     |
    PC2
```

---

# Configuration and Investigation Steps

---

## Step 1 - STEP TITLE

```bash
enable
configure terminal
```

### Explanation

Explain what this step does and why it matters.

Try to keep this section friendly and practical. For example:

This moves from the basic user prompt into global configuration mode, where device-wide settings can be changed. I used this before applying hostname, interface, VLAN or security configuration.

---

## Step 2 - STEP TITLE

```bash
hostname DEVICE-NAME
no ip domain-lookup
```

### Explanation

Explain the purpose of these commands.

Example:

The hostname makes the CLI prompt meaningful, which helps avoid configuring the wrong device. Disabling DNS lookup prevents long delays when a command is mistyped.

---

## Step 3 - STEP TITLE

```bash
interface INTERFACE-ID
description DESCRIPTION-HERE
no shutdown
```

### Explanation

Explain what interface you configured, what it connects to, and why the description is useful.

Example:

The description documents the purpose of the port directly in the running configuration. This makes later troubleshooting easier because the interface role can be checked without tracing cables physically.

---

## Step 4 - STEP TITLE

```bash
show command or configuration command here
```

### Explanation

Explain what the command proved or changed.

For verification commands, say what you were looking for in the output.

Example:

This command confirmed that the trunk was active, using 802.1Q encapsulation, and carrying the expected VLANs.

---

## Step 5 - STEP TITLE

```bash
additional commands here
```

### Explanation

Explain the result clearly.

Use short tables where helpful:

| Item Checked     | Expected Result | Actual Result |
| ---------------- | --------------- | ------------- |
| Interface status | up/up           | up/up         |
| VLAN membership  | VLAN 10         | VLAN 10       |
| Ping test        | Success         | Success       |

---

# Verification

## Device Verification

```bash
show ip interface brief
show running-config
show interfaces description
```

### Expected / Confirmed Results

| Check                    | Result |
| ------------------------ | ------ |
| Hostname configured      | Yes    |
| Required interfaces up   | Yes    |
| Management IP configured | Yes    |
| Configuration saved      | Yes    |

---

## Connectivity Verification

Delete this section if the lab does not include connectivity tests.

```bash
ping x.x.x.x
ping x.x.x.x
```

### Results

| Source | Destination |       Expected |         Result |
| ------ | ----------- | -------------: | -------------: |
| `PC1`  | `Gateway`   |        Success |        Success |
| `PC1`  | `PC2`       | Success / Fail | Success / Fail |

---

## Feature-Specific Verification

Use this for VLANs, trunks, ACLs, DHCP, CAM tables, CDP, routing, SSH, etc.

```bash
show vlan brief
show interfaces trunk
show access-lists
show ip dhcp binding
show mac address-table
show cdp neighbors
show ip route
```

### Summary

| Feature   | Verification Command     | Result                         |
| --------- | ------------------------ | ------------------------------ |
| VLANs     | `show vlan brief`        | Correct VLANs present          |
| Trunks    | `show interfaces trunk`  | Expected VLANs allowed         |
| DHCP      | `show ip dhcp binding`   | Clients received addresses     |
| ACLs      | `show access-lists`      | Expected rules matched         |
| CAM table | `show mac address-table` | MACs learned on expected ports |

---

# Troubleshooting

## Issue 1 - SHORT ISSUE TITLE

### What happened

Describe the mistake or unexpected result.

Example:

The command failed because I entered it in the wrong configuration mode.

### Diagnosis

Explain how you identified the issue.

Example:

The CLI caret marker appeared under the command, and the prompt showed I was still in global configuration mode.

### Fix

Show the corrected command or process.

```bash
correct command here
```

### Lesson

Write the useful takeaway.

Example:

The prompt matters. Some commands only work in privileged EXEC mode, while others must be entered under interface, line or global configuration mode.

---

## Issue 2 - SHORT ISSUE TITLE

### What happened

Describe the issue.

### Diagnosis

Explain how you worked out what was wrong.

### Fix

```bash
correct command here
```

### Lesson

Summarise what you would remember next time.

---

# Key Learnings

* Explain the main concept you learned.
* Mention any command syntax that became clearer.
* Note any link between theory and real behaviour you observed.
* Include any troubleshooting habit that improved.
* Mention any verification command that proved especially useful.

Example:

* ARP maps IP addresses to MAC addresses.
* The MAC/CAM table maps MAC addresses to switchports.
* If a MAC address appears on an uplink, the device is likely further downstream.
* `show ip interface brief` is one of the quickest ways to spot interface state problems.
* Small syntax details, such as hyphens and command mode, matter in Cisco IOS.

---

# Improvements for Next Time

* Add one thing you would do more efficiently.
* Add one thing you would document better.
* Add one command or concept to practise again.
* Add one improvement to the lab design or verification process.

Example:

* Capture screenshots of key verification outputs as I progress.
* Record IP, MAC, VLAN and port details in a table from the start.
* Use more targeted show commands where available.
* Check the current CLI mode before entering commands.
* Redact passwords and secrets before publishing to GitHub.

---

# Final Result

Summarise the completed lab in a short, confident paragraph.

Example:

This lab successfully configured and verified a small Cisco network feature set. The required devices were configured, the expected connectivity or security behaviour was confirmed, and the final outputs demonstrated that the intended design was working.

The main practical workflow reinforced by this lab was:

```text
Plan → Configure → Verify → Troubleshoot → Document
```

---

# Raw CLI Dump

Keep this section in a separate file if the command output is very long.

Suggested file path:

```text
evidence/raw-cli-output.md
```

Or include below if the lab is short.

```bash
Paste raw CLI output here.
```
