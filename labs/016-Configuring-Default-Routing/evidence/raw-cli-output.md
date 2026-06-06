```bash
Username: cisco
Password: 
Cafe-RT1#
*Jun  6 15:28:47.537: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: cisco] [Source: LOCAL] [localport: 0] at 15:28:47 UTC Sat Jun 6 2026
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
Cafe-RT1#
Cafe-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES TFTP   up                    up      
Ethernet0/1            192.168.2.1     YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RT1#
Cafe-RT1#
Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#  
*Jun  6 15:30:18.499: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jun  6 15:30:18.601: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 15:30:18.602: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun  6 15:30:18.708: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-RT1(config)#
*Jun  6 15:30:18.809: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun  6 15:30:18.810: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-RT1(config)#interface et0/2        
Cafe-RT1(config-if)#description ## Public Uplink
Cafe-RT1(config-if)#ip address 216.0.5.2 255.255.255.252
Cafe-RT1(config-if)#no shutdown
Cafe-RT1(config-if)#
Cafe-RT1(config-if)#^Z
Cafe-RT1#
*Jun  6 15:33:46.654: %LINK-3-UPDOWN: Interface Ethernet0/2, changed state to up
*Jun  6 15:33:47.261: %SYS-5-CONFIG_I: Configured from console by cisco on console
Cafe-RT1#
*Jun  6 15:33:47.654: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES TFTP   up                    up      
Ethernet0/1            192.168.2.1     YES TFTP   up                    up      
Ethernet0/2            216.0.5.2       YES manual up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RT1#


Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#ip route 0.0.0.0 0.0.0.0 216.0.5.1
Cafe-RT1(config)#end
Cafe-RT1#
*Jun  6 15:37:32.558: %SYS-5-CONFIG_I: Configured from console by cisco on console
Cafe-RT1#show ip route | include Gateway
Gateway of last resort is 216.0.5.1 to network 0.0.0.0
Cafe-RT1#show ip route static
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
S     192.168.3.0/24 [1/0] via 192.168.2.2
Cafe-RT1#


Connecting to console for Cafe-PC

Core Linux
cafe-pc login: 
Core Linux
cafe-pc login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-pc:~$ ping -c 5 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=254 time=1.421 ms
64 bytes from 8.8.8.8: seq=1 ttl=254 time=1.005 ms
64 bytes from 8.8.8.8: seq=2 ttl=254 time=1.143 ms
64 bytes from 8.8.8.8: seq=3 ttl=254 time=1.138 ms
64 bytes from 8.8.8.8: seq=4 ttl=254 time=1.117 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.005/1.164/1.421 ms
cisco@cafe-pc:~$ ^C

cisco@cafe-pc:~$
```
