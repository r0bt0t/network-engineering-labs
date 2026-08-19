# Lab 055 - Raw CLI Output

```bash
Connecting to console for Castle-Cafe-RTR

Castle-Cafe-RTR#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/0.20         10.0.18.33      YES TFTP   up                    up      
Ethernet0/1            10.0.16.1       YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Castle-Cafe-RTR#show access-lists
Castle-Cafe-RTR#show running-config | section line vty
line vty 0 4
 password CastleRysen!
 login
 transport input telnet ssh
Castle-Cafe-RTR#show running-config | include access-class
Castle-Cafe-RTR#show ip interface Ethernet0/0.10
Ethernet0/0.10 is up, line protocol is up
  Internet address is 10.0.18.1/27
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
Castle-Cafe-RTR#show ip interface Ethernet0/0.20
Ethernet0/0.20 is up, line protocol is up
  Internet address is 10.0.18.33/27
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is not set
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
Castle-Cafe-RTR#


Castle-Cafe-RTR#show access-lists 50
Castle-Cafe-RTR#show running-config | section line vty
line vty 0 4
 password CastleRysen!
 login
 transport input telnet ssh
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#line vty 0 4
Castle-Cafe-RTR(config-line)#no access-class 50 in
 % Access-class 50 is not configured
 % Access-class 50 is not configured
 % Access-class 50 is not configured
 % Access-class 50 is not configured
 % Access-class 50 is not configured
Castle-Cafe-RTR(config-line)#exit
Castle-Cafe-RTR(config)#no access-list 50
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Aug 18 10:14:37.849: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show access-lists
Castle-Cafe-RTR#



Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)# ip access-list standard PC1-FILTER
Castle-Cafe-RTR(config-std-nacl)#$permitting the remainder of VLAN 10          
Castle-Cafe-RTR(config-std-nacl)#20 deny host 10.0.18.2
Castle-Cafe-RTR(config-std-nacl)#30 permit 10.0.18.0 0.0.0.31
Castle-Cafe-RTR(config-std-nacl)#exit
Castle-Cafe-RTR(config)#interface Ethernet0/0.10
Castle-Cafe-RTR(config-subif)#ip access-group PC1-FILTER in
Castle-Cafe-RTR(config-subif)#exit
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Aug 18 10:19:19.411: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ip interface Ethernet0/0.10
Ethernet0/0.10 is up, line protocol is up
  Internet address is 10.0.18.1/27
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is PC1-FILTER
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: Access List, MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
Castle-Cafe-RTR#show ip access-lists PC1-FILTER
Standard IP access list PC1-FILTER
    20 deny   10.0.18.2
    30 permit 10.0.18.0, wildcard bits 0.0.0.31
Castle-Cafe-RTR#


Connecting to console for Cafe-PC1

Core Linux
cafe-pc1 login: cisco
Password: 
Login incorrect
login[640]: invalid password for 'UNKNOWN' on 'ttyS0'
cafe-pc1 login: CastleRysen!
Password: 
Login incorrect
login[640]: invalid password for 'UNKNOWN' on 'ttyS0'
cafe-pc1 login: patron 
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

patron@cafe-pc1:~$ ping -c 4 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes

--- 10.0.18.1 ping statistics ---
4 packets transmitted, 0 packets received, 100% packet loss
patron@cafe-pc1:~$ 



Castle-Cafe-RTR#
Castle-Cafe-RTR#show ip access-lists PC1-FILTER
Standard IP access list PC1-FILTER
    20 deny   10.0.18.2 (8 matches)
    30 permit 10.0.18.0, wildcard bits 0.0.0.31
Castle-Cafe-RTR#


Connecting to console for Plex-SRV

Core Linux
plex-srv login: patron
Password: 
Login incorrect
login[643]: invalid password for 'UNKNOWN' on 'ttyS0'
plex-srv login: CastleRysen!
Password: 
Login incorrect
login[643]: invalid password for 'UNKNOWN' on 'ttyS0'
plex-srv login: cisco
Password: 
Login incorrect
login[643]: invalid password for 'UNKNOWN' on 'ttyS0'

Core Linux
plex-srv login: tc
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

tc@plex-srv:~$ ping -c 4 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes
64 bytes from 10.0.18.1: seq=0 ttl=255 time=1.820 ms
64 bytes from 10.0.18.1: seq=1 ttl=255 time=1.144 ms
64 bytes from 10.0.18.1: seq=2 ttl=255 time=1.138 ms
64 bytes from 10.0.18.1: seq=3 ttl=255 time=1.166 ms

--- 10.0.18.1 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 1.138/1.317/1.820 ms
tc@plex-srv:~$ 


Castle-Cafe-RTR#
Castle-Cafe-RTR#show ip access-lists PC1-FILTER
Standard IP access list PC1-FILTER
    20 deny   10.0.18.2 (8 matches)
    30 permit 10.0.18.0, wildcard bits 0.0.0.31 (8 matches)
Castle-Cafe-RTR#


Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ip access-list extended S18-L03-FILTER
Castle-Cafe-RTR(config-ext-nacl)#$atron-PC ICMP echo only to Plex-SRV        
Castle-Cafe-RTR(config-ext-nacl)#$cmp host 10.0.18.34 host 10.0.18.6 echo      
Castle-Cafe-RTR(config-ext-nacl)#30 deny icmp host 10.0.18.34 any echo
Castle-Cafe-RTR(config-ext-nacl)#40 permit ip any any
Castle-Cafe-RTR(config-ext-nacl)#exit
Castle-Cafe-RTR(config)#interface Ethernet0/0.20
Castle-Cafe-RTR(config-subif)#ip access-group S18-L03-FILTER in
Castle-Cafe-RTR(config-subif)#exit
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Aug 18 10:38:16.214: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ip interface Ethernet0/0.20
Ethernet0/0.20 is up, line protocol is up
  Internet address is 10.0.18.33/27
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is S18-L03-FILTER
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: Access List, MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
Castle-Cafe-RTR#


Connecting to console for Patron-PC

Core Linux
patron-pc login: patron 
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

patron@patron-pc:~$ ping -c 4 10.0.18.6
PING 10.0.18.6 (10.0.18.6): 56 data bytes
64 bytes from 10.0.18.6: seq=0 ttl=63 time=2.120 ms
64 bytes from 10.0.18.6: seq=1 ttl=63 time=1.453 ms
64 bytes from 10.0.18.6: seq=2 ttl=63 time=1.448 ms
64 bytes from 10.0.18.6: seq=3 ttl=63 time=1.404 ms

--- 10.0.18.6 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 1.404/1.606/2.120 ms
patron@patron-pc:~$ 


Castle-Cafe-RTR#show ip access-lists S18-L03-FILTER
Extended IP access list S18-L03-FILTER
    20 permit icmp host 10.0.18.34 host 10.0.18.6 echo (4 matches)
    30 deny icmp host 10.0.18.34 any echo
    40 permit ip any any (34 matches)
Castle-Cafe-RTR#


patron@patron-pc:~$ 
patron@patron-pc:~$ ping -c 4 10.0.18.33
PING 10.0.18.33 (10.0.18.33): 56 data bytes

--- 10.0.18.33 ping statistics ---
4 packets transmitted, 0 packets received, 100% packet loss
patron@patron-pc:~$ 



Castle-Cafe-RTR#
Castle-Cafe-RTR#show ip access-lists S18-L03-FILTER
Extended IP access list S18-L03-FILTER
    20 permit icmp host 10.0.18.34 host 10.0.18.6 echo (4 matches)
    30 deny icmp host 10.0.18.34 any echo (4 matches)
    40 permit ip any any (54 matches)
Castle-Cafe-RTR#


patron@cafe-pc1:~$ ping -c 4 10.0.18.2
PING 10.0.18.2 (10.0.18.2): 56 data bytes
64 bytes from 10.0.18.2: seq=0 ttl=64 time=0.070 ms
64 bytes from 10.0.18.2: seq=1 ttl=64 time=0.056 ms
64 bytes from 10.0.18.2: seq=2 ttl=64 time=0.072 ms
64 bytes from 10.0.18.2: seq=3 ttl=64 time=0.063 ms

--- 10.0.18.2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.056/0.065/0.072 ms
patron@cafe-pc1:~$ 



Castle-Cafe-RTR#
Castle-Cafe-RTR#show ip access-lists S18-L03-FILTER
Extended IP access list S18-L03-FILTER
    20 permit icmp host 10.0.18.34 host 10.0.18.6 echo (4 matches)
    30 deny icmp host 10.0.18.34 any echo (4 matches)
    40 permit ip any any (72 matches)
Castle-Cafe-RTR#


patron@patron-pc:~$ 
patron@patron-pc:~$ ping -c 4 10.0.18.2
PING 10.0.18.2 (10.0.18.2): 56 data bytes

--- 10.0.18.2 ping statistics ---
4 packets transmitted, 0 packets received, 100% packet loss
patron@patron-pc:~$ 


Castle-Cafe-RTR#show ip access-lists S18-L03-FILTER
Extended IP access list S18-L03-FILTER
    20 permit icmp host 10.0.18.34 host 10.0.18.6 echo (4 matches)
    30 deny icmp host 10.0.18.34 any echo (8 matches)
    40 permit ip any any (114 matches)
Castle-Cafe-RTR#


Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    
10   VLAN0010                         active    Et0/1, Et0/3
20   VLAN0020                         active    Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 


Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ip access-list extended CAFE-FILTER
Castle-Cafe-RTR(config-ext-nacl)#$llow approved Patron-to-Plex services      
Castle-Cafe-RTR(config-ext-nacl)#$.32 0.0.0.31 host 10.0.18.6 eq 443         
Castle-Cafe-RTR(config-ext-nacl)#$.32 0.0.0.31 host 10.0.18.6 eq 32400       
Castle-Cafe-RTR(config-ext-nacl)#$.32 0.0.0.31 host 10.0.18.6 eq 32469       
Castle-Cafe-RTR(config-ext-nacl)#$.32 0.0.0.31 host 10.0.18.6 eq 1900        
Castle-Cafe-RTR(config-ext-nacl)#$.32 0.0.0.31 host 10.0.18.6 eq 5353        
Castle-Cafe-RTR(config-ext-nacl)#$lock all other Patron-to-Cafe traffic      
Castle-Cafe-RTR(config-ext-nacl)#$10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31     
Castle-Cafe-RTR(config-ext-nacl)#90 permit ip any any
Castle-Cafe-RTR(config-ext-nacl)#exit
Castle-Cafe-RTR(config)#interface Ethernet0/0.20
Castle-Cafe-RTR(config-subif)#no ip access-group S18-L03-FILTER in
Castle-Cafe-RTR(config-subif)#ip access-group CAFE-FILTER in
Castle-Cafe-RTR(config-subif)#exit
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Aug 18 11:00:13.110: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ip interface Ethernet0/0.20
Ethernet0/0.20 is up, line protocol is up
  Internet address is 10.0.18.33/27
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is CAFE-FILTER
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: Access List, MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
Castle-Cafe-RTR#show ip access-lists S18-L03-FILTER
Extended IP access list S18-L03-FILTER
    20 permit icmp host 10.0.18.34 host 10.0.18.6 echo (4 matches)
    30 deny icmp host 10.0.18.34 any echo (8 matches)
    40 permit ip any any (270 matches)
Castle-Cafe-RTR#


patron@patron-pc:~$ 
patron@patron-pc:~$ nc -vz -w 2 10.0.18.6 443
10.0.18.6 (10.0.18.6:443) open
patron@patron-pc:~$ nc -vz -w 2 10.0.18.6 32400
10.0.18.6 (10.0.18.6:32400) open
patron@patron-pc:~$ nc -vz -w 2 10.0.18.6 32469
10.0.18.6 (10.0.18.6:32469) open
patron@patron-pc:~$ nc -vzu -w 2 10.0.18.6 1900
10.0.18.6 (10.0.18.6:1900) open


patron@patron-pc:~$ nc -vzu -w 2 10.0.18.6 1900
10.0.18.6 (10.0.18.6:1900) open
patron@patron-pc:~$ nc -vzu -w 2 10.0.18.6 5353
10.0.18.6 (10.0.18.6:5353) open
patron@patron-pc:~$ nc -vz -w 2 10.0.18.6 80
nc: 10.0.18.6 (10.0.18.6:80): No route to host
patron@patron-pc:~$ 


Castle-Cafe-RTR#show ip access-lists CAFE-FILTER
Extended IP access list CAFE-FILTER
    20 permit tcp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 443 (4 matches)
    30 permit tcp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 32400 (4 matches)
    40 permit tcp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 32469 (3 matches)
    50 permit udp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 1900 (2 matches)
    60 permit udp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 5353 (2 matches)
    80 deny ip 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 (1 match)
    90 permit ip any any (62 matches)
Castle-Cafe-RTR#



patron@patron-pc:~$ ping -c 4 10.0.18.6
PING 10.0.18.6 (10.0.18.6): 56 data bytes

--- 10.0.18.6 ping statistics ---
4 packets transmitted, 0 packets received, 100% packet loss
patron@patron-pc:~$ 



Castle-Cafe-RTR#
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ip access-list standard ADMIN-MGMT-ONLY
Castle-Cafe-RTR(config-std-nacl)#10 remark Permit Cafe admin subnet
Castle-Cafe-RTR(config-std-nacl)#10 permit 10.0.18.0 0.0.0.31
Castle-Cafe-RTR(config-std-nacl)#30 remark Permit Fallout management subnet
Castle-Cafe-RTR(config-std-nacl)#40 permit 10.0.16.0 0.0.0.127
Castle-Cafe-RTR(config-std-nacl)#exit
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#sh
*Aug 18 11:08:43.472: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show running-config | section line vty
line vty 0 4
 password CastleRysen!
 login
 transport input telnet ssh
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#line vty 0 4
Castle-Cafe-RTR(config-line)#access-class ADMIN-MGMT-ONLY in
Castle-Cafe-RTR(config-line)#transport input ssh telnet
Castle-Cafe-RTR(config-line)#exit
Castle-Cafe-RTR(config)#show running-config | section line vty 
                          ^
% Invalid input detected at '^' marker.

Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#conf t
*Aug 18 11:10:42.563: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show running-config | section line vty
line vty 0 4
 access-class ADMIN-MGMT-ONLY in
 password CastleRysen!
 login
 transport input telnet ssh
Castle-Cafe-RTR#show ip access-lists ADMIN-MGMT-ONLY
Standard IP access list ADMIN-MGMT-ONLY
    10 permit 10.0.18.0, wildcard bits 0.0.0.31
    40 permit 10.0.16.0, wildcard bits 0.0.0.127
Castle-Cafe-RTR#


Cafe-SW1>en
Password: 
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#ip access-list standard ADMIN-MGMT-ONLY
Cafe-SW1(config-std-nacl)#10 remark Permit Cafe admin subnet
Cafe-SW1(config-std-nacl)#20 permit 10.0.18.0 0.0.0.31
Cafe-SW1(config-std-nacl)#30 remark Permit Fallout management subnet
Cafe-SW1(config-std-nacl)#40 permit 10.0.16.0 0.0.0.127
Cafe-SW1(config-std-nacl)#exit
Cafe-SW1(config)#line vty 0 15
                             ^
% Invalid input detected at '^' marker.

Cafe-SW1(config)#line vty 0 4 
Cafe-SW1(config-line)#access-class ADIN-MGMT-ONLY in
Cafe-SW1(config-line)#transport input ssh telnet
Cafe-SW1(config-line)#exit
Cafe-SW1(config)#end
Cafe-SW1#
*Aug 18 11:14:30.871: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    
10   VLAN0010                         active    Et0/1, Et0/3
20   VLAN0020                         active    Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW1#show vlan status



patron@patron-pc:~$ 
patron@patron-pc:~$ telnet 10.0.18.33
telnet: can't connect to remote host (10.0.18.33): Connection refused
patron@patron-pc:~$ telnet <SW1-MGMT-IP>
-sh: syntax error: unexpected newline
patron@patron-pc:~$ 



patron@cafe-pc1:~$ Cafe-SW1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#interface vlan 10
Cafe-SW1(config-if)# ip address 10.0.18.3 255.255.255.224
Cafe-SW1(config-if)# no shutdown
Cafe-SW1(config-if)#exit
Cafe-SW1(config)#ip default-gateway 10.0.18.1
Cafe-SW1(config)#end
Cafe-SW1#
*Aug 18 11:22:16.925: %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan10, changed state to up
*Aug 18 11:22:17.628: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#
*Aug 18 11:22:17.928: %LINK-3-UPDOWN: Interface Vlan10, changed state to up
Cafe-SW1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Vlan10                 10.0.18.3       YES manual up                    up      
Cafe-SW1#


patron@patron-pc:~$ telnet 10.0.18.3
telnet: can't connect to remote host (10.0.18.3): No route to host
patron@patron-pc:~$ 


patron@cafe-pc1:~$ telnet 10.0.18.3
Connected to 10.0.18.3

Entering character mode
Escape character is '^]'.



User Access Verification

Password: 
Cafe-SW1>



patron@cafe-pc1:~$ telnet <SW1-MGMT-IP>
-sh: syntax error: unexpected newline
patron@cafe-pc1:~$ 



Castle-Cafe-RTR>en
Password: 
Castle-Cafe-RTR#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
Castle-Cafe-RTR#show ip access-lists PC1-FILTER
Standard IP access list PC1-FILTER
    20 deny   10.0.18.2 (8 matches)
    30 permit 10.0.18.0, wildcard bits 0.0.0.31 (21 matches)
Castle-Cafe-RTR#show ip access-lists S18-L03-FILTER
Extended IP access list S18-L03-FILTER
    20 permit icmp host 10.0.18.34 host 10.0.18.6 echo (4 matches)
    30 deny icmp host 10.0.18.34 any echo (8 matches)
    40 permit ip any any (270 matches)
Castle-Cafe-RTR#show ip access-lists CAFE-FILTER
Extended IP access list CAFE-FILTER
    20 permit tcp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 443 (4 matches)
    30 permit tcp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 32400 (4 matches)
    40 permit tcp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 32469 (3 matches)
    50 permit udp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 1900 (2 matches)
    60 permit udp 10.0.18.32 0.0.0.31 host 10.0.18.6 eq 5353 (2 matches)
    80 deny ip 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 (6 matches)
    90 permit ip any any (380 matches)
Castle-Cafe-RTR#show ip access-lists ADMIN-MGMT-ONLY
Standard IP access list ADMIN-MGMT-ONLY
    10 permit 10.0.18.0, wildcard bits 0.0.0.31
    40 permit 10.0.16.0, wildcard bits 0.0.0.127
Castle-Cafe-RTR#show running-config | section line vty
line vty 0 4
 access-class ADMIN-MGMT-ONLY in
 password CastleRysen!
 login
 transport input telnet ssh
Castle-Cafe-RTR#show ip interface Ethernet0/0.10
Ethernet0/0.10 is up, line protocol is up
  Internet address is 10.0.18.1/27
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is PC1-FILTER
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
          
Castle-Cafe-RTR#show ip interface Ethernet0/0.20
Ethernet0/0.20 is up, line protocol is up
  Internet address is 10.0.18.33/27
  Broadcast address is 255.255.255.255
  Address determined by configuration file
  MTU is 1500 bytes
  Helper address is not set
  Directed broadcast forwarding is disabled
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is CAFE-FILTER
  Proxy ARP is enabled
  Local Proxy ARP is disabled
  Security level is default
  Split horizon is enabled
  ICMP redirects are always sent
  ICMP unreachables are always sent
  ICMP mask replies are never sent
  IP fast switching is enabled
  IP Flow switching is disabled
  IP CEF switching is enabled
  IP CEF switching turbo vector
  IP Null turbo vector
  Associated unicast routing topologies:
        Topology "base", operation state is UP
  IP multicast fast switching is enabled
  IP multicast distributed fast switching is disabled
  IP route-cache flags are Fast, CEF
  Router Discovery is disabled
  IP output packet accounting is disabled
  IP access violation accounting is disabled
  TCP/IP header compression is disabled
  RTP/IP header compression is disabled
  Probe proxy name replies are disabled
  Policy routing is disabled
  Network address translation is disabled
  BGP Policy Mapping is disabled
  Input features: Access List, MCI Check
  IPv4 WCCP Redirect outbound is disabled
  IPv4 WCCP Redirect inbound is disabled
  IPv4 WCCP Redirect exclude is disabled
  IP Clear Dont Fragment is disabled
Castle-Cafe-RTR#



Cafe-SW1#
Cafe-SW1#show ip access-lists ADMIN-MGMT-ONLY
Standard IP access list ADMIN-MGMT-ONLY
    20 permit 10.0.18.0, wildcard bits 0.0.0.31
    40 permit 10.0.16.0, wildcard bits 0.0.0.127
Cafe-SW1#show running-config | section line vty
line vty 0 4
 access-class ADIN-MGMT-ONLY in
 password CastleRysen!
 login
 transport input telnet ssh
Cafe-SW1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Vlan10                 10.0.18.3       YES manual up                    up      
Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    
10   VLAN0010                         active    Et0/1, Et0/3
20   VLAN0020                         active    Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW1#
```
