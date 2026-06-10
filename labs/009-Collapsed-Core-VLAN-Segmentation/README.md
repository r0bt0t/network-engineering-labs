# Lab 009 - Collapsed Core VLAN Segmentation with Router-on-a-Stick, DHCP and ACL Security

<p class="back-link">
  <a href="../../Lab-index.html">← Back to Lab Index</a>
</p>

<table>
<tr>
<td colspan="2" valign="top">

<h1>Objective</h1>

<h4>Build a small business-style collapsed core network using two Layer 2 switches, a router, wired clients and wireless access points.</h4>

<h4>Segment the network into separate VLANs for Main, Guest, IoT and Management traffic.</h4>

<h4>Configure router-on-a-stick inter-VLAN routing using 802.1Q subinterfaces.</h4>

<h4>Provide DHCP services from the router for client VLANs.</h4>

<h4>Secure the design by hardening trunks, moving unused ports to a blackhole VLAN, shutting down unused ports and applying ACLs to restrict Guest and IoT access.</h4>

<h4>Verify the completed design using interface, VLAN, trunk, DHCP, ACL and end-device connectivity tests.</h4>

</td>
</tr>

<tr>
<td valign="top" width="50%">
<img src="Images/Small Business VLAN Segmentation Lab Topology.png" width="100%" alt="Small business VLAN segmentation lab topology">
</td>
</tr>

<tr>
<td valign="middle" width="50%">
<img src="Images/Small Business VLAN Segmentation Lab Trunk Core SW1.png" width="100%" alt="Core switch trunk verification screenshot">
</td>
</tr>

<tr>
<td valign="bottom" width="50%">
<img src="Images/Small Business VLAN Segmentation Lab Main PC.png" width="100%" alt="Main PC verification screenshot">
</td>
</tr>
</table>

---

## Scenario

This lab represents a small office or advanced home network where different device types should not all sit in the same flat network.

The design separates trusted devices, guest devices, IoT devices and management traffic into dedicated VLANs. A router-on-a-stick configuration provides inter-VLAN routing, while ACLs restrict traffic between less trusted and more trusted networks.

The intended security model is:

| Source        |        Destination | Result  |
| ------------- | -----------------: | ------- |
| Main network  |        IoT network | Allowed |
| IoT network   |       Main network | Blocked |
| Guest network |       Main network | Blocked |
| Guest network |        IoT network | Blocked |
| Guest network | Management network | Blocked |
| Main network  | Management network | Allowed |

---

## Devices Used

| Device       | Model           | Role                                         |
| ------------ | --------------- | -------------------------------------------- |
| `ISP-CLOUD`  | Cloud-PT        | Simulated external/ISP connection            |
| `RTR1`       | Cisco 2911      | Router-on-a-stick gateway and DHCP server    |
| `CORE-SW1`   | Cisco 2960-24TT | Main collapsed core / central Layer 2 switch |
| `ACCESS-SW2` | Cisco 2960-24TT | Secondary access switch                      |
| `MAIN-PC1`   | PC-PT           | Trusted wired client                         |
| `IOT-PC1`    | PC-PT           | IoT/test client                              |
| `MAIN-WAP1`  | AccessPoint-PT  | Main wireless access point                   |
| `GUEST-WAP1` | AccessPoint-PT  | Guest wireless access point                  |

---

## Topology Summary

```text
             ISP-CLOUD
                 |
                RTR1
                 |
              CORE-SW1
              /      \
        MAIN-PC1     ACCESS-SW2
           |          /       \
       MAIN-WAP1  IOT-PC1   GUEST-WAP1
```

Logical trunk view:

```text
RTR1 Gi0/0
   |
   | 802.1Q trunk carrying VLANs 10, 20, 30, 99
   |
CORE-SW1 Gi0/1

CORE-SW1 Gi0/2
   |
   | 802.1Q trunk carrying VLANs 10, 20, 30, 99
   |
ACCESS-SW2 Gi0/1
```

---

## VLAN and IP Addressing Plan

