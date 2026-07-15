# Lab 036 - Configuring STP in Castle Rysen

<p class="back-link">
  <a href="../../Lab-index.html">← Back to Lab Index</a>
</p>

<table>
<tr>
<td colspan="2" valign="top">

<h1>Objective</h1>

<h4>Convert the five live Castle Rysen switches to Rapid PVST.</h4>
<h4>Create the VLANs required for the cafe and fallout shelter segments.</h4>
<h4>Configure deterministic spanning-tree root and backup bridge priorities.</h4>
<h4>Configure the actual trunk links present in the live topology and verify loop prevention.</h4>
<h4>Apply PortFast and BPDU Guard to available unused/access-facing interfaces.</h4>

</td>
</tr>

<tr>
<td valign="top">
<img src="Images/Topology.png" width="100%" alt="Castle Rysen Rapid PVST topology">
</td>
</tr>
</table>

---

## Scenario

This lab completes a Rapid PVST rollout across the live Castle Rysen switching topology. The environment contains two cafe switches and three fallout shelter switches: `Cafe-SW1`, `Cafe-SW2`, `Fallout-SW1`, `Fallout-SW2`, and `Fallout-SW3`.

The work involved creating the required VLANs, enabling Rapid PVST, setting root and backup bridge priorities, configuring the live trunk links, and protecting available access-facing ports with PortFast and BPDU Guard.

A major learning point in this lab was that the live topology did not fully match the older guide labels. The actual redundant Fallout-SW1/Fallout-SW2 links were Ethernet1/2 and Ethernet1/3, not older Ethernet0/6 and Ethernet0/7 references. The lab also showed that a VLAN-specific STP instance may not appear until that VLAN is active on a port or trunk.

---

## Devices Used

* Cafe-SW1
* Cafe-SW2
* Fallout-SW1
* Fallout-SW2
* Fallout-SW3

---

## Live Topology

| Link | Interfaces |
| ---- | ---------- |
| Cafe-SW1 to Cafe-SW2 | Cafe-SW1 Ethernet0/1 to Cafe-SW2 Ethernet0/1 |
| Cafe-SW1 to Fallout-SW1 | Cafe-SW1 Ethernet0/2 to Fallout-SW1 Ethernet0/1 |
| Cafe-SW2 to Fallout-SW2 | Cafe-SW2 Ethernet0/2 to Fallout-SW2 Ethernet0/1 |
| Fallout-SW1 to Fallout-SW2 | Fallout-SW1 Ethernet1/2 to Fallout-SW2 Ethernet1/2 |
| Fallout-SW1 to Fallout-SW2 | Fallout-SW1 Ethernet1/3 to Fallout-SW2 Ethernet1/3 |
| Fallout-SW1 to Fallout-SW3 | Fallout-SW1 Ethernet0/3 to Fallout-SW3 Ethernet0/1 |
| Fallout-SW2 to Fallout-SW3 | Fallout-SW2 Ethernet0/3 to Fallout-SW3 Ethernet0/2 |

---

## VLAN Plan

| Area | VLANs |
| ---- | ----- |
| Cafe | VLAN 1, VLAN 10, VLAN 20 |
| Fallout shelter | VLAN 1, VLAN 10, VLAN 20, VLAN 30, VLAN 40 |

---

## Root Bridge Plan

| Switch | Intended Role | VLANs |
| ------ | ------------- | ----- |
| Cafe-SW1 | Cafe primary/root | 1, 10, 20 |
| Cafe-SW2 | Cafe secondary/backup | 1, 10, 20 |
| Fallout-SW1 | Fallout root | 1, 10, 20, 30, 40 |
| Fallout-SW2 | Fallout secondary/backup | 1, 10, 20, 30, 40 |

### Important Design Observation

The final evidence showed `Fallout-SW1` as the observed root for VLAN 10, even from the cafe switches. This happened because VLAN 10 was allowed across the cafe-to-fallout trunks and `Fallout-SW1` had a lower bridge priority than the cafe switches. This is an important spanning-tree design lesson: if the same VLAN is extended across multiple areas, the lowest bridge ID wins for the entire Layer 2 VLAN, regardless of the intended local area boundary.

---

## Configuration Steps

### Step 1 - Enable Rapid PVST on the Cafe Switches

Cafe VLANs 10 and 20 were created on `Cafe-SW1` and `Cafe-SW2`, then Rapid PVST was enabled.

```bash
vlan 10
vlan 20
spanning-tree mode rapid-pvst
```

Verification showed both cafe switches reporting:

```bash
Switch is in rapid-pvst mode
```

At this early stage, the switches mainly showed VLAN 1 in `show spanning-tree summary`. Later checks showed VLAN 10 once the VLAN became active across trunk links.

---

### Step 2 - Enable Rapid PVST on the Fallout Switches

