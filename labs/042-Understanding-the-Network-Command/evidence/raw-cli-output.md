# Lab 042 - Raw CLI Output

```bash
Connecting to console for Cafe-RTR1

Cafe-RTR1#terminal length 0                           
Cafe-RTR1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/1            192.168.10.2    YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RTR1#shwo running-config interface ethernet0/0.10
            ^
% Invalid input detected at '^' marker.

Cafe-RTR1#show running-config interface ethernet0/0.10
Building configuration...

Current configuration : 123 bytes
!
interface Ethernet0/0.10
 description Cafe Admin VLAN
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.224
end

Cafe-RTR1#show running-config interface ethernet0/1   
Building configuration...

Current configuration : 107 bytes
!
interface Ethernet0/1
 description Transit to Shelter-RTR1
 ip address 192.168.10.2 255.255.255.252
end

Cafe-RTR1#show ip ospf neighbor
Cafe-RTR1#
Connecting to console for Cafe-RTR1

Cafe-RTR1#terminal length 0                           
Cafe-RTR1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/1            192.168.10.2    YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RTR1#shwo running-config interface ethernet0/0.10
            ^
% Invalid input detected at '^' marker.

Cafe-RTR1#show running-config interface ethernet0/0.10
Building configuration...

Current configuration : 123 bytes
!
interface Ethernet0/0.10
 description Cafe Admin VLAN
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.224
end

Cafe-RTR1#show running-config interface ethernet0/1   
Building configuration...

Current configuration : 107 bytes
!
interface Ethernet0/1
 description Transit to Shelter-RTR1
 ip address 192.168.10.2 255.255.255.252
end

Cafe-RTR1#show ip ospf neighbor
Cafe-RTR1#
! Ethernet0/0.10 should appear in area 0 with 10.0.18.1/27 and 0/0 neighbors.


Cafe-RTR1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RTR1(config)#router ospf 15
Cafe-RTR1(config-router)#network 192.168.10.0 0.0.0.3 area 0
Cafe-RTR1(config-router)#
*Jul 17 18:29:09.960: %OSPF-5-ADJCHG: Process 15, Nbr 15.15.15.2 on Ethernet0/1 from LOADING to FULL, Loading Done
Cafe-RTR1(config-router)#end
Cafe-RTR1#
*Jul 17 18:29:12.648: %SYS-5-CONFIG_I: Configured from console by console
Cafe-RTR1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
15.15.15.2        1   FULL/DR         00:00:38    192.168.10.1    Ethernet0/1
Cafe-RTR1#show ip route ospf
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

      172.16.0.0/32 is subnetted, 1 subnets
O        172.16.50.1 [110/11] via 192.168.10.1, 00:00:26, Ethernet0/1
Cafe-RTR1#

! Cafe-RTR1 should form a FULL adjacency to Shelter-RTR1 on Ethernet0/1.
! The OSPF route learned on Cafe-RTR1 is Shelter-RTR1's loopback:
! O        172.16.50.1 [110/11] via 192.168.10.1, Ethernet0/1


Cafe-RTR1#
Cafe-RTR1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RTR1(config)#router ospf 15
Cafe-RTR1(config-router)#passive-interface
% Incomplete command.

Cafe-RTR1(config-router)#passive-interface ethernet0/0.10
Cafe-RTR1(config-router)#end
Cafe-RTR1#
*Jul 17 18:32:13.962: %SYS-5-CONFIG_I: Configured from console by console
Cafe-RTR1#show ip ospf int
Cafe-RTR1#show ip ospf interface ethe
Cafe-RTR1#show ip ospf interface ethernet0/0.10
%OSPF: OSPF not enabled on Ethernet0/0.10
Cafe-RTR1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
15.15.15.2        1   FULL/DR         00:00:36    192.168.10.1    Ethernet0/1
Cafe-RTR1#
! In the interface output, look for:
! No Hellos (Passive interface)
!
! The neighbor table should still show only Shelter-RTR1 as FULL on Ethernet0/1.


Shelter-RTR1#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
15.15.15.1        1   FULL/BDR        00:00:33    192.168.10.2    Ethernet0/0
Shelter-RTR1#
```