| VLAN | Name        | Purpose                    | Subnet            | Gateway        |
| ---: | ----------- | -------------------------- | ----------------- | -------------- |
|   10 | `MAIN`      | Trusted client devices     | `192.168.10.0/24` | `192.168.10.1` |
|   20 | `GUEST`     | Guest network              | `192.168.20.0/24` | `192.168.20.1` |
|   30 | `IOT`       | IoT / less trusted devices | `192.168.30.0/24` | `192.168.30.1` |
|   99 | `MGMT`      | Switch management          | `192.168.99.0/24` | `192.168.99.1` |
|  999 | `BLACKHOLE` | Unused ports / native VLAN | No active subnet  | N/A            |

---

## Port Allocation

### CORE-SW1

| Interface              | Connected Device | VLAN / Role        |
| ---------------------- | ---------------- | ------------------ |
| `Fa0/1`                | `MAIN-PC1`       | VLAN 10 MAIN       |
| `Fa0/10`               | `MAIN-WAP1`      | VLAN 10 MAIN       |
| `Gi0/1`                | `RTR1`           | 802.1Q trunk       |
| `Gi0/2`                | `ACCESS-SW2`     | 802.1Q trunk       |
| `Fa0/2-9`, `Fa0/11-24` | Unused           | VLAN 999, shutdown |

### ACCESS-SW2

| Interface                       | Connected Device | VLAN / Role        |
| ------------------------------- | ---------------- | ------------------ |
| `Fa0/1`                         | `IOT-PC1`        | VLAN 30 IOT        |
| `Fa0/10`                        | `GUEST-WAP1`     | VLAN 20 GUEST      |
| `Gi0/1`                         | `CORE-SW1`       | 802.1Q trunk       |
| `Fa0/2-9`, `Fa0/11-24`, `Gi0/2` | Unused           | VLAN 999, shutdown |

---

## Configuration Steps

---

## Step 1 - Basic Router Setup

```bash
enable
configure terminal
hostname RTR1
no ip domain-lookup
banner motd ^Authorised access only.^
end
```

### Explanation

The router was given a meaningful hostname, DNS lookup was disabled to prevent delays after mistyped commands, and a message-of-the-day banner was added to represent standard access warning practice.

---

## Step 2 - Enable the Router LAN Interface

```bash
configure terminal
interface gigabitEthernet0/0
description LAN Trunk for VLANs
no shutdown
end
```

### Explanation

`GigabitEthernet0/0` was used as the LAN-facing interface between `RTR1` and `CORE-SW1`.

No IP address was assigned directly to the physical interface because this lab uses router-on-a-stick. IP addresses were assigned to subinterfaces instead.

---

## Step 3 - Basic Switch Setup

### CORE-SW1

```bash
enable
configure terminal
hostname CORE-SW1
no ip domain-lookup
banner motd ^Authorised access only.^
end
```

### ACCESS-SW2

```bash
enable
configure terminal
hostname ACCESS-SW2
no ip domain-lookup
banner motd ^Authorised access only.^
end
```

### Explanation

Both switches were given clear hostnames so that configuration and verification output could be easily identified. DNS lookup was disabled for smoother CLI work, and access banners were applied.

---

## Step 4 - Create VLANs on Both Switches

The same VLAN database was created on both `CORE-SW1` and `ACCESS-SW2`.

```bash
configure terminal

vlan 10
name MAIN

vlan 20
name GUEST

vlan 30
name IOT

vlan 99
name MGMT

vlan 999
name BLACKHOLE

end
```

### Explanation

Each VLAN represents a separate broadcast domain:

| VLAN | Purpose                               |
| ---: | ------------------------------------- |
|   10 | Trusted client devices                |
|   20 | Guest access                          |
|   30 | IoT / less trusted devices            |
|   99 | Network management                    |
|  999 | Unused ports and hardened native VLAN |

This creates logical separation before routing and access control are applied.

---

## Step 5 - Configure CORE-SW1 Access Ports

```bash
configure terminal

interface fastEthernet0/1
description Main-PC1 Access Port
switchport mode access
switchport access vlan 10
spanning-tree portfast

interface fastEthernet0/10
description Main-WAP1 Access Port
switchport mode access
switchport access vlan 10
spanning-tree portfast

end
```

### Explanation

