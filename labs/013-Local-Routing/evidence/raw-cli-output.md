# Raw CLI Output - Lab 013 Coffee House to Fallout Local Routing

```bash
Cafe-RT1#show running-config                                
Building configuration...

Current configuration : 3440 bytes
!
version 17.16
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname Cafe-RT1
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
spanning-tree mode rapid-pvst
!
enable secret 9 $9$Q8SsPerxDkbg9U$vtC/eA/ikZUzWToIqGCYz2VQl3DUVogDJVteNnO316o
!
username cisco privilege 15 secret 9 $9$TMKqbQtukkRr9E$rZ.5aNGGtoSZutLxQCbCwKj/BwoFXcNZPcv32PbNYOU
!
!
!
!
!
interface Ethernet0/0
 description ## Coffee House LAN - configure during lab
 no ip address
 shutdown
!
interface Ethernet0/1
 description ## P2P-to-Fallout - configure during lab
 no ip address
 shutdown
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
 exec-timeout 0 0
 logging synchronous
 login local
line aux 0
 exec-timeout 0 0
 login local
line vty 0 4
 exec-timeout 0 0
 login local
 transport input telnet ssh
!
!
!
!
end

Username: cisco
Password: 
Fallout-RT1#show running-config
Building configuration...

Current configuration : 3495 bytes
!
version 17.16
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname Fallout-RT1
!
boot-start-marker
boot-end-marker
!
!
no logging console
no aaa new-model
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
spanning-tree mode rapid-pvst
!
enable secret 9 $9$VuJ37J2nbpHigE$zWKd7UBSZ7naYejnRuQsjwgBIvfJyYRvIvOYTojYyGI
!
username cisco privilege 15 secret 9 $9$XVfk1Lm7LBj.zU$u0.W4s6yc3XkttmCszzY2rkLIjEoAz8RunoRhfyX8xM
!
!
!
!
!
interface Ethernet0/0
 description ## Fallout Shelter LAN - configure during lab
 no ip address
 shutdown
!
interface Ethernet0/1
 description ## P2P-to-CoffeeHouse - configure during lab
 no ip address
 shutdown
!
interface Ethernet0/2
 description ## Spare module - keep shutdown
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
 exec-timeout 0 0
 logging synchronous
 login local
line aux 0
 exec-timeout 0 0
 login local
line vty 0 4
 exec-timeout 0 0
 login local
 transport input telnet ssh
!
!
!
!
end

Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#interface ethernet0/0
Cafe-RT1(config-if)#ip address 192.168.42.1 255.255.255.0
Cafe-RT1(config-if)#no shutdown
Cafe-RT1(config-if)#exit
Cafe-RT1(config)#exit
Cafe-RT1#show ip interface brief 
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.42.1    YES manual up                    up      
Ethernet0/1            unassigned      YES TFTP   administratively down down    
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down    
Cafe-RT1#
Cafe-RT1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       ## Coffee House LAN - configure during lab
Et0/1                          admin down     down     ## P2P-to-Fallout - configure during lab
Et0/2                          admin down     down     
Et0/3                          admin down     down     
Cafe-RT1#

Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#interface ethernet0/0
Fallout-RT1(config-if)#ip address 192.168.84.1 255.255.255.0
Fallout-RT1(config-if)#no shutdown
Fallout-RT1(config-if)#end
Fallout-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.84.1    YES manual up                    up      
Ethernet0/1            unassigned      YES TFTP   administratively down down    
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down    
Fallout-RT1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       ## Fallout Shelter LAN - configure during lab
Et0/1                          admin down     down     ## P2P-to-CoffeeHouse - configure during lab
Et0/2                          admin down     down     ## Spare module - keep shutdown
Et0/3                          admin down     down     
Fallout-RT1#

Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#interface ethernet0/1
Cafe-RT1(config-if)#ip address 10.8.0.1 255.255.255.252
Cafe-RT1(config-if)#no shutdown
Cafe-RT1(config-if)#end
Cafe-RT1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       ## Coffee House LAN - configure during lab
Et0/1                          up             up       ## P2P-to-Fallout - configure during lab
Et0/2                          admin down     down     
Et0/3                          admin down     down     
Cafe-RT1#
Cafe-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.42.1    YES manual up                    up      
Ethernet0/1            10.8.0.1        YES manual up                    up      
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down    
Cafe-RT1#
Cafe-RT1#
Cafe-RT1#show interfaces ethernet0/1 | include line protocol
Ethernet0/1 is up, line protocol is up 
Cafe-RT1#

Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#interface ethernet0/1
Fallout-RT1(config-if)#ip address 10.8.0.2 255.255.255.252
Fallout-RT1(config-if)#no shutdown
Fallout-RT1(config-if)#end
Fallout-RT1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       ## Fallout Shelter LAN - configure during lab
Et0/1                          up             up       ## P2P-to-CoffeeHouse - configure during lab
Et0/2                          admin down     down     ## Spare module - keep shutdown
Et0/3                          admin down     down     
Fallout-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.84.1    YES manual up                    up      
Ethernet0/1            10.8.0.2        YES manual up                    up      
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down    
Fallout-RT1#
Fallout-RT1#show interfaces ethernet0/1 | include line protocol
Ethernet0/1 is up, line protocol is up 
Fallout-RT1#

Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#ip route 192.168.84.0 255.255.255.0 10.8.0.2
Cafe-RT1(config)#end
Cafe-RT1#ping 192.168.84.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.84.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
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

      10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        10.8.0.0/30 is directly connected, Ethernet0/1
L        10.8.0.1/32 is directly connected, Ethernet0/1
      192.168.42.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.42.0/24 is directly connected, Ethernet0/0
L        192.168.42.1/32 is directly connected, Ethernet0/0
S     192.168.84.0/24 [1/0] via 10.8.0.2

Fallout-RT1#ping 192.168.42.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Fallout-RT1#
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

      10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        10.8.0.0/30 is directly connected, Ethernet0/1
L        10.8.0.2/32 is directly connected, Ethernet0/1
S     192.168.42.0/24 [1/0] via 10.8.0.1
      192.168.84.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.84.0/24 is directly connected, Ethernet0/0
L        192.168.84.1/32 is directly connected, Ethernet0/0
Fallout-RT1#


Cafe-RT1#
Cafe-RT1#
Cafe-RT1#show interfaces ethernet0/0
Ethernet0/0 is up, line protocol is up 
  Hardware is AmdP2, address is aabb.cc00.0100 (bia aabb.cc00.0100)
  Description: ## Coffee House LAN - configure during lab
  Internet address is 192.168.42.1/24
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:04, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     347 packets output, 42137 bytes, 0 underruns
     Output 64 broadcasts (0 IP multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Cafe-RT1#show interfaces ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Hardware is AmdP2, address is aabb.cc00.0110 (bia aabb.cc00.0110)
  Description: ## P2P-to-Fallout - configure during lab
  Internet address is 10.8.0.1/30
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:43, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     55 packets input, 18436 bytes, 0 no buffer
     Received 44 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     256 packets output, 31432 bytes, 0 underruns
     Output 48 broadcasts (0 IP multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Cafe-RT1#

Fallout-RT1#
Fallout-RT1#show interfaces ethernet0/0
Ethernet0/0 is up, line protocol is up 
  Hardware is AmdP2, address is aabb.cc00.0200 (bia aabb.cc00.0200)
  Description: ## Fallout Shelter LAN - configure during lab
  Internet address is 192.168.84.1/24
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:07, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     260 packets output, 32544 bytes, 0 underruns
     Output 51 broadcasts (0 IP multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Fallout-RT1#show interfaces ethernet0/1
Ethernet0/1 is up, line protocol is up 
  Hardware is AmdP2, address is aabb.cc00.0210 (bia aabb.cc00.0210)
  Description: ## P2P-to-CoffeeHouse - configure during lab
  Internet address is 10.8.0.2/30
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     42 packets input, 14003 bytes, 0 no buffer
     Received 32 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     222 packets output, 28100 bytes, 0 underruns
     Output 43 broadcasts (0 IP multicasts)
     0 output errors, 0 collisions, 2 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Fallout-RT1#

Cafe-RT1#
Cafe-RT1#show cdp neighbors detail
-------------------------
Device ID: Fallout-RT1
Entry address(es): 
  IP address: 10.8.0.2
Platform: Linux Unix,  Capabilities: Router 
Interface: Ethernet0/1,  Port ID (outgoing port): Ethernet0/1
Holdtime : 160 sec

Version :
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.16.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 19-Dec-24 17:54 by mcpre

advertisement version: 2
Peer Source MAC: aabb.cc00.0210
Duplex: full
Management address(es): 
  IP address: 10.8.0.2


Total cdp entries displayed : 1
Cafe-RT1#
Cafe-RT1#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Cafe-RT1#

Fallout-RT1#
Fallout-RT1#show cdp neighbors detail
-------------------------
Device ID: Cafe-RT1
Entry address(es): 
  IP address: 10.8.0.1
Platform: Linux Unix,  Capabilities: Router 
Interface: Ethernet0/1,  Port ID (outgoing port): Ethernet0/1
Holdtime : 133 sec

Version :
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.16.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 19-Dec-24 17:54 by mcpre

advertisement version: 2
Peer Source MAC: aabb.cc00.0110
Duplex: full
Management address(es): 
  IP address: 10.8.0.1


Total cdp entries displayed : 1
Fallout-RT1#
Fallout-RT1#
Fallout-RT1#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Fallout-RT1#
```
