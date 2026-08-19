# Lab 051 - Raw CLI Output

```bash
Castle-Cafe-RTR#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  administratively down down    
Ethernet0/0.10         10.0.18.1       YES TFTP   administratively down down    
Ethernet0/0.20         10.0.18.65      YES TFTP   administratively down down    
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Castle-Cafe-RTR#conf t 
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#interface ethernet0/0
Castle-Cafe-RTR(config-if)#no shutdown
Castle-Cafe-RTR(config-if)#end
Castle-Cafe-RTR#
*Jul 19 19:47:10.929: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Jul 19 19:47:11.929: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Castle-Cafe-RTR#
*Jul 19 19:47:12.036: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/0.20         10.0.18.65      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Castle-Cafe-RTR#
Castle-Cafe-RTR#show running-config interface Ethernet0/0.10
Building configuration...

Current configuration : 133 bytes
!
interface Ethernet0/0.10
 description Cafe VLAN 10 Cafe Service
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.192
end

Castle-Cafe-RTR#show running-config interface Ethernet0/0.20
Building configuration...

Current configuration : 132 bytes
!
interface Ethernet0/0.20
 description Cafe VLAN 20 Operations
 encapsulation dot1Q 20
 ip address 10.0.18.65 255.255.255.192
end

Castle-Cafe-RTR#





Castle-LAN-SW#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Ethernet1/0            unassigned      YES unset  administratively down down    
Ethernet1/1            unassigned      YES unset  up                    up      
Ethernet1/2            unassigned      YES unset  up                    up      
Ethernet1/3            unassigned      YES unset  up                    up      
Castle-LAN-SW#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3, Et1/0, Et1/1, Et1/2
                                                Et1/3
10   VLAN0010                         active    Et0/1
20   VLAN0020                         active    Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0   
10   enet  100010     1500  -      -      -        -    -        0      0   
20   enet  100020     1500  -      -      -        -    -        0      0   
1002 fddi  101002     1500  -      -      -        -    -        0      0   
1003 tr    101003     1500  -      -      -        -    -        0      0   
1004 fdnet 101004     1500  -      -      -        ieee -        0      0   
1005 trnet 101005     1500  -      -      -        ibm  -        0      0   

Remote SPAN VLANs
          
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
------------------------------------------------------------------------------


Primary Secondary Type              Ports
------- --------- ----------------- ------------------------------------------

Castle-LAN-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20

Port           Vlans allowed and active in management domain
Et0/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20
Castle-LAN-SW#





Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ipv6 unicast-routing
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Jul 19 19:51:30.284: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    unassigned
Ethernet0/0.20         [up/up]
    unassigned
Ethernet0/1            [administratively down/down]
    unassigned
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#interface ethernet0/0.10
Castle-Cafe-RTR(config-subif)#ipv6 address 2001:DB8:1:1::1/64
Castle-Cafe-RTR(config-subif)#exit
Castle-Cafe-RTR(config)#interface ethernet0/0.20       
Castle-Cafe-RTR(config-subif)#ipv6 address 2001:DB8:1:2::1/64
Castle-Cafe-RTR(config-subif)#end
Castle-Cafe-RTR#conf t
*Jul 19 19:53:30.654: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:100
    2001:DB8:1:1::1
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:100
    2001:DB8:1:2::1
Ethernet0/1            [administratively down/down]
    unassigned
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Cafe-RTR#show ipv6 interface Ethernet0/0.10
Ethernet0/0.10 is up, line protocol is up
  IPv6 is enabled, link-local address is FE80::A8BB:CCFF:FE00:100 
  No Virtual link-local address(es):
  Description: Cafe VLAN 10 Cafe Service
  Global unicast address(es):
    2001:DB8:1:1::1, subnet is 2001:DB8:1:1::/64 
  Joined group address(es):
    FF02::1
    FF02::2
    FF02::1:FF00:1
    FF02::1:FF00:100
  MTU is 1500 bytes
  ICMP error messages limited to one every 100 milliseconds
  ICMP redirects are enabled
  ICMP unreachables are sent
  ND DAD is enabled, number of DAD attempts: 1
  ND reachable time is 30000 milliseconds (using 30000)
  ND advertised reachable time is 0 (unspecified)
  ND advertised retransmit interval is 0 (unspecified)
  ND router advertisements are sent every 200 seconds
  ND router advertisements live for 1800 seconds
  ND advertised default router preference is Medium
  Hosts use stateless autoconfig for addresses.
Castle-Cafe-RTR#show ipv6 interface Ethernet0/0.20
Ethernet0/0.20 is up, line protocol is up
  IPv6 is enabled, link-local address is FE80::A8BB:CCFF:FE00:100 
  No Virtual link-local address(es):
  Description: Cafe VLAN 20 Operations
  Global unicast address(es):
    2001:DB8:1:2::1, subnet is 2001:DB8:1:2::/64 
  Joined group address(es):
    FF02::1
    FF02::2
    FF02::1:FF00:1
    FF02::1:FF00:100
  MTU is 1500 bytes
  ICMP error messages limited to one every 100 milliseconds
  ICMP redirects are enabled
  ICMP unreachables are sent
  ND DAD is enabled, number of DAD attempts: 1
  ND reachable time is 30000 milliseconds (using 30000)
  ND advertised reachable time is 0 (unspecified)
  ND advertised retransmit interval is 0 (unspecified)
  ND router advertisements are sent every 200 seconds
  ND router advertisements live for 1800 seconds
  ND advertised default router preference is Medium
  Hosts use stateless autoconfig for addresses.
Castle-Cafe-RTR#




Castle-Fallout-RTR>en
Password: 
Castle-Fallout-RTR#
Castle-Fallout-RTR#
Castle-Fallout-RTR#
Castle-Fallout-RTR#
Castle-Fallout-RTR#
Castle-Fallout-RTR#show running-config | include ipv6 unicast-routing
ipv6 unicast-routing
Castle-Fallout-RTR#show ipv6 interface brief
Ethernet0/0            [administratively down/down]
    unassigned
Ethernet0/0.10         [administratively down/down]
    unassigned
Ethernet0/0.20         [administratively down/down]
    unassigned
Ethernet0/0.30         [administratively down/down]
    unassigned
Ethernet0/0.40         [administratively down/down]
    unassigned
Ethernet0/1            [administratively down/down]
    unassigned
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Fallout-RTR#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#interface Ethernet0/0
Castle-Fallout-RTR(config-if)#no shutdown
Castle-Fallout-RTR(config-if)#interface Ethernet0/1
Castle-Fallout-RTR(config-if)#no shutdown
Castle-Fallout-RTR(config-if)#end
Castle-Fallout-RTR#
*Jul 19 19:59:53.367: %SYS-5-CONFIG_I: Configured from console by console
Castle-Fallout-RTR#
*Jul 19 19:59:53.367: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Jul 19 19:59:53.372: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
Castle-Fallout-RTR#
*Jul 19 19:59:54.367: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
*Jul 19 19:59:54.372: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Castle-Fallout-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#interface ethernet0/0.10
Castle-Fallout-RTR(config-subif)#ipv6 address 2001:DB8:1:4::/64 eui-64
Castle-Fallout-RTR(config-subif)#exit
Castle-Fallout-RTR(config)#interface ethernet0/0.20             
Castle-Fallout-RTR(config-subif)#ipv6 address 2001:DB8:1:5::/64 eui-64
Castle-Fallout-RTR(config-subif)#exit
Castle-Fallout-RTR(config)#interface ethernet0/0.30             
Castle-Fallout-RTR(config-subif)#ipv6 address 2001:DB8:1:6::/64 eui-64
Castle-Fallout-RTR(config-subif)#exit
Castle-Fallout-RTR(config)#interface ethernet0/0.40             
Castle-Fallout-RTR(config-subif)#ipv6 address 2001:DB8:1:7::/64 eui-64
Castle-Fallout-RTR(config-subif)#exit
Castle-Fallout-RTR(config)#end
Castle-Fallout-RTR#
*Jul 19 20:03:02.211: %SYS-5-CONFIG_I: Configured from console by console
Castle-Fallout-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:4:A8BB:CCFF:FE00:200
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:5:A8BB:CCFF:FE00:200
Ethernet0/0.30         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:6:A8BB:CCFF:FE00:200
Ethernet0/0.40         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:7:A8BB:CCFF:FE00:200
Ethernet0/1            [up/up]
    unassigned
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Fallout-RTR#




Shelter-Sector-SW#
Shelter-Sector-SW#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  up                    up      
Ethernet1/1            unassigned      YES unset  up                    up      
Ethernet1/2            unassigned      YES unset  up                    up      
Ethernet1/3            unassigned      YES unset  up                    up      
Shelter-Sector-SW#show vlans

No Virtual LANs configured.

Shelter-Sector-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/0          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20,30,40
Shelter-Sector-SW#




Castle-Fallout-RTR#
Castle-Fallout-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#interface ethernet0/1
Castle-Fallout-RTR(config-if)#description IPv6 uplink to Castle-Cafe-RTR   
Castle-Fallout-RTR(config-if)#ipv6 address 2001:DB8:1:3::2/64
Castle-Fallout-RTR(config-if)#no shutdown 
Castle-Fallout-RTR(config-if)#end
Castle-Fallout-RTR#show i
*Jul 19 20:16:13.535: %SYS-5-CONFIG_I: Configured from console by console
Castle-Fallout-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:4:A8BB:CCFF:FE00:200
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:5:A8BB:CCFF:FE00:200
Ethernet0/0.30         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:6:A8BB:CCFF:FE00:200
Ethernet0/0.40         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:7:A8BB:CCFF:FE00:200
Ethernet0/1            [up/up]
    FE80::A8BB:CCFF:FE00:210
    2001:DB8:1:3::2
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Fallout-RTR#ping ipv6 2001:DB8:1:3::1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 2001:DB8:1:3::1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Castle-Fallout-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#ipv6 route 2001:DB8:1:1::/64 2001:DB8:1:3::1
Castle-Fallout-RTR(config)#ipv6 route 2001:DB8:1:2::/64 2001:DB8:1:3::1
Castle-Fallout-RTR(config)#end
Castle-Fallout-RTR#
*Jul 19 20:18:17.597: %SYS-5-CONFIG_I: Configured from console by console
Castle-Fallout-RTR#show ipv6 route static
IPv6 Routing Table - default - 13 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, R - RIP, H - NHRP, HG - NHRP registered
       Hg - NHRP registration summary, HE - NHRP External, I1 - ISIS L1
       I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
       EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
       NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
       OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
       ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
       ld - LISP dyn-eid, lA - LISP away, le - LISP extranet-policy
       lp - LISP publications, ls - LISP destinations-summary, a - Application
       m - OMP
S   2001:DB8:1:1::/64 [1/0]
     via 2001:DB8:1:3::1
S   2001:DB8:1:2::/64 [1/0]
     via 2001:DB8:1:3::1
Castle-Fallout-RTR#show running-config | include ^ipv6 route
ipv6 route 2001:DB8:1:1::/64 2001:DB8:1:3::1
ipv6 route 2001:DB8:1:2::/64 2001:DB8:1:3::1
Castle-Fallout-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:4:A8BB:CCFF:FE00:200
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:5:A8BB:CCFF:FE00:200
Ethernet0/0.30         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:6:A8BB:CCFF:FE00:200
Ethernet0/0.40         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:7:A8BB:CCFF:FE00:200
Ethernet0/1            [up/up]
    FE80::A8BB:CCFF:FE00:210
    2001:DB8:1:3::2
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Fallout-RTR#show ipv6 route connected
IPv6 Routing Table - default - 13 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, R - RIP, H - NHRP, HG - NHRP registered
       Hg - NHRP registration summary, HE - NHRP External, I1 - ISIS L1
       I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
       EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
       NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
       OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
       ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
       ld - LISP dyn-eid, lA - LISP away, le - LISP extranet-policy
       lp - LISP publications, ls - LISP destinations-summary, a - Application
       m - OMP
C   2001:DB8:1:3::/64 [0/0]
     via Ethernet0/1, directly connected
C   2001:DB8:1:4::/64 [0/0]
     via Ethernet0/0.10, directly connected
C   2001:DB8:1:5::/64 [0/0]
     via Ethernet0/0.20, directly connected
C   2001:DB8:1:6::/64 [0/0]
     via Ethernet0/0.30, directly connected
C   2001:DB8:1:7::/64 [0/0]
     via Ethernet0/0.40, directly connected
Castle-Fallout-RTR#show ipv6 route static
IPv6 Routing Table - default - 13 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, R - RIP, H - NHRP, HG - NHRP registered
       Hg - NHRP registration summary, HE - NHRP External, I1 - ISIS L1
       I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
       EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
       NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
       OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
       ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
       ld - LISP dyn-eid, lA - LISP away, le - LISP extranet-policy
       lp - LISP publications, ls - LISP destinations-summary, a - Application
       m - OMP
S   2001:DB8:1:1::/64 [1/0]
     via 2001:DB8:1:3::1
S   2001:DB8:1:2::/64 [1/0]
     via 2001:DB8:1:3::1
Castle-Fallout-RTR#show running-config | include ^ipv6 route
ipv6 route 2001:DB8:1:1::/64 2001:DB8:1:3::1
ipv6 route 2001:DB8:1:2::/64 2001:DB8:1:3::1





Castle-Cafe-RTR>en
Password: 
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#interface ethernet0/1 
Castle-Cafe-RTR(config-if)#description IPv6 Uplink to Castle-Fallout-RTR
Castle-Cafe-RTR(config-if)#ipv6 address 2001:DB8:1:3::1/64
Castle-Cafe-RTR(config-if)#no shutdown
Castle-Cafe-RTR(config-if)#end
Castle-Cafe-RTR#
*Jul 19 20:14:56.178: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#
*Jul 19 20:14:56.774: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
Castle-Cafe-RTR#
*Jul 19 20:14:57.774: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Castle-Cafe-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:100
    2001:DB8:1:1::1
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:100
    2001:DB8:1:2::1
Ethernet0/1            [up/up]
    FE80::A8BB:CCFF:FE00:110
    2001:DB8:1:3::1
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Cafe-RTR#show ipv6 route 2001:DB8:1:3::/64
Routing entry for 2001:DB8:1:3::/64
  Known via "connected", distance 0, metric 0, type connected
  Route count is 1/1, share count 0
  Routing paths:
    directly connected via Ethernet0/1
      Route metric is 0, traffic share count is 1
      Last updated 00:01:51 ago

Castle-Cafe-RTR#ping ipv6 2001:DB8:1:3::2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 2001:DB8:1:3::2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/3 ms
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ipv6 route 2001:DB8:1:4::/64 2001:DB8:1:3::2
Castle-Cafe-RTR(config)#ipv6 route 2001:DB8:1:5::/64 2001:DB8:1:3::2
Castle-Cafe-RTR(config)#ipv6 route 2001:DB8:1:6::/64 2001:DB8:1:3::2
Castle-Cafe-RTR(config)#ipv6 route 2001:DB8:1:7::/64 2001:DB8:1:3::2
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Jul 19 20:19:31.889: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ipv6 route static
IPv6 Routing Table - default - 11 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, R - RIP, H - NHRP, HG - NHRP registered
       Hg - NHRP registration summary, HE - NHRP External, I1 - ISIS L1
       I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
       EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
       NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
       OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
       ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
       ld - LISP dyn-eid, lA - LISP away, le - LISP extranet-policy
       lp - LISP publications, ls - LISP destinations-summary, a - Application
       m - OMP
S   2001:DB8:1:4::/64 [1/0]
     via 2001:DB8:1:3::2
S   2001:DB8:1:5::/64 [1/0]
     via 2001:DB8:1:3::2
S   2001:DB8:1:6::/64 [1/0]
     via 2001:DB8:1:3::2
S   2001:DB8:1:7::/64 [1/0]
     via 2001:DB8:1:3::2
Castle-Cafe-RTR#show running-config | include ^ipv6 route
ipv6 route 2001:DB8:1:4::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:5::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:6::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:7::/64 2001:DB8:1:3::2
Castle-Cafe-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:100
    2001:DB8:1:1::1
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:100
    2001:DB8:1:2::1
Ethernet0/1            [up/up]
    FE80::A8BB:CCFF:FE00:110
    2001:DB8:1:3::1
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Cafe-RTR#show ipv6 route connected
IPv6 Routing Table - default - 11 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, R - RIP, H - NHRP, HG - NHRP registered
       Hg - NHRP registration summary, HE - NHRP External, I1 - ISIS L1
       I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
       EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
       NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
       OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
       ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
       ld - LISP dyn-eid, lA - LISP away, le - LISP extranet-policy
       lp - LISP publications, ls - LISP destinations-summary, a - Application
       m - OMP
C   2001:DB8:1:1::/64 [0/0]
     via Ethernet0/0.10, directly connected
C   2001:DB8:1:2::/64 [0/0]
     via Ethernet0/0.20, directly connected
C   2001:DB8:1:3::/64 [0/0]
     via Ethernet0/1, directly connected
Castle-Cafe-RTR#show ipv6 route static
IPv6 Routing Table - default - 11 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       B - BGP, R - RIP, H - NHRP, HG - NHRP registered
       Hg - NHRP registration summary, HE - NHRP External, I1 - ISIS L1
       I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary, D - EIGRP
       EX - EIGRP external, ND - ND Default, NDp - ND Prefix, DCE - Destination
       NDr - Redirect, RL - RPL, O - OSPF Intra, OI - OSPF Inter
       OE1 - OSPF ext 1, OE2 - OSPF ext 2, ON1 - OSPF NSSA ext 1
       ON2 - OSPF NSSA ext 2, la - LISP alt, lr - LISP site-registrations
       ld - LISP dyn-eid, lA - LISP away, le - LISP extranet-policy
       lp - LISP publications, ls - LISP destinations-summary, a - Application
       m - OMP
S   2001:DB8:1:4::/64 [1/0]
     via 2001:DB8:1:3::2
S   2001:DB8:1:5::/64 [1/0]
     via 2001:DB8:1:3::2
S   2001:DB8:1:6::/64 [1/0]
     via 2001:DB8:1:3::2
S   2001:DB8:1:7::/64 [1/0]
     via 2001:DB8:1:3::2
Castle-Cafe-RTR#show running-config | include ^ipv6 route
ipv6 route 2001:DB8:1:4::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:5::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:6::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:7::/64 2001:DB8:1:3::2
```