VLANs 10, 20, 30 and 40 were created on `Fallout-SW1`, `Fallout-SW2`, and `Fallout-SW3`, followed by Rapid PVST.

```bash
vlan 10
vlan 20
vlan 30
vlan 40
spanning-tree mode rapid-pvst
```

Each fallout switch was verified with:

```bash
show spanning-tree summary
```

The output confirmed Rapid PVST mode on all three fallout switches.

---

### Step 3 - Configure Cafe Root and Backup Priorities

`Cafe-SW1` was configured as root primary for the cafe VLANs:

```bash
spanning-tree vlan 1,10,20 root primary
```

`Cafe-SW2` was configured as secondary:

```bash
spanning-tree vlan 1,10,20 root secondary
```

An early check for VLAN 10 returned:

```bash
Spanning tree instance(s) for vlan 10 does not exist.
```

This was not a failed priority command. It showed that the VLAN did not yet have an active STP instance at that moment. Once the trunks were configured, VLAN 10 appeared in spanning-tree output.

---

### Step 4 - Configure Fallout Root and Backup Priorities

`Fallout-SW1` was configured as the fallout root:

```bash
spanning-tree vlan 1,10,20,30,40 priority 4096
```

`Fallout-SW2` was configured as the secondary switch:

```bash
spanning-tree vlan 1,10,20,30,40 priority 8192
```

Fallout-SW1 verified as root for VLAN 1:

```bash
Root ID    Priority    4097
           This bridge is the root
```

Fallout-SW2 showed its root path through Ethernet1/2 and the redundant path blocked on Ethernet1/3:

```bash
Et1/2               Root FWD 100       128.7    P2p
Et1/3               Altn BLK 100       128.8    P2p
```

---

## Trunk Configuration

### Step 5 - Configure Cafe Trunks

The cafe inter-switch trunk and the cafe-to-fallout trunks were configured.

On Cafe-SW1:

```bash
interface ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20
exit
interface ethernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
```

On Cafe-SW2:

```bash
interface ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20
exit
interface ethernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
```

Verification showed the cafe trunks operating as 802.1Q trunks.

A useful distinction appeared in the output: VLANs 30 and 40 were allowed on the cafe-to-fallout trunks but were not active in the cafe switches' local management domain at that point.

---

### Step 6 - Configure Fallout Trunks

The fallout switch trunks were configured using the actual live interface map.

On Fallout-SW1:

```bash
interface ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
exit
interface ethernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
exit
interface range ethernet1/2 - 3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
 spanning-tree link-type point-to-point
```

On Fallout-SW2:

```bash
interface ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
exit
interface ethernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
exit
interface range ethernet1/2 - 3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
 spanning-tree link-type point-to-point
```

On Fallout-SW3:

```bash
interface range ethernet0/1 - 2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 1,10,20,30,40
```

---

## Spanning-Tree Verification

### Fallout-SW2 Redundant Pair

`Fallout-SW2` showed all four configured trunks, with Ethernet1/3 not forwarding due to spanning tree:

```bash
Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20,30,40
Et0/3          1,10,20,30,40
Et1/2          1,10,20,30,40
Et1/3          none
```

This proved Rapid PVST was blocking the redundant path to prevent a loop.

### Fallout-SW3 VLAN 30

`Fallout-SW3` showed VLAN 30 using Fallout-SW1 as the root path:

```bash
Root ID    Priority    4126
           Address     aabb.cc00.0100
           Port        2 (Ethernet0/1)
```

The port roles confirmed:

```bash
Et0/1               Root FWD 100       128.2    P2p
Et0/2               Altn BLK 100       128.3    P2p
```

### Cafe VLAN 10

Later checks showed VLAN 10 active on the cafe switches. Both cafe switches pointed toward Fallout-SW1 as the root for VLAN 10 because VLAN 10 was extended across the cafe-to-fallout trunk and Fallout-SW1 had the lower priority.

Cafe-SW2 showed:

```bash
Et0/1               Altn BLK 100       128.2    P2p
Et0/2               Root FWD 100       128.3    P2p
```

---

## Access Edge Hardening

### Cafe-SW1 Access-Facing Ports

Cafe-SW1 access-facing ports were configured with PortFast and BPDU Guard:

```bash
interface range ethernet0/3, ethernet1/0 - 3
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
```

Verification showed:

```bash
The port is in the portfast mode
Bpdu guard is enabled
```

### Fallout-SW3 Access-Facing Ports

Fallout-SW3 access-facing ports were configured in the same way:

```bash
interface range ethernet0/0, ethernet0/3, ethernet1/0 - 3
 switchport mode access
 spanning-tree portfast
 spanning-tree bpduguard enable
```

Verification again confirmed:

```bash
The port is in the portfast mode
Bpdu guard is enabled
```