`MAIN-PC1` and `MAIN-WAP1` were placed into VLAN 10. These are endpoint-facing access ports, so PortFast was enabled to allow the ports to transition quickly to forwarding state.

PortFast was only used on endpoint ports, not trunk ports.

---

## Step 6 - Configure ACCESS-SW2 Access Ports

```bash
configure terminal

interface fastEthernet0/1
description IOT-PC1 Access Port
switchport mode access
switchport access vlan 30
spanning-tree portfast

interface fastEthernet0/10
description GUEST-WAP1 Access Port
switchport mode access
switchport access vlan 20
spanning-tree portfast

end
```

### Explanation

`IOT-PC1` was placed into VLAN 30 and `GUEST-WAP1` was placed into VLAN 20. This separates less trusted IoT and guest devices from the main trusted network.

---

## Step 7 - Configure Trunk Links on CORE-SW1

```bash
configure terminal

interface gigabitEthernet0/1
description Trunk to RTR1
switchport mode trunk
switchport trunk native vlan 999
switchport trunk allowed vlan 10,20,30,99

interface gigabitEthernet0/2
description Trunk to ACCESS-SW2
switchport mode trunk
switchport trunk native vlan 999
switchport trunk allowed vlan 10,20,30,99

end
```

### Explanation

The trunk to the router and the trunk to the second switch were configured to carry VLANs 10, 20, 30 and 99.

The native VLAN was changed from VLAN 1 to VLAN 999. This is a trunk-hardening measure to avoid using VLAN 1 for untagged trunk traffic.

VLAN 999 was not added to the allowed VLAN list because it is being used as a blackhole/native VLAN, not as an active routed client VLAN.

---

## Step 8 - Configure Trunk Link on ACCESS-SW2

```bash
configure terminal

interface gigabitEthernet0/1
description Trunk to CORE-SW1
switchport mode trunk
switchport trunk native vlan 999
switchport trunk allowed vlan 10,20,30,99

end
```

### Explanation

The trunk between `ACCESS-SW2` and `CORE-SW1` was configured to match the trunk settings on the other side.

Both sides must use the same native VLAN to avoid native VLAN mismatch warnings and potential untagged traffic issues.

---

## Step 9 - Configure Router-on-a-Stick Subinterfaces

```bash
configure terminal

interface gigabitEthernet0/0.10
description Gateway for VLAN 10 MAIN
encapsulation dot1Q 10
ip address 192.168.10.1 255.255.255.0

interface gigabitEthernet0/0.20
description Gateway for VLAN 20 GUEST
encapsulation dot1Q 20
ip address 192.168.20.1 255.255.255.0

interface gigabitEthernet0/0.30
description Gateway for VLAN 30 IOT
encapsulation dot1Q 30
ip address 192.168.30.1 255.255.255.0

interface gigabitEthernet0/0.99
description Gateway for VLAN 99 MGMT
encapsulation dot1Q 99
ip address 192.168.99.1 255.255.255.0

end
```

### Explanation

The 2960 switches are Layer 2 switches, so routing between VLANs was provided by `RTR1`.

Each subinterface on `Gi0/0` acts as the default gateway for a VLAN. The `encapsulation dot1Q` command tells the router which VLAN tag each subinterface should process.

For example:

```bash
encapsulation dot1Q 10
```

means that the subinterface handles VLAN 10 traffic.

---

## Step 10 - Configure DHCP on RTR1

```bash
configure terminal

ip dhcp excluded-address 192.168.10.1 192.168.10.20
ip dhcp excluded-address 192.168.20.1 192.168.20.20
ip dhcp excluded-address 192.168.30.1 192.168.30.20

ip dhcp pool MAIN
network 192.168.10.0 255.255.255.0
default-router 192.168.10.1
dns-server 8.8.8.8

ip dhcp pool GUEST
network 192.168.20.0 255.255.255.0
default-router 192.168.20.1
dns-server 8.8.8.8

ip dhcp pool IOT
network 192.168.30.0 255.255.255.0
default-router 192.168.30.1
dns-server 8.8.8.8

end
```

### Explanation

DHCP was configured on `RTR1` so that clients in VLANs 10, 20 and 30 could automatically receive IP addressing.

