```bash
Connecting to console for Cafe-RT1
Connected to CML terminalserver.


User Access Verification

Username: cisco
Password: 
Cafe-RT1#
*Jun  6 20:23:43.977: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: cisco] [Source: LOCAL] [localport: 0] at 20:23:43 UTC Sat Jun 6 2026
Cafe-RT1#
Cafe-RT1#
Cafe-RT1#show running-config | include ip route
ip route 0.0.0.0 0.0.0.0 216.0.5.1
ip route 192.168.3.0 255.255.255.0 192.168.2.2
Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#
*Jun  6 20:24:16.670: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-RT1(config)#no 
*Jun  6 20:24:16.772: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 20:24:16.773: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 20:24:16.878: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-RT1(config)#no ip 
*Jun  6 20:24:16.978: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun  6 20:24:16.978: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-RT1(config)#no ip route 192.168.3.0 255.255.255.0 192.168.2.2
Cafe-RT1(config)#end
Cafe-RT1#sh
*Jun  6 20:24:44.080: %SYS-5-CONFIG_I: Configured from console by cisco on console
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
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/2
L        216.0.5.2/32 is directly connected, Ethernet0/2
Cafe-RT1#


User Access Verification

Username: cisco
Password: 
Fallout-RT1#
*Jun  6 20:25:39.150: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: cisco] [Source: LOCAL] [localport: 0] at 20:25:39 UTC Sat Jun 6 2026
Fallout-RT1#show running-config | include ip route
ip route 0.0.0.0 0.0.0.0 192.168.2.1
ip route 192.168.1.0 255.255.255.0 192.168.2.1
Fallout-RT1#
Fallout-RT1#
Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#
*Jun  6 20:26:00.658: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Fallout-RT1(config)#
*Jun  6 20:26:00.760: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 20:26:00.761: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 20:26:00.868: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Fallout-RT1(config)#no i
*Jun  6 20:26:00.968: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun  6 20:26:00.968: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Fallout-RT1(config)#no ip route 192.168.1.0 255.255.255.0 192.168.2.1
Fallout-RT1(config)#end
Fallout-RT1#show 
*Jun  6 20:26:32.341: %SYS-5-CONFIG_I: Configured from console by cisco on console
Fallout-RT1#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is 192.168.2.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 192.168.2.1
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.2/32 is directly connected, Ethernet0/1
      192.168.3.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.3.0/24 is directly connected, Ethernet0/0
L        192.168.3.1/32 is directly connected, Ethernet0/0
Fallout-RT1#

Cafe-RT1#
Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#router eigrp 1
Cafe-RT1(config-router)#network 192.168.1.0 0.0.0.255
Cafe-RT1(config-router)#network 192.168.2.0 0.0.0.3
Cafe-RT1(config-router)#end
Cafe-RT1#
*Jun  6 20:27:51.875: %SYS-5-CONFIG_I: Configured from console by cisco on console
Cafe-RT1#show ip eigrp neighbors
EIGRP-IPv4 Neighbors for AS(1)
Cafe-RT1#
Cafe-RT1#


Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#router eigrp 1
Fallout-RT1(config-router)#network 192.168.3.0 0.0.0.255
Fallout-RT1(config-router)#network 192.168.2.0 0.0.0.3  
Fallout-RT1(config-router)#
*Jun  6 20:29:32.823: %DUAL-5-NBRCHANGE: EIGRP-IPv4 1: Neighbor 192.168.2.1 (Ethernet0/1) is up: new adjacency
Fallout-RT1(config-router)#end
Fallout-RT1#
*Jun  6 20:29:35.326: %SYS-5-CONFIG_I: Configured from console by cisco on console
Fallout-RT1#show ip  eigrp neighbors
EIGRP-IPv4 Neighbors for AS(1)
H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
0   192.168.2.1             Et0/1                    13 00:00:20    1   100  0  3
Fallout-RT1#show ip route eigrp
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is 192.168.2.1 to network 0.0.0.0

D     192.168.1.0/24 [90/307200] via 192.168.2.1, 00:00:45, Ethernet0/1
Fallout-RT1#


Cafe-RT1#show ip route eigrp
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF external type 2
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

D     192.168.3.0/24 [90/307200] via 192.168.2.2, 00:02:02, Ethernet0/1
Cafe-RT1#
Cafe-RT1#


Fallout-RT1#
Fallout-RT1#show ip route eigrp
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is 192.168.2.1 to network 0.0.0.0

D     192.168.1.0/24 [90/307200] via 192.168.2.1, 00:02:22, Ethernet0/1
Fallout-RT1#


Connecting to console for Cafe-PC

Core Linux
cafe-pc login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-pc:~$ 
cisco@cafe-pc:~$ 
cisco@cafe-pc:~$ ping -c 5 192.168.3.100
PING 192.168.3.100 (192.168.3.100): 56 data bytes
64 bytes from 192.168.3.100: seq=0 ttl=62 time=2.233 ms
64 bytes from 192.168.3.100: seq=1 ttl=62 time=1.067 ms
64 bytes from 192.168.3.100: seq=2 ttl=62 time=1.166 ms
64 bytes from 192.168.3.100: seq=3 ttl=62 time=1.036 ms
64 bytes from 192.168.3.100: seq=4 ttl=62 time=1.174 ms

--- 192.168.3.100 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.036/1.335/2.233 ms
cisco@cafe-pc:~$ 


Connecting to console for Fallout-SRV

Core Linux
fallout-srv login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@fallout-srv:~$ 
cisco@fallout-srv:~$ 
cisco@fallout-srv:~$ ping -c 5 192.168.1.50
PING 192.168.1.50 (192.168.1.50): 56 data bytes
64 bytes from 192.168.1.50: seq=0 ttl=62 time=1.127 ms
64 bytes from 192.168.1.50: seq=1 ttl=62 time=1.154 ms
64 bytes from 192.168.1.50: seq=2 ttl=62 time=1.119 ms
64 bytes from 192.168.1.50: seq=3 ttl=62 time=1.152 ms
64 bytes from 192.168.1.50: seq=4 ttl=62 time=1.133 ms

--- 192.168.1.50 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.119/1.137/1.154 ms
cisco@fallout-srv:~$ 


Cafe-RT1#
Cafe-RT1#write memory
Building configuration...
[OK]
Cafe-RT1#


Fallout-RT1#
Fallout-RT1#write memory
Building configuration...
[OK]
Fallout-RT1#
```
