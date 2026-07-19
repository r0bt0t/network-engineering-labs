# Lab 050 - Raw CLI Output

```bash
Castle-Fallout-RTR>en
Castle-Fallout-RTR#
*Jul 19 17:33:28.584: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Jul 19 17:33:28.584: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
*Jul 19 17:33:28.584: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
Castle-Fallout-RTR#show
*Jul 19 17:33:28.588: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Castle-Fallout-RTR#show runn
*Jul 19 17:33:28.688: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 20 seconds).
*Jul 19 17:33:28.688: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
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
Castle-Fallout-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#interface Ethernet0/0
Castle-Fallout-RTR(config-if)#no shutdown
Castle-Fallout-RTR(config-if)#interface
*Jul 19 17:34:22.496: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Castle-Fallout-RTR(config-if)#interface Eth
*Jul 19 17:34:23.496: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Castle-Fallout-RTR(config-if)#interface Ethernet0/1
Castle-Fallout-RTR(config-if)#no shutdown
Castle-Fallout-RTR(config-if)#end
Castle-Fallout-RTR#
*Jul 19 17:34:45.956: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
*Jul 19 17:34:46.956: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Castle-Fallout-RTR#s
*Jul 19 17:34:46.964: %SYS-5-CONFIG_I: Configured from console by console
Castle-Fallout-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    unassigned
Ethernet0/0.20         [up/up]
    unassigned
Ethernet0/0.30         [up/up]
    unassigned
Ethernet0/0.40         [up/up]
    unassigned
Ethernet0/1            [up/up]
    unassigned
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Fallout-RTR#


Castle-Fallout-RTR#
Castle-Fallout-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#int
Castle-Fallout-RTR(config)#interface Ethe
Castle-Fallout-RTR(config)#interface Ethernet0/0.10
Castle-Fallout-RTR(config-subif)#ipv6 address 2001:DB8:1:4::/64 eui-64
Castle-Fallout-RTR(config-subif)#exit
Castle-Fallout-RTR(config)#interface Ethernet0/0.20             
Castle-Fallout-RTR(config-subif)#ipv6 address 2001:DB8:1:5::/64 eui-64
Castle-Fallout-RTR(config-subif)#exit                                 
Castle-Fallout-RTR(config)#interface Ethernet0/0.30             
Castle-Fallout-RTR(config-subif)#ipv6 address 2001:DB8:1:6::/64 eui-64
Castle-Fallout-RTR(config-subif)#exit                                 
Castle-Fallout-RTR(config)#interface Ethernet0/0.40             
Castle-Fallout-RTR(config-subif)#ipv6 address 2001:DB8:1:7::/64 eui-64
Castle-Fallout-RTR(config-subif)#end                                  
Castle-Fallout-RTR#
*Jul 19 17:37:31.883: %SYS-5-CONFIG_I: Configured from console by console
Castle-Fallout-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:300
    2001:DB8:1:4:A8BB:CCFF:FE00:300
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:300
    2001:DB8:1:5:A8BB:CCFF:FE00:300
Ethernet0/0.30         [up/up]
    FE80::A8BB:CCFF:FE00:300
    2001:DB8:1:6:A8BB:CCFF:FE00:300
Ethernet0/0.40         [up/up]
    FE80::A8BB:CCFF:FE00:300
    2001:DB8:1:7:A8BB:CCFF:FE00:300
Ethernet0/1            [up/up]
    unassigned
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Fallout-RTR#


Castle-Fallout-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#int
Castle-Fallout-RTR(config)#interface  eth
Castle-Fallout-RTR(config)#interface  ethernet0/1
Castle-Fallout-RTR(config-if)#ipv6 address 2001:DB8:1:3::2/64
Castle-Fallout-RTR(config-if)#end
Castle-Fallout-RTR#
*Jul 19 17:39:16.839: %SYS-5-CONFIG_I: Configured from console by console
Castle-Fallout-RTR#show ipv6 interface Ethernet0/1
Ethernet0/1 is up, line protocol is up
  IPv6 is enabled, link-local address is FE80::A8BB:CCFF:FE00:310 
  No Virtual link-local address(es):
  Description: Uplink toward Castle-Cafe-RTR
  Global unicast address(es):
    2001:DB8:1:3::2, subnet is 2001:DB8:1:3::/64 
  Joined group address(es):
    FF02::1
    FF02::2
    FF02::1:FF00:2
    FF02::1:FF00:310
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
Castle-Fallout-RTR#



Castle-Fallout-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#ipv6 route 2001:DB8:1:1::/64 2001:DB8:1:3::1
Castle-Fallout-RTR(config)#ipv6 route 2001:DB8:1:2::/64 2001:DB8:1:3::1
Castle-Fallout-RTR(config)#end
Castle-Fallout-RTR#
*Jul 19 17:41:14.832: %SYS-5-CONFIG_I: Configured from console by console
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
Castle-Fallout-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Fallout-RTR(config)#ipv6 route 2001:DB8:1:4::/64 2001:DB8:1:3::2
% Not allowed to point static routes through yourself
Castle-Fallout-RTR(config)#ipv6 route 2001:DB8:1:5::/64 2001:DB8:1:3::2
% Not allowed to point static routes through yourself
Castle-Fallout-RTR(config)#ipv6 route 2001:DB8:1:5::/64 2001:DB8:1:3::2
% Not allowed to point static routes through yourself
Castle-Fallout-RTR(config)#
Castle-Fallout-RTR(config)#
Castle-Fallout-RTR(config)#end
Castle-Fallout-RTR#show 
*Jul 19 17:45:16.299: %SYS-5-CONFIG_I: Configured from console by console
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
Castle-Fallout-RTR#


Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ipv6 route 2001:DB8:1:4::/64 2001:DB8:1:3::2
Castle-Cafe-RTR(config)#ipv6 route 2001:DB8:1:5::/64 2001:DB8:1:3::2
Castle-Cafe-RTR(config)#ipv6 route 2001:DB8:1:6::/64 2001:DB8:1:3::2
Castle-Cafe-RTR(config)#ipv6 route 2001:DB8:1:7::/64 2001:DB8:1:3::2
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#sho
*Jul 19 17:44:13.051: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ipv6 route static
IPv6 Routing Table - default - 1 entries
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
Castle-Cafe-RTR#show ipv6 route static
IPv6 Routing Table - default - 1 entries
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
Castle-Cafe-RTR#ping 2001:DB8:1:4:A8BB:CCFF:FE01:5B00
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 2001:DB8:1:4:A8BB:CCFF:FE01:5B00, timeout is 2 seconds:

% No valid route for destination
Success rate is 0 percent (0/1)
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#show ipv6 interface brief
Ethernet0/0            [administratively down/down]
    unassigned
Ethernet0/0.10         [administratively down/down]
    FE80::A8BB:CCFF:FE00:400
    2001:DB8:1:1::1
Ethernet0/0.20         [administratively down/down]
    FE80::A8BB:CCFF:FE00:400
    2001:DB8:1:2::1
Ethernet0/1            [administratively down/down]
    FE80::A8BB:CCFF:FE00:410
    2001:DB8:1:3::1
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Cafe-RTR#show running-config | include ipv6
ipv6 unicast-routing
ipv6 cef
 ipv6 address 2001:DB8:1:1::1/64
 ipv6 address 2001:DB8:1:2::1/64
 ipv6 address 2001:DB8:1:3::1/64
ipv6 route 2001:DB8:1:4::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:5::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:6::/64 2001:DB8:1:3::2
ipv6 route 2001:DB8:1:7::/64 2001:DB8:1:3::2
Castle-Cafe-RTR#show running-config | section interface
interface Ethernet0/0
 description Cafe trunk toward distribution switch
 no ip address
 shutdown
interface Ethernet0/0.10
 description Cafe Admin VLAN
 encapsulation dot1Q 10
 ipv6 address 2001:DB8:1:1::1/64
interface Ethernet0/0.20
 description Cafe Management VLAN
 encapsulation dot1Q 20
 ipv6 address 2001:DB8:1:2::1/64
interface Ethernet0/1
 description Uplink toward Castle-Fallout-RTR
 no ip address
 shutdown
 ipv6 address 2001:DB8:1:3::1/64
interface Ethernet0/2
 no ip address
 shutdown
interface Ethernet0/3
 no ip address
 shutdown
Castle-Cafe-RTR#how ipv6 route
                 ^
% Invalid input detected at '^' marker.

Castle-Cafe-RTR#show ipv6 route 2001:DB8:1:3::2
IPv6 Routing Table - default - 1 entries
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
% Route not found
Castle-Cafe-RTR#show ipv6 route                
IPv6 Routing Table - default - 1 entries
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
L   FF00::/8 [0/0]
     via Null0, receive
Castle-Cafe-RTR#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ipv6 unicast-routing
Castle-Cafe-RTR(config)#interface Ethernet0/0
Castle-Cafe-RTR(config-if)# ipv6 address 2001:DB8:1:3::1/64
%Ethernet0/0: Informational: 2001:DB8:1:3::1/64 is in use on shutdown Ethernet0/1
Castle-Cafe-RTR(config-if)# no shutdown
%Ethernet0/0: Informational: 2001:DB8:1:3::/64 is in use on shutdown Ethernet0/1
Castle-Cafe-RTR(config-if)#exit
Castle-Cafe-RTR(config)#
*Jul 19 17:49:17.925: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Castle-Cafe-RTR(config)#
*Jul 19 17:49:18.925: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    FE80::A8BB:CCFF:FE00:400
    2001:DB8:1:3::1
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:400
    2001:DB8:1:1::1
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:400
    2001:DB8:1:2::1
Ethernet0/1            [administratively down/down]
    FE80::A8BB:CCFF:FE00:410
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
     via Ethernet0/0, directly connected
Castle-Cafe-RTR#ping 2001:DB8:1:3::2
*Jul 19 17:49:29.450: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#ping 2001:DB8:1:3::2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 2001:DB8:1:3::2, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
Castle-Cafe-RTR#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#
Castle-Cafe-RTR(config)#interface Ethernet0/0
Castle-Cafe-RTR(config-if)# no ipv6 address 2001:DB8:1:3::1/64
Castle-Cafe-RTR(config-if)# no shutdown
Castle-Cafe-RTR(config-if)# exit
Castle-Cafe-RTR(config)#
Castle-Cafe-RTR(config)#interface Ethernet0/1
Castle-Cafe-RTR(config-if)# no shutdown
Castle-Cafe-RTR(config-if)# exit
Castle-Cafe-RTR(config)#
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Jul 19 17:51:49.478: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#
*Jul 19 17:51:50.380: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
Castle-Cafe-RTR#
*Jul 19 17:51:51.380: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Castle-Cafe-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:400
    2001:DB8:1:1::1
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:400
    2001:DB8:1:2::1
Ethernet0/1            [up/up]
    FE80::A8BB:CCFF:FE00:410
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
Castle-Cafe-RTR#ping 2001:DB8:1:3::2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 2001:DB8:1:3::2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Castle-Cafe-RTR#
```