The first 20 addresses in each subnet were excluded from DHCP so they could be reserved for gateways, infrastructure devices or future static assignments.

---

## Step 11 - Configure Switch Management IPs

### CORE-SW1

```bash
configure terminal

interface vlan 99
description MGMT
ip address 192.168.99.2 255.255.255.0
no shutdown

ip default-gateway 192.168.99.1

end
```

### ACCESS-SW2

```bash
configure terminal

interface vlan 99
ip address 192.168.99.3 255.255.255.0
no shutdown

ip default-gateway 192.168.99.1

end
```

### Explanation

Layer 2 switches are managed using an SVI rather than by assigning an IP address to a physical switchport.

VLAN 99 was used as the dedicated management VLAN. The switches use `192.168.99.1`, the router’s VLAN 99 gateway, as their default gateway.

---

## Step 12 - Harden Unused Ports on CORE-SW1

```bash
configure terminal

interface range fastEthernet0/2-9
switchport mode access
switchport access vlan 999
description Unused - shutdown
shutdown

interface range fastEthernet0/11-24
switchport mode access
switchport access vlan 999
description Unused - shutdown
shutdown

end
```

### Explanation

Unused ports were moved into VLAN 999, given a clear description and administratively shut down.

This prevents unused switchports from remaining active in the default VLAN.

---

## Step 13 - Harden Unused Ports on ACCESS-SW2

```bash
configure terminal

interface range fastEthernet0/2-9
switchport mode access
switchport access vlan 999
description Unused - shutdown
shutdown

interface range fastEthernet0/11-24
switchport mode access
switchport access vlan 999
description Unused - shutdown
shutdown

interface gigabitEthernet0/2
switchport mode access
switchport access vlan 999
description Unused - shutdown
shutdown

end
```

### Explanation

The same unused port hardening was applied to `ACCESS-SW2`. The unused gigabit port `Gi0/2` was also placed into VLAN 999 and shut down.

---

## Step 14 - Configure IoT ACL

```bash
configure terminal

ip access-list extended IOT_IN
permit icmp 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 echo-reply
deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255
permit ip any any

interface gigabitEthernet0/0.30
ip access-group IOT_IN in

end
```

### Explanation

This ACL restricts IoT devices from initiating access to the Main network.

The first rule permits ICMP echo replies from IoT back to Main. This allows Main devices to ping IoT devices successfully. The deny rule then blocks other IoT-to-Main traffic.

This was necessary because router ACLs are not stateful. Without the echo-reply permit, a Main-to-IoT ping would fail because the reply traffic would be blocked on its return from VLAN 30.

---

## Step 15 - Configure Guest ACL

```bash
configure terminal

ip access-list extended GUEST_IN
deny ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255
deny ip 192.168.20.0 0.0.0.255 192.168.30.0 0.0.0.255
deny ip 192.168.20.0 0.0.0.255 192.168.99.0 0.0.0.255
permit ip any any

interface gigabitEthernet0/0.20
ip access-group GUEST_IN in

end
```

### Explanation

The Guest ACL prevents Guest devices from reaching the Main, IoT and Management networks.

A final `permit ip any any` was included so that Guest traffic to future external/internet networks would still be allowed if internet simulation is added later.

---

## Step 16 - Save Configurations

### RTR1

```bash
write memory
```

### CORE-SW1

```bash
write memory
```

### ACCESS-SW2

```bash
write memory
```

### Explanation

The running configurations were saved to startup configuration so that the lab would survive a reload.

---

## Verification

## RTR1 Verification

### Interface Status

```bash
show ip interface brief
```

Expected result:

```text
GigabitEthernet0/0     unassigned      up    up 
GigabitEthernet0/0.10  192.168.10.1    up    up 
GigabitEthernet0/0.20  192.168.20.1    up    up 
GigabitEthernet0/0.30  192.168.30.1    up    up 
GigabitEthernet0/0.99  192.168.99.1    up    up 
```

### DHCP Bindings

```bash
show ip dhcp binding
```

Observed result:

```text
192.168.10.21    0005.5E12.9E3D    Automatic
192.168.20.21    000A.41AD.C07A    Automatic
192.168.30.21    000A.41AD.C07A    Automatic
```

