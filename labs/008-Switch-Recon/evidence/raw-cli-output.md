# Lab 008 - Raw CLI Dump

```bash
Connecting to console for RW-CORE-SW


User Access Verification

Username: cisco
Password: 
RW-CORE-SW>en
Password: 
RW-CORE-SW#show run | include hostname
hostname RW-CORE-SW
RW-CORE-SW#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.1    YES TFTP   up                    up      
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          42

Port           Vlans allowed and active in management domain
Et0/0          42

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          42
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/2, Et0/3
42   VLAN0042                         active    Et0/1
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
RW-ACC-SW        Eth 0/0           136             R S I  Linux Uni Eth 0/0

Total cdp entries displayed : 1
RW-CORE-SW#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RW-CORE-SW(config)#interface ethernet0/0 
RW-CORE-SW(config-if)#description Uplink-To-RW-ACC-SW-ET0/0
RW-CORE-SW(config-if)#end
RW-CORE-SW#write memory
Building configuration...
[OK]
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show run interface vlan 42
Building configuration...

Current configuration : 63 bytes
!
interface Vlan42
 ip address 192.168.42.1 255.255.255.0
end

RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show run | include default gateway
RW-CORE-SW#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is not set

      192.168.42.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.42.0/24 is directly connected, Vlan42
L        192.168.42.1/32 is directly connected, Vlan42
RW-CORE-SW#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink-To-RW-ACC-SW-ET0/0
Et0/1                          up             up       
Et0/2                          admin down     down     
Et0/3                          admin down     down     
Vl42                           up             up       
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#ping 192.168.42.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.2, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show interfaces ethernet0/1 switchport
Name: Et0/1
Switchport: Enabled
Administrative Mode: static access
Operational Mode: static access
Administrative Trunking Encapsulation: negotiate
Operational Trunking Encapsulation: native
Negotiation of Trunking: Off
Access Mode VLAN: 42 (VLAN0042)
Trunking Native Mode VLAN: 1 (default)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: ALL
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Protected: false
Appliance trust: none




User Access Verification

Username: cisco
Password: 
RW-ACC-SW>en
Password: 
RW-ACC-SW#show run | hostname
                     ^
% Invalid input detected at '^' marker.

RW-ACC-SW#show run | include hostname
hostname RW-ACC-SW
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.2    YES TFTP   up                    up      
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          42

Port           Vlans allowed and active in management domain
Et0/0          42

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          42
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3
42   VLAN0042                         active    Et0/1, Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
RW-CORE-SW       Eth 0/0           128             R S I  Linux Uni Eth 0/0

Total cdp entries displayed : 1
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show run interface vlan 42
Building configuration...

Current configuration : 63 bytes
!
interface Vlan42
 ip address 192.168.42.2 255.255.255.0
end

RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is not set

      192.168.42.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.42.0/24 is directly connected, Vlan42
L        192.168.42.2/32 is directly connected, Vlan42
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show run | include default gateway
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       
Et0/1                          up             up       
Et0/2                          up             up       
Et0/3                          admin down     down     
Vl42                           up             up     
RW-ACC-SW#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RW-ACC-SW(config)#interface et0/0
RW-ACC-SW(config-if)#description Uplink To RW-CORE-SW Et0/0
RW-ACC-SW(config-if)#end
RW-ACC-SW#write memory
Building configuration...
[OK]
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink To RW-CORE-SW Et0/0
Et0/1                          up             up       
Et0/2                          up             up       
Et0/3                          admin down     down     
Vl42                           up             up       
RW-ACC-SW#

RW-CORE-SW#ping 192.168.42.37
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.37, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#ping 192.168.42.38
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.38, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#ping 192.168.42.39
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.39, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show ip arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.42.1            -   aabb.cc80.0200  ARPA   Vlan42
Internet  192.168.42.2           20   aabb.cc80.0100  ARPA   Vlan42
Internet  192.168.42.37           0   5254.0024.1d40  ARPA   Vlan42
Internet  192.168.42.38           0   5254.0048.eef9  ARPA   Vlan42
Internet  192.168.42.39           0   5254.0083.1986  ARPA   Vlan42
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show mac address-table address 5254.0024.1d40
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0024.1d40    DYNAMIC     Et0/1
Total Mac Addresses for this criterion: 1
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#conf t                                       
Enter configuration commands, one per line.  End with CNTL/Z.
RW-CORE-SW(config)#interface et0/1
RW-CORE-SW(config-if)#description BaristaPOS 192.168.42.37
RW-CORE-SW(config-if)#end
RW-CORE-SW#write memory
Building configuration...
[OK]
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink-To-RW-ACC-SW-ET0/0
Et0/1                          up             up       BaristaPOS 192.168.42.37
Et0/2                          admin down     down     
Et0/3                          admin down     down     
Vl42                           up             up       
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show mac address-table address 5254.0048.eef9
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0048.eef9    DYNAMIC     Et0/0
Total Mac Addresses for this criterion: 1
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show mac address-table address 5254.0083.1986
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0083.1986    DYNAMIC     Et0/0
Total Mac Addresses for this criterion: 1
RW-CORE-SW#


RW-ACC-SW#show mac address-table address 5254.0048.eef9
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0048.eef9    DYNAMIC     Et0/1
Total Mac Addresses for this criterion: 1
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show mac address-table address 5254.0083.1986
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0083.1986    DYNAMIC     Et0/2
Total Mac Addresses for this criterion: 1
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RW-ACC-SW(config)#interface et0/1
RW-ACC-SW(config-if)#description InventoryStation 192.168.42.38
RW-ACC-SW(config-if)#interface et0/2
RW-ACC-SW(config-if)#description ManagerConsole 192.168.42.39
RW-ACC-SW(config-if)#end
RW-ACC-SW#write memory
Building configuration...
[OK]
RW-ACC-SW#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink To RW-CORE-SW Et0/0
Et0/1                          up             up       InventoryStation 192.168.42.38
Et0/2                          up             up       ManagerConsole 192.168.42.39
Et0/3                          admin down     down     
Vl42                           up             up       
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          42

Port           Vlans allowed and active in management domain
Et0/0          42

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          42
RW-ACC-SW#
RW-ACC-SW#show mac address-table address 5254.0048.eef9
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0048.eef9    DYNAMIC     Et0/1
Total Mac Addresses for this criterion: 1
RW-ACC-SW#
RW-ACC-SW#
RW-ACC-SW#show mac address-table address 5254.0083.1986
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0083.1986    DYNAMIC     Et0/2
Total Mac Addresses for this criterion: 1
RW-ACC-SW#


RW-CORE-SW#
RW-CORE-SW#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink-To-RW-ACC-SW-ET0/0
Et0/1                          up             up       BaristaPOS 192.168.42.37
Et0/2                          admin down     down     
Et0/3                          admin down     down     
Vl42                           up             up       
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          42

Port           Vlans allowed and active in management domain
Et0/0          42

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          42
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show mac address-table address 5254.0024.1d40
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0024.1d40    DYNAMIC     Et0/1
Total Mac Addresses for this criterion: 1
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show mac address-table address 5254.0048.eef9
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0048.eef9    DYNAMIC     Et0/0
Total Mac Addresses for this criterion: 1
RW-CORE-SW#
RW-CORE-SW#
RW-CORE-SW#show mac address-table address 5254.0083.1986
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  42    5254.0083.1986    DYNAMIC     Et0/0
Total Mac Addresses for this criterion: 1
RW-CORE-SW#
```
