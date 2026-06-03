# Raw CLI Output - Lab 011 Configuring Router Interfaces

```bash
Connecting to console for Cafe-RT1

Cafe-RT1>enable
Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#hostname Cafe-RT1
Cafe-RT1(config)#username cisco secret cisco
Cafe-RT1(config)#line con 0
Cafe-RT1(config-line)#login local
Cafe-RT1(config-line)#logging synchronous
Cafe-RT1(config-line)#exit
Cafe-RT1(config)#line vty 0 4
Cafe-RT1(config-line)#login local
Cafe-RT1(config-line)#transport input ssh telnet
Cafe-RT1(config-line)#exit
Cafe-RT1(config)#enable secret CrC0ffee!
Cafe-RT1(config)#end
Cafe-RT1#write memory
Building configuration...
[OK]
Cafe-RT1#

Cafe-RT1#
Cafe-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   administratively down down    
Ethernet0/1            unassigned      YES TFTP   administratively down down    
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down    
Ethernet1/0            unassigned      YES TFTP   administratively down down    
Ethernet1/1            unassigned      YES TFTP   administratively down down    
Ethernet1/2            unassigned      YES TFTP   administratively down down    
Ethernet1/3            unassigned      YES TFTP   administratively down down    
Cafe-RT1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          admin down     down     
Et0/1                          admin down     down     
Et0/2                          admin down     down     
Et0/3                          admin down     down     
Et1/0                          admin down     down     
Et1/1                          admin down     down     
Et1/2                          admin down     down     
Et1/3                          admin down     down     
Cafe-RT1#

Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#interface ethernet0/0
Cafe-RT1(config-if)#description ## CoffeeHouse-LAN  
Cafe-RT1(config-if)#ip address 192.168.42.1 255.255.255.0
Cafe-RT1(config-if)#no shutdown
Cafe-RT1(config-if)#exit
Cafe-RT1(config)#interface ethernet 0/1
Cafe-RT1(config-if)#description ## WAN-Pending
Cafe-RT1(config-if)#shutdown
Cafe-RT1(config-if)#exit
Cafe-RT1(config)#end
Cafe-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.42.1    YES manual up                    up      
Ethernet0/1            unassigned      YES TFTP   administratively down down    
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down    
Ethernet1/0            unassigned      YES TFTP   administratively down down    
Ethernet1/1            unassigned      YES TFTP   administratively down down    
Ethernet1/2            unassigned      YES TFTP   administratively down down    
Ethernet1/3            unassigned      YES TFTP   administratively down down    
Cafe-RT1#

Cafe-RT1#show cdp neighbors detail
-------------------------
Device ID: Cafe-SW1
Entry address(es): 
  IP address: 192.168.42.2
Platform: Linux Unix,  Capabilities: Router Switch IGMP 
Interface: Ethernet0/0,  Port ID (outgoing port): Ethernet0/0
Holdtime : 150 sec

Version :
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX_L2-ADVENTERPRISEK9-M), Version 17.16.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 19-Dec-24 17:53 by mcpre

advertisement version: 2
Peer Source MAC: aabb.cc00.0400
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 192.168.42.2

          
Cafe-RT1#ping 192.168.42.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.2, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
Cafe-RT1#write memory
Building configuration...
[OK]
Cafe-RT1#
```