Note: The same client MAC appeared in both VLAN 20 and VLAN 30 because `IOT-PC1` was temporarily moved to VLAN 20 to test Guest DHCP.

### ACLs

```bash
show access-lists
```

Observed result:

```text
Extended IP access list IOT_IN
    10 permit icmp 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 echo-reply
    15 deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255
    20 permit ip any any

Extended IP access list GUEST_IN
    10 deny ip 192.168.20.0 0.0.0.255 192.168.10.0 0.0.0.255
    20 deny ip 192.168.20.0 0.0.0.255 192.168.30.0 0.0.0.255
    30 deny ip 192.168.20.0 0.0.0.255 192.168.99.0 0.0.0.255
    40 permit ip any any
```

---

## CORE-SW1 Verification

### VLANs

```bash
show vlan brief
```

Expected result:

```text
10   MAIN        active    Fa0/1, Fa0/10
20   GUEST       active
30   IOT         active
99   MGMT        active
999  BLACKHOLE   active    Fa0/2-9, Fa0/11-24
```

### Trunks

```bash
show interfaces trunk
```

Expected result:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      on           802.1q         trunking      999
Gig0/2      on           802.1q         trunking      999

Port        Vlans allowed on trunk
Gig0/1      10,20,30,99
Gig0/2      10,20,30,99
```

### Interface Status

```bash
show ip interface brief
```

Expected result:

```text
FastEthernet0/1        up                    up 
FastEthernet0/10       up                    up 
GigabitEthernet0/1     up                    up 
GigabitEthernet0/2     up                    up 
Vlan99                 192.168.99.2          up    up
```

Unused FastEthernet ports should show:

```text
administratively down down
```

---

## ACCESS-SW2 Verification

### VLANs

```bash
show vlan brief
```

Expected result:

```text
20   GUEST       active    Fa0/10
30   IOT         active    Fa0/1
999  BLACKHOLE   active    Fa0/2-9, Fa0/11-24, Gig0/2
```

### Trunk

```bash
show interfaces trunk
```

Expected result:

```text
Port        Mode         Encapsulation  Status        Native vlan
Gig0/1      on           802.1q         trunking      999

