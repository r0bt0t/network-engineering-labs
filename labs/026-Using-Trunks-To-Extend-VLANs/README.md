# Lab 026 - Using Trunks to Extend VLANs

<table>
<tr>
<td colspan="2" valign="top">

# Objective

#### Configure 802.1Q trunk links between Cafe-SW1 and Cafe-SW2.
#### Extend VLAN 10 and VLAN 20 across both switches.
#### Place admin endpoints into the same VLAN and confirm cross-switch connectivity.
#### Move a patron endpoint into a separate VLAN and prove isolation without inter-VLAN routing.

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

Castle Rysen's district cafe switches already had the required VLANs defined, but each switch was still acting like a separate island. The next task was to connect those VLANs across the inter-switch links so the same logical networks could exist on both switches.

The lab followed this sequence:

```text
Create VLANs -> Configure trunks -> Assign VLAN 10 endpoints -> Test connectivity -> Move one endpoint to VLAN 20 -> Prove isolation
```

In plain English:

> A trunk link allows multiple VLANs to cross the same physical cable by adding VLAN tags to the frames. Access ports carry traffic for one VLAN only, while trunk ports can carry several VLANs between switches.

---

## Lab Topology

| Device | Role | Key Interfaces |
|---|---|---|
| Cafe-SW1 | First cafe access switch | Ethernet0/1-2 trunks, Ethernet0/3 access port |
| Cafe-SW2 | Second cafe access switch | Ethernet0/1-2 trunks, Ethernet0/3 access port |
| Cafe-Admin1 | Admin workstation | Connected to Cafe-SW1 Ethernet0/3 |
| Cafe-Client1 | Client/patron workstation | Connected to Cafe-SW2 Ethernet0/3 |

---

## VLAN Plan

| VLAN ID | VLAN Name | Purpose |
|---:|---|---|
| 1 | default | Native/default VLAN retained |
| 10 | ADMIN_DEVICES | Admin workstation network |
| 20 | PATRON_DEVICES | Patron/client workstation network |

---

## Addressing

| Device | VLAN | IP Address | Default Gateway | Purpose |
|---|---:|---:|---:|---|
| Cafe-Admin1 | 10 | 10.0.18.2/27 | 10.0.18.1 | Admin endpoint |
| Cafe-Client1 | 10 | 10.0.18.3/27 | 10.0.18.1 | Initial same-VLAN connectivity test |
| Cafe-Client1 | 20 | 10.0.18.34/27 | 10.0.18.33 | Final patron VLAN isolation test |

---

## Task 0 - Fortify the Inter-Switch Lifeline

VLANs 10 and 20 were created on Cafe-SW1:

```text
vlan 10
 name ADMIN_DEVICES

vlan 20
 name PATRON_DEVICES
```

The two inter-switch links were then configured as 802.1Q trunk ports:

```text
interface range ethernet0/1-2
 switchport trunk encapsulation dot1q
 switchport mode trunk
```

The same VLAN and trunk configuration was repeated on Cafe-SW2. Verification showed both `Ethernet0/1` and `Ethernet0/2` trunking on each switch:

```text
Port           Mode             Encapsulation  Status        Native vlan
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1
```

Both trunks also showed VLANs 10 and 20 as active in the management domain:

```text
Port           Vlans allowed and active in management domain
Et0/1          1,10,20
Et0/2          1,10,20
```

On Cafe-SW2, `Et0/2` appeared as `none` in the spanning-tree forwarding section, which is expected where STP has blocked the redundant path to prevent a Layer 2 loop.

---

## Task 1 - Stretch VLAN 10 Across the Bunker

The access port for Cafe-Admin1 on Cafe-SW1 was placed into VLAN 10:

```text
interface ethernet0/3
 switchport mode access
 switchport access vlan 10
```

The matching access port for Cafe-Client1 on Cafe-SW2 was also placed into VLAN 10:

```text
interface ethernet0/3
 switchport mode access
 switchport access vlan 10
```

