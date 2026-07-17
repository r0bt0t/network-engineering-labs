# Lab 044 - Raw CLI Output

```bash
Shelter-R2>en
Shelter-R2#show i
*Jul 17 19:08:12.578: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Shelter-R2#show ip 
*Jul 17 19:08:12.680: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 19:08:12.681: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 19:08:12.786: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Shelter-R2#show ip osp
*Jul 17 19:08:12.886: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 17 19:08:12.886: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Shelter-R2#show ip ospf neighbor
Shelter-R2#show ip ospf interface ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.2/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 2.2.2.2, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 2.2.2.2, Interface address 172.16.0.2
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:09
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
Shelter-R2#show ip ospf interface brief | include Et0/1
Et0/1        1     0               172.16.0.2/30      10    DR    0/0
Shelter-R2#


Cafe-R1>en
Cafe-R1#term
*Jul 17 19:09:16.855: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-R1#terminal
*Jul 17 19:09:16.958: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 19:09:16.959: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 19:09:17.064: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-R1#terminal len
*Jul 17 19:09:17.164: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 17 19:09:17.164: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-R1#terminal length 0
Cafe-R1#show ip ospf interface ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.1/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 1.1.1.1, Network Type POINT_TO_POINT, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State POINT_TO_POINT
  Timer intervals configured, Hello 5, Dead 20, Wait 20, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:02
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
Cafe-R1#show ip ospf interface brief | include et0/1
Cafe-R1#show ip ospf interface brief | include Et0/1
Et0/1        1     0               172.16.0.1/30      10    P2P   0/0
Cafe-R1#


Cafe-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#in
Cafe-R1(config)#interface eth
Cafe-R1(config)#interface ethernet0/1
Cafe-R1(config-if)#no ip ospf hello-interval
Cafe-R1(config-if)#no ip ospf dead-interval 
Cafe-R1(config-if)#
*Jul 17 19:14:58.509: %OSPF-4-NET_TYPE_MISMATCH: Received Hello from 2.2.2.2 on Ethernet0/1 indicating a  potential 
             network type mismatch
Cafe-R1(config-if)#end
*Jul 17 19:14:58.510: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1(config-if)#end
Cafe-R1#
*Jul 17 19:15:00.424: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#clear ip ospf process
Reset ALL OSPF processes? [no]: yes
Cafe-R1#
*Jul 17 19:15:38.608: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Interface down or detached
*Jul 17 19:15:38.610: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1#show ip ospf int
Cafe-R1#show ip ospf interface eth
Cafe-R1#show ip ospf interface ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.1/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 1.1.1.1, Network Type POINT_TO_POINT, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State POINT_TO_POINT
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:04
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
    Adjacent with neighbor 2.2.2.2
  Suppress hello for 0 neighbor(s)
Cafe-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           0   FULL/  -        00:00:34    172.16.0.2      Ethernet0/1
Cafe-R1#


Cafe-R1#
Cafe-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#in
Cafe-R1(config)#interface eth
Cafe-R1(config)#interface ethernet0/1
Cafe-R1(config-if)#no ip ospf network point-to-point
Cafe-R1(config-if)#e
*Jul 17 19:18:08.633: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Interface down or detached
*Jul 17 19:18:08.635: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1(config-if)#end
Cafe-R1#
*Jul 17 19:18:11.139: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#clear ip ospf process
Reset ALL OSPF processes? [no]: yes
Cafe-R1#
*Jul 17 19:18:28.481: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from FULL to DOWN, Neighbor Down: Interface down or detached
*Jul 17 19:18:28.483: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-R1#show ip ospf int
Cafe-R1#show ip ospf interface eth
Cafe-R1#show ip ospf interface ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.1/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 1.1.1.1, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State BDR, Priority 1
  Designated Router (ID) 2.2.2.2, Interface address 172.16.0.2
  Backup Designated router (ID) 1.1.1.1, Interface address 172.16.0.1
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:04
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/2/2, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 1, maximum is 1
  Last flood scan time is 0 msec, maximum is 1 msec
  Neighbor Count is 1, Adjacent neighbor count is 1 
    Adjacent with neighbor 2.2.2.2  (Designated Router)
  Suppress hello for 0 neighbor(s)
Cafe-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:31    172.16.0.2      Ethernet0/1
Cafe-R1#show ip ospf database router

            OSPF Router with ID (1.1.1.1) (Process ID 1)

                Router Link States (Area 0)

  LS age: 30
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 1.1.1.1
  Advertising Router: 1.1.1.1
  LS Seq Number: 8000000C
  Checksum: 0x6122
  Length: 48
  Number of Links: 2

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 172.16.0.2
     (Link Data) Router Interface address: 172.16.0.1
      Number of MTID metrics: 0
       TOS 0 Metrics: 10

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 10.0.18.0
     (Link Data) Network Mask: 255.255.255.224
      Number of MTID metrics: 0
       TOS 0 Metrics: 10


  LS age: 70
  Options: (No TOS-capability, DC)
  LS Type: Router Links
  Link State ID: 2.2.2.2
  Advertising Router: 2.2.2.2
  LS Seq Number: 80000008
  Checksum: 0xC16A
  Length: 60
  Number of Links: 3

    Link connected to: a Transit Network
     (Link ID) Designated Router address: 172.16.0.2
     (Link Data) Router Interface address: 172.16.0.2
      Number of MTID metrics: 0
       TOS 0 Metrics: 10

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 10.0.17.0
     (Link Data) Network Mask: 255.255.255.0
      Number of MTID metrics: 0
       TOS 0 Metrics: 10

    Link connected to: a Stub Network
     (Link ID) Network/subnet number: 10.0.16.0
     (Link Data) Network Mask: 255.255.255.0
      Number of MTID metrics: 0
       TOS 0 Metrics: 10


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
O        10.0.16.0/24 [110/20] via 172.16.0.2, 00:01:43, Ethernet0/1
O        10.0.17.0/24 [110/20] via 172.16.0.2, 00:01:43, Ethernet0/1
Cafe-R1#ping 10.0.16.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.16.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#


Shelter-R2#ping 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R2#


Shelter-R2#
Shelter-R2#ping 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R2#
Shelter-R2#
Shelter-R2#
Shelter-R2#show ip ospf interface Ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.2/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 2.2.2.2, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 2.2.2.2, Interface address 172.16.0.2
  Backup Designated router (ID) 1.1.1.1, Interface address 172.16.0.1
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:08
  Supports Link-local Signaling (LLS)
  Cisco NSF helper support enabled
  IETF NSF helper support enabled
  Can be protected by per-prefix Loop-Free FastReroute
  Can be used for per-prefix Loop-Free FastReroute repair paths
  Not Protected by per-prefix TI-LFA
  Index 1/3/3, flood queue length 0
  Next 0x0(0)/0x0(0)/0x0(0)
  Last flood scan length is 0, maximum is 2
  Last flood scan time is 0 msec, maximum is 0 msec
  Neighbor Count is 1, Adjacent neighbor count is 1 
    Adjacent with neighbor 1.1.1.1  (Backup Designated Router)
  Suppress hello for 0 neighbor(s)
Shelter-R2#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
1.1.1.1           1   FULL/BDR        00:00:37    172.16.0.1      Ethernet0/1
Shelter-R2#show ip route ospf
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

      10.0.0.0/8 is variably subnetted, 5 subnets, 3 masks
O        10.0.18.0/27 [110/20] via 172.16.0.1, 00:05:20, Ethernet0/1
Shelter-R2#
```
