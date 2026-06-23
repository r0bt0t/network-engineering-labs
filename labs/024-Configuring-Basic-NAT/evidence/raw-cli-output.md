# Lab 024 - Raw CLI Output

```text
Router>enable
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#ho
*Jun 23 13:04:09.887: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Jun 23 13:04:09.888: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
*Jun 23 13:04:09.888: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
Router(config)#hostnam
*Jun 23 13:04:09.891: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Router(config)#hostname I
*Jun 23 13:04:09.991: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 19 seconds).
*Jun 23 13:04:09.991: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Router(config)#hostname ISP-Rtr
ISP-Rtr(config)#
ISP-Rtr(config)#enable secret Cisco
ISP-Rtr(config)#
ISP-Rtr(config)#line console 0
ISP-Rtr(config-line)#password Cisco
ISP-Rtr(config-line)#login
ISP-Rtr(config-line)#exit
ISP-Rtr(config)#
ISP-Rtr(config)#line vty 0 4
ISP-Rtr(config-line)#password Cisco
ISP-Rtr(config-line)#login 
ISP-Rtr(config-line)#exit
ISP-Rtr(config)#
ISP-Rtr(config)#service password-encryption

ISP-Rtr(config)#interface ethernet0/0
ISP-Rtr(config-if)#description WAN Link to Cafe-Rtr
ISP-Rtr(config-if)#ip address 216.0.5.1 255.255.255.252
ISP-Rtr(config-if)#no shutdown
ISP-Rtr(config-if)#exit
ISP-Rtr(config)#
*Jun 23 13:07:32.104: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
ISP-Rtr(config)#
*Jun 23 13:07:33.104: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
ISP-Rtr(config)#
ISP-Rtr(config)#show ip interface brief
                  ^
% Invalid input detected at '^' marker.

ISP-Rtr(config)#exit
ISP-Rtr#
*Jun 23 13:07:58.467: %SYS-5-CONFIG_I: Configured from console by console
ISP-Rtr#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            216.0.5.1       YES manual up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
ISP-Rtr#

Cafe-Rtr>en
Password: 
*Jun 23 13:09:04.321: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jun 23 13:09:04.423: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 23 13:09:04.424: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 23 13:09:04.531: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 23 13:09:04.631: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 23 13:09:04.631: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Password: 
Cafe-Rtr#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES TFTP   up                    up      
Ethernet0/1            216.0.5.2       YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#ip route 0.0.0.0 0.0.0.0 216.0.5.1
Cafe-Rtr(config)#show ip route
                   ^
% Invalid input detected at '^' marker.

Cafe-Rtr(config)#exit
Cafe-Rtr#
*Jun 23 13:10:54.859: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show ip route
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
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/1
L        216.0.5.2/32 is directly connected, Ethernet0/1
Cafe-Rtr#

ISP-Rtr#
ISP-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
ISP-Rtr(config)#interface loopback1
ISP-Rtr(config-if)#
*Jun 23 13:11:58.339: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback1, changed state to up
ISP-Rtr(config-if)#ip address 1.1.1.1 255.255.255.255
ISP-Rtr(config-if)#exit
ISP-Rtr(config)#
ISP-Rtr(config)#interface loopback8                 
ISP-Rtr(config-if)#
*Jun 23 13:13:01.672: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback8, changed state to up
ISP-Rtr(config-if)#ip address 8.8.8.8 255.255.255.255
ISP-Rtr(config-if)#exit
ISP-Rtr(config)#exit
ISP-Rtr#
*Jun 23 13:13:32.841: %SYS-5-CONFIG_I: Configured from console by console
ISP-Rtr#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            216.0.5.1       YES manual up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Loopback1              1.1.1.1         YES manual up                    up      
Loopback8              8.8.8.8         YES manual up                    up      
ISP-Rtr#

Cafe-Rtr#
Cafe-Rtr#ping 216.0.5.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-Rtr#ping 1.1.1.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 1.1.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms
Cafe-Rtr#ping 8.8.8.8
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-Rtr#

Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#interface ethernet0/0
Cafe-Rtr(config-if)#ip nat inside
Cafe-Rtr(config-if)#exit
Cafe-Rtr(config)#
Cafe-Rtr(config)#interface ethernet0/1
Cafe-Rtr(config-if)#ip nat outside
Cafe-Rtr(config-if)#exit
Cafe-Rtr(config)#
Cafe-Rtr(config)#end
Cafe-Rtr#
*Jun 23 13:17:02.365: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show running-config interface ethernet0/0
Building configuration...

Current configuration : 127 bytes
!
interface Ethernet0/0
 description Cafe LAN to Cafe-Sw Ethernet0/0
 ip address 192.168.1.1 255.255.255.0
 ip nat inside
end

Cafe-Rtr#show running-config interface ethernet0/1
Building configuration...

Current configuration : 127 bytes
!
interface Ethernet0/1
 description WAN toward ISP-Rtr Ethernet0/0
 ip address 216.0.5.2 255.255.255.252
 ip nat outside
end

Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#ip nat inside source static 192.168.1.50 216.0.5.20
Cafe-Rtr(config)#exit
Cafe-Rtr#sh
*Jun 23 13:19:12.761: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show ip nat translation
Pro Inside global      Inside local       Outside local      Outside global
--- 216.0.5.20         192.168.1.50       ---                ---
Cafe-Rtr#

ISP-Rtr#
ISP-Rtr#ping 216.0.5.20
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.20, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/2 ms
ISP-Rtr#
ISP-Rtr#ping 192.168.1.51
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.51, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
ISP-Rtr#

Cafe-Rtr#show ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
--- 216.0.5.20         192.168.1.50       ---                ---
Cafe-Rtr#
Cafe-Rtr#show ip nat statistics
Total active translations: 1 (1 static, 0 dynamic; 0 extended)
Outside interfaces:
  Ethernet0/1
Inside interfaces: 
  Ethernet0/0
Hits: 10  Misses: 0
CEF Translated packets: 10, CEF Punted packets: 0
 Reserved port setting disabled provisioned no
 Dynamic overload mapping configured: 0
Expired translations: 1
Dynamic mappings:
nat-limit statistics:
 max entry: max allowed 0, used 0, missed 0
Cafe-Rtr#

Cafe-Rtr#
Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#no ip nat inside source static 192.168.1.50 216.0.5.20
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#$ Cafe-Public 216.0.5.50 216.0.5.100 netmask 255.255.255.0  
Cafe-Rtr(config)#access-list 1 permit 192.168.1.0 0.0.0.255                    
Cafe-Rtr(config)#ip nat inside source list 1 pool Cafe-Public
Cafe-Rtr(config)#
Cafe-Rtr(config)#

pc1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@pc1:~$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: seq=0 ttl=254 time=1.312 ms
64 bytes from 1.1.1.1: seq=1 ttl=254 time=1.285 ms
64 bytes from 1.1.1.1: seq=2 ttl=254 time=1.253 ms
64 bytes from 1.1.1.1: seq=3 ttl=254 time=1.264 ms
64 bytes from 1.1.1.1: seq=4 ttl=254 time=2.233 ms
64 bytes from 1.1.1.1: seq=5 ttl=254 time=1.260 ms
64 bytes from 1.1.1.1: seq=6 ttl=254 time=1.243 ms
64 bytes from 1.1.1.1: seq=7 ttl=254 time=1.338 ms
^C
--- 1.1.1.1 ping statistics ---
8 packets transmitted, 8 packets received, 0% packet loss
round-trip min/avg/max = 1.243/1.398/2.233 ms
cisco@pc1:~$ 


pc2 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@pc2:~$ ping -c 5 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=254 time=2.227 ms
64 bytes from 8.8.8.8: seq=1 ttl=254 time=1.300 ms
64 bytes from 8.8.8.8: seq=2 ttl=254 time=1.379 ms
64 bytes from 8.8.8.8: seq=3 ttl=254 time=1.412 ms
64 bytes from 8.8.8.8: seq=4 ttl=254 time=1.315 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.300/1.526/2.227 ms
cisco@pc2:~$ 

Cafe-Rtr#
Cafe-Rtr#show ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
icmp 216.0.5.50:738    192.168.1.50:738   1.1.1.1:738        1.1.1.1:738
--- 216.0.5.50         192.168.1.50       ---                ---
icmp 216.0.5.51:739    192.168.1.51:739   8.8.8.8:739        8.8.8.8:739
--- 216.0.5.51         192.168.1.51       ---                ---
Cafe-Rtr#

Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#no ip nat inside source list 1 pool Cafe-Public
%Dynamic mapping in use, cannot remove
Cafe-Rtr(config)#end
Cafe-Rtr#
*Jun 23 13:32:13.215: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#clear ip nat translation * 
Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#no ip nat inside source list 1 pool Cafe-Public
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#interface ethernet0/0
Cafe-Rtr(config-if)#shutdown
Cafe-Rtr(config-if)#exit
Cafe-Rtr(config)#
*Jun 23 13:33:09.643: %LINK-5-CHANGED: Interface Ethernet0/0, changed state to administratively down
*Jun 23 13:33:10.643: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Cafe-Rtr(config)#
Cafe-Rtr(config)#interface ethernet0/1
Cafe-Rtr(config-if)#shutdown             
Cafe-Rtr(config-if)#exit                 
Cafe-Rtr(config)#
*Jun 23 13:33:23.078: %LINK-5-CHANGED: Interface Ethernet0/1, changed state to administratively down
*Jun 23 13:33:24.078: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#end
Cafe-Rtr#conf t
*Jun 23 13:33:35.108: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#clear ip nat translation *
Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#
Cafe-Rtr(config)#ip nat inside source list 1 interface ethernet0/1 overload
Cafe-Rtr(config)#interface ethernet0/0
Cafe-Rtr(config-if)#no shutdown
Cafe-Rtr(config-if)#exit
Cafe-Rtr(config)#
*Jun 23 13:34:52.683: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Cafe-Rtr(config)#
*Jun 23 13:34:53.683: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-Rtr(config)#interface ethernet0/1
Cafe-Rtr(config-if)#no shutdown          
Cafe-Rtr(config-if)#exit                 
*Jun 23 13:35:05.516: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
Cafe-Rtr(config-if)#exit
*Jun 23 13:35:06.516: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-Rtr(config-if)#exit
Cafe-Rtr(config)#exit
Cafe-Rtr#
*Jun 23 13:35:16.751: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES TFTP   up                    up      
Ethernet0/1            216.0.5.2       YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-Rtr#

cisco@pc1:~$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: seq=0 ttl=254 time=2.146 ms
64 bytes from 1.1.1.1: seq=1 ttl=254 time=1.278 ms
64 bytes from 1.1.1.1: seq=2 ttl=254 time=1.310 ms
64 bytes from 1.1.1.1: seq=3 ttl=254 time=1.281 ms
64 bytes from 1.1.1.1: seq=4 ttl=254 time=1.324 ms
64 bytes from 1.1.1.1: seq=5 ttl=254 time=1.237 ms
64 bytes from 1.1.1.1: seq=6 ttl=254 time=1.262 ms
64 bytes from 1.1.1.1: seq=7 ttl=254 time=1.282 ms
64 bytes from 1.1.1.1: seq=8 ttl=254 time=1.306 ms
64 bytes from 1.1.1.1: seq=9 ttl=254 time=1.381 ms
64 bytes from 1.1.1.1: seq=10 ttl=254 time=1.327 ms
64 bytes from 1.1.1.1: seq=11 ttl=254 time=1.372 ms
64 bytes from 1.1.1.1: seq=12 ttl=254 time=1.281 ms
64 bytes from 1.1.1.1: seq=13 ttl=254 time=1.317 ms
64 bytes fr

cisco@pc2:~$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=254 time=2.328 ms
64 bytes from 8.8.8.8: seq=1 ttl=254 time=1.421 ms
64 bytes from 8.8.8.8: seq=2 ttl=254 time=1.325 ms
64 bytes from 8.8.8.8: seq=3 ttl=254 time=1.330 ms
64 bytes from 8.8.8.8: seq=4 ttl=254 time=1.312 ms
64 bytes from 8.8.8.8: seq=5 ttl=254 time=1.326 ms
64 bytes from 8.8.8.8: seq=6 ttl=254 time=1.283 ms
64 bytes from 8.8.8.8: seq=7 ttl=254 time=1.323 ms
64 bytes from 8.8.8.8: seq=8 ttl=254 time=1.274 ms
64 bytes from 8.8.8.8: seq=9 ttl=254 time=1.271 ms
64 bytes from 8.8.8.8: seq=10 ttl=254 time=1.240 ms
64 bytes from 8.8.8.8: seq=11 ttl=254 time=1.275 ms
64 bytes from 8.8.8.8: seq=12 ttl=254 time=1.308 ms
64 bytes from 8.8.8.8: seq=13 ttl=254 time=1.327 ms
64 bytes from 8.8.8.8: seq=14 ttl=254 time=1.290 ms
64 bytes from 8.8.8.8: seq=15 ttl=254 time=1.260 ms
64 bytes from 8.8.8.8: seq=16 ttl=254 time=1.291 ms

Cafe-Rtr#show ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
icmp 216.0.5.2:1024    192.168.1.50:753   1.1.1.1:753        1.1.1.1:1024
icmp 216.0.5.2:1025    192.168.1.51:753   8.8.8.8:753        8.8.8.8:1025
Cafe-Rtr#

Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#$ublic 216.0.5.50 216.0.5.100 netmask 255.255.255.0         
Cafe-Rtr(config)#end
Cafe-Rtr#
*Jun 23 13:38:56.832: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES TFTP   up                    up      
Ethernet0/1            216.0.5.2       YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#show ip route
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
      216.0.5.0/24 is variably subnetted, 2 subnets, 2 masks
C        216.0.5.0/30 is directly connected, Ethernet0/1
L        216.0.5.2/32 is directly connected, Ethernet0/1
Cafe-Rtr#
Cafe-Rtr#show running-config | include ip nat 
 ip nat inside
 ip nat outside
ip nat inside source list 1 interface Ethernet0/1 overload
Cafe-Rtr#
Cafe-Rtr#show running-config | include access-list 
ip access-list standard 1
Cafe-Rtr#
Cafe-Rtr#show ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
icmp 216.0.5.2:1024    192.168.1.50:753   1.1.1.1:753        1.1.1.1:1024
icmp 216.0.5.2:1025    192.168.1.51:753   8.8.8.8:753        8.8.8.8:1025
Cafe-Rtr#show ip nat statistics
Total active translations: 2 (0 static, 2 dynamic; 2 extended)
Outside interfaces:
  Ethernet0/1
Inside interfaces: 
  Ethernet0/0
Hits: 1304  Misses: 0
CEF Translated packets: 1304, CEF Punted packets: 0
 Reserved port setting disabled provisioned no
 Dynamic overload mapping configured: 1
Expired translations: 6
Dynamic mappings:
-- Inside Source
[Id: 2] access-list 1 interface Ethernet0/1 refcount 2
nat-limit statistics:
 max entry: max allowed 0, used 0, missed 0
Cafe-Rtr#

ISP-Rtr#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            216.0.5.1       YES manual up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Loopback1              1.1.1.1         YES manual up                    up      
Loopback8              8.8.8.8         YES manual up                    up      
ISP-Rtr#
ISP-Rtr#
ISP-Rtr#show ip route
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

      1.0.0.0/32 is subnetted, 1 subnets
C        1.1.1.1 is directly connected, Loopback1
      8.0.0.0/32 is subnetted, 1 subnets
C        8.8.8.8 is directly connected, Loopback8
      216.0.5.0/24 is variably subnetted, 3 subnets, 3 masks
S        216.0.5.0/24 [1/0] via 216.0.5.2
C        216.0.5.0/30 is directly connected, Ethernet0/0
L        216.0.5.1/32 is directly connected, Ethernet0/0
ISP-Rtr# 
ISP-Rtr#ping 216.0.5.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 216.0.5.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```
