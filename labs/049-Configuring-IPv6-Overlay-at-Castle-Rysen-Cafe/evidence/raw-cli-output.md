# Lab 049 - Raw CLI Output

```bash
Connecting to console for Castle-Cafe-RTR

Castle-Cafe-RTR>en
Castle-Cafe-RTR#show ip 
*Jul 19 17:19:58.783: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Castle-Cafe-RTR#show ip inte
*Jul 19 17:19:58.885: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 17:19:58.886: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 17:19:58.991: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Castle-Cafe-RTR#show ip interface
*Jul 19 17:19:59.091: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 19 17:19:59.091: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Castle-Cafe-RTR#show ip interface brief | include Ethernet0/0 
Ethernet0/0            unassigned      YES unset  administratively down down    
Ethernet0/0.10         10.0.18.1       YES TFTP   administratively down down    
Ethernet0/0.20         10.0.18.65      YES TFTP   administratively down down    
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#int
Castle-Cafe-RTR(config)#interface eth
Castle-Cafe-RTR(config)#interface ethernet0/0
Castle-Cafe-RTR(config-if)#no shutdown
Castle-Cafe-RTR(config-if)#end
Castle-Cafe-RTR#
*Jul 19 17:20:39.044: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Castle-Cafe-RTR#sh
*Jul 19 17:20:39.049: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ip
*Jul 19 17:20:40.044: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Castle-Cafe-RTR#show ip interface brief | include ethernet0/0
Castle-Cafe-RTR#show ip interface brief | include Ethernet0/0
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/0.20         10.0.18.65      YES TFTP   up                    up      
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#show running-config interface Ethernet0/0.10
Building configuration...

Current configuration : 128 bytes
!
interface Ethernet0/0.10
 description VLAN 10 Cafe Service
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.192
end

Castle-Cafe-RTR#show running-config interface Ethernet0/0.20
Building configuration...

Current configuration : 132 bytes
!
interface Ethernet0/0.20
 description VLAN 20 Cafe Operations
 encapsulation dot1Q 20
 ip address 10.0.18.65 255.255.255.192
end

Castle-Cafe-RTR#



Castle-Cafe-RTR#
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ipv6 unicast-routing
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Jul 19 17:22:57.459: %SYS-5-CONFIG_I: Configured from console by console
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
Castle-Cafe-RTR#show ipv6 interface brief| include Ethernet0/0
                                         ^
% Invalid input detected at '^' marker.

Castle-Cafe-RTR#show ipv6 interface brief | include Ethernet0/0
Ethernet0/0            [up/up]
Ethernet0/0.10         [up/up]
Ethernet0/0.20         [up/up]
Castle-Cafe-RTR#


Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ipv6 unicast-routing
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Jul 19 17:22:57.459: %SYS-5-CONFIG_I: Configured from console by console
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
Castle-Cafe-RTR#show ipv6 interface brief| include Ethernet0/0
                                         ^
% Invalid input detected at '^' marker.

Castle-Cafe-RTR#show ipv6 interface brief | include Ethernet0/0
Ethernet0/0            [up/up]
Ethernet0/0.10         [up/up]
Ethernet0/0.20         [up/up]
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#interface Ethernet0/0.10
Castle-Cafe-RTR(config-subif)#ipv6 address 2001:DB8:1:1::1/64
Castle-Cafe-RTR(config-subif)#exit
Castle-Cafe-RTR(config)#interface Ethernet0/0.20       
Castle-Cafe-RTR(config-subif)#ipv6 address 2001:DB8:1:2::1/64
Castle-Cafe-RTR(config-subif)#end
Castle-Cafe-RTR#show 
*Jul 19 17:25:05.957: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ipv6 interface brief
Ethernet0/0            [up/up]
    unassigned
Ethernet0/0.10         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:1::1
Ethernet0/0.20         [up/up]
    FE80::A8BB:CCFF:FE00:200
    2001:DB8:1:2::1
Ethernet0/1            [administratively down/down]
    unassigned
Ethernet0/2            [administratively down/down]
    unassigned
Ethernet0/3            [administratively down/down]
    unassigned
Castle-Cafe-RTR#



Castle-Cafe-RTR#show ipv6 interface Ethernet0/0.10
Ethernet0/0.10 is up, line protocol is up
  IPv6 is enabled, link-local address is FE80::A8BB:CCFF:FE00:200 
  No Virtual link-local address(es):
  Description: VLAN 10 Cafe Service
  Global unicast address(es):
    2001:DB8:1:1::1, subnet is 2001:DB8:1:1::/64 
  Joined group address(es):
    FF02::1
    FF02::2
    FF02::1:FF00:1
    FF02::1:FF00:200
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
Castle-Cafe-RTR#
```
