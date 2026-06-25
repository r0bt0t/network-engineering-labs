# Lab 027 - Raw CLI Output

```bash
Cafe-SW1>en
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#
*Jun 24 17:04:59.712: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW1(config)#
*Jun 24 17:04:59.815: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 17:04:59.815: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 17:04:59.920: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW1(config)#in
*Jun 24 17:05:00.020: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jun 24 17:05:00.020: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW1(config)#interface eth
Cafe-SW1(config)#interface ethernet0/0
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#
*Jun 24 17:05:36.145: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Cafe-SW1(config-if)#e
*Jun 24 17:05:39.145: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-SW1(config-if)#end
Cafe-SW1#show
*Jun 24 17:05:41.663: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          1-4094

Port           Vlans allowed and active in management domain
Et0/0          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          none
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#vlan 10
Cafe-SW1(config-vlan)#name ADMIN
Cafe-SW1(config-vlan)#exit
Cafe-SW1(config)#vlan 20
Cafe-SW1(config-vlan)#name PATRON
Cafe-SW1(config-vlan)#end
Cafe-SW1#
*Jun 24 17:07:41.538: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          1-4094

Port           Vlans allowed and active in management domain
Et0/0          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          1,10,20
Cafe-SW1#


Cafe-RTR1>en
Cafe-RTR1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RTR1(config)#
*Jun 24 17:08:47.754: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-RTR1(config)#
*Jun 24 17:08:47.856: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 17:08:47.857: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 17:08:47.963: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-RTR1(config)#
*Jun 24 17:08:48.063: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 24 17:08:48.063: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-RTR1(config)#interface ehernet0/0
                             ^
% Invalid input detected at '^' marker.

Cafe-RTR1(config)#no ip address
% Incomplete command.

Cafe-RTR1(config)#end
Cafe-RTR1#s
*Jun 24 17:09:30.480: %SYS-5-CONFIG_I: Configured from console by console
Cafe-RTR1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            10.0.18.1       YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RTR1#
Cafe-RTR1#
Cafe-RTR1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RTR1(config)#int
Cafe-RTR1(config)#interface ethe
Cafe-RTR1(config)#interface ethernet0/0
Cafe-RTR1(config-if)#no ip address 10.0.18.1 255.255.255.224
Invalid address
Cafe-RTR1(config-if)#no ip address 10.0.18.1 255.255.255.0  
Invalid address
Cafe-RTR1(config-if)#no ip address 10.0.18.1              
% Incomplete command.

Cafe-RTR1(config-if)#end
Cafe-RTR1#
*Jun 24 17:11:03.697: %SYS-5-CONFIG_I: Configured from console by console
Cafe-RTR1#show running-config | include ethernet0/0
Cafe-RTR1#show running-config | ethernet0/0        
                                 ^
% Invalid input detected at '^' marker.

Cafe-RTR1#show run
Building configuration...

Current configuration : 1107 bytes
!
! Last configuration change at 17:11:03 UTC Wed Jun 24 2026
!
version 17.16
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname Cafe-RTR1
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
ip dhcp excluded-address 10.0.18.1 10.0.18.10
!
ip dhcp pool Cafe-Base
 network 10.0.18.0 255.255.255.192
 default-router 10.0.18.1 
 dns-server 1.1.1.11 
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
 description Link to Cafe-SW1 Et0/0
 ip address 10.0.18.1 255.255.255.192
!
interface Ethernet0/1
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

Cafe-RTR1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RTR1(config)#int
Cafe-RTR1(config)#interface eth
Cafe-RTR1(config)#interface ethernet0/0
Cafe-RTR1(config-if)#no ip address 10.0.18.1 255.255.255.192
Cafe-RTR1(config-if)#exit
Cafe-RTR1(config)#interface eth
Cafe-RTR1(config)#interface ethernet0/0.10
Cafe-RTR1(config-subif)#switchport mode trunk
                         ^
% Invalid input detected at '^' marker.

Cafe-RTR1(config-subif)#switchport trunk encapsulation dot1q
                         ^
% Invalid input detected at '^' marker.

Cafe-RTR1(config-subif)#switchport vlan 10
                         ^
% Invalid input detected at '^' marker.

Cafe-RTR1(config-subif)#encapsulation dot1q 10
Cafe-RTR1(config-subif)#ip address 10.0.18.1 255.255.255.224
Cafe-RTR1(config-subif)#exit
Cafe-RTR1(config)#int
Cafe-RTR1(config)#interface eth
Cafe-RTR1(config)#interface ethernet0/0.20
Cafe-RTR1(config-subif)#encapsulation dot1q 20
Cafe-RTR1(config-subif)#ip address 10.0.18.33 255.255.255.224
Cafe-RTR1(config-subif)#exit
Cafe-RTR1(config)#
*Jun 24 17:18:17.024: %DHCPD-7-NAK: DHCP nak sent to client 0152.5400.e44b.fe
Cafe-RTR1(config)#interface 0/0
                            ^
% Invalid input detected at '^' marker.

Cafe-RTR1(config)#interface eth
Cafe-RTR1(config)#interface ethernet0/0
Cafe-RTR1(config-if)#no ip address 
Cafe-RTR1(config-if)#no shutdown
Cafe-RTR1(config-if)#exit
Cafe-RTR1(config)#exit
Cafe-RTR1#show ip
*Jun 24 17:19:01.079: %SYS-5-CONFIG_I: Configured from console by console
Cafe-RTR1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.0.18.1       YES manual up                    up      
Ethernet0/0.20         10.0.18.33      YES manual up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RTR1#
*Jun 24 17:19:21.304: %DHCPD-7-NAK: DHCP nak sent to client 0152.5400.e44b.fe
Cafe-RTR1#show run | section interface Ethernet0/0
interface Ethernet0/0
 description Link to Cafe-SW1 Et0/0
 no ip address
interface Ethernet0/0.10
 encapsulation dot1Q 10
 ip address 10.0.18.1 255.255.255.224
interface Ethernet0/0.20
 encapsulation dot1Q 20
 ip address 10.0.18.33 255.255.255.224
Cafe-RTR1#
*Jun 24 17:20:25.584: %DHCPD-7-NAK: DHCP nak sent to client 0152.5400.e44b.fe
Cafe-RTR1#
Cafe-RTR1#
Cafe-RTR1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RTR1(config)#no ip dhcp pool Cafe-Base
Cafe-RTR1(config)#no ip dhcp excluded-address 10.0.18.1 10.0.18.10
Cafe-RTR1(config)#ip dhcp excluded-address 10.0.18.1 10.0.18.1
Cafe-RTR1(config)#ip dhcp excluded-address 10.0.18.33 10.0.18.33
Cafe-RTR1(config)#ip dhcp pool PATRON-20
Cafe-RTR1(dhcp-config)#
*Jun 24 17:22:25.004: %DHCPD-7-NO_LEASE: DHCP lease assignment failure, client 5254.00e4.4bfe reason NO POOL
Cafe-RTR1(dhcp-config)#network 10.0.18.32 255.255.255.224
Cafe-RTR1(dhcp-config)#default-router 10.0.18.33
Cafe-RTR1(dhcp-config)#dns-server 1.1.1.1
Cafe-RTR1(dhcp-config)#exit
Cafe-RTR1(config)#ip dhcp pool ADMIN-10
Cafe-RTR1(dhcp-config)#network 10.0.18.0 255.255.255.224
Cafe-RTR1(dhcp-config)#default-router 10.0.18.1
Cafe-RTR1(dhcp-config)#dns-server 1.1.1.1
Cafe-RTR1(dhcp-config)#exit
Cafe-RTR1(config)#end
Cafe-RTR1#show 
*Jun 24 17:24:09.391: %SYS-5-CONFIG_I: Configured from console by console
Cafe-RTR1#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address      Client-ID/              Lease expiration        Type       State      Interface
                Hardware address/
                User name
10.0.18.34      0152.5400.e44b.fe       Jun 25 2026 05:22 PM    Automatic  Active     Ethernet0/0.20
Cafe-RTR1#


Connecting to console for Cafe-Admin1

Core Linux
cafe-admin1 login: cisco
Password: 

ciscLogin incorrect
login[654]: invalid password for 'cisco' on 'ttyS0'
cafe-admin1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-admin1:~$ sudo ifconfig eth0 0.0.0.0 up
cisco@cafe-admin1:~$ sudo route del default 2>/dev/null
cisco@cafe-admin1:~$ sudo udhcpc -i eth0 -n -q
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.0.18.2, server 10.0.18.1
udhcpc: lease of 10.0.18.2 obtained from 10.0.18.1, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 1.1.1.1
cisco@cafe-admin1:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:F0:D2:46  
          inet addr:10.0.18.2  Bcast:10.0.18.31  Mask:255.255.255.224
          inet6 addr: fe80::5054:ff:fef0:d246/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:20 errors:0 dropped:1 overruns:0 frame:0
          TX packets:24 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:2328 (2.2 KiB)  TX bytes:3740 (3.6 KiB)

cisco@cafe-admin1:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.18.1       0.0.0.0         UG    0      0        0 eth0
10.0.18.0       0.0.0.0         255.255.255.224 U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@cafe-admin1:~$ 


Connecting to console for Cafe-Client1

Core Linux
cafe-client1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-client1:~$ sudo ifconfig eth0 0.0.0.0 up
cisco@cafe-client1:~$ sudo route del default 2>/dev/null
cisco@cafe-client1:~$ sudo udhcpc -i eth0 -n -q
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.0.18.34, server 10.0.18.33
udhcpc: lease of 10.0.18.34 obtained from 10.0.18.33, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 1.1.1.1
cisco@cafe-client1:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:E4:4B:FE  
          inet addr:10.0.18.34  Bcast:10.0.18.63  Mask:255.255.255.224
          inet6 addr: fe80::5054:ff:fee4:4bfe/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:18 errors:0 dropped:1 overruns:0 frame:0
          TX packets:144 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:5028 (4.9 KiB)  TX bytes:45032 (43.9 KiB)

cisco@cafe-client1:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.18.33      0.0.0.0         UG    0      0        0 eth0
10.0.18.32      0.0.0.0         255.255.255.224 U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@cafe-client1:~$
```
