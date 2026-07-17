# Lab 043 - Raw CLI Output

```bash
Cafe-R1>en
Cafe-R1#terminal length
*Jul 17 18:45:31.181: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-R1#terminal length 0
Cafe-R1#
*Jul 17 18:45:31.283: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 18:45:31.284: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 18:45:31.389: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-R1#
*Jul 17 18:45:31.489: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 17 18:45:31.489: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-R1#show running-config | section router
router ospf 1
 router-id 1.1.1.1
Cafe-R1#show ip interface brief | include ethernet0
Cafe-R1#show ip interface brief | include ethernet0/0.10
Cafe-R1#show ip interface brief                         
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/1            172.16.0.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-R1#
! You should see router ospf 1 with router-id 1.1.1.1.
! Do not remove this placeholder OSPF process; you will add network statements to it.


Shelter-R2>en
Shelter-R2#
*Jul 17 18:47:35.376: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Shelter-R2#term
*Jul 17 18:47:35.480: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 18:47:35.480: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 17 18:47:35.587: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Shelter-R2#terminal 
*Jul 17 18:47:35.688: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jul 17 18:47:35.688: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Shelter-R2#terminal length 0
Shelter-R2#show running-config | section router
router ospf 1
 router-id 2.2.2.2
Shelter-R2#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.16.1       YES TFTP   up                    up      
Ethernet0/0.20         10.0.17.1       YES TFTP   up                    up      
Ethernet0/1            172.16.0.2      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Shelter-R2#show ip interface brief | include ethernet0/1
Shelter-R2#
! You should see router ospf 1 with router-id 2.2.2.2.


Cafe-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-R1(config)#router ospf 1
Cafe-R1(config-router)#network 10.0.18.1 0.0.0.0 area 0
Cafe-R1(config-router)#network 172.16.0.1 0.0.0.0 area 0
Cafe-R1(config-router)#passive-interface eth
Cafe-R1(config-router)#passive-interface ethernet0/0.10
Cafe-R1(config-router)#end
Cafe-R1#
*Jul 17 18:50:44.253: %SYS-5-CONFIG_I: Configured from console by console
Cafe-R1#show ip ospf int
Cafe-R1#show ip ospf interface eth
Cafe-R1#show ip ospf interface ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Internet Address 172.16.0.1/30, Interface ID 3, Area 0
  Attached via Network Statement
  Process ID 1, Router ID 1.1.1.1, Network Type BROADCAST, Cost: 10
  Topology-MTID    Cost    Disabled    Shutdown      Topology Name
        0           10        no          no            Base
  Transmit Delay is 1 sec, State WAITING, Priority 1
  No designated router on this network
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    oob-resync timeout 40
    Hello due in 00:00:08
    Wait time before Designated router selection 00:00:11
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
Cafe-R1#


Shelter-R2#
Shelter-R2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-R2(config)#router ospf 1
Shelter-R2(config-router)#network 172.16.0.02 0.0.0.0 area 0
Shelter-R2(config-router)#network 172.16. 0.0.0.0 area 0    
*Jul 17 18:53:08.524: %OSPF-5-ADJCHG: Process 1, Nbr 1.1.1.1 on Ethernet0/1 from LOADING to FULL, Loading Done
Shelter-R2(config-router)#network 10.0.16.8 0.0.1.255 area 0
Shelter-R2(config-router)#passive-interface eth
Shelter-R2(config-router)#passive-interface ethernet0/0.10
Shelter-R2(config-router)#passive-interface ethernet0/0.20
Shelter-R2(config-router)#end
Shelter-R2#sh
*Jul 17 18:54:11.548: %SYS-5-CONFIG_I: Configured from console by console
Shelter-R2#show ip ospf interface brief
Interface    PID   Area            IP Address/Mask    Cost  State Nbrs F/C
Et0/0.20     1     0               10.0.17.1/24       10    WAIT  0/0
Et0/0.10     1     0               10.0.16.1/24       10    WAIT  0/0
Et0/1        1     0               172.16.0.2/30      10    BDR   1/1
Shelter-R2#
! Ethernet0/1 should have one neighbor.
! Ethernet0/0.10 and Ethernet0/0.20 should be passive, with 0/0 neighbors.


Cafe-R1#
Cafe-R1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/BDR        00:00:35    172.16.0.2      Ethernet0/1
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
O        10.0.16.0/24 [110/20] via 172.16.0.2, 00:02:22, Ethernet0/1
O        10.0.17.0/24 [110/20] via 172.16.0.2, 00:02:22, Ethernet0/1
Cafe-R1#ping 10.0.16.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.16.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#ping 10.0.17.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.17.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#ping 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-R1#
! Cafe-R1 should learn:
! O        10.0.16.0/24 [110/20] via 172.16.0.2, Ethernet0/1
! O        10.0.17.0/24 [110/20] via 172.16.0.2, Ethernet0/1



Shelter-R2#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
1.1.1.1           1   FULL/DR         00:00:32    172.16.0.1      Ethernet0/1
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
O        10.0.18.0/27 [110/20] via 172.16.0.1, 00:04:41, Ethernet0/1
Shelter-R2#ping 10.0.16.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.16.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R2#ping 10.0.17.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.17.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R2#ping 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Shelter-R2#
! Shelter-R2 should learn:
! O        10.0.18.0/27 [110/20] via 172.16.0.1, Ethernet0/1
```