### Evidence Note

This live lab did not provide a rogue host or rogue switch to trigger BPDU Guard. BPDU Guard was therefore verified by configuration output only, rather than by an err-disable event.

---

## Troubleshooting

### Issue 1 - VLAN-specific STP instances missing at first

#### Problem

Several early checks returned:

```bash
Spanning tree instance(s) for vlan 10 does not exist.
Spanning tree instance(s) for vlan 30 does not exist.
```

#### Diagnosis

The VLANs had been created, but the VLANs were not yet active on relevant ports/trunks. IOS did not yet have live STP instances to display.

#### Outcome

After the trunks were configured, VLAN-specific spanning-tree output appeared normally.

---

### Issue 2 - Live interfaces differed from older guide labels

#### Problem

The written guide referenced older interface labels for the redundant fallout links.

#### Diagnosis

The live topology used Ethernet1/2 and Ethernet1/3 between Fallout-SW1 and Fallout-SW2.

#### Fix

The live interfaces were used:

```bash
interface range ethernet1/2 - 3
```

---

### Issue 3 - VLANs allowed on trunk but not active locally

#### Problem

The cafe-to-fallout trunks allowed VLANs 30 and 40, but the active VLAN section only showed VLANs 1, 10 and 20 on the cafe switches.

#### Diagnosis

Allowed VLANs and locally active VLANs are different checks. VLANs 30 and 40 were permitted on the trunk but were not present in the cafe switch VLAN database.

#### Outcome

This was documented as a useful verification distinction.

---

### Issue 4 - Cafe root expectation changed after VLAN 10 was extended

#### Problem

Cafe-SW1 was configured as root primary for VLAN 10, but final VLAN 10 output pointed to Fallout-SW1 as the root.

#### Diagnosis

Fallout-SW1 had a lower bridge priority for VLAN 10, and VLAN 10 was allowed across the cafe-to-fallout trunk. Spanning tree elects one root for the whole Layer 2 VLAN, not per visual network area.

#### Outcome

This is a design lesson: if separate areas need separate roots for the same VLAN number, the Layer 2 boundaries must be designed accordingly.

---

### Issue 5 - BPDU Guard could not be triggered

#### Problem

The lab had no rogue endpoint or rogue switch available.

#### Diagnosis

BPDU Guard could not be tested by forcing a BPDU violation.

#### Outcome

The feature was verified with interface detail output showing:

```bash
Bpdu guard is enabled
```

---

## Key Learning Points

* Rapid PVST must be enabled consistently across all switches in the Layer 2 topology.
* A VLAN may not show an STP instance until it is active on a trunk or access port.
* Root bridge priority is evaluated per VLAN.
* The lowest bridge ID wins across the entire Layer 2 domain for that VLAN.
* Allowing the same VLAN across cafe and fallout links caused Fallout-SW1 to become the observed root for VLAN 10.
* Trunk allowed VLANs and VLANs active in the local management domain are not the same thing.
* Rapid PVST correctly blocked redundant links on Fallout-SW2 and Fallout-SW3.
* The live interface map must be trusted over older guide interface labels.
* PortFast and BPDU Guard should be applied only to access-facing ports.
* BPDU Guard can be verified by configuration, even if a rogue BPDU source is not available.

---

## Completion Check

The lab was substantially completed.

* Cafe-SW1 was converted to Rapid PVST.
* Cafe-SW2 was converted to Rapid PVST.
* Fallout-SW1 was converted to Rapid PVST.
* Fallout-SW2 was converted to Rapid PVST.
* Fallout-SW3 was converted to Rapid PVST.
* Cafe VLANs 10 and 20 were created.
* Fallout VLANs 10, 20, 30 and 40 were created.
* Cafe-SW1 was configured as the intended cafe root for VLANs 1, 10 and 20.
* Cafe-SW2 was configured as the intended cafe backup for VLANs 1, 10 and 20.
* Fallout-SW1 was configured with priority 4096 for VLANs 1, 10, 20, 30 and 40.
* Fallout-SW2 was configured with priority 8192 for VLANs 1, 10, 20, 30 and 40.
* Cafe and fallout trunk links were configured using the live interface map.
* Fallout-SW1/Fallout-SW2 used Ethernet1/2 and Ethernet1/3 as the redundant pair.
* Fallout-SW2 showed Ethernet1/2 forwarding and Ethernet1/3 blocked.
* Fallout-SW3 showed Ethernet0/1 root forwarding and Ethernet0/2 alternate blocking for VLAN 30.
* PortFast and BPDU Guard were configured on selected access-facing ports.
* BPDU Guard was verified by configuration output only because no rogue host was available.
* The final evidence highlighted a design caveat: Fallout-SW1 became the observed root for VLAN 10 once VLAN 10 was extended across the cafe-to-fallout trunks.
