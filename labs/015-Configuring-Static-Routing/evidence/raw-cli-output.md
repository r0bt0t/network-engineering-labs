Connecting to console for Cafe-RT1


User Access Verification

Username: cisco
Password: 
Cafe-RT1#
*Jun  6 11:26:06.857: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: cisco] [Source: LOCAL] [localport: 0] at 11:26:06 UTC Sat Jun 6 2026
Cafe-RT1#en
Cafe-RT1#CrC0ffee!
% Bad IP address or host name% Unknown command or computer name, or unable to find computer address
Cafe-RT1#
*Jun  6 11:26:13.994: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-RT1#
*Jun  6 11:26:14.096: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 11:26:14.096: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 11:26:14.204: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-RT1#
*Jun  6 11:26:14.305: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun  6 11:26:14.306: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-RT1#
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

Gateway of last resort is not set

      192.168.1.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.1.0/24 is directly connected, Ethernet0/0
L        192.168.1.1/32 is directly connected, Ethernet0/0
      192.168.2.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.1/32 is directly connected, Ethernet0/1
Cafe-RT1#
Cafe-RT1#
Cafe-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES TFTP   up                    up      
Ethernet0/1            192.168.2.1     YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down 


Connecting to console for Fallout-RT1


User Access Verification

Username: 
% Username:  timeout expired!
Username: 
% Username:  timeout expired!
Username: cisco
Password: 
Fallout-RT1#
*Jun  6 11:27:23.002: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: cisco] [Source: LOCAL] [localport: 0] at 11:27:23 UTC Sat Jun 6 2026
Fallout-RT1#en
Fallout-RT1#
*Jun  6 11:27:27.856: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Fallout-RT1#
*Jun  6 11:27:27.958: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 11:27:27.958: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 11:27:28.064: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Fallout-RT1#
*Jun  6 11:27:28.164: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun  6 11:27:28.164: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
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
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.2/32 is directly connected, Ethernet0/1
      192.168.3.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.3.0/24 is directly connected, Ethernet0/0
L        192.168.3.1/32 is directly connected, Ethernet0/0
Fallout-RT1#
Fallout-RT1#
Fallout-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.3.1     YES TFTP   up                    up      
Ethernet0/1            192.168.2.2     YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Fallout-RT1#
Fallout-RT1#


Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#ip route 192.168.3.0 255.255.255.0 192.168.2.2
Cafe-RT1(config)#
Cafe-RT1(config)#^Z
Cafe-RT1#s
*Jun  6 11:29:02.668: %SYS-5-CONFIG_I: Configured from console by cisco on console
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
Cafe-RT1#
Cafe-RT1#
Cafe-RT1#


Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#ip route 192.168.1.0 255.255.255.0 192.168.2.1
Fallout-RT1(config)#^Z
Fallout-RT1#show
*Jun  6 11:30:45.161: %SYS-5-CONFIG_I: Configured from console by cisco on console
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
C        192.168.2.0/30 is directly connected, Ethernet0/1
L        192.168.2.2/32 is directly connected, Ethernet0/1
      192.168.3.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.3.0/24 is directly connected, Ethernet0/0
L        192.168.3.1/32 is directly connected, Ethernet0/0
Fallout-RT1#
Fallout-RT1#


Cafe-RT1#
Cafe-RT1#ping 192.168.3.100
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.3.100, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms
Cafe-RT1#
Cafe-RT1#


Connecting to console for Fallout-SRV
Connected to CML terminalserver.

Core Linux
fallout-srv login: 
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
64 bytes from 192.168.1.50: seq=0 ttl=62 time=1.619 ms
64 bytes from 192.168.1.50: seq=1 ttl=62 time=1.057 ms
64 bytes from 192.168.1.50: seq=2 ttl=62 time=1.065 ms
64 bytes from 192.168.1.50: seq=3 ttl=62 time=1.582 ms
64 bytes from 192.168.1.50: seq=4 ttl=62 time=1.065 ms

--- 192.168.1.50 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.057/1.277/1.619 ms
cisco@fallout-srv:~$ 



Cafe-RT1#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Cafe-RT1#


Fallout-RT1#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Fallout-RT1#