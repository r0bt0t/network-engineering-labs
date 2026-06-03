# CLI Command Summary

## Collapsed Core VLAN Lab — Router-on-a-Stick, DHCP, Trunking, Management VLAN and ACL Security

## 1. RTR1 Configuration

### Basic router setup

```text
enable
configure terminal
hostname RTR1
no ip domain-lookup
banner motd ^Authorised access only.^
end
```

### Enable LAN-facing router interface

```text
configure terminal
interface gigabitEthernet0/0
description LAN Trunk for VLANs
no shutdown
end
```

### Router-on-a-stick subinterfaces

```text
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

### DHCP configuration

```text
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

### IoT ACL

Purpose: allow Main devices to reach IoT, but prevent IoT devices from initiating access to Main devices.

```text
configure terminal

ip access-list extended IOT_IN
permit icmp 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255 echo-reply
deny ip 192.168.30.0 0.0.0.255 192.168.10.0 0.0.0.255
permit ip any any

interface gigabitEthernet0/0.30
ip access-group IOT_IN in

end
```

### Guest ACL

Purpose: prevent Guest devices from reaching Main, IoT or Management networks.

```text
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

### Save router configuration

```text
write memory
```

---

## 2. CORE-SW1 Configuration

### Basic switch setup

```text
enable
configure terminal
hostname CORE-SW1
no ip domain-lookup
banner motd ^Authorised access only.^
end
```

### VLAN creation

```text
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

### Interface descriptions

```text
configure terminal

interface gigabitEthernet0/1
description Trunk to RTR1

interface gigabitEthernet0/2
description Trunk to ACCESS-SW2

interface fastEthernet0/1
description Main-PC1 Access Port

interface fastEthernet0/10
description Main-WAP1 Access Port

end
```

### Access ports

```text
configure terminal

interface fastEthernet0/1
switchport mode access
switchport access vlan 10
spanning-tree portfast

interface fastEthernet0/10
switchport mode access
switchport access vlan 10
spanning-tree portfast

end
```

### Trunk ports

```text
configure terminal

interface gigabitEthernet0/1
switchport mode trunk
switchport trunk native vlan 999
switchport trunk allowed vlan 10,20,30,99

interface gigabitEthernet0/2
switchport mode trunk
switchport trunk native vlan 999
switchport trunk allowed vlan 10,20,30,99

end
```

### Management SVI

```text
configure terminal

interface vlan 99
description MGMT
ip address 192.168.99.2 255.255.255.0
no shutdown

ip default-gateway 192.168.99.1

end
```

### Unused port hardening

```text
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

### Save switch configuration

```text
write memory
```

---

## 3. ACCESS-SW2 Configuration

### Basic switch setup

```text
enable
configure terminal
hostname ACCESS-SW2
no ip domain-lookup
banner motd ^Authorised access only.^
end
```

### VLAN creation

```text
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

### Interface descriptions

```text
configure terminal

interface fastEthernet0/1
description IOT-PC1 Access Port

interface fastEthernet0/10
description GUEST-WAP1 Access Port

interface gigabitEthernet0/1
description Trunk to CORE-SW1

end
```

### Access ports

```text
configure terminal

interface fastEthernet0/1
switchport mode access
switchport access vlan 30
spanning-tree portfast

interface fastEthernet0/10
switchport mode access
switchport access vlan 20
spanning-tree portfast

end
```

### Trunk port

```text
configure terminal

interface gigabitEthernet0/1
switchport mode trunk
switchport trunk native vlan 999
switchport trunk allowed vlan 10,20,30,99

end
```

### Management SVI

```text
configure terminal

interface vlan 99
ip address 192.168.99.3 255.255.255.0
no shutdown

ip default-gateway 192.168.99.1

end
```

### Unused port hardening

```text
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

### Save switch configuration

```text
write memory
```

---

# 4. Verification Commands Used

## RTR1

```text
show ip interface brief
show access-lists
show running-config
show ip dhcp binding
```

## CORE-SW1

```text
show vlan brief
show interfaces trunk
show ip interface brief
show running-config
```

## ACCESS-SW2

```text
show vlan brief
show interfaces trunk
show ip interface brief
show running-config
```

## MAIN-PC1

```text
ipconfig
ping 192.168.10.1
ping 192.168.30.1
ping 192.168.30.21
```

## IOT-PC1

```text
ipconfig
ping 192.168.30.1
ping 192.168.10.21
```

---

# 5. Final Verification Results Summary

## MAIN-PC1

Expected DHCP result:

```text
IPv4 Address: 192.168.10.21
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.10.1
```

Successful tests:

```text
ping 192.168.10.1
ping 192.168.30.1
ping 192.168.30.21
```

## IOT-PC1

Expected DHCP result:

```text
IPv4 Address: 192.168.30.21
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.30.1
```

Successful test:

```text
ping 192.168.30.1
```

Blocked test:

```text
ping 192.168.10.21
```

Expected result:

```text
Reply from 192.168.30.1: Destination host unreachable.
```

## Guest VLAN Test

Because the Packet Tracer `AccessPoint-PT` did not expose a normal DHCP client interface, `IOT-PC1` was temporarily moved to VLAN 20 to validate Guest DHCP and ACL behaviour.

Temporary change:

```text
configure terminal
interface fastEthernet0/1
switchport access vlan 20
end
```

Expected DHCP result:

```text
IPv4 Address: 192.168.20.21
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.20.1
```

Expected blocked tests from Guest VLAN:

```text
ping 192.168.10.21
ping 192.168.30.1
ping 192.168.99.1
```

Restore command:

```text
configure terminal
interface fastEthernet0/1
switchport access vlan 30
end
```

---

# 6. Final Security Policy Achieved

| Source             |           Destination | Result   |
| ------------------ | --------------------: | -------- |
| MAIN VLAN 10       |           IOT VLAN 30 | Allowed  |
| IOT VLAN 30        |          MAIN VLAN 10 | Blocked  |
| GUEST VLAN 20      |          MAIN VLAN 10 | Blocked  |
| GUEST VLAN 20      |           IOT VLAN 30 | Blocked  |
| GUEST VLAN 20      |          MGMT VLAN 99 | Blocked  |
| MAIN VLAN 10       |          MGMT VLAN 99 | Allowed  |
| Trunks             |       Native VLAN 999 | Hardened |
| Unused switchports | VLAN 999 and shutdown | Hardened |
