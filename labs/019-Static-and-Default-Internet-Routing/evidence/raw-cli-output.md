# Lab 019 - Raw CLI Output

```bash
Connecting to console for Cafe-RT1


User Access Verification

Username: 
Username: cisco
Password: 
Cafe-RT1#
*Jun  7 10:34:19.565: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: cisco] [Source: LOCAL] [localport: 0] at 10:34:19 UTC Sun Jun 7 2026
Cafe-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES TFTP   up                    up      
Ethernet0/1            192.168.2.1     YES TFTP   up                    up      
Ethernet0/2            216.0.5.2       YES TFTP   up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RT1#





User Access Verification

Username: cisco
Password: 
Fallout-RT1#
*Jun  7 10:35:59.712: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: cisco] [Source: LOCAL] [localport: 0] at 10:35:59 UTC Sun Jun 7 2026
Fallout-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.2.2     YES TFTP   up                    up      
Ethernet0/1            192.168.3.1     YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Fallout-RT1#


Cafe-RT1#
Cafe-RT1#
Cafe-RT1#show running-config | section router
router eigrp 1
 network 192.168.1.0
 network 192.168.2.0 0.0.0.3
Cafe-RT1#
Cafe-RT1#
Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#no router eigrp 1
Cafe-RT1(config)#exit
Cafe-RT1#
*Jun  7 10:45:55.482: %SYS-5-CONFIG_I: Configured from console by cisco on console
Cafe-RT1#show ip route
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

      192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.1.0/24 is directly connected, Ethernet0/0
L        192.168.1.1/32 is directly connected, Ethernet0/0
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.1/32 is directly connected, Ethernet0/1
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/2
L        216.0.5.2/32 is directly connected, Ethernet0/2
Cafe-RT1#


Fallout-RT1#
Fallout-RT1#show running-config | section router
router eigrp 1
 network 192.168.2.0 0.0.0.3
 network 192.168.3.0
Fallout-RT1#
Fallout-RT1#
Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#no ro
*Jun  7 10:46:53.515: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Fallout-RT1(config)#no router
*Jun  7 10:46:53.617: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  7 10:46:53.618: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  7 10:46:53.728: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Fallout-RT1(config)#no router
*Jun  7 10:46:53.829: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun  7 10:46:53.829: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Fallout-RT1(config)#no routereigrp 1
                             ^
% Invalid input detected at '^' marker.

Fallout-RT1(config)#no router eigrp 1
Fallout-RT1(config)#exit
Fallout-RT1#sho
*Jun  7 10:47:15.184: %SYS-5-CONFIG_I: Configured from console by cisco on console
Fallout-RT1#show ip route
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

      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/0
L        192.168.2.2/32 is directly connected, Ethernet0/0
      192.168.3.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.3.0/24 is directly connected, Ethernet0/1
L        192.168.3.1/32 is directly connected, Ethernet0/1
Fallout-RT1# 


Cafe-RT1#
Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#ip route 192.168.3.0 255.255.255.0 192.168.2.2 
Cafe-RT1(config)#end
Cafe-RT1#
*Jun  7 10:49:05.904: %SYS-5-CONFIG_I: Configured from console by cisco on console
Cafe-RT1#show ip route
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

      192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.1.0/24 is directly connected, Ethernet0/0
L        192.168.1.1/32 is directly connected, Ethernet0/0
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.1/32 is directly connected, Ethernet0/1
S     192.168.3.0/24 [1/0] via 192.168.2.2
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/2
L        216.0.5.2/32 is directly connected, Ethernet0/2
Cafe-RT1#


Fallout-RT1#
Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#ip route 192.168.1.0 255.255.255.0 192.168.2.1
Fallout-RT1(config)#exit
Fallout-RT1#
*Jun  7 10:50:31.391: %SYS-5-CONFIG_I: Configured from console by cisco on console
Fallout-RT1#show ip route 
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

S     192.168.1.0/24 [1/0] via 192.168.2.1
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/0
L        192.168.2.2/32 is directly connected, Ethernet0/0
      192.168.3.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.3.0/24 is directly connected, Ethernet0/1
L        192.168.3.1/32 is directly connected, Ethernet0/1
Fallout-RT1# 


Connecting to console for Cafe-PC1
Connected to CML terminalserver.
Escape character is '^]'.

Core Linux
Cafe-PC1 login: 
Core Linux
Cafe-PC1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@Cafe-PC1:~$ ping -c 5 192.168.3.100
PING 192.168.3.100 (192.168.3.100): 56 data bytes
64 bytes from 192.168.3.100: seq=0 ttl=62 time=2.167 ms
64 bytes from 192.168.3.100: seq=1 ttl=62 time=1.125 ms
64 bytes from 192.168.3.100: seq=2 ttl=62 time=1.214 ms
64 bytes from 192.168.3.100: seq=3 ttl=62 time=1.199 ms
64 bytes from 192.168.3.100: seq=4 ttl=62 time=1.213 ms

--- 192.168.3.100 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.125/1.383/2.167 ms
cisco@Cafe-PC1:~$ 


Connecting to console for Shelter-SRV

Core Linux
Shelter-SRV login: 
Core Linux
Shelter-SRV login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@Shelter-SRV:~$ 
cisco@Shelter-SRV:~$ ping 192.168.1.50
PING 192.168.1.50 (192.168.1.50): 56 data bytes
64 bytes from 192.168.1.50: seq=0 ttl=62 time=1.080 ms
64 bytes from 192.168.1.50: seq=1 ttl=62 time=1.908 ms
64 bytes from 192.168.1.50: seq=2 ttl=62 time=1.122 ms
64 bytes from 192.168.1.50: seq=3 ttl=62 time=1.177 ms
64 bytes from 192.168.1.50: seq=4 ttl=62 time=1.155 ms
64 bytes from 192.168.1.50: seq=5 ttl=62 time=1.205 ms
64 bytes from 192.168.1.50: seq=6 ttl=62 time=1.103 ms
64 bytes from 192.168.1.50: seq=7 ttl=62 time=1.223 ms
64 bytes from 192.168.1.50: seq=8 ttl=62 time=1.223 ms
^C
--- 192.168.1.50 ping statistics ---
9 packets transmitted, 9 packets received, 0% packet loss
round-trip min/avg/max = 1.080/1.244/1.908 ms
cisco@Shelter-SRV:~$ 


Cafe-RT1#
*Jun  7 10:55:02.148: %SYS-5-CONFIG_I: Configured from console by cisco on console
Cafe-RT1#show ip route
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

      192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.1.0/24 is directly connected, Ethernet0/0
L        192.168.1.1/32 is directly connected, Ethernet0/0
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.1/32 is directly connected, Ethernet0/1
S     192.168.3.0/24 [1/0] via 192.168.2.2
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/2
L        216.0.5.2/32 is directly connected, Ethernet0/2
Cafe-RT1#ping 216.0.5.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-RT1#
Cafe-RT1#
Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#ip route 0.0.0.0 0.0.0.0 216.0.5.1
Cafe-RT1(config)#exit
Cafe-RT1#
*Jun  7 10:56:20.319: %SYS-5-CONFIG_I: Configured from console by cisco on console
Cafe-RT1#show ip route 
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
      192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.1.0/24 is directly connected, Ethernet0/0
L        192.168.1.1/32 is directly connected, Ethernet0/0
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.1/32 is directly connected, Ethernet0/1
S     192.168.3.0/24 [1/0] via 192.168.2.2
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/2
L        216.0.5.2/32 is directly connected, Ethernet0/2
Cafe-RT1#ping 203.0.113.8
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 203.0.113.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-RT1#


cisco@Cafe-PC1:~$ ping 203.0.113.8
PING 203.0.113.8 (203.0.113.8): 56 data bytes
64 bytes from 203.0.113.8: seq=0 ttl=254 time=0.894 ms
64 bytes from 203.0.113.8: seq=1 ttl=254 time=0.987 ms
64 bytes from 203.0.113.8: seq=2 ttl=254 time=0.989 ms
64 bytes from 203.0.113.8: seq=3 ttl=254 time=0.999 ms
64 bytes from 203.0.113.8: seq=4 ttl=254 time=1.032 ms
64 bytes from 203.0.113.8: seq=5 ttl=254 time=1.009 ms
64 bytes from 203.0.113.8: seq=6 ttl=254 time=1.040 ms
64 bytes from 203.0.113.8: seq=7 ttl=254 time=1.022 ms
64 bytes from 203.0.113.8: seq=8 ttl=254 time=0.959 ms

--- 203.0.113.8 ping statistics ---
9 packets transmitted, 9 packets received, 0% packet loss
^Cround-trip min/avg/max = 0.894/0.992/1.040 ms
cisco@Cafe-PC1:~$ 


Cafe-RT1#
Cafe-RT1#show ip route
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
      192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.1.0/24 is directly connected, Ethernet0/0
L        192.168.1.1/32 is directly connected, Ethernet0/0
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.1/32 is directly connected, Ethernet0/1
S     192.168.3.0/24 [1/0] via 192.168.2.2
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/2
L        216.0.5.2/32 is directly connected, Ethernet0/2
Cafe-RT1#
Cafe-RT1#
Cafe-RT1#show ip route 192.168.3.0
Routing entry for 192.168.3.0/24
  Known via "static", distance 1, metric 0
  Routing Descriptor Blocks:
  * 192.168.2.2
      Route metric is 0, traffic share count is 1
Cafe-RT1#show ip route 0.0.0.0
Routing entry for 0.0.0.0/0, supernet
  Known via "static", distance 1, metric 0, candidate default path
  Routing Descriptor Blocks:
  * 216.0.5.1
      Route metric is 0, traffic share count is 1
Cafe-RT1#show ip route 203.0.113.8
% Network not in table
Cafe-RT1#show ip route 192.168.3.10
Routing entry for 192.168.3.0/24
  Known via "static", distance 1, metric 0
  Routing Descriptor Blocks:
  * 192.168.2.2
      Route metric is 0, traffic share count is 1
Cafe-RT1#


Fallout-RT1#
Fallout-RT1#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is not set

S     192.168.1.0/24 [1/0] via 192.168.2.1
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/0
L        192.168.2.2/32 is directly connected, Ethernet0/0
      192.168.3.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.3.0/24 is directly connected, Ethernet0/1
L        192.168.3.1/32 is directly connected, Ethernet0/1
Fallout-RT1#show ip route 0.0.0.0
% Network not in table
Fallout-RT1#ping 203.0.113.8
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 203.0.113.8, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#ip route 0.0.0.0 0.0.0.0 192.168.2.1 5
Fallout-RT1(config)#end
Fallout-RT1#
*Jun  7 11:08:52.457: %SYS-5-CONFIG_I: Configured from console by cisco on console
Fallout-RT1#
Fallout-RT1#
Fallout-RT1#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is 192.168.2.1 to network 0.0.0.0

S*    0.0.0.0/0 [5/0] via 192.168.2.1
S     192.168.1.0/24 [1/0] via 192.168.2.1
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/0
L        192.168.2.2/32 is directly connected, Ethernet0/0
      192.168.3.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.3.0/24 is directly connected, Ethernet0/1
L        192.168.3.1/32 is directly connected, Ethernet0/1
Fallout-RT1#show runn in-config | include ip route
                        ^
% Invalid input detected at '^' marker.

Fallout-RT1#show running-config | include ip route
ip route 0.0.0.0 0.0.0.0 192.168.2.1 5
ip route 192.168.1.0 255.255.255.0 192.168.2.1
Fallout-RT1#show running-config | include ip route 0.0.0.0
ip route 0.0.0.0 0.0.0.0 192.168.2.1 5
Fallout-RT1#show ip route 0.0.0.0
Routing entry for 0.0.0.0/0, supernet
  Known via "static", distance 5, metric 0, candidate default path
  Routing Descriptor Blocks:
  * 192.168.2.1
      Route metric is 0, traffic share count is 1
Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#no ip route 0.0.0.0 0.0.0.0 192.168.2.1 5
Fallout-RT1(config)#end
Fallout-RT1#
*Jun  7 11:15:58.651: %SYS-5-CONFIG_I: Configured from console by cisco on console
Fallout-RT1#show ip route                                 
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is not set

S     192.168.1.0/24 [1/0] via 192.168.2.1
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/0
L        192.168.2.2/32 is directly connected, Ethernet0/0
      192.168.3.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.3.0/24 is directly connected, Ethernet0/1
L        192.168.3.1/32 is directly connected, Ethernet0/1
Fallout-RT1#show running-config | include ip route        
ip route 192.168.1.0 255.255.255.0 192.168.2.1
Fallout-RT1#
```
