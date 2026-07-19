# Lab 046 - Raw CLI Output

```bash
Connecting to console for Cafe-R1

Cafe-R1>en
Cafe-R1#show running-con
*Jul 19 13:14:35.591: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-R1#show running-config
*Jul 19 13:14:35.692: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 13:14:35.693: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 13:14:35.798: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-R1#show running-config 
*Jul 19 13:14:35.898: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 19 13:14:35.898: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-R1#show running-config | section router
router eigrp 15
 network 10.0.18.0 0.0.0.255
router ospf 99
 router-id 15.15.15.10
 passive-interface default
 network 10.0.18.0 0.0.0.255 area 0
 network 172.16.0.0 0.0.0.3 area 0
Cafe-R1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/1            172.16.0.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-R1#show running-config | include ^ip route
ip route 10.0.16.0 255.255.254.0 172.16.0.2
Cafe-R1#show ip route static
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

      10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
S        10.0.16.0/23 [1/0] via 172.16.0.2
Cafe-R1#ping 10.0.18.1 source 10.0.16.1
% Invalid source address- IP address not on any of our up interfaces
Cafe-R1#ping 10.0.18.1 source 10.0.17.1
% Invalid source address- IP address not on any of our up interfaces
Cafe-R1#ping 172.16.0.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.16.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#no router eigrp 15
Cafe-R1(config)#no router ospf 99
Cafe-R1(config)#end
Cafe-R1#
*Jul 19 13:30:02.513: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#show running-config | section ^router
Cafe-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Cafe-R1#show ip route
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

      10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
S        10.0.16.0/23 [1/0] via 172.16.0.2
C        10.0.18.0/27 is directly connected, Ethernet0/0.10
L        10.0.18.1/32 is directly connected, Ethernet0/0.10
      172.16.0.0/16 is variably subnetted, 2 subnets, 2 masks
C        172.16.0.0/30 is directly connected, Ethernet0/1
L        172.16.0.1/32 is directly connected, Ethernet0/1
Cafe-R1#ping 172.16.0.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.16.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#
Cafe-R1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/1            172.16.0.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-R1#


Connecting to console for Shelter-R1
Escape character is '^]'.

Shelter-R1>en
Shelter-R1#show running-
*Jul 19 13:17:01.621: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul 19 13:17:01.723: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 13:17:01.724: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 13:17:01.830: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Shelter-R1#show running-
*Jul 19 13:17:01.930: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 19 13:17:01.930: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Shelter-R1#show running-config | section router
router eigrp 12
 network 10.0.16.0 0.0.0.255
 network 10.0.17.0 0.0.0.255
 passive-interface default
router ospf 50
 router-id 25.25.25.25
 passive-interface Ethernet0/2.110
 passive-interface Ethernet0/2.120
 network 10.0.16.0 0.0.0.255 area 0
 network 10.0.17.0 0.0.0.255 area 0
 network 172.16.0.0 0.0.0.3 area 0
Shelter-R1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            216.0.5.2       YES TFTP   up                    up      
Ethernet0/1            172.16.0.2      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES TFTP   up                    up      
Ethernet0/2.110        10.0.16.1       YES TFTP   up                    up      
Ethernet0/2.120        10.0.17.1       YES TFTP   up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Shelter-R1#show running-config | include ^ip route
ip route 0.0.0.0 0.0.0.0 216.0.5.1
Shelter-R1#show ip route static
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

Gateway of last resort is 216.0.5.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 216.0.5.1
Shelter-R1#ip route 10.0.18.0 255.255.255.224 172.16.0.1
              ^
% Invalid input detected at '^' marker.

Shelter-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#ip route 10.0.18.0 255.255.255.224 172.16.0.1
Shelter-R1(config)#exit
Shelter-R1#
*Jul 19 13:25:57.195: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show ip route 10.0.18.0
Routing entry for 10.0.18.0/27
  Known via "static", distance 1, metric 0
  Routing Descriptor Blocks:
  * 172.16.0.1
      Route metric is 0, traffic share count is 1
Shelter-R1#ping 172.16.0.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.16.0.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#ping 10.0.18.1 source 10.0.16.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.16.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#no router eigrp 12
Shelter-R1(config)#no router ospf 50
Shelter-R1(config)#end
Shelter-R1#
*Jul 19 13:30:14.673: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show running-config | section ^router
Shelter-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Shelter-R1#show ip route
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

Gateway of last resort is 216.0.5.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 216.0.5.1
      10.0.0.0/8 is variably subnetted, 5 subnets, 3 masks
C        10.0.16.0/24 is directly connected, Ethernet0/2.110
L        10.0.16.1/32 is directly connected, Ethernet0/2.110
C        10.0.17.0/24 is directly connected, Ethernet0/2.120
L        10.0.17.1/32 is directly connected, Ethernet0/2.120
S        10.0.18.0/27 [1/0] via 172.16.0.1
      172.16.0.0/16 is variably subnetted, 2 subnets, 2 masks
C        172.16.0.0/30 is directly connected, Ethernet0/1
L        172.16.0.2/32 is directly connected, Ethernet0/1
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/0
L        216.0.5.2/32 is directly connected, Ethernet0/0
Shelter-R1#ping 10.0.18.1 source 10.0.16.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.16.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#
Shelter-R1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            216.0.5.2       YES TFTP   up                    up      
Ethernet0/1            172.16.0.2      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES TFTP   up                    up      
Ethernet0/2.110        10.0.16.1       YES TFTP   up                    up      
Ethernet0/2.120        10.0.17.1       YES TFTP   up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Shelter-R1#


Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#no router eigrp 15
Cafe-R1(config)#no router ospf 99
Cafe-R1(config)#end
Cafe-R1#
*Jul 19 13:30:02.513: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#show running-config | section ^router
Cafe-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Cafe-R1#show ip route
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

      10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
S        10.0.16.0/23 [1/0] via 172.16.0.2
C        10.0.18.0/27 is directly connected, Ethernet0/0.10
L        10.0.18.1/32 is directly connected, Ethernet0/0.10
      172.16.0.0/16 is variably subnetted, 2 subnets, 2 masks
C        172.16.0.0/30 is directly connected, Ethernet0/1
L        172.16.0.1/32 is directly connected, Ethernet0/1
Cafe-R1#ping 172.16.0.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.16.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/1            172.16.0.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-R1#
Cafe-R1#
Cafe-R1#
Cafe-R1#
Cafe-R1#
Cafe-R1#show running-config | section ^router
Cafe-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#router ospf 1
Cafe-R1(config-router)# passive-interface default
Cafe-R1(config-router)# no passive-interface Ethernet0/1
Cafe-R1(config-router)# network 10.0.18.0 0.0.0.31 area 0
Cafe-R1(config-router)# network 172.16.0.0 0.0.0.3 area 0
Cafe-R1(config-router)#end
*Jul 19 13:43:42.659: %OSPF-6-DFT_OPT: Protocol timers for fast convergence are Enabled.
Cafe-R1(config-router)#end
Cafe-R1#
*Jul 19 13:43:52.177: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#show running-config | section ^router ospf
router ospf 1
 passive-interface default
 no passive-interface Ethernet0/1
 network 10.0.18.0 0.0.0.31 area 0
 network 172.16.0.0 0.0.0.3 area 0
Cafe-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Routing Protocol is "ospf 1"
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Router ID 172.16.0.1
  Number of areas in this router is 1. 1 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    10.0.18.0 0.0.0.31 area 0
    172.16.0.0 0.0.0.3 area 0
  Passive Interface(s):
          
Cafe-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/1        1     0               172.16.0.1/30      10    P2P   0/0
Et0/0.10     1     0               10.0.18.1/27       10    DR    0/0
Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#interface Ethernet0/1
Cafe-R1(config-if)# ip ospf network point-to-point
Cafe-R1(config-if)#end
Cafe-R1#
*Jul 19 13:49:29.617: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/1        1     0               172.16.0.1/30      10    P2P   0/0
Et0/0.10     1     0               10.0.18.1/27       10    DR    0/0
Cafe-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/1        1     0               172.16.0.1/30      10    P2P   0/0
Et0/0.10     1     0               10.0.18.1/27       10    DR    0/0
Cafe-R1#clear ip ospf process
Reset ALL OSPF processes? [no]: yes
Cafe-R1#show ip ospf neighbor
Cafe-R1#show running-config interface Ethernet0/1
Building configuration...

Current configuration : 187 bytes
!
interface Ethernet0/1
 description Transit to Shelter-R1
 ip address 172.16.0.1 255.255.255.252
 ip ospf network point-to-point
 ip ospf dead-interval 20
 ip ospf hello-interval 5
end

Cafe-R1#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.1/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 172.16.0.1, Network Type POINT_TO_POINT, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State POINT_TO_POINT
  Timer intervals configured, Hello 5, Dead 20, Wait 20, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:00
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/2/2, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 0, Adjacent neighbor count is 0 
  Suppress hello for 0 neighbor(s)
Cafe-R1#show ip interface Ethernet0/1
Ethernet0/1 is up, line protocol is up
  Internet address is 172.16.0.1/30
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Multicast reserved groups joined: 224.0.0.5
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#interface Ethernet0/1
Cafe-R1(config-if)# no ip ospf hello-interval
Cafe-R1(config-if)# no ip ospf dead-interval
Cafe-R1(config-if)#end
Cafe-R1#
*Jul 19 13:59:36.135: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#
*Jul 19 13:59:40.284: %OSPF-5-ADJCHG: Process 1, Nbr 216.0.5.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1#show ospf neighbor
Cafe-R1#show ospf neighbors
                          ^
% Invalid input detected at '^' marker.

Cafe-R1#show ip ospf neighbors
                             ^
% Invalid input detected at '^' marker.

Cafe-R1#show ip ospf neighbor 

Neighbor ID     Pri   State           Dead Time   Address         Interface
216.0.5.2         0   FULL/  -        00:00:31    172.16.0.2      Ethernet0/1
Cafe-R1#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.1/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 172.16.0.1, Network Type POINT_TO_POINT, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State POINT_TO_POINT
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:05
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/2/2, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1 
    Adjacent with neighbor 216.0.5.2
  Suppress hello for 0 neighbor(s)
Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#no ip route 10.0.16.0 255.255.254.0 172.16.0.2
Cafe-R1(config)#end
Cafe-R1#
*Jul 19 14:01:59.549: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#show ip route ospf
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

      10.0.0.0/8 is variably subnetted, 4 subnets, 3 masks
O        10.0.16.0/24 [110/20] via 172.16.0.2, 00:02:48, Ethernet0/1
O        10.0.17.0/24 [110/20] via 172.16.0.2, 00:02:48, Ethernet0/1
Cafe-R1#


Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#no router eigrp 12
Shelter-R1(config)#no router ospf 50
Shelter-R1(config)#end
Shelter-R1#
*Jul 19 13:30:14.673: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show running-config | section ^router
Shelter-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Shelter-R1#show ip route
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

Gateway of last resort is 216.0.5.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 216.0.5.1
      10.0.0.0/8 is variably subnetted, 5 subnets, 3 masks
C        10.0.16.0/24 is directly connected, Ethernet0/2.110
L        10.0.16.1/32 is directly connected, Ethernet0/2.110
C        10.0.17.0/24 is directly connected, Ethernet0/2.120
L        10.0.17.1/32 is directly connected, Ethernet0/2.120
S        10.0.18.0/27 [1/0] via 172.16.0.1
      172.16.0.0/16 is variably subnetted, 2 subnets, 2 masks
C        172.16.0.0/30 is directly connected, Ethernet0/1
L        172.16.0.2/32 is directly connected, Ethernet0/1
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/0
L        216.0.5.2/32 is directly connected, Ethernet0/0
Shelter-R1#ping 10.0.18.1 source 10.0.16.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.16.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            216.0.5.2       YES TFTP   up                    up      
Ethernet0/1            172.16.0.2      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES TFTP   up                    up      
Ethernet0/2.110        10.0.16.1       YES TFTP   up                    up      
Ethernet0/2.120        10.0.17.1       YES TFTP   up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Shelter-R1#
Shelter-R1#
Shelter-R1#
Shelter-R1#
Shelter-R1#
Shelter-R1#
Shelter-R1#show running-config | section ^router
Shelter-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Shelter-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)#
*Jul 19 13:37:25.014: %OSPF-6-DFT_OPT: Protocol timers for fast convergence are Enabled.
Shelter-R1(config-router)#passive interface default
                                   ^
% Invalid input detected at '^' marker.

Shelter-R1(config-router)#passive-interface default
Shelter-R1(config-router)#no passive-interface ethernet0/1
Shelter-R1(config-router)#network 10.0.18.0 0.0.0.31 area 0
Shelter-R1(config-router)#network 172.16.0.0 0.0.0.3 area 0
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 19 13:39:09.250: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show running-config | section ^router ospf
router ospf 1
 passive-interface default
 no passive-interface Ethernet0/1
 network 10.0.18.0 0.0.0.31 area 0
 network 172.16.0.0 0.0.0.3 area 0
Shelter-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Routing Protocol is "ospf 1"
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Router ID 216.0.5.2
  Number of areas in this router is 1. 1 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    10.0.18.0 0.0.0.31 area 0
    172.16.0.0 0.0.0.3 area 0
  Passive Interface(s):
          
Shelter-R1#how ip ospf interface brief
            ^
% Invalid input detected at '^' marker.

Shelter-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)#no network 10.0.18.0 0.0.0.31 area 0
Shelter-R1(config-router)#no network 172.16.0.0 0.0.0.3 area 0
Shelter-R1(config-router)#network 172.16.0.0 0.0.0.3 area 0
Shelter-R1(config-router)#network 10.0.16.0 0.0.0.255 area 0
Shelter-R1(config-router)#network 10.0.17.0 0.0.0.255 area 0
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 19 13:43:09.382: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show ip ospf neighbor
Shelter-R1#show running-config | section ^router ospf
router ospf 1
 passive-interface default
 no passive-interface Ethernet0/1
 network 10.0.16.0 0.0.0.255 area 0
 network 10.0.17.0 0.0.0.255 area 0
 network 172.16.0.0 0.0.0.3 area 0
Shelter-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Routing Protocol is "ospf 1"
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Router ID 216.0.5.2
  Number of areas in this router is 1. 1 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    10.0.16.0 0.0.0.255 area 0
    10.0.17.0 0.0.0.255 area 0
    172.16.0.0 0.0.0.3 area 0
          
Shelter-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/2.120    1     0               10.0.17.1/24       10    DR    0/0
Et0/2.110    1     0               10.0.16.1/24       10    DR    0/0
Et0/1        1     0               172.16.0.2/30      10    DR    0/0
Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#interface Ethernet0/1
Shelter-R1(config-if)# ip ospf network point-to-point
Shelter-R1(config-if)#end
Shelter-R1#
*Jul 19 13:49:43.349: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/2.120    1     0               10.0.17.1/24       10    DR    0/0
Et0/2.110    1     0               10.0.16.1/24       10    DR    0/0
Et0/1        1     0               172.16.0.2/30      10    P2P   0/0
Shelter-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/2.120    1     0               10.0.17.1/24       10    DR    0/0
Et0/2.110    1     0               10.0.16.1/24       10    DR    0/0
Et0/1        1     0               172.16.0.2/30      10    P2P   0/0
Shelter-R1#clear ip ospf process
Reset ALL OSPF processes? [no]: yes
Shelter-R1#show ip ospf neighbor
Shelter-R1#show running-config interface Ethernet0/1
Building configuration...

Current configuration : 132 bytes
!
interface Ethernet0/1
 description Transit to Cafe-R1
 ip address 172.16.0.2 255.255.255.252
 ip ospf network point-to-point
end

Shelter-R1#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.2/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 216.0.5.2, Network Type POINT_TO_POINT, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State POINT_TO_POINT
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:02
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 0, Adjacent neighbor count is 0 
  Suppress hello for 0 neighbor(s)
Shelter-R1#show ip interface Ethernet0/1
Ethernet0/1 is up, line protocol is up
  Internet address is 172.16.0.2/30
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Multicast reserved groups joined: 224.0.0.5
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
Shelter-R1#
*Jul 19 13:59:40.284: %OSPF-5-ADJCHG: Process 1, Nbr 172.16.0.1 on Ethernet0/1 from LOADING to FULL, Loading Done
Shelter-R1#
Shelter-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
172.16.0.1        0   FULL/  -        00:00:32    172.16.0.1      Ethernet0/1
Shelter-R1#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.2/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 216.0.5.2, Network Type POINT_TO_POINT, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State POINT_TO_POINT
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:09
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1 
    Adjacent with neighbor 172.16.0.1
  Suppress hello for 0 neighbor(s)
Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#no ip route 10.0.18.0 255.255.255.224 172.16.0.1
Shelter-R1(config)#end
Shelter-R1#
*Jul 19 14:02:10.470: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show ip route ospf
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

Gateway of last resort is 216.0.5.1 to network 0.0.0.0

      10.0.0.0/8 is variably subnetted, 5 subnets, 3 masks
O        10.0.18.0/27 [110/20] via 172.16.0.1, 00:00:12, Ethernet0/1
Shelter-R1#


Cafe-R1#
Cafe-R1#debug ip ospf adj
OSPF adjacency debugging is on
Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#interface Ethernet0/1
Cafe-R1(config-if)# no ip ospf hello-interval
Cafe-R1(config-if)# no ip ospf dead-interval
Cafe-R1(config-if)# no ip ospf network point-to-point
Cafe-R1(config-if)#end
*Jul 19 14:07:38.185: OSPF-1 ADJ   Et0/1: Interface going Down
*Jul 19 14:07:38.185: OSPF-1 ADJ   Et0/1: 216.0.5.2 address 172.16.0.2 is dead, state DOWN
*Jul 19 14:07:38.185: %OSPF-5-ADJCHG: Process 1, Nbr 216.0.5.2 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Interface down or detached
Cafe-R1(config-if)#end
Cafe-R1#
*Jul 19 14:07:38.185: OSPF-1 ADJ   Et0/1: 172.16.0.1 address 172.16.0.1 is dead, state DOWN
*Jul 19 14:07:38.185: OSPF-1 ADJ   Et0/1: Interface going Up
*Jul 19 14:07:38.186: OSPF-1 ADJ   Et0/1: 2 Way Communication to 216.0.5.2, state 2WAY
*Jul 19 14:07:38.186: OSPF-1 ADJ   Et0/1: Rcv DBD from 216.0.5.2 seq 0x1D08 opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jul 19 14:07:38.186: OSPF-1 ADJ   Et0/1: Nbr state is 2WAY
Cafe-R1#
*Jul 19 14:07:39.681: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#
*Jul 19 14:07:42.946: OSPF-1 ADJ   Et0/1: Rcv DBD from 216.0.5.2 seq 0x1D08 opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jul 19 14:07:42.946: OSPF-1 ADJ   Et0/1: Nbr state is 2WAY
Cafe-R1#
*Jul 19 14:07:47.643: OSPF-1 ADJ   Et0/1: Rcv DBD from 216.0.5.2 seq 0x1D08 opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jul 19 14:07:47.643: OSPF-1 ADJ   Et0/1: Nbr state is 2WAY
Cafe-R1#
*Jul 19 14:07:52.415: OSPF-1 ADJ   Et0/1: Rcv DBD from 216.0.5.2 seq 0x1D08 opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jul 19 14:07:52.415: OSPF-1 ADJ   Et0/1: Nbr state is 2WAY
Cafe-R1#
*Jul 19 14:07:57.082: OSPF-1 ADJ   Et0/1: Rcv DBD from 216.0.5.2 seq 0x1D08 opt 0x52 flag 0x7 len 32  mtu 1500 state 2WAY
*Jul 19 14:07:57.082: OSPF-1 ADJ   Et0/1: Nbr state is 2WAY
Cafe-R1#
*Jul 19 14:07:59.432: OSPF-1 ADJ   Et0/1: Cannot see ourself in hello from 216.0.5.2, state INIT
*Jul 19 14:07:59.433: OSPF-1 ADJ   Et0/1: 2 Way Communication to 216.0.5.2, state 2WAY
Cafe-R1#
*Jul 19 14:08:18.185: OSPF-1 ADJ   Et0/1: end of Wait on interface
*Jul 19 14:08:18.185: OSPF-1 ADJ   Et0/1: DR/BDR election
*Jul 19 14:08:18.185: OSPF-1 ADJ   Et0/1: Elect BDR 216.0.5.2
*Jul 19 14:08:18.185: OSPF-1 ADJ   Et0/1: Elect DR 216.0.5.2
*Jul 19 14:08:18.185: OSPF-1 ADJ   Et0/1: DR: 216.0.5.2 (Id)
*Jul 19 14:08:18.185: OSPF-1 ADJ   Et0/1:    BDR: 216.0.5.2 (Id)
*Jul 19 14:08:18.185: OSPF-1 ADJ   Et0/1: Nbr 216.0.5.2: Prepare dbase exchange
*Jul 19 14:08:18.185: OSPF-1 ADJ   Et0/1: Send DBD to 216.0.5.2 seq 0xBD1 opt 0x52 flag 0x7 len 32
Cafe-R1#
*Jul 19 14:08:22.766: OSPF-1 ADJ   Et0/1: Send DBD to 216.0.5.2 seq 0xBD1 opt 0x52 flag 0x7 len 32
*Jul 19 14:08:22.766: OSPF-1 ADJ   Et0/1: Retransmitting DBD to 216.0.5.2 [1]
Cafe-R1#
*Jul 19 14:08:27.645: OSPF-1 ADJ   Et0/1: Send DBD to 216.0.5.2 seq 0xBD1 opt 0x52 flag 0x7 len 32
*Jul 19 14:08:27.645: OSPF-1 ADJ   Et0/1: Retransmitting DBD to 216.0.5.2 [2]
Cafe-R1#
*Jul 19 14:08:32.591: OSPF-1 ADJ   Et0/1: Send DBD to 216.0.5.2 seq 0xBD1 opt 0x52 flag 0x7 len 32
*Jul 19 14:08:32.591: OSPF-1 ADJ   Et0/1: Retransmitting DBD to 216.0.5.2 [3]
Cafe-R1#
*Jul 19 14:08:37.098: OSPF-1 ADJ   Et0/1: Send DBD to 216.0.5.2 seq 0xBD1 opt 0x52 flag 0x7 len 32
*Jul 19 14:08:37.098: OSPF-1 ADJ   Et0/1: Retransmitting DBD to 216.0.5.2 [4]
Cafe-R1#
*Jul 19 14:08:39.432: OSPF-1 ADJ   Et0/1: Rcv DBD from 216.0.5.2 seq 0x69B opt 0x52 flag 0x7 len 32  mtu 1500 state EXSTART
*Jul 19 14:08:39.432: OSPF-1 ADJ   Et0/1: NBR Negotiation Done. We are the SLAVE
*Jul 19 14:08:39.432: OSPF-1 ADJ   Et0/1: Nbr 216.0.5.2: Summary list built, size 2
*Jul 19 14:08:39.432: OSPF-1 ADJ   Et0/1: Send DBD to 216.0.5.2 seq 0x69B opt 0x52 flag 0x2 len 72
*Jul 19 14:08:39.433: OSPF-1 ADJ   Et0/1: Rcv DBD from 216.0.5.2 seq 0x69C opt 0x52 flag 0x1 len 72  mtu 1500 state EXCHANGE
*Jul 19 14:08:39.433: OSPF-1 ADJ   Et0/1: Exchange Done with 216.0.5.2
*Jul 19 14:08:39.433: OSPF-1 ADJ   Et0/1: Send LS REQ to 216.0.5.2 length 36
*Jul 19 14:08:39.433: OSPF-1 ADJ   Et0/1: Send DBD to 216.0.5.2 seq 0x69C opt 0x52 flag 0x0 len 32
*Jul 19 14:08:39.433: OSPF-1 ADJ   Et0/1: Rcv LS UPD from Nbr ID 216.0.5.2 length 88 LSA count 1
*Jul 19 14:08:39.433: OSPF-1 ADJ   Et0/1: Synchronized with 216.0.5.2, state FULL
*Jul 19 14:08:39.433: %OSPF-5-ADJCHG: Process 1, Nbr 216.0.5.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1#
*Jul 19 14:08:39.433: OSPF-1 ADJ   Et0/1: Rcv LS REQ from 216.0.5.2 length 36 LSA count 1
Cafe-R1#
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: Neighbor change event
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: DR/BDR election
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: Elect BDR 172.16.0.1
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: Elect DR 216.0.5.2
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: Elect BDR 172.16.0.1
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: Elect DR 216.0.5.2
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: DR: 216.0.5.2 (Id)
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1:    BDR: 172.16.0.1 (Id)
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: Neighbor change event
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: DR/BDR election
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: Elect BDR 172.16.0.1
Cafe-R1#
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: Elect DR 216.0.5.2
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1: DR: 216.0.5.2 (Id)
*Jul 19 14:08:46.584: OSPF-1 ADJ   Et0/1:    BDR: 172.16.0.1 (Id)
Cafe-R1#
*Jul 19 14:09:19.433: OSPF-1 ADJ   Et0/1: Nbr 216.0.5.2: Clean-up dbase exchange
Cafe-R1#undebug all
All possible debugging has been turned off
Cafe-R1#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.1/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 172.16.0.1, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State BDR, Priority 1
  Designated Router (ID) 216.0.5.2, Interface address 172.16.0.2
  Backup Designated router (ID) 172.16.0.1, Interface address 172.16.0.1
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:01
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/2/2, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1 
    Adjacent with neighbor 216.0.5.2  (Designated Router)
  Suppress hello for 0 neighbor(s)
Cafe-R1#show running-config interface Ethernet0/1
Building configuration...

Current configuration : 103 bytes
!
interface Ethernet0/1
 description Transit to Shelter-R1
 ip address 172.16.0.1 255.255.255.252
end

Cafe-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
216.0.5.2         1   FULL/DR         00:00:33    172.16.0.2      Ethernet0/1
Cafe-R1#show ip route ospf
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

      10.0.0.0/8 is variably subnetted, 4 subnets, 3 masks
O        10.0.16.0/24 [110/20] via 172.16.0.2, 00:04:48, Ethernet0/1
O        10.0.17.0/24 [110/20] via 172.16.0.2, 00:04:48, Ethernet0/1
Cafe-R1#show ip route 10.0.16.0
Routing entry for 10.0.16.0/24
  Known via "ospf 1", distance 110, metric 20, type intra area
  Last update from 172.16.0.2 on Ethernet0/1, 00:04:48 ago
  Routing Descriptor Blocks:
  * 172.16.0.2, from 216.0.5.2, 00:04:48 ago, via Ethernet0/1
      Route metric is 20, traffic share count is 1
Cafe-R1#show ip route 10.0.17.0
Routing entry for 10.0.17.0/24
  Known via "ospf 1", distance 110, metric 20, type intra area
  Last update from 172.16.0.2 on Ethernet0/1, 00:04:50 ago
  Routing Descriptor Blocks:
  * 172.16.0.2, from 216.0.5.2, 00:04:50 ago, via Ethernet0/1
      Route metric is 20, traffic share count is 1
Cafe-R1#ping 10.0.16.1 source 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.16.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.18.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#
Cafe-R1#show ip ospf interface Ethernet0/0.10
Ethernet0/0.10 is up, line protocol is up 
  Internet Address 10.0.18.1/27, Interface ID 7, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 172.16.0.1, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 172.16.0.1, Interface address 10.0.18.1
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    No Hellos (Passive interface) 
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 0, Adjacent neighbor count is 0 
  Suppress hello for 0 neighbor(s)
Cafe-R1#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Cafe-R1#


Shelter-R1#
Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#interface Ethernet0/1
Shelter-R1(config-if)# no ip ospf hello-interval
Shelter-R1(config-if)# no ip ospf dead-interval
Shelter-R1(config-if)# no ip ospf network point-to-point
Shelter-R1(config-if)#end
Shelter-R1#
*Jul 19 14:07:59.431: %OSPF-5-ADJCHG: Process 1, Nbr 172.16.0.1 on Ethernet0/1 from EXSTART to DOWN, Neighbor Down: Interface down or detached
*Jul 19 14:08:00.329: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#
*Jul 19 14:08:39.434: %OSPF-5-ADJCHG: Process 1, Nbr 172.16.0.1 on Ethernet0/1 from LOADING to FULL, Loading Done
Shelter-R1#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.2/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 216.0.5.2, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 216.0.5.2, Interface address 172.16.0.2
  Backup Designated router (ID) 172.16.0.1, Interface address 172.16.0.1
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:07
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1 
    Adjacent with neighbor 172.16.0.1  (Backup Designated Router)
  Suppress hello for 0 neighbor(s)
Shelter-R1#show running-config interface Ethernet0/1
Building configuration...

Current configuration : 100 bytes
!
interface Ethernet0/1
 description Transit to Cafe-R1
 ip address 172.16.0.2 255.255.255.252
end

Shelter-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
172.16.0.1        1   FULL/BDR        00:00:38    172.16.0.1      Ethernet0/1
Shelter-R1#show ip route ospf
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

Gateway of last resort is 216.0.5.1 to network 0.0.0.0

      10.0.0.0/8 is variably subnetted, 5 subnets, 3 masks
O        10.0.18.0/27 [110/20] via 172.16.0.1, 00:05:06, Ethernet0/1
Shelter-R1#show ip route 10.0.18.0
Routing entry for 10.0.18.0/27
  Known via "ospf 1", distance 110, metric 20, type intra area
  Last update from 172.16.0.1 on Ethernet0/1, 00:05:07 ago
  Routing Descriptor Blocks:
  * 172.16.0.1, from 172.16.0.1, 00:05:07 ago, via Ethernet0/1
      Route metric is 20, traffic share count is 1
Shelter-R1#ping 10.0.18.1 source 10.0.16.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.16.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#
Shelter-R1#show ip ospf interface Ethernet0/2.110
Ethernet0/2.110 is up, line protocol is up 
  Internet Address 10.0.16.1/24, Interface ID 7, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 216.0.5.2, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 216.0.5.2, Interface address 10.0.16.1
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    No Hellos (Passive interface) 
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/2/2, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 0, Adjacent neighbor count is 0 
          
Shelter-R1#how ip ospf interface Ethernet0/2.120
            ^
% Invalid input detected at '^' marker.

Shelter-R1#show ip ospf interface Ethernet0/2.120
Ethernet0/2.120 is up, line protocol is up 
  Internet Address 10.0.17.1/24, Interface ID 8, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 216.0.5.2, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 216.0.5.2, Interface address 10.0.17.1
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    No Hellos (Passive interface) 
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/3/3, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 0, Adjacent neighbor count is 0 
  Suppress hello for 0 neighbor(s)
Shelter-R1#copy running-config startup-config
Destination filename [startup-config]? y
%Error copying nvram:y (Invalid argument)
Shelter-R1#copy running-config startup-config
Destination filename [startup-config]? yes
%Error copying nvram:yes (Invalid argument)
Shelter-R1#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Shelter-R1#


Cafe-R1#show ospf neighbor
Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#router ospf 1
Cafe-R1(config-router)# no network 10.0.18.0 0.0.0.31 area 0
Cafe-R1(config-router)# no network 172.16.0.0 0.0.0.3 area 0
Cafe-R1(config-router)# network 10.0.18.0 0.0.0.31 area 1
Cafe-R1(config-router)# network 172.16.0.0 0.0.0.3 area 1
Cafe-R1(config-router)#end
Cafe-R1#
*Jul 19 15:01:04.541: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/1        1     0               172.16.0.1/30      10    BDR   1/1
Et0/0.10     1     0               10.0.18.1/27       10    DR    0/0
Cafe-R1#show running-config | section ^router ospf
router ospf 1
 passive-interface default
 no passive-interface Ethernet0/1
 network 10.0.18.0 0.0.0.31 area 1
 network 172.16.0.0 0.0.0.3 area 1
Cafe-R1#show running-config interface Ethernet0/0.10
Building configuration...

Current configuration : 123 bytes
!
interface Ethernet0/0.10
 description Cafe Admin VLAN
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.224
end

Cafe-R1#show running-config interface Ethernet0/1
Building configuration...

Current configuration : 103 bytes
!
interface Ethernet0/1
 description Transit to Shelter-R1
 ip address 172.16.0.1 255.255.255.252
end

Cafe-R1#clear ip ospf process
Reset ALL OSPF processes? [no]: yes
Cafe-R1#
*Jul 19 15:04:31.836: %OSPF-5-ADJCHG: Process 1, Nbr 216.0.5.2 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Interface down or detached
*Jul 19 15:04:31.903: %OSPF-5-ADJCHG: Process 1, Nbr 216.0.5.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/1        1     0               172.16.0.1/30      10    BDR   1/1
Et0/0.10     1     0               10.0.18.1/27       10    WAIT  0/0
Cafe-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#no router ospf 1
Cafe-R1(config)#
Cafe-R1(config)#router ospf 1
Cafe-R1(config-router)# passive-interface default
Cafe-R1(config-router)# no passive-interface Ethernet0/1
Cafe-R1(config-router)# network 10.0.18.0 0.0.0.31 area 1
Cafe-R1(config-router)# network 172.16.0.0 0.0.0.3 area 1
Cafe-R1(config-router)#end
*Jul 19 15:07:21.920: %OSPF-5-ADJCHG: Process 1, Nbr 216.0.5.2 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Interface down or detached
Cafe-R1(config-router)#end
*Jul 19 15:07:21.988: %OSPF-6-DFT_OPT: Protocol timers for fast convergence are Enabled.
Cafe-R1(config-router)#end
Cafe-R1#
*Jul 19 15:07:24.387: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.2, Ethernet0/1
Cafe-R1#
*Jul 19 15:07:25.192: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#
*Jul 19 15:07:31.375: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.2, Ethernet0/1
Cafe-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/1        1     1               172.16.0.1/30      10    WAIT  0/0
Et0/0.10     1     1               10.0.18.1/27       10    WAIT  0/0
Cafe-R1#
*Jul 19 15:07:41.033: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.2, Ethernet0/1
Cafe-R1#
*Jul 19 15:07:50.519: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.2, Ethernet0/1
Cafe-R1#
*Jul 19 15:08:00.338: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.2, Ethernet0/1
Cafe-R1#show ip ospf interface Ethernet0/0.10
Ethernet0/0.10 is up, line protocol is up 
  Internet Address 10.0.18.1/27, Interface ID 7, Area 1
  Attached via Network Statement
  Process ID 1, Router ID 172.16.0.1, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 172.16.0.1, Interface address 10.0.18.1
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    No Hellos (Passive interface) 
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/1/1, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 0, maximum is 0
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 0, Adjacent neighbor count is 0 
  Suppress hello for 0 neighbor(s)
Cafe-R1#
*Jul 19 15:08:10.291: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.2, Ethernet0/1
Cafe-R1#
*Jul 19 15:08:19.760: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.2, Ethernet0/1
Cafe-R1#
*Jul 19 15:08:28.862: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.2, Ethernet0/1
Cafe-R1#
*Jul 19 15:08:31.075: %OSPF-5-ADJCHG: Process 1, Nbr 216.0.5.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
216.0.5.2         1   FULL/BDR        00:00:38    172.16.0.2      Ethernet0/1
Cafe-R1#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.1/30, Interface ID 3, Area 1
  Attached via Network Statement
  Process ID 1, Router ID 172.16.0.1, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 172.16.0.1, Interface address 172.16.0.1
  Backup Designated router (ID) 216.0.5.2, Interface address 172.16.0.2
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:08
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/2/2, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 0, maximum is 1
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1 
    Adjacent with neighbor 216.0.5.2  (Backup Designated Router)
  Suppress hello for 0 neighbor(s)
Cafe-R1#show running-config interface Ethernet0/1 
Building configuration...

Current configuration : 103 bytes
!
interface Ethernet0/1
 description Transit to Shelter-R1
 ip address 172.16.0.1 255.255.255.252
end

Cafe-R1#show ip ospf
 Routing Process "ospf 1" with ID 172.16.0.1
 Start time: 01:54:07.205, Time elapsed: 00:03:38.482
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Supports Link-local Signaling (LLS)
 Supports area transit capability
 Supports NSSA (compatible with RFC 3101)
 Supports Database Exchange Summary List Optimization (RFC 5243)
 Maximum number of non self-generated LSA allowed 50000
    Current number of non self-generated LSA 3
    Threshold for warning message 75%
    Ignore-time 5 minutes, reset-time 10 minutes
    Ignore-count allowed 5, current ignore-count 0
 Event-log enabled, Maximum number of events: 1000, Mode: cyclic
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 50 msecs
 Minimum hold time between two consecutive SPFs 200 msecs
 Maximum wait time between two consecutive SPFs 5000 msecs
 Incremental-SPF disabled
 Per-prefix-distribution disabled
 Initial LSA throttle delay 50 msecs
 Minimum hold time for LSA throttle 200 msecs
 Maximum wait time for LSA throttle 5000 msecs
          
Cafe-R1#how ip protocols
         ^
% Invalid input detected at '^' marker.

Cafe-R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "application"
  Sending updates every 0 seconds
  Invalid after 0 seconds, hold down 0, flushed after 0
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Maximum path: 32
  Routing for Networks:
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 4)

Routing Protocol is "ospf 1"
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Router ID 172.16.0.1
  Number of areas in this router is 1. 1 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    10.0.18.0 0.0.0.31 area 1
    172.16.0.0 0.0.0.3 area 1
  Passive Interface(s):
  Passive Interface(s):
    Ethernet0/0
    Ethernet0/0.10
    Ethernet0/2
    Ethernet0/3
  Routing Information Sources:
    Gateway         Distance      Last Update
    216.0.5.2            110      00:02:35
  Distance: (default is 110)

Cafe-R1#show ip route ospf
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

      10.0.0.0/8 is variably subnetted, 4 subnets, 3 masks
O IA     10.0.16.0/24 [110/20] via 172.16.0.2, 00:04:08, Ethernet0/1
O IA     10.0.17.0/24 [110/20] via 172.16.0.2, 00:04:08, Ethernet0/1
Cafe-R1#ping 10.0.16.1 source 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.16.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.18.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#


Shelter-R1#show ospf neighbor
Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)# no network 172.16.0.0 0.0.0.3 area 0
Shelter-R1(config-router)# network 172.16.0.0 0.0.0.3 area 1
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 19 15:00:38.210: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#
*Jul 19 15:04:31.903: %OSPF-5-ADJCHG: Process 1, Nbr 172.16.0.1 on Ethernet0/1 from LOADING to FULL, Loading Done
Shelter-R1#
*Jul 19 15:08:01.886: %OSPF-5-ADJCHG: Process 1, Nbr 172.16.0.1 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Dead timer expired
Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#no router ospf 1
Shelter-R1(config)#
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)# passive-interface default
Shelter-R1(config-router)# no passive-interface Ethernet0/1
Shelter-R1(config-router)# network 10.0.16.0 0.0.0.255 area 0
Shelter-R1(config-router)# network 10.0.17.0 0.0.0.255 area 0
Shelter-R1(config-router)# network 172.16.0.0 0.0.0.3 area 1
Shelter-R1(config-router)#end
*Jul 19 15:08:31.068: %OSPF-6-DFT_OPT: Protocol timers for fast convergence are Enabled.
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 19 15:08:31.075: %OSPF-5-ADJCHG: Process 1, Nbr 172.16.0.1 on Ethernet0/1 from LOADING to FULL, Loading Done
*Jul 19 15:08:31.968: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/2.120    1     0               10.0.17.1/24       10    WAIT  0/0
Et0/2.110    1     0               10.0.16.1/24       10    WAIT  0/0
Et0/1        1     1               172.16.0.2/30      10    BDR   1/1
Shelter-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
172.16.0.1        1   FULL/DR         00:00:36    172.16.0.1      Ethernet0/1
Shelter-R1#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.2/30, Interface ID 3, Area 1
  Attached via Network Statement
  Process ID 1, Router ID 216.0.5.2, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State BDR, Priority 1
  Designated Router (ID) 172.16.0.1, Interface address 172.16.0.1
  Backup Designated router (ID) 216.0.5.2, Interface address 172.16.0.2
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:05
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/1/3, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 2, maximum is 2
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1 
    Adjacent with neighbor 172.16.0.1  (Designated Router)
  Suppress hello for 0 neighbor(s)
Shelter-R1#show running-config interface Ethernet0/1
Building configuration...

Current configuration : 100 bytes
!
interface Ethernet0/1
 description Transit to Cafe-R1
 ip address 172.16.0.2 255.255.255.252
end

Shelter-R1#show ip ospf
 Routing Process "ospf 1" with ID 216.0.5.2
 Start time: 01:55:20.248, Time elapsed: 00:03:12.633
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Supports Link-local Signaling (LLS)
 Supports area transit capability
 Supports NSSA (compatible with RFC 3101)
 Supports Database Exchange Summary List Optimization (RFC 5243)
 Maximum number of non self-generated LSA allowed 50000
    Current number of non self-generated LSA 2
    Threshold for warning message 75%
    Ignore-time 5 minutes, reset-time 10 minutes
    Ignore-count allowed 5, current ignore-count 0
 Event-log enabled, Maximum number of events: 1000, Mode: cyclic
 It is an area border router
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 50 msecs
 Minimum hold time between two consecutive SPFs 200 msecs
 Maximum wait time between two consecutive SPFs 5000 msecs
 Incremental-SPF disabled
 Per-prefix-distribution disabled
 Initial LSA throttle delay 50 msecs
 Minimum hold time for LSA throttle 200 msecs
 Maximum wait time for LSA throttle 5000 msecs
 Minimum LSA arrival 100 msecs
 LSA group pacing timer 240 secs
 Interface flood pacing timer 33 msecs
 Retransmission pacing timer 66 msecs
 EXCHANGE/LOADING adjacency limit: initial 300, process maximum 300
 Number of external LSA 0. Checksum Sum 0x000000
 Number of opaque AS LSA 0. Checksum Sum 0x000000
 Number of DCbitless external and opaque AS LSA 0
 Number of DoNotAge external and opaque AS LSA 0
 Number of areas in this router is 2. 2 normal 0 stub 0 nssa
 Number of areas transit capable is 0
 External flood list length 0
 IETF NSF helper support enabled
 Cisco NSF helper support enabled
 Reference bandwidth unit is 100 mbps
    Area BACKBONE(0) (Inactive)
        Number of interfaces in this area is 2
        Area has no authentication
        SPF algorithm last executed 00:02:32.526 ago
        SPF algorithm executed 2 times
        Area ranges are
        Number of LSA 3. Checksum Sum 0x0112E9
        Number of opaque link LSA 0. Checksum Sum 0x000000
        Number of DCbitless LSA 0
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0
    Area 1
        Number of interfaces in this area is 1
        Area has no authentication
        SPF algorithm last executed 00:03:05.132 ago
        SPF algorithm executed 4 times
        Area ranges are
        Number of LSA 5. Checksum Sum 0x03A8EC
        Number of opaque link LSA 0. Checksum Sum 0x000000
        Number of DCbitless LSA 0
        Number of indication LSA 0
        Number of DoNotAge LSA 0
        Flood list length 0
 Maintenance Mode ID:     130348868879552
 Maintenance Mode:        disabled
 Maintenance Mode Timer:  stopped (0)
  Graceful Reload FSU Global status : None (global: None)

Shelter-R1#show ip route ospf
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

Gateway of last resort is 216.0.5.1 to network 0.0.0.0

      10.0.0.0/8 is variably subnetted, 5 subnets, 3 masks
O        10.0.18.0/27 [110/20] via 172.16.0.1, 00:04:26, Ethernet0/1
Shelter-R1#ping 10.0.18.1 source 10.0.16.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.16.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#


Cafe-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/1        1     1               172.16.0.1/30      10    DR    1/1
Et0/0.10     1     1               10.0.18.1/27       10    DR    0/0
Cafe-R1#show ip route ospf
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

      10.0.0.0/8 is variably subnetted, 4 subnets, 3 masks
O IA     10.0.16.0/24 [110/20] via 172.16.0.2, 00:10:01, Ethernet0/1
O IA     10.0.17.0/24 [110/20] via 172.16.0.2, 00:10:01, Ethernet0/1
Cafe-R1#show ip ospf database summary

            OSPF Router with ID (172.16.0.1) (Process ID 1)

                Summary Net Link States (Area 1)

  LS age: 574
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.16.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000002
  Checksum: 0xE94E
  Length: 28
  Network Mask: /24
        MTID: 0         Metric: 10 

  LS age: 574
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.17.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000002
  Checksum: 0xDE58
  Length: 28
  Network Mask: /24
        MTID: 0         Metric: 10 

Cafe-R1#show ip route ospf
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

      10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
O IA     10.0.16.0/22 [110/20] via 172.16.0.2, 00:01:14, Ethernet0/1
Cafe-R1#show ip route 10.0.16.0
Routing entry for 10.0.16.0/22
  Known via "ospf 1", distance 110, metric 20, type inter area
  Last update from 172.16.0.2 on Ethernet0/1, 00:01:37 ago
  Routing Descriptor Blocks:
  * 172.16.0.2, from 216.0.5.2, 00:01:37 ago, via Ethernet0/1
      Route metric is 20, traffic share count is 1
Cafe-R1#show ip route 10.0.17.1
Routing entry for 10.0.16.0/22
  Known via "ospf 1", distance 110, metric 20, type inter area
  Last update from 172.16.0.2 on Ethernet0/1, 00:02:09 ago
  Routing Descriptor Blocks:
  * 172.16.0.2, from 216.0.5.2, 00:02:09 ago, via Ethernet0/1
      Route metric is 20, traffic share count is 1
Cafe-R1#show ip ospf database summary

            OSPF Router with ID (172.16.0.1) (Process ID 1)

                Summary Net Link States (Area 1)

  LS age: 190
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.16.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000003
  Checksum: 0xD861
  Length: 28
  Network Mask: /22
        MTID: 0         Metric: 10 

Cafe-R1#show ip ospf database summary

            OSPF Router with ID (172.16.0.1) (Process ID 1)

                Summary Net Link States (Area 1)

  LS age: 264
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.16.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000003
  Checksum: 0xD861
  Length: 28
  Network Mask: /22
        MTID: 0         Metric: 10 

Cafe-R1#show ip route ospf
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

Gateway of last resort is 172.16.0.2 to network 0.0.0.0

O*E2  0.0.0.0/0 [110/1] via 172.16.0.2, 00:01:00, Ethernet0/1
      10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
O IA     10.0.16.0/22 [110/20] via 172.16.0.2, 00:05:51, Ethernet0/1
Cafe-R1#show ip route 0.0.0.0
Routing entry for 0.0.0.0/0, supernet
  Known via "ospf 1", distance 110, metric 1, candidate default path
  Tag 1, type extern 2, forward metric 10
  Last update from 172.16.0.2 on Ethernet0/1, 00:01:36 ago
  Routing Descriptor Blocks:
  * 172.16.0.2, from 216.0.5.2, 00:01:36 ago, via Ethernet0/1
      Route metric is 1, traffic share count is 1
      Route tag 1
Cafe-R1#show ip ospf database external

            OSPF Router with ID (172.16.0.1) (Process ID 1)

                Type-5 AS External Link States

  LS age: 111
  Options: (No TOS-capability, DC, Upward)
  LS Type: AS External Link
  Link State ID: 0.0.0.0 (External Network Number )
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000001
  Checksum: 0x6C66
  Length: 36
  Network Mask: /0
        Metric Type: 2 (Larger than any link state path)
        MTID: 0 
        Metric: 1 
        Forward Address: 0.0.0.0
        External Route Tag: 1

Cafe-R1#show ip route 216.0.5.1
% Network not in table
Cafe-R1#ping 10.0.16.1 source 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.16.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.18.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#ping 216.0.5.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#ping 216.0.5.1 source 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.18.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
216.0.5.2         1   FULL/BDR        00:00:36    172.16.0.2      Ethernet0/1
Cafe-R1#show ip route ospf
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

Gateway of last resort is 172.16.0.2 to network 0.0.0.0

O*E2  0.0.0.0/0 [110/1] via 172.16.0.2, 00:05:20, Ethernet0/1
      10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
O IA     10.0.16.0/22 [110/20] via 172.16.0.2, 00:10:11, Ethernet0/1
Cafe-R1#show ip route 10.0.16.0
Routing entry for 10.0.16.0/22
  Known via "ospf 1", distance 110, metric 20, type inter area
  Last update from 172.16.0.2 on Ethernet0/1, 00:10:11 ago
  Routing Descriptor Blocks:
  * 172.16.0.2, from 216.0.5.2, 00:10:11 ago, via Ethernet0/1
      Route metric is 20, traffic share count is 1
Cafe-R1#show ip route 0.0.0.0
Routing entry for 0.0.0.0/0, supernet
  Known via "ospf 1", distance 110, metric 1, candidate default path
  Tag 1, type extern 2, forward metric 10
  Last update from 172.16.0.2 on Ethernet0/1, 00:05:20 ago
  Routing Descriptor Blocks:
  * 172.16.0.2, from 216.0.5.2, 00:05:20 ago, via Ethernet0/1
      Route metric is 1, traffic share count is 1
      Route tag 1
Cafe-R1#show ip route 216.0.5.1
% Network not in table
Cafe-R1#show ip ospf database summary

            OSPF Router with ID (172.16.0.1) (Process ID 1)

                Summary Net Link States (Area 1)

  LS age: 611
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.16.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000003
  Checksum: 0xD861
  Length: 28
  Network Mask: /22
        MTID: 0         Metric: 10 

Cafe-R1#show ip ospf database external

            OSPF Router with ID (172.16.0.1) (Process ID 1)

                Type-5 AS External Link States

  LS age: 320
  Options: (No TOS-capability, DC, Upward)
  LS Type: AS External Link
  Link State ID: 0.0.0.0 (External Network Number )
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000001
  Checksum: 0x6C66
  Length: 36
  Network Mask: /0
        Metric Type: 2 (Larger than any link state path)
        MTID: 0 
        Metric: 1 
        Forward Address: 0.0.0.0
        External Route Tag: 1

Cafe-R1#ping 10.0.16.1 source 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.16.1, timeout is 2 seconds:
Packet sent with a source address of 10.0.18.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Cafe-R1#


Shelter-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/2.120    1     0               10.0.17.1/24       10    DR    0/0
Et0/2.110    1     0               10.0.16.1/24       10    DR    0/0
Et0/1        1     1               172.16.0.2/30      10    BDR   1/1
Shelter-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
172.16.0.1        1   FULL/DR         00:00:36    172.16.0.1      Ethernet0/1
Shelter-R1#show running-config | include ^ip route
ip route 0.0.0.0 0.0.0.0 216.0.5.1
Shelter-R1#show ip route 0.0.0.0
Routing entry for 0.0.0.0/0, supernet
  Known via "static", distance 1, metric 0, candidate default path
  Routing Descriptor Blocks:
  * 216.0.5.1
      Route metric is 0, traffic share count is 1
Shelter-R1#ping 216.0.5.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)# area 0 range 10.0.16.0 255.255.252.0
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 19 15:19:55.717: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show running-config | section ^router ospf
router ospf 1
 area 0 range 10.0.16.0 255.255.252.0
 passive-interface default
 no passive-interface Ethernet0/1
 network 10.0.16.0 0.0.0.255 area 0
 network 10.0.17.0 0.0.0.255 area 0
 network 172.16.0.0 0.0.0.3 area 1
Shelter-R1#show ip route 10.0.16.0
Routing entry for 10.0.16.0/24
  Known via "connected", distance 0, metric 0 (connected, via interface)
  Routing Descriptor Blocks:
  * directly connected, via Ethernet0/2.110
      Route metric is 0, traffic share count is 1
Shelter-R1#show ip ospf database summary

            OSPF Router with ID (216.0.5.2) (Process ID 1)

                Summary Net Link States (Area 0)

  LS age: 954
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.18.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000001
  Checksum: 0x7FCC
  Length: 28
  Network Mask: /27
        MTID: 0         Metric: 20 

  LS age: 954
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 172.16.0.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000002
  Checksum: 0x8513
  Length: 28
  Network Mask: /30
        MTID: 0         Metric: 10 


                Summary Net Link States (Area 1)

  LS age: 271
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.16.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000003
  Checksum: 0xD861
  Length: 28
  Network Mask: /22
        MTID: 0         Metric: 10 

Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)# default-information originate
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 19 15:24:46.879: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show running-config | section ^router ospf
router ospf 1
 area 0 range 10.0.16.0 255.255.252.0
 passive-interface default
 no passive-interface Ethernet0/1
 network 10.0.16.0 0.0.0.255 area 0
 network 10.0.17.0 0.0.0.255 area 0
 network 172.16.0.0 0.0.0.3 area 1
 default-information originate
Shelter-R1#show ip ospf database external

            OSPF Router with ID (216.0.5.2) (Process ID 1)

                Type-5 AS External Link States

  LS age: 41
  Options: (No TOS-capability, DC, Upward)
  LS Type: AS External Link
  Link State ID: 0.0.0.0 (External Network Number )
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000001
  Checksum: 0x6C66
  Length: 36
  Network Mask: /0
        Metric Type: 2 (Larger than any link state path)
        MTID: 0 
        Metric: 1 
        Forward Address: 0.0.0.0
        External Route Tag: 1

Shelter-R1#ping 216.0.5.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#show running-config | include ^ip route
ip route 0.0.0.0 0.0.0.0 216.0.5.1
Shelter-R1#show running-config | section ^router ospf
router ospf 1
 area 0 range 10.0.16.0 255.255.252.0
 passive-interface default
 no passive-interface Ethernet0/1
 network 10.0.16.0 0.0.0.255 area 0
 network 10.0.17.0 0.0.0.255 area 0
 network 172.16.0.0 0.0.0.3 area 1
 default-information originate
Shelter-R1#show ip ospf
 Routing Process "ospf 1" with ID 216.0.5.2
 Start time: 01:55:20.248, Time elapsed: 00:21:18.542
 Supports only single TOS(TOS0) routes
 Supports opaque LSA
 Supports Link-local Signaling (LLS)
 Supports area transit capability
 Supports NSSA (compatible with RFC 3101)
 Supports Database Exchange Summary List Optimization (RFC 5243)
 Maximum number of non self-generated LSA allowed 50000
    Current number of non self-generated LSA 2
    Threshold for warning message 75%
    Ignore-time 5 minutes, reset-time 10 minutes
    Ignore-count allowed 5, current ignore-count 0
 Event-log enabled, Maximum number of events: 1000, Mode: cyclic
 It is an area border and autonomous system boundary router
 Redistributing External Routes from,
    Maximum limit of redistributed prefixes 10240
    Threshold for warning message 75%
 Router is not originating router-LSAs with maximum metric
 Initial SPF schedule delay 50 msecs
 Minimum hold time between two consecutive SPFs 200 msecs
 Maximum wait time between two consecutive SPFs 5000 msecs
 Incremental-SPF disabled
          
Shelter-R1#how ip ospf interface brief
            ^
% Invalid input detected at '^' marker.

Shelter-R1#show ip ospf database summary

            OSPF Router with ID (216.0.5.2) (Process ID 1)

                Summary Net Link States (Area 0)

  LS age: 1278
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.18.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000001
  Checksum: 0x7FCC
  Length: 28
  Network Mask: /27
        MTID: 0         Metric: 20 

  LS age: 1278
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 172.16.0.0 (summary Network Number)
  Advertising Router: 216.0.5.2
  LS Seq Number: 80000002
  Checksum: 0x8513
          
Shelter-R1#how ip ospf database external
            ^
% Invalid input detected at '^' marker.

Shelter-R1#show ip route 0.0.0.0
Routing entry for 0.0.0.0/0, supernet
  Known via "static", distance 1, metric 0, candidate default path
  Routing Descriptor Blocks:
  * 216.0.5.1
      Route metric is 0, traffic share count is 1
Shelter-R1#show ip route 10.0.16.0
Routing entry for 10.0.16.0/24
  Known via "connected", distance 0, metric 0 (connected, via interface)
  Routing Descriptor Blocks:
  * directly connected, via Ethernet0/2.110
      Route metric is 0, traffic share count is 1
Shelter-R1#ping 216.0.5.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)# area 0 range 10.0.16.0 255.255.252.0
Shelter-R1(config-router)# default-information originate
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 19 15:30:37.062: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Shelter-R1#
```
