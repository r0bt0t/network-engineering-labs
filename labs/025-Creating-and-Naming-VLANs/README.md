# Lab 025 - Creating and Naming VLANs

<table>
<tr>
<td colspan="2" valign="top">

# Objective

#### Create dedicated VLANs for administrative and patron device groups.
#### Apply clear VLAN names that match the intended security roles.
#### Mirror the VLAN database across both cafe switches.
#### Move patron-facing access ports on CafeSwitch01 into the correct VLAN.

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

Castle Rysen's district cafe access layer needed to be divided into separate security zones before further switch-to-switch trunking work could begin.

The aim of this lab was to take two switches that were still relying on the default VLAN and prepare them for a more structured access-layer design:

```text
Default switch state -> Create VLANs -> Name VLANs -> Mirror VLANs -> Assign patron ports
```

In plain English:

> VLANs allow one physical switch to be split into multiple logical networks. Devices in different VLANs are separated at Layer 2, which helps reduce unnecessary broadcast traffic and keeps different user groups apart until routing or firewall rules deliberately connect them.

---

## Lab Topology

| Device | Role | Key Interfaces |
|---|---|---|
| CafeSwitch01 | Primary cafe access switch | Ethernet2/2, Ethernet2/3, Ethernet3/0-3 |
| CafeSwitch02 | Secondary cafe access switch | VLAN database mirrored from CafeSwitch01 |
| Patron devices | Cafe-facing access devices | Connected to VLAN 20 ports on CafeSwitch01 |
| Administrative devices | Internal operational devices | Prepared for VLAN 10 |

---

## VLAN Plan

| VLAN ID | VLAN Name | Purpose |
|---:|---|---|
| 1 | default | Existing default VLAN retained for legacy connectivity |
| 10 | ADMIN_DEVICES | Administrative and operational devices |
| 20 | PATRON_DEVICES | Patron-facing cafe access ports |

---

## Task 0 - Inspect the Default VLAN Footprint

The lab began on CafeSwitch01 by entering privileged EXEC mode and checking the existing VLAN table:

```text
show vlan brief
```

The baseline output showed all active Ethernet interfaces still assigned to VLAN 1:

```text
1    default    active    Et0/0, Et0/1, Et0/2, Et0/3
                         Et1/0, Et1/1, Et1/2, Et1/3
                         Et2/0, Et2/1, Et2/2, Et2/3
                         Et3/0, Et3/1, Et3/2, Et3/3
```

This confirmed that no segmentation had been applied yet.

---

## Task 1 - Establish Security VLANs on CafeSwitch01

CafeSwitch01 was then configured with two new VLANs:

```text
vlan 10
 name ADMIN_DEVICES

vlan 20
 name PATRON_DEVICES
```

Verification confirmed both VLANs had been added successfully:

```text
10   ADMIN_DEVICES                    active
20   PATRON_DEVICES                   active
```

At this stage, the VLANs existed but no access ports had been moved into them yet.

---

## Task 2 - Mirror the VLAN Definitions on CafeSwitch02

The same VLAN IDs and names were then configured on CafeSwitch02:

```text
vlan 10
 name ADMIN_DEVICES

vlan 20
 name PATRON_DEVICES
```

The `show vlan brief` output confirmed CafeSwitch02 matched CafeSwitch01:

```text
10   ADMIN_DEVICES                    active
20   PATRON_DEVICES                   active
```

This keeps the VLAN database consistent across both switches, which will be important when trunk links are configured later.

---

## Task 3 - Place Patron Ports into the Correct VLAN

The patron-facing ports on CafeSwitch01 were selected as an interface range:

```text
interface range ethernet2/2 - 3, ethernet3/0 - 3
```

The ports were then locked into access mode and assigned to VLAN 20:

```text
switchport mode access
switchport access vlan 20
```

The final VLAN table confirmed that the selected interfaces had moved from the default VLAN into `PATRON_DEVICES`:

```text
20   PATRON_DEVICES    active    Et2/2, Et2/3, Et3/0, Et3/1
                                Et3/2, Et3/3
```

---

## Verification

| Verification Command | Device | Result |
|---|---|---|
| `show vlan brief` | CafeSwitch01 | VLANs 10 and 20 were present |
| `show vlan brief` | CafeSwitch02 | VLANs 10 and 20 were present with matching names |
| `show vlan brief` | CafeSwitch01 | Ethernet2/2, Ethernet2/3, and Ethernet3/0-3 were assigned to VLAN 20 |
| `show vlan brief` | CafeSwitch01 | Default VLAN 1 remained active for unassigned legacy ports |

Final CafeSwitch01 patron VLAN membership:

```text
20   PATRON_DEVICES                   active    Et2/2, Et2/3, Et3/0, Et3/1
                                                Et3/2, Et3/3
```

---

## Final Outcome

The lab was completed successfully.

CafeSwitch01 now contains VLAN 10 `ADMIN_DEVICES` and VLAN 20 `PATRON_DEVICES`. The patron-facing interfaces `Ethernet2/2`, `Ethernet2/3`, and `Ethernet3/0` through `Ethernet3/3` were moved into VLAN 20.

CafeSwitch02 was also configured with the same VLAN IDs and names, preparing both switches for future trunking and wider access-layer segmentation.

---

## Key Takeaways

- VLANs divide a single switch into separate Layer 2 broadcast domains.
- Meaningful VLAN names make the purpose of each segment easier to identify during troubleshooting.
- VLAN IDs and names should be kept consistent across switches that will later share trunk links.
- Access ports should be explicitly configured with `switchport mode access` before being assigned to an access VLAN.
- `show vlan brief` is the quickest command for confirming VLAN creation and access-port membership.
