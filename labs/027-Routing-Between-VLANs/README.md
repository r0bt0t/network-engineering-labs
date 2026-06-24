# Lab 027 - Routing Between VLANs

<table>
<tr>
<td colspan="2" valign="top">

# Objective

#### Convert the switch-to-router uplink into an 802.1Q trunk.
#### Configure router-on-a-stick subinterfaces for VLAN 10 and VLAN 20.
#### Assign routed gateway addresses for each VLAN subnet.
#### Replace the legacy DHCP scope with VLAN-specific DHCP pools.
#### Confirm clients receive addresses from the correct VLAN and are ready for inter-VLAN routing.

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

The previous lab proved that VLAN 10 and VLAN 20 could be carried across trunk links and kept separate at Layer 2. This lab added the next major feature: routing between those VLANs using a single physical router interface.

Cafe-RTR1 was converted into a router-on-a-stick gateway. Its physical Ethernet0/0 interface remained connected to Cafe-SW1, but the IP addressing was moved onto VLAN-tagged subinterfaces:

```text
Switch trunk -> Router subinterfaces -> VLAN gateways -> DHCP scopes -> Client addressing
```

In plain English:

> Router-on-a-stick allows one physical router link to route for multiple VLANs. The switch sends tagged VLAN traffic to the router, and the router uses subinterfaces to provide a separate default gateway for each VLAN.

---

## Lab Topology

| Device | Role | Key Interfaces |
|---|---|---|
| Cafe-SW1 | Access switch | Ethernet0/0 trunk to Cafe-RTR1 |
| Cafe-RTR1 | Router-on-a-stick gateway | Ethernet0/0, Ethernet0/0.10, Ethernet0/0.20 |
| Cafe-Admin1 | Admin workstation | DHCP client in VLAN 10 |
| Cafe-Client1 | Patron workstation | DHCP client in VLAN 20 |

---

## VLAN and Subnet Plan

| VLAN ID | VLAN Name | Subnet | Gateway |
|---:|---|---|---|
| 10 | ADMIN | 10.0.18.0/27 | 10.0.18.1 |
| 20 | PATRON | 10.0.18.32/27 | 10.0.18.33 |

---

## DHCP Plan

| DHCP Pool | Network | Default Router | DNS Server |
|---|---|---|---|
| ADMIN-10 | 10.0.18.0/27 | 10.0.18.1 | 1.1.1.1 |
| PATRON-20 | 10.0.18.32/27 | 10.0.18.33 | 1.1.1.1 |

Reserved gateway addresses were excluded from DHCP leasing:

```text
ip dhcp excluded-address 10.0.18.1 10.0.18.1
ip dhcp excluded-address 10.0.18.33 10.0.18.33
```

---

## Task 0 - Unlock the Switch-to-Router Trunk

Cafe-SW1 Ethernet0/0 was converted from a regular switchport into an 802.1Q trunk towards Cafe-RTR1:

```text
interface ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
```

The initial trunk verification showed the port trunking, but with no VLANs in the spanning-tree forwarding section:

```text
Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          none
```

VLANs 10 and 20 were then confirmed on Cafe-SW1:

```text
vlan 10
 name ADMIN

vlan 20
 name PATRON
```

After the VLANs and router tagging were in place, the trunk showed VLANs 10 and 20 active and forwarding:

```text
Port           Vlans allowed and active in management domain
Et0/0          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          1,10,20
```

---

## Task 1 - Carve Router-on-a-Stick Subinterfaces

Cafe-RTR1 originally had a single legacy IP address directly on Ethernet0/0:

```text
interface Ethernet0/0
 description Link to Cafe-SW1 Et0/0
 ip address 10.0.18.1 255.255.255.192
```

That physical interface address was removed so the router could use VLAN-tagged subinterfaces instead:

```text
interface ethernet0/0
 no ip address 10.0.18.1 255.255.255.192
```

The VLAN 10 subinterface was then created:

```text
interface ethernet0/0.10
 encapsulation dot1q 10
 ip address 10.0.18.1 255.255.255.224
```

The VLAN 20 subinterface was created in the same way:

```text
interface ethernet0/0.20
 encapsulation dot1q 20
 ip address 10.0.18.33 255.255.255.224
```

The physical interface was left enabled with no IP address:

```text
interface ethernet0/0
 no ip address
 no shutdown
```

Verification showed the parent interface and both VLAN subinterfaces up/up:

```text
Ethernet0/0            unassigned      YES unset  up                    up
Ethernet0/0.10         10.0.18.1       YES manual up                    up
Ethernet0/0.20         10.0.18.33      YES manual up                    up
```

The final router-on-a-stick section of the running configuration confirmed the subinterface design:

```text
interface Ethernet0/0
 description Link to Cafe-SW1 Et0/0
 no ip address
interface Ethernet0/0.10
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.224
interface Ethernet0/0.20
 encapsulation dot1Q 20
 ip address 10.0.18.33 255.255.255.224
```

---

## Task 2 - Serve DHCP and Prepare Inter-VLAN Reachability

The old single DHCP pool was removed because it referenced the larger combined network:

```text
no ip dhcp pool Cafe-Base
no ip dhcp excluded-address 10.0.18.1 10.0.18.10
```

New exclusions were added for the two gateway addresses:

```text
ip dhcp excluded-address 10.0.18.1 10.0.18.1
ip dhcp excluded-address 10.0.18.33 10.0.18.33
```

The VLAN 20 DHCP pool was configured first:

```text
ip dhcp pool PATRON-20
 network 10.0.18.32 255.255.255.224
 default-router 10.0.18.33
 dns-server 1.1.1.1
```

The VLAN 10 DHCP pool was then configured:

```text
ip dhcp pool ADMIN-10
 network 10.0.18.0 255.255.255.224
 default-router 10.0.18.1
 dns-server 1.1.1.1
```

The router's DHCP binding table showed Cafe-Client1 receiving an address from the VLAN 20 pool:

```text
10.0.18.34      0152.5400.e44b.fe       Jun 25 2026 05:22 PM    Automatic  Active     Ethernet0/0.20
```

Cafe-Admin1 also successfully requested an address using DHCP:

```text
udhcpc: lease of 10.0.18.2 obtained from 10.0.18.1, lease time 86400
```

Cafe-Client1 successfully received its VLAN 20 address:

```text
udhcpc: lease of 10.0.18.34 obtained from 10.0.18.33, lease time 86400
```

---

## Client Verification

Cafe-Admin1 received an address in the VLAN 10 subnet:

```text
inet addr:10.0.18.2  Bcast:10.0.18.31  Mask:255.255.255.224
```

Its default route pointed to the VLAN 10 gateway:

```text
0.0.0.0         10.0.18.1       0.0.0.0         UG    0      0        0 eth0
10.0.18.0       0.0.0.0         255.255.255.224 U     0      0        0 eth0
```

Cafe-Client1 received an address in the VLAN 20 subnet:

```text
inet addr:10.0.18.34  Bcast:10.0.18.63  Mask:255.255.255.224
```

Its default route pointed to the VLAN 20 gateway:

```text
0.0.0.0         10.0.18.33      0.0.0.0         UG    0      0        0 eth0
10.0.18.32      0.0.0.0         255.255.255.224 U     0      0        0 eth0
```

---

## Troubleshooting Notes

Several useful mistakes were captured during the lab:

| Issue | Cause | Fix |
|---|---|---|
| `interface ehernet0/0` failed | Typo in the interface name | Re-entered the command as `interface ethernet0/0` |
| `no ip address` failed from global config mode | The command must be entered under the interface | Moved into `interface ethernet0/0` first |
| `no ip address 10.0.18.1 255.255.255.224` failed | The existing mask was actually `/26`, not `/27` | Checked `show run` and removed the correct address/mask |
| `switchport` commands failed on router subinterfaces | `switchport` commands belong on switch interfaces, not router routed subinterfaces | Used `encapsulation dot1q` on the router subinterfaces |
| DHCP NAK and NO_POOL messages appeared | Clients were requesting leases while DHCP was being rebuilt | Completed the new VLAN-specific DHCP pools |

---

## Verification

| Verification Command | Device | Result |
|---|---|---|
| `show interface trunk` | Cafe-SW1 | Ethernet0/0 was trunking with VLANs 10 and 20 active |
| `show ip interface brief` | Cafe-RTR1 | Ethernet0/0.10 and Ethernet0/0.20 were up/up |
| `show run \| section interface Ethernet0/0` | Cafe-RTR1 | Subinterfaces were mapped to VLAN 10 and VLAN 20 |
| `show ip dhcp binding` | Cafe-RTR1 | Cafe-Client1 had an active lease on Ethernet0/0.20 |
| `udhcpc -i eth0 -n -q` | Cafe-Admin1 | Lease `10.0.18.2` obtained from `10.0.18.1` |
| `udhcpc -i eth0 -n -q` | Cafe-Client1 | Lease `10.0.18.34` obtained from `10.0.18.33` |
| `route -n` | Both clients | Default gateways pointed to the correct VLAN subinterface |

The supplied raw CLI confirms the trunk, subinterfaces, DHCP pools and client leases. A final inter-VLAN ping was part of the task objective, but no final ping transcript was included in the provided evidence.

---

## Final Outcome

The lab successfully converted the design from Layer 2 VLAN separation into a router-on-a-stick inter-VLAN routing design.

Cafe-SW1 now trunks VLANs 10 and 20 towards Cafe-RTR1. Cafe-RTR1 uses Ethernet0/0.10 and Ethernet0/0.20 as VLAN-specific gateways, each with a separate `/27` subnet. The old combined DHCP scope was replaced with dedicated pools for the admin and patron VLANs, and both clients successfully obtained addresses and default gateways from the correct subnet.

---

## Key Takeaways

- Router-on-a-stick uses subinterfaces to route for multiple VLANs over one physical link.
- The switch side of the link uses `switchport mode trunk`; the router side uses `encapsulation dot1q`.
- The parent router interface should remain up with no IP address when subinterfaces hold the routed gateway addresses.
- DHCP scopes must match the VLAN subnet they serve.
- Excluding gateway addresses prevents DHCP from leasing critical infrastructure IPs to clients.
- `show ip interface brief`, `show interface trunk`, `show ip dhcp binding`, `ifconfig` and `route -n` provide a strong verification chain.

---

## Raw CLI Output

The raw CLI evidence for this lab is stored here:

```text
evidence/raw-cli-output.md
```