The VLAN table confirmed both access ports were assigned correctly:

```text
10   ADMIN_DEVICES                    active    Et0/3
```

The Linux endpoints were then configured in the same subnet:

```text
sudo ifconfig eth0 10.0.18.2 netmask 255.255.255.224 up
sudo route add default gw 10.0.18.1 eth0
```

```text
sudo ifconfig eth0 10.0.18.3 netmask 255.255.255.224 up
sudo route add default gw 10.0.18.1 eth0
```

Cafe-Admin1 successfully pinged Cafe-Client1 across the trunked switch path:

```text
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.275/1.462/2.060 ms
```

This proved VLAN 10 had been extended successfully between the two switches.

---

## Task 2 - Prove the VLAN Boundary Holds

Cafe-Client1 was then moved out of VLAN 10 and into VLAN 20 by changing the access VLAN on Cafe-SW2 Ethernet0/3:

```text
interface ethernet0/3
 switchport access vlan 20
```

The VLAN table confirmed the port move:

```text
20   PATRON_DEVICES                   active    Et0/3
```

Cafe-Client1 was readdressed for the VLAN 20 subnet:

```text
sudo ifconfig eth0 10.0.18.34 netmask 255.255.255.224 up
sudo route add default gw 10.0.18.33 eth0
```

Cafe-Admin1 then attempted to ping Cafe-Client1 at its new VLAN 20 address:

```text
5 packets transmitted, 0 packets received, 100% packet loss
```

This failure was the expected result. The two hosts were now in separate VLANs, and no Layer 3 routing had been configured between those VLANs.

---

## Verification

| Verification Command | Device | Result |
|---|---|---|
| `show interface trunk` | Cafe-SW1 | Ethernet0/1 and Ethernet0/2 were trunking with VLANs 10 and 20 active |
| `show interface trunk` | Cafe-SW2 | Ethernet0/1 and Ethernet0/2 were trunking with VLANs 10 and 20 active |
| `show vlan brief` | Cafe-SW1 | Ethernet0/3 was assigned to VLAN 10 |
| `show vlan brief` | Cafe-SW2 | Ethernet0/3 was initially assigned to VLAN 10, then moved to VLAN 20 |
| `ping -c 5 10.0.18.3` | Cafe-Admin1 | Ping succeeded while both hosts were in VLAN 10 |
| `ping -c 5 10.0.18.34` | Cafe-Admin1 | Ping failed after Cafe-Client1 moved to VLAN 20 |

Final Cafe-SW1 trunk confirmation:

```text
Et0/1          1,10,20
Et0/2          1,10,20
```

Final Cafe-SW2 access-port confirmation:

```text
20   PATRON_DEVICES                   active    Et0/3
```

---

## Final Outcome

The lab was completed successfully.

Cafe-SW1 and Cafe-SW2 were configured with matching VLANs 10 and 20, and their inter-switch links were configured as 802.1Q trunks. VLAN 10 was successfully extended across both switches, allowing Cafe-Admin1 and Cafe-Client1 to communicate while they shared the same VLAN and subnet.

Cafe-Client1 was then moved into VLAN 20 and readdressed into a different subnet. The final failed ping from Cafe-Admin1 confirmed that the VLAN boundary was working as intended and that no inter-VLAN routing existed between the two segments.

---

## Key Takeaways

- Trunk links carry multiple VLANs across a single physical connection.
- Access ports belong to one VLAN and are used for endpoint connections.
- VLANs must exist on both switches before they can be carried meaningfully over a trunk.
- `show interface trunk` confirms trunk status, encapsulation, native VLAN, allowed VLANs and active VLANs.
- Spanning Tree can block a redundant trunk while still leaving it configured as a trunk.
- Devices in the same VLAN and subnet can communicate across trunked switches.
- Devices in different VLANs require Layer 3 routing before they can communicate.

---

## Raw CLI Output

The raw CLI evidence for this lab is stored here:

```text
evidence/raw-cli-output.md
```
