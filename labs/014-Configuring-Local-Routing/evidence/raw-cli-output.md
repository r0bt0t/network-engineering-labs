# Raw CLI Output - Lab 011 Configuring Local Routing

```bash
Connecting to console for Cafe-RT1


User Access Verification

Username: 
Username: cisco
Password: 
Cafe-RT1#en
Cafe-RT1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   administratively down down    
Ethernet0/1            unassigned      YES TFTP   administratively down down    
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down    
Cafe-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RT1(config)#int et0/0
Cafe-RT1(config-if)#description ## Coffee House LAN
Cafe-RT1(config-if)#ip address 192.168.1.1 255.255.255.0
Cafe-RT1(config-if)#no shut
Cafe-RT1(config-if)#no shutdown 
Cafe-RT1(config-if)#INT 0/1                
Cafe-RT1(config-if)#description ## P2P Link to Fallout-RT1
Cafe-RT1(config-if)#ip address 192.168.2.1 255.255.255.252
Cafe-RT1(config-if)#no shutdown
Cafe-RT1(config-if)#^Z
Cafe-RT1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            192.168.1.1     YES manual up                    up      
Ethernet0/1            192.168.2.1     YES manual up                    up      
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down   
Cafe-RT1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       ## Coffee House LAN
Et0/1                          up             up       ## P2P Link to Fallout-RT1
Et0/2                          admin down     down     
Et0/3                          admin down     down     
Cafe-RT1#
Cafe-RT1#wr
Building configuration...
[OK]
Cafe-RT1#


User Access Verification

Username: 
% Username:  timeout expired!
Username: cisco
Password: 
Fallout-RT1#en
Fallout-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   administratively down down    
Ethernet0/1            unassigned      YES TFTP   administratively down down    
Ethernet0/2            unassigned      YES TFTP   administratively down down    
Ethernet0/3            unassigned      YES TFTP   administratively down down    
Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#int et0/1
Fallout-RT1(config-if)#description ## P2P Link to Cafe-RT1
Fallout-RT1(config-if)#ip address 192.168.2.2 255.255.255.252
Fallout-RT1(config-if)#no shutdown
Fallout-RT1(config-if)#int et0/0
Fallout-RT1(config-if)#description ## Shelter LAN
Fallout-RT1(config-if)#ip address 192.168.3.1 255.255.255.0
Fallout-RT1(config-if)#no shutdown
Fallout-RT1(config-if)#^Z
Fallout-RT1#wr
Building configuration...
[OK]
Fallout-RT1#


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


Cafe-RT1#
Cafe-RT1#ping 192.168.2.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.2.2, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
Cafe-RT1#ping 192.168.2.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.2.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-RT1#^Z
Cafe-RT1#wr
Building configuration...
[OK]
Cafe-RT1#


Fallout-RT1#
Fallout-RT1#ping 192.168.2.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.2.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Fallout-RT1#
Fallout-RT1#
Fallout-RT1#wr
Building configuration...
[OK]
Fallout-RT1#
```