Port        Vlans allowed on trunk
Gig0/1      10,20,30,99
```

### Interface Status

```bash
show ip interface brief
```

Expected result:

```text
FastEthernet0/1        up                    up 
FastEthernet0/10       up                    up 
GigabitEthernet0/1     up                    up 
Vlan99                 192.168.99.3          up    up
```

Unused ports should show:

```text
administratively down down
```

---

## PC Verification

### MAIN-PC1

```bash
ipconfig
```

Expected result:

```text
IPv4 Address....................: 192.168.10.21
Subnet Mask.....................: 255.255.255.0
Default Gateway.................: 192.168.10.1
```

Connectivity tests:

```bash
ping 192.168.10.1
ping 192.168.30.1
ping 192.168.30.21
```

Expected result:

```text
Packets: Sent = 4, Received = 4, Lost = 0
```

### IOT-PC1

```bash
ipconfig
```

Expected result:

```text
IPv4 Address....................: 192.168.30.21
Subnet Mask.....................: 255.255.255.0
Default Gateway.................: 192.168.30.1
```

Gateway test:

```bash
ping 192.168.30.1
```

Expected result:

```text
Packets: Sent = 4, Received = 4, Lost = 0
```

Blocked Main network test:

```bash
ping 192.168.10.21
```

Expected result:

```text
Reply from 192.168.30.1: Destination host unreachable.
```

---

## Troubleshooting

### Issue 1 - VLAN names did not appear correctly

### Diagnosis

VLANs were initially created by entering interface configuration mode, for example:

```bash
interface vlan 10
description MAIN
```

This created a Switch Virtual Interface rather than properly naming the VLAN in the VLAN database.

### Fix

The VLANs were correctly named using:

```bash
vlan 10
name MAIN
```

### Lesson

`interface vlan X` creates or configures an SVI.
`vlan X` enters the VLAN database and is used to name or create the VLAN itself.

---

### Issue 2 - DHCP pool used the wrong network

### Diagnosis

The `MAIN` DHCP pool was initially configured with the wrong network statement. This would have caused clients to receive addresses from the wrong subnet.

### Fix

The DHCP pool was corrected to:

```bash
ip dhcp pool MAIN
network 192.168.10.0 255.255.255.0
default-router 192.168.10.1
dns-server 8.8.8.8
```

### Lesson

The DHCP network statement must match the subnet of the VLAN being served, and the default router must match that VLAN’s gateway.

---

### Issue 3 - Native VLAN mismatch warning

### Diagnosis

After changing the native VLAN on the `CORE-SW1` side of the trunk, Cisco Discovery Protocol reported a native VLAN mismatch with `ACCESS-SW2`.

### Fix

The native VLAN was configured as VLAN 999 on both sides of the trunk:

```bash
switchport trunk native vlan 999
```

### Lesson

Both sides of a trunk should use the same native VLAN. Mismatches can cause warnings and may lead to untagged traffic being handled unexpectedly.

---

### Issue 4 - ACL blocked return traffic from IoT

### Diagnosis

The first version of the IoT ACL blocked all traffic from VLAN 30 to VLAN 10. This also blocked ICMP replies when the Main PC tried to ping the IoT PC.

### Fix

The ACL was adjusted to permit ICMP echo replies before denying other IoT-to-Main traffic:

```bash
permit icmp 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 echo-reply
deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255
permit ip any any
```

### Lesson

Router ACLs are not stateful. Return traffic must be explicitly permitted if it would otherwise match a deny rule.

---

### Issue 5 - Packet Tracer AccessPoint-PT DHCP limitation

### Diagnosis

The `AccessPoint-PT` device did not expose the same normal DHCP client interface as a PC.

### Fix

`IOT-PC1` was temporarily moved into VLAN 20 to validate the Guest DHCP pool and Guest ACL behaviour.

Temporary command:

```bash
interface fastEthernet0/1
switchport access vlan 20
```

Restore command:

```bash
interface fastEthernet0/1
switchport access vlan 30
```

### Lesson

Packet Tracer device limitations sometimes require practical testing workarounds. The important point is to validate the VLAN, DHCP and ACL logic.

---

## Key Learnings

* VLANs separate Layer 2 broadcast domains and provide the foundation for network segmentation.
* Router-on-a-stick allows a single router interface to route between multiple VLANs using 802.1Q subinterfaces.
* Trunk links must carry the correct VLANs and must match on both ends.
* The native VLAN should not be left on VLAN 1 in a hardened design.
* Layer 2 switches use SVIs for management, not physical switchport IP addresses.
* DHCP pools must match the correct VLAN subnet and default gateway.
* ACL order matters because rules are processed from top to bottom.
* Router ACLs are not stateful, so return traffic may need explicit handling.
* Unused switchports should not remain active in the default VLAN.
* Verification commands are just as important as configuration commands.

---

## Improvements for Next Time

* Add SSH management for `RTR1`, `CORE-SW1` and `ACCESS-SW2`.
* Add local usernames and encrypted secrets.
* Replace the simple Packet Tracer access points with wireless devices that better support SSID and DHCP testing.
* Add a fuller internet simulation using the cloud/router edge.
* Add NAT/PAT so VLANs can reach a simulated external network.
* Add more granular ACLs for specific services rather than broad IP restrictions.
* Test with additional end devices in each VLAN.
* Add screenshots of Packet Tracer simulation mode to show packet flow and ACL filtering.
* Document the final running configurations as separate files in the lab folder.

---

## Final Result

The final lab successfully implemented a segmented small network with separate Main, Guest, IoT and Management VLANs. Inter-VLAN routing was provided by `RTR1` using router-on-a-stick subinterfaces. DHCP was configured for client networks, switch management was moved to VLAN 99, and basic switch hardening was applied.

The final ACL policy allowed trusted Main devices to reach IoT devices, while preventing IoT devices from initiating access back into the Main network. Guest devices were blocked from accessing Main, IoT and Management networks.

This completed design demonstrates practical VLAN segmentation, trunking, DHCP, router-on-a-stick, switch management and ACL-based traffic control.
