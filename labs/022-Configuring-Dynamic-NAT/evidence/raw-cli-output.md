# Lab 022 - Raw CLI Output

```text
Connecting to console for Cafe-Rtr
Connected to CML terminalserver.

Cafe-Rtr>
Cafe-Rtr>show run
Cafe-Rtr>show running-config
               ^
% Invalid input detected at '^' marker.

Cafe-Rtr>en
Cafe-Rtr#show running-config
Building configuration...

Current configuration : 1090 bytes
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
 --More-- 
*Jun 13 17:09:41.380: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
 --More-- 
*Jun 13 17:09:41.482: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 13 17:09:41.482: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 13 17:09:41.587: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
 --More-- 
*Jun 13 17:09:41.687: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 13 17:09:41.687: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
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
ip nat inside source static 192.168.1.50 216.0.5.20
ip nat inside source static 192.168.1.51 216.0.5.21
ip route 0.0.0.0 0.0.0.0 216.0.5.1
ip ssh bulk-mode 131072
no logging btrace
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
Cafe-Rtr#no ip nat inside source static 192.168.1.50 216.0.5.20
            ^
% Invalid input detected at '^' marker.

Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#no ip nat inside source static 192.168.1.50 216.0.5.20
Cafe-Rtr(config)#no ip nat inside source static 192.168.1.51 216.0.5.20
%Translation not found!!!!
Cafe-Rtr(config)#no ip nat inside source static 192.168.1.51 216.0.5.21
Cafe-Rtr(config)#exit
Cafe-Rtr#
*Jun 13 17:12:16.320: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#
Cafe-Rtr#show nat ?
% Ambiguous command:  "show nat "
Cafe-Rtr#show ip nat ?
  aggregation   Aggregation
  platform      Platform entries
  portblock     TCP/UDP port blocks allocated for NAT
  statistics    Translation statistics
  translations  Translation entries

Cafe-Rtr#show ip nat translations
Cafe-Rtr#


Cafe-Rtr#
Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#access-list 1 permit 192.168.1.0 0.0.0.255
Cafe-Rtr(config)#end
Cafe-Rtr#
*Jun 13 17:15:05.047: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show ip access-lists
Standard IP access list 1
    10 permit 192.168.1.0, wildcard bits 0.0.0.255
Cafe-Rtr#


Cafe-Rtr#
Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#
Cafe-Rtr(config)#
Cafe-Rtr(config)#$ Cafe-Public 216.0.5.50 216.0.5.100 netmask 255.255.255.0    
Cafe-Rtr(config)#end
Cafe-Rtr#
*Jun 13 17:17:24.823: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show running-config | include ip nat pool
ip nat pool Cafe-Public 216.0.5.50 216.0.5.100 netmask 255.255.255.0
Cafe-Rtr#


Cafe-Rtr#
Cafe-Rtr#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Rtr(config)#ip nat inside source list 1 pool Cafe-Public
Cafe-Rtr(config)#end
Cafe-Rtr#
*Jun 13 17:19:14.735: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Rtr#show running-config interface ethernet0/0
Building configuration...

Current configuration : 104 bytes
!
interface Ethernet0/0
 description Cafe LAN
 ip address 192.168.1.1 255.255.255.0
 ip nat inside
end

Cafe-Rtr#show running-config interface ethernet0/1
Building configuration...

Current configuration : 115 bytes
!
interface Ethernet0/1
 description WAN toward ISP-Rtr
 ip address 216.0.5.2 255.255.255.252
 ip nat outside
end

Cafe-Rtr#


Connecting to console for PC1
Connected to CML terminalserver.

Core Linux
pc1 login: cisco 
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@pc1:~$ ping -c 5 1.1.1.1
PING 1.1.1.1 (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: seq=0 ttl=254 time=1.582 ms
64 bytes from 1.1.1.1: seq=1 ttl=254 time=0.849 ms
64 bytes from 1.1.1.1: seq=2 ttl=254 time=0.855 ms
64 bytes from 1.1.1.1: seq=3 ttl=254 time=0.808 ms
64 bytes from 1.1.1.1: seq=4 ttl=254 time=0.909 ms

--- 1.1.1.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.808/1.000/1.582 ms
cisco@pc1:~$ 



Connecting to console for PC2
Escape character is '^]'.

Core Linux
pc2 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@pc2:~$ oing -c 5 1.1.1.1
-sh: oing: not found
cisco@pc2:~$ ping -c 5 1.1.1.1
PING 1.1.1.1 (1.1.1.1): 56 data bytes
64 bytes from 1.1.1.1: seq=0 ttl=254 time=1.510 ms
64 bytes from 1.1.1.1: seq=1 ttl=254 time=0.828 ms
64 bytes from 1.1.1.1: seq=2 ttl=254 time=0.816 ms
64 bytes from 1.1.1.1: seq=3 ttl=254 time=0.847 ms
64 bytes from 1.1.1.1: seq=4 ttl=254 time=0.788 ms

--- 1.1.1.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.788/0.957/1.510 ms
cisco@pc2:~$ 



Cafe-Rtr#show ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
--- 216.0.5.50         192.168.1.50       ---                ---
icmp 216.0.5.51:710    192.168.1.51:710   1.1.1.1:710        1.1.1.1:710
--- 216.0.5.51         192.168.1.51       ---                ---
Cafe-Rtr#
Cafe-Rtr#
Cafe-Rtr#show ip nat statistics
Total active translations: 2 (0 static, 2 dynamic; 0 extended)
Outside interfaces:
  Ethernet0/1
Inside interfaces: 
  Ethernet0/0
Hits: 20  Misses: 0
CEF Translated packets: 20, CEF Punted packets: 0
 Reserved port setting disabled provisioned no
 Dynamic overload mapping configured: 0
Expired translations: 2
Dynamic mappings:
-- Inside Source
[Id: 1] access-list 1 pool Cafe-Public refcount 2
 pool Cafe-Public: id 1, netmask 255.255.255.0
        start 216.0.5.50 end 216.0.5.100
        type generic, total addresses 51, allocated 2 (3%), misses 0
nat-limit statistics:
 max entry: max allowed 0, used 0, missed 0
Cafe-Rtr#
```
