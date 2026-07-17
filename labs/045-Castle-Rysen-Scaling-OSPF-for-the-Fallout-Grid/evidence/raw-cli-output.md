# Lab 045 - Raw CLI Output

```bash
Shelter-R1>
*Jul 17 19:35:34.842: %OSPF-5-ADJCHG: Process 1, Nbr 1.1.1.1 on Ethernet0/1 from LOADING to FULL, Loading Done
Shelter-R1>en
Shelter-R1#
*Jul 17 19:35:41.214: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Shelter-R1#
*Jul 17 19:35:41.316: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 19:35:41.317: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 19:35:41.422: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Shelter-R1#show 
*Jul 17 19:35:41.522: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 17 19:35:41.522: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Shelter-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/1        1     0               172.16.0.2/30      10    DR    1/1
Et0/2.20     1     0               10.0.17.1/24       10    DR    0/0
Et0/2.10     1     0               10.0.16.1/24       10    DR    0/0
Shelter-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)#no network 172.16.0.0 0.0.0.3 area 0
Shelter-R1(config-router)#no network 172.16.0.0 0.0.0.3 area 0
*Jul 17 19:37:16.737: %OSPF-5-ADJCHG: Process 1, Nbr 1.1.1.1 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Interface down or detached
Shelter-R1(config-router)#network 172.16.0.0 0.0.0.3 area 1   
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 17 19:37:32.780: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#
*Jul 17 19:37:36.442: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.1, Ethernet0/1
Shelter-R1#show ip ospf interface
*Jul 17 19:37:45.468: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.1, Ethernet0/1
Shelter-R1#show ip ospf interface brief
*Jul 17 19:37:55.374: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.1, Ethernet0/1
Shelter-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/2.20     1     0               10.0.17.1/24       10    DR    0/0
Et0/2.10     1     0               10.0.16.1/24       10    DR    0/0
Et0/1        1     1               172.16.0.2/30      10    WAIT  0/0
Shelter-R1#
*Jul 17 19:38:05.262: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.1, Ethernet0/1
Shelter-R1#
*Jul 17 19:38:15.081: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.1, Ethernet0/1
Shelter-R1#show ip ospf neighbor
Shelter-R1#
*Jul 17 19:38:24.857: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.1, Ethernet0/1
Shelter-R1#
*Jul 17 19:38:33.934: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 172.16.0.1, Ethernet0/1
Shelter-R1#


Cafe-R1>
*Jul 17 19:35:34.842: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1>
*Jul 17 19:37:52.304: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Dead timer expired
Cafe-R1>
Cafe-R1>
Cafe-R1>en
Cafe-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#router 
*Jul 17 19:39:05.053: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul 17 19:39:05.156: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 19:39:05.156: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 19:39:05.263: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-R1(config)#router ospf
*Jul 17 19:39:05.363: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 17 19:39:05.363: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-R1(config)#router ospf 1
Cafe-R1(config-router)#no network 172.16.0.0 0.0.0.3 area 0
Cafe-R1(config-router)#no network 10.0.18.0 0.0.0.63 area 0  
Cafe-R1(config-router)#network 172.16.0.0 0.0.0.3 area 1   
Cafe-R1(config-router)#
*Jul 17 19:40:19.110: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1(config-router)#network 10.0.18.0 0.0.0.63 area 1 
Cafe-R1(config-router)#end
Cafe-R1#
*Jul 17 19:40:48.878: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:37    172.16.0.2      Ethernet0/1
Cafe-R1#show ip protocols | include Areas
Cafe-R1#show ip protocols | include Areas
Cafe-R1#show ip protocols | include Area 
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
  Router ID 1.1.1.1
  Number of areas in this router is 1. 1 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    10.0.18.0 0.0.0.63 area 1
    172.16.0.0 0.0.0.3 area 1
  Routing Information Sources:
    Gateway         Distance      Last Update
    Gateway         Distance      Last Update
    2.2.2.2              110      00:02:09
  Distance: (default is 110)

Cafe-R1#


Shelter-R1#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/2.20     1     0               10.0.17.1/24       10    DR    0/0
Et0/2.10     1     0               10.0.16.1/24       10    DR    0/0
Et0/1        1     1               172.16.0.2/30      10    DR    1/1
Shelter-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)#area 0 range 10.0.16.0 255.255.252.0
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 17 19:45:06.259: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show ip ospf database summary

            OSPF Router with ID (2.2.2.2) (Process ID 1)

                Summary Net Link States (Area 0)

  LS age: 277
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.18.0 (summary Network Number)
  Advertising Router: 2.2.2.2
  LS Seq Number: 80000001
  Checksum: 0x51F2
  Length: 28
  Network Mask: /26
        MTID: 0         Metric: 20 

  LS age: 470
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 172.16.0.0 (summary Network Number)
  Advertising Router: 2.2.2.2
  LS Seq Number: 80000001
  Checksum: 0x1A57
  Length: 28
  Network Mask: /30
        MTID: 0         Metric: 10 


                Summary Net Link States (Area 1)

  LS age: 16
  Options: (No TOS-capability, DC, Upward)
  LS Type: Summary Links(Network)
  Link State ID: 10.0.16.0 (summary Network Number)
  Advertising Router: 2.2.2.2
  LS Seq Number: 80000002
  Checksum: 0x6DA5
  Length: 28
  Network Mask: /22
        MTID: 0         Metric: 10 

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

      10.0.0.0/8 is variably subnetted, 6 subnets, 4 masks
O        10.0.16.0/22 is a summary, 00:00:30, Null0
O        10.0.18.0/26 [110/20] via 172.16.0.1, 00:00:30, Ethernet0/1
Shelter-R1#


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
O IA     10.0.16.0/22 [110/20] via 172.16.0.2, 00:01:27, Ethernet0/1
Cafe-R1#


Shelter-R1#
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
Shelter-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R1(config)#router ospf 1
Shelter-R1(config-router)#default-information originate
Shelter-R1(config-router)#end
Shelter-R1#
*Jul 17 19:49:13.946: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R1#show ip ospf database external

            OSPF Router with ID (2.2.2.2) (Process ID 1)

                Type-5 AS External Link States

  LS age: 43
  Options: (No TOS-capability, DC, Upward)
  LS Type: AS External Link
  Link State ID: 0.0.0.0 (External Network Number )
  Advertising Router: 2.2.2.2
  LS Seq Number: 80000001
  Checksum: 0xFEAB
  Length: 36
  Network Mask: /0
        Metric Type: 2 (Larger than any link state path)
        MTID: 0 
        Metric: 1 
        Forward Address: 0.0.0.0
        External Route Tag: 1

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
      10.0.0.0/8 is variably subnetted, 6 subnets, 4 masks
O        10.0.16.0/22 is a summary, 00:05:03, Null0
C        10.0.16.0/24 is directly connected, Ethernet0/2.10
L        10.0.16.1/32 is directly connected, Ethernet0/2.10
C        10.0.17.0/24 is directly connected, Ethernet0/2.20
L        10.0.17.1/32 is directly connected, Ethernet0/2.20
O        10.0.18.0/26 [110/20] via 172.16.0.1, 00:05:03, Ethernet0/1
      172.16.0.0/16 is variably subnetted, 2 subnets, 2 masks
C        172.16.0.0/30 is directly connected, Ethernet0/1
L        172.16.0.2/32 is directly connected, Ethernet0/1
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/0
L        216.0.5.2/32 is directly connected, Ethernet0/0
Shelter-R1#
Shelter-R1#show ip route | include 0.0.0.0
Gateway of last resort is 216.0.5.1 to network 0.0.0.0
S*    0.0.0.0/0 [1/0] via 216.0.5.1
      10.0.0.0/8 is variably subnetted, 6 subnets, 4 masks
Shelter-R1#


Cafe-R1#show ip ospf database external

            OSPF Router with ID (1.1.1.1) (Process ID 1)

                Type-5 AS External Link States

  LS age: 98
  Options: (No TOS-capability, DC, Upward)
  LS Type: AS External Link
  Link State ID: 0.0.0.0 (External Network Number )
  Advertising Router: 2.2.2.2
  LS Seq Number: 80000001
  Checksum: 0xFEAB
  Length: 36
  Network Mask: /0
        Metric Type: 2 (Larger than any link state path)
        MTID: 0 
        Metric: 1 
        Forward Address: 0.0.0.0
        External Route Tag: 1

Cafe-R1#show ip route | include 0.0.0.0
Gateway of last resort is 172.16.0.2 to network 0.0.0.0
O*E2  0.0.0.0/0 [110/1] via 172.16.0.2, 00:02:02, Ethernet0/1
      10.0.0.0/8 is variably subnetted, 3 subnets, 3 masks
Cafe-R1#
Cafe-R1#
Cafe-R1#
Cafe-R1#ping 216.0.5.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#
```
