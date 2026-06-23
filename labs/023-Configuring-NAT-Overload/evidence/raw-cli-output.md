# Lab 023 - Raw CLI Output

```text
Connecting to console for Cafe-Rtr

Cafe-Rtr>en
Cafe-Rtr#sh
*Jun 13 17:51:53.902: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-Rtr#show r
*Jun 13 17:51:54.005: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 13 17:51:54.005: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 13 17:51:54.110: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-Rtr#show run
*Jun 13 17:51:54.210: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 13 17:51:54.210: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-Rtr#show running-config
Building configuration...

Current configuration : 1222 bytes
!
! Last configuration change at 17:51:54 UTC Sat Jun 13 2026
!
version 17.16
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname Cafe-Rtr
!
boot-start-marker
boot-end-marker
!
!
no aaa new-model
!
!
!
!
!
!
!
!         
!
!
!
!
!
ip cef
login on-success log
no ipv6 cef
!
!
!
!
!
!
!
!
!
!
!
!
!
memory free low-watermark processor 79983
!         
!
spanning-tree mode rapid-pvst
!
!
!
!
!
!
!
! 
!
!
!
!
!
!
!
!
!
!
!
!
!         
!
!
interface Ethernet0/0
 description Cafe LAN
 ip address 192.168.1.1 255.255.255.0
 ip nat inside
!
interface Ethernet0/1
 description WAN toward ISP-Rtr
 ip address 216.0.5.2 255.255.255.252
 ip nat outside
!
interface Ethernet0/2
 no ip address
 shutdown
!
interface Ethernet0/3
 no ip address
 shutdown
!
ip forward-protocol nd
ip forward-protocol udp
!         
!
ip http server
ip http secure-server
ip nat pool Cafe-Public 216.0.5.20 216.0.5.30 netmask 255.255.255.240
ip nat inside source list 1 pool Cafe-Public
ip route 0.0.0.0 0.0.0.0 216.0.5.1
ip ssh bulk-mode 131072
no logging btrace
ip access-list standard 1
 10 permit 192.168.1.0 0.0.0.255
!
!
!
control-plane
!
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input telnet ssh
!
!
!
!
end

Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#conf t                                         
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#no ip nat inside source list 1 pool Cafe-Public
Cafe-Rtr(config)#exit
Cafe-Rtr#
*Jun 13 17:53:12.882: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show ip nat translations
Cafe-Rtr#


Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#interface ethernet0/0
Cafe-Rtr(config-if)#no shutdown
Cafe-Rtr(config-if)#interface ethernet0/1
Cafe-Rtr(config-if)#no shutdown          
Cafe-Rtr(config-if)#interface ethernet0/1
Cafe-Rtr(config-if)#shutdown             
Cafe-Rtr(config-if)#interface ethernet0/1
*Jun 13 17:54:33.440: %LINK-5-CHANGED: Interface Ethernet0/1, changed state to administratively down
*Jun 13 17:54:34.440: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-Rtr(config-if)#interface ethernet0/0
Cafe-Rtr(config-if)#shutdown             
Cafe-Rtr(config-if)#
*Jun 13 17:54:43.262: %LINK-5-CHANGED: Interface Ethernet0/0, changed state to administratively down
*Jun 13 17:54:44.263: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Cafe-Rtr(config-if)#exit
Cafe-Rtr(config)#exit
Cafe-Rtr#
*Jun 13 17:55:38.272: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#


Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#ip nat inside source list 1 interface ethernet0/1 overload
Cafe-Rtr(config)#end
Cafe-Rtr#
*Jun 13 17:57:52.829: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show running-config interface ethernet0/0
Building configuration...

Current configuration : 114 bytes
!
interface Ethernet0/0
 description Cafe LAN
 ip address 192.168.1.1 255.255.255.0
 ip nat inside
 shutdown
end

Cafe-Rtr#show running-config interface ethernet0/1
Building configuration...

Current configuration : 125 bytes
!
interface Ethernet0/1
 description WAN toward ISP-Rtr
 ip address 216.0.5.2 255.255.255.252
 ip nat outside
 shutdown
end


Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#interface ethernet0/0
Cafe-Rtr(config-if)#no shutdown
Cafe-Rtr(config-if)#interface ethernet0/ 
*Jun 13 17:59:29.414: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Cafe-Rtr(config-if)#interface ethernet0/1
*Jun 13 17:59:30.414: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-Rtr(config-if)#interface ethernet0/1
Cafe-Rtr(config-if)#no shutdown
Cafe-Rtr(config-if)#
*Jun 13 17:59:43.848: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
Cafe-Rtr(config-if)#
*Jun 13 17:59:44.848: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-Rtr(config-if)#end
Cafe-Rtr#
*Jun 13 17:59:57.783: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show running-confir interface ethernet0/0
                           ^
% Invalid input detected at '^' marker.

Cafe-Rtr#show running-config interface ethernet0/0
Building configuration...

Current configuration : 104 bytes
!
interface Ethernet0/0
 description Cafe LAN
 ip address 192.168.1.1 255.255.255.0
 ip nat inside
end

Cafe-Rtr#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES TFTP   up                    up      
Ethernet0/1            216.0.5.2       YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-Rtr#

cisco@pc1:~$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: seq=0 ttl=254 time=0.990 ms
64 bytes from 1.1.1.1: seq=1 ttl=254 time=0.740 ms
64 bytes from 1.1.1.1: seq=2 ttl=254 time=0.847 ms
64 bytes from 1.1.1.1: seq=3 ttl=254 time=0.847 ms
64 bytes from 1.1.1.1: seq=4 ttl=254 time=0.699 ms
64 bytes from 1.1.1.1: seq=5 ttl=254 time=0.729 ms
64 bytes from 1.1.1.1: seq=6 ttl=254 time=0.706 ms
64 bytes from 1.1.1.1: seq=7 ttl=254 time=0.729 ms
64 bytes from 1.1.1.1: seq=8 ttl=254 time=0.695 ms
64 bytes from 1.1.1.1: seq=9 ttl=254 time=0.639 ms
64 bytes from 1.1.1.1: seq=10 ttl=254 time=0.667 ms
64 bytes from 1.1.1.1: seq=11 ttl=254 time=0.713 ms
64 bytes from 1.1.1.1: seq=12 ttl=254 time=0.615 ms
64 bytes from 1.1.1.1: seq=13 ttl=254 time=0.657 ms
^C
--- 1.1.1.1 ping statistics ---
14 packets transmitted, 14 packets received, 0% packet loss
round-trip min/avg/max = 0.615/0.733/0.990 ms
cisco@pc1:~$ 


Connecting to console for PC2

Core Linux
pc2 login: 
Core Linux
pc2 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@pc2:~$ ping -c 5 1.1.1.1
PING 1.1.1.1 (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: seq=0 ttl=254 time=1.511 ms
64 bytes from 1.1.1.1: seq=1 ttl=254 time=1.268 ms
64 bytes from 1.1.1.1: seq=2 ttl=254 time=0.887 ms
64 bytes from 1.1.1.1: seq=3 ttl=254 time=0.787 ms
64 bytes from 1.1.1.1: seq=4 ttl=254 time=0.973 ms

--- 1.1.1.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.787/1.085/1.511 ms
cisco@pc2:~$ 


Cafe-Rtr#show ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
icmp 216.0.5.2:1024    192.168.1.50:694   1.1.1.1:694        1.1.1.1:1024
icmp 216.0.5.2:1025    192.168.1.51:707   1.1.1.1:707        1.1.1.1:1025
Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#show ip nat statistics
Total active translations: 2 (0 static, 2 dynamic; 2 extended)
Outside interfaces:
  Ethernet0/1
Inside interfaces: 
  Ethernet0/0
Hits: 58  Misses: 0
CEF Translated packets: 58, CEF Punted packets: 0
 Reserved port setting disabled provisioned no
 Dynamic overload mapping configured: 1
Expired translations: 2
Dynamic mappings:
-- Inside Source
[Id: 2] access-list 1 interface Ethernet0/1 refcount 2
nat-limit statistics:
 max entry: max allowed 0, used 0, missed 0
Cafe-Rtr#
```
