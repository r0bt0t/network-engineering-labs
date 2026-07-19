# Lab 048 - Raw CLI Output

```bash
FS-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R1(config)#interface ethernet0/0
FS-R1(config-if)#no shutdown
FS-R1(config-if)#
*Jul 19 16:32:41.017: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
FS-R1(config-if)#
*Jul 19 16:32:42.017: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
FS-R1(config-if)#interface ethernet0/0.10
FS-R1(config-subif)#no ip address
FS-R1(config-subif)#ip address 10.0.16.2 255.255.255.224
FS-R1(config-subif)#interface ethernet0/0.20            
FS-R1(config-subif)#no ip address                       
FS-R1(config-subif)#ip address 10.0.16.130 255.255.255.224
FS-R1(config-subif)#interface ethernet0/0.30              
FS-R1(config-subif)#no ip address                         
FS-R1(config-subif)#ip address 10.0.17.2 255.255.255.224  
FS-R1(config-subif)#interface ethernet0/0.40            
FS-R1(config-subif)#no ip address                       
FS-R1(config-subif)#ip address 10.0.17.130 255.255.255.224
FS-R1(config-subif)#end
FS-R1#
*Jul 19 16:35:44.024: %SYS-5-CONFIG_I: Configured from console by console
FS-R1#show ip interface brief | include Ethernet0/0
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.0.16.2       YES manual up                    up      
Ethernet0/0.20         10.0.16.130     YES manual up                    up      
Ethernet0/0.30         10.0.17.2       YES manual up                    up      
Ethernet0/0.40         10.0.17.130     YES manual up                    up      
FS-R1#


FS-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R1(config)#interface ethernet0/0.10
FS-R1(config-subif)#standby version 2
FS-R1(config-subif)#standby 10 ip 10.0.16.1
FS-R1(config-subif)#standby 10 priority 105
FS-R1(config-subif)#standby 10 pree
*Jul 19 16:38:21.407: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Standby -> Active
FS-R1(config-subif)#standby 10 preempt
FS-R1(config-subif)#interface ethernet0/0.20
FS-R1(config-subif)#standby version 2       
FS-R1(config-subif)#standby 20 ip 10.0.16.129
FS-R1(config-subif)#standby 20 priority 105  
FS-R1(config-subif)#standby 20 preempt       
FS-R1(config-subif)#interface ethernet0/0.30 
FS-R1(config-subif)#standby version 2        
*Jul 19 16:39:13.406: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Standby -> Active
FS-R1(config-subif)#standby version 2
FS-R1(config-subif)#standby 20 ip 10.0.17.1  
FS-R1(config-subif)#standby 20 ip 10.0.17.1  
*Jul 19 16:39:46.987: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 20 state Standby -> Active
FS-R1(config-subif)#no standby 20 ip 10.0.17.1
FS-R1(config-subif)#
*Jul 19 16:39:52.690: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 20 state Active -> Disabled
FS-R1(config-subif)#standby 30 ip 10.0.17.1   
FS-R1(config-subif)#standby 30 priority 105   
FS-R1(config-subif)#standby 30 preempt        
*Jul 19 16:40:39.801: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Standby -> Active
FS-R1(config-subif)#standby 30 preempt
FS-R1(config-subif)#interface ethernet0/0.40  
FS-R1(config-subif)#standby version 2         
FS-R1(config-subif)#standby 40 ip 10.0.17.129
FS-R1(config-subif)#standby 40 priority 105  
FS-R1(config-subif)#standby 40 preempt       
FS-R1(config-subif)#
*Jul 19 16:42:06.699: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Standby -> Active
FS-R1(config-subif)#end
FS-R1#show s
*Jul 19 16:42:18.162: %SYS-5-CONFIG_I: Configured from console by console
FS-R1#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   105 P Active  local           unknown         10.0.16.1
Et0/0.20    20   105 P Active  local           unknown         10.0.16.129
Et0/0.30    30   105 P Active  local           unknown         10.0.17.1
Et0/0.40    40   105 P Active  local           unknown         10.0.17.129
FS-R1#


FS-R2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R2(config)#int
FS-R2(config)#interface ethe
FS-R2(config)#interface ethernet0/0
FS-R2(config-if)#no shutdown
FS-R2(config-if)#int
FS-R2(config-if)#int
*Jul 19 16:43:57.705: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
FS-R2(config-if)#int et
*Jul 19 16:43:58.705: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
FS-R2(config-if)#int eth
FS-R2(config-if)#interface ethernet0/0.10
FS-R2(config-subif)#ip address 10.0.16.3 255.255.255.224
FS-R2(config-subif)#standby version 2
FS-R2(config-subif)#standby 10 ip 10.0.16.1
FS-R2(config-subif)#standby 10 preempt
FS-R2(config-subif)#interface ethernet0/0.20            
FS-R2(config-subif)#ip address 10.0.16.3 255.255.255.224
*Jul 19 16:45:51.162: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Speak -> Standby
FS-R2(config-subif)#ip address 10.0.16.131 255.255.255.224
FS-R2(config-subif)#standby version 2                     
FS-R2(config-subif)#standby 20 ip 10.0.16.129             
FS-R2(config-subif)#standby 20 preempt                    
FS-R2(config-subif)#interface ethernet0/0.30              
FS-R2(config-subif)#ip address 10.0.1 255.255.255.224     
*Jul 19 16:46:55.615: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Standby -> Active
FS-R2(config-subif)#ip address 10.0.17.3 255.255.255.224
FS-R2(config-subif)#standby version 2                   
FS-R2(config-subif)#standby 30 ip 10.0.17.1               
FS-R2(config-subif)#standby 30 preempt                  
FS-R2(config-subif)#interface ethernet0/0.40            
FS-R2(config-subif)#ip address 10.0.17.3 255.255.255.224
*Jul 19 16:47:46.985: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Standby -> Active
FS-R2(config-subif)#ip address 10.0.17.131 255.255.255.224
FS-R2(config-subif)#standby version 2                     
FS-R2(config-subif)#standby 40 ip 10.0.17.129             
FS-R2(config-subif)#standby 40 preempt                    
FS-R2(config-subif)#end                                   
FS-R2#
*Jul 19 16:48:27.382: %SYS-5-CONFIG_I: Configured from console by console
FS-R2#
*Jul 19 16:48:32.210: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Standby -> Active
FS-R2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   100 P Standby 10.0.16.2       local           10.0.16.1
Et0/0.20    20   100 P Active  local           unknown         10.0.16.129
Et0/0.30    30   100 P Active  local           unknown         10.0.17.1
Et0/0.40    40   100 P Active  local           unknown         10.0.17.129
FS-R2#show interface trunk
                      ^
% Invalid input detected at '^' marker.

FS-R2#show interface trunks
                      ^
% Invalid input detected at '^' marker.

FS-R2#
*Jul 19 16:59:54.692: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Active -> Speak
*Jul 19 16:59:55.023: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Active -> Speak
*Jul 19 16:59:55.199: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Active -> Speak
FS-R2#
*Jul 19 17:00:04.769: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Speak -> Standby
*Jul 19 17:00:05.651: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Speak -> Standby
FS-R2#
*Jul 19 17:00:06.086: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Speak -> Standby
FS-R2#show standby brief 
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   100 P Standby 10.0.16.2       local           10.0.16.1
Et0/0.20    20   100 P Standby 10.0.16.130     local           10.0.16.129
Et0/0.30    30   100 P Standby 10.0.17.2       local           10.0.17.1
Et0/0.40    40   100 P Standby 10.0.17.130     local           10.0.17.129
FS-R2#


Connecting to console for Shelter-SW


User Access Verification

Password: 
Shelter-SW>
Shelter-SW>en
Password: 
*Jul 19 16:30:26.551: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Password: 
*Jul 19 16:30:26.653: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 16:30:26.653: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 16:30:26.759: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 16:30:26.859: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 19 16:30:26.859: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Password: 
Shelter-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20,30,40
Et0/1          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/0          10
Et0/1          10

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10
Et0/1          10
Shelter-SW#

































Shelter-SW con0 is now available





Press RETURN to get started.














*Jul 19 16:40:44.778: %SYS-6-TTY_EXPIRE_TIMER: (exec timer expired, tty 0 (0.0.0.0)), user 

User Access Verification

Password: 
Password: 
Shelter-SW>en
Password: 
Shelter-SW#enable
Shelter-SW#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW(config)#
Shelter-SW(config)#interface ethernet0/0
Shelter-SW(config-if)# switchport trunk allowed vlan add 20,30,40
Shelter-SW(config-if)# exit
Shelter-SW(config)#
Shelter-SW(config)#interface ethernet0/1
Shelter-SW(config-if)# switchport trunk allowed vlan add 20,30,40
Shelter-SW(config-if)# exit
Shelter-SW(config)#
Shelter-SW(config)#end
Shelter-SW#
*Jul 19 16:58:24.877: %SYS-5-CONFIG_I: Configured from console by console
Shelter-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20,30,40
Et0/1          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/0          10
Et0/1          10

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10
Et0/1          10
Shelter-SW#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW(config)#
Shelter-SW(config)#vlan 20
Shelter-SW(config-vlan)# name VLAN20
Shelter-SW(config-vlan)#
Shelter-SW(config-vlan)#vlan 30
Shelter-SW(config-vlan)# name VLAN30
Shelter-SW(config-vlan)#
Shelter-SW(config-vlan)#vlan 40
Shelter-SW(config-vlan)# name VLAN40
Shelter-SW(config-vlan)#
Shelter-SW(config-vlan)#end
Shelter-SW#
*Jul 19 16:59:54.437: %SYS-5-CONFIG_I: Configured from console by console
Shelter-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20,30,40
Et0/1          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/0          10,20,30,40
Et0/1          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20,30,40
Et0/1          10,20,30,40
Shelter-SW#


Connecting to console for FS-Client10

Core Linux
fs-client10 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@fs-client10:~$ ip addr
-sh: ip: not found
cisco@fs-client10:~$ ip route
-sh: ip: not found
cisco@fs-client10:~$ ifconfig
eth0      Link encap:Ethernet  HWaddr 52:54:00:01:69:E8  
          inet addr:10.0.16.50  Bcast:10.0.16.63  Mask:255.255.255.224
          inet6 addr: fe80::5054:ff:fe01:69e8/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:19 errors:0 dropped:1 overruns:0 frame:0
          TX packets:240 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:1140 (1.1 KiB)  TX bytes:77592 (75.7 KiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

cisco@fs-client10:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
10.0.16.32      0.0.0.0         255.255.255.224 U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@fs-client10:~$ sudo ifconfig eth0 10.0.16.10 netmask 255.255.255.224 broad
cast 10.0.16.31 up
cisco@fs-client10:~$ sudo route add default gw 10.0.16.1 eth0
cisco@fs-client10:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:01:69:E8  
          inet addr:10.0.16.10  Bcast:10.0.16.31  Mask:255.255.255.224
          inet6 addr: fe80::5054:ff:fe01:69e8/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:19 errors:0 dropped:1 overruns:0 frame:0
          TX packets:257 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:1140 (1.1 KiB)  TX bytes:83406 (81.4 KiB)

cisco@fs-client10:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.16.1       0.0.0.0         UG    0      0        0 eth0
10.0.16.0       0.0.0.0         255.255.255.224 U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@fs-client10:~$ ping -c 5 10.0.16.1
PING 10.0.16.1 (10.0.16.1): 56 data bytes
64 bytes from 10.0.16.1: seq=0 ttl=255 time=2.069 ms
64 bytes from 10.0.16.1: seq=1 ttl=255 time=1.216 ms
64 bytes from 10.0.16.1: seq=2 ttl=255 time=1.100 ms
64 bytes from 10.0.16.1: seq=3 ttl=255 time=1.254 ms
64 bytes from 10.0.16.1: seq=4 ttl=255 time=0.915 ms

--- 10.0.16.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.915/1.310/2.069 ms
cisco@fs-client10:~$ ping -c 5 10.0.16.2
PING 10.0.16.2 (10.0.16.2): 56 data bytes
64 bytes from 10.0.16.2: seq=0 ttl=255 time=1.267 ms
64 bytes from 10.0.16.2: seq=1 ttl=255 time=1.008 ms
64 bytes from 10.0.16.2: seq=2 ttl=255 time=0.830 ms
64 bytes from 10.0.16.2: seq=3 ttl=255 time=0.942 ms
64 bytes from 10.0.16.2: seq=4 ttl=255 time=0.924 ms

--- 10.0.16.2 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.830/0.994/1.267 ms
cisco@fs-client10:~$ ping -c 5 10.0.16.3
PING 10.0.16.3 (10.0.16.3): 56 data bytes
64 bytes from 10.0.16.3: seq=0 ttl=255 time=1.754 ms
64 bytes from 10.0.16.3: seq=1 ttl=255 time=0.960 ms
64 bytes from 10.0.16.3: seq=2 ttl=255 time=0.872 ms
64 bytes from 10.0.16.3: seq=3 ttl=255 time=0.911 ms
64 bytes from 10.0.16.3: seq=4 ttl=255 time=0.809 ms

--- 10.0.16.3 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.809/1.061/1.754 ms
cisco@fs-client10:~$ ping 10.0.16.1
PING 10.0.16.1 (10.0.16.1): 56 data bytes
64 bytes from 10.0.16.1: seq=0 ttl=255 time=1.036 ms
64 bytes from 10.0.16.1: seq=1 ttl=255 time=1.006 ms
64 bytes from 10.0.16.1: seq=2 ttl=255 time=0.994 ms
64 bytes from 10.0.16.1: seq=3 ttl=255 time=1.467 ms
64 bytes from 10.0.16.1: seq=4 ttl=255 time=0.977 ms
64 bytes from 10.0.16.1: seq=5 ttl=255 time=0.933 ms
64 bytes from 10.0.16.1: seq=6 ttl=255 time=0.878 ms
64 bytes from 10.0.16.1: seq=7 ttl=255 time=0.876 ms
64 bytes from 10.0.16.1: seq=8 ttl=255 time=0.944 ms
64 bytes from 10.0.16.1: seq=9 ttl=255 time=0.879 ms
64 bytes from 10.0.16.1: seq=10 ttl=255 time=1.103 ms
64 bytes from 10.0.16.1: seq=11 ttl=255 time=0.824 ms
64 bytes from 10.0.16.1: seq=12 ttl=255 time=0.922 ms
64 bytes from 10.0.16.1: seq=13 ttl=255 time=0.854 ms
64 bytes from 10.0.16.1: seq=14 ttl=255 time=0.906 ms
64 bytes from 10.0.16.1: seq=15 ttl=255 time=0.848 ms
64 bytes from 10.0.16.1: seq=16 ttl=255 time=1.125 ms
64 bytes from 10.0.16.1: seq=17 ttl=255 time=0.827 ms
64 bytes from 10.0.16.1: seq=18 ttl=255 time=0.875 ms
64 bytes from 10.0.16.1: seq=19 ttl=255 time=1.103 ms
64 bytes from 10.0.16.1: seq=20 ttl=255 time=1.055 ms
64 bytes from 10.0.16.1: seq=21 ttl=255 time=0.812 ms
64 bytes from 10.0.16.1: seq=22 ttl=255 time=0.720 ms
64 bytes from 10.0.16.1: seq=23 ttl=255 time=1.094 ms
64 bytes from 10.0.16.1: seq=24 ttl=255 time=0.987 ms
64 bytes from 10.0.16.1: seq=25 ttl=255 time=0.901 ms
64 bytes from 10.0.16.1: seq=26 ttl=255 time=0.764 ms
64 bytes from 10.0.16.1: seq=27 ttl=255 time=0.924 ms
64 bytes from 10.0.16.1: seq=28 ttl=255 time=1.007 ms
64 bytes from 10.0.16.1: seq=29 ttl=255 time=0.865 ms
64 bytes from 10.0.16.1: seq=30 ttl=255 time=0.999 ms
64 bytes from 10.0.16.1: seq=31 ttl=255 time=1.116 ms
64 bytes from 10.0.16.1: seq=32 ttl=255 time=0.859 ms
64 bytes from 10.0.16.1: seq=33 ttl=255 time=0.889 ms
64 bytes from 10.0.16.1: seq=34 ttl=255 time=1.060 ms
64 bytes from 10.0.16.1: seq=35 ttl=255 time=0.971 ms
64 bytes from 10.0.16.1: seq=36 ttl=255 time=1.017 ms
64 bytes from 10.0.16.1: seq=37 ttl=255 time=0.979 ms
64 bytes from 10.0.16.1: seq=38 ttl=255 time=0.993 ms
64 bytes from 10.0.16.1: seq=39 ttl=255 time=1.035 ms
64 bytes from 10.0.16.1: seq=40 ttl=255 time=1.169 ms
64 bytes from 10.0.16.1: seq=41 ttl=255 time=0.924 ms
64 bytes from 10.0.16.1: seq=42 ttl=255 time=0.879 ms
64 bytes from 10.0.16.1: seq=43 ttl=255 time=0.714 ms
64 bytes from 10.0.16.1: seq=44 ttl=255 time=1.009 ms
64 bytes from 10.0.16.1: seq=45 ttl=255 time=0.972 ms
64 bytes from 10.0.16.1: seq=46 ttl=255 time=1.009 ms
64 bytes from 10.0.16.1: seq=47 ttl=255 time=0.970 ms
64 bytes from 10.0.16.1: seq=48 ttl=255 time=0.866 ms
64 bytes from 10.0.16.1: seq=49 ttl=255 time=0.891 ms
64 bytes from 10.0.16.1: seq=50 ttl=255 time=0.899 ms
64 bytes from 10.0.16.1: seq=51 ttl=255 time=1.018 ms
64 bytes from 10.0.16.1: seq=52 ttl=255 time=0.876 ms
64 bytes from 10.0.16.1: seq=53 ttl=255 time=0.973 ms
64 bytes from 10.0.16.1: seq=54 ttl=255 time=0.965 ms
64 bytes from 10.0.16.1: seq=55 ttl=255 time=1.009 ms
64 bytes from 10.0.16.1: seq=56 ttl=255 time=0.867 ms
^C
--- 10.0.16.1 ping statistics ---
57 packets transmitted, 57 packets received, 0% packet loss
round-trip min/avg/max = 0.714/0.954/1.467 ms
cisco@fs-client10:~$ ping -c 5 10.0.16.1
PING 10.0.16.1 (10.0.16.1): 56 data bytes
64 bytes from 10.0.16.1: seq=0 ttl=255 time=0.967 ms
64 bytes from 10.0.16.1: seq=1 ttl=255 time=1.075 ms
64 bytes from 10.0.16.1: seq=2 ttl=255 time=1.047 ms
64 bytes from 10.0.16.1: seq=3 ttl=255 time=1.024 ms
64 bytes from 10.0.16.1: seq=4 ttl=255 time=0.938 ms

--- 10.0.16.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.938/1.010/1.075 ms
cisco@fs-client10:~$ ping -c 5 10.0.16.1
PING 10.0.16.1 (10.0.16.1): 56 data bytes
64 bytes from 10.0.16.1: seq=1 ttl=255 time=0.989 ms
64 bytes from 10.0.16.1: seq=2 ttl=255 time=1.036 ms
64 bytes from 10.0.16.1: seq=3 ttl=255 time=0.904 ms
64 bytes from 10.0.16.1: seq=4 ttl=255 time=0.766 ms

--- 10.0.16.1 ping statistics ---
5 packets transmitted, 4 packets received, 20% packet loss
round-trip min/avg/max = 0.766/0.923/1.036 ms
cisco@fs-client10:~$ 



FS-R1#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   105 P Active  local           10.0.16.3       10.0.16.1
Et0/0.20    20   105 P Active  local           10.0.16.131     10.0.16.129
Et0/0.30    30   105 P Active  local           10.0.17.3       10.0.17.1
Et0/0.40    40   105 P Active  local           10.0.17.131     10.0.17.129
FS-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R1(config)#interface ethernet0/0
FS-R1(config-if)# shutdown
FS-R1(config-if)#end
FS-R1#
*Jul 19 17:10:19.358: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Active -> Init
*Jul 19 17:10:19.358: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Active -> Init
*Jul 19 17:10:19.358: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Active -> Init
*Jul 19 17:10:19.358: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Active -> Init
*Jul 19 17:10:20.253: %SYS-5-CONFIG_I: Configured from console by console
FS-R1#
*Jul 19 17:10:21.355: %LINK-5-CHANGED: Interface Ethernet0/0, changed state to administratively down
*Jul 19 17:10:22.355: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
FS-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R1(config)#interface ethernet0/0
FS-R1(config-if)# no shutdown
FS-R1(config-if)#end
FS-R1#
*Jul 19 17:11:27.038: %SYS-5-CONFIG_I: Configured from console by console
*Jul 19 17:11:27.825: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Listen -> Active
FS-R1#
*Jul 19 17:11:28.639: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Jul 19 17:11:28.998: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Listen -> Active
*Jul 19 17:11:29.609: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Listen -> Active
FS-R1#
*Jul 19 17:11:29.639: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
FS-R1#
*Jul 19 17:11:29.913: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Listen -> Active
FS-R1#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   105 P Active  local           unknown         10.0.16.1
Et0/0.20    20   105 P Active  local           unknown         10.0.16.129
Et0/0.30    30   105 P Active  local           unknown         10.0.17.1
Et0/0.40    40   105 P Active  local           unknown         10.0.17.129
FS-R1#



FS-R2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   100 P Standby 10.0.16.2       local           10.0.16.1
Et0/0.20    20   100 P Standby 10.0.16.130     local           10.0.16.129
Et0/0.30    30   100 P Standby 10.0.17.2       local           10.0.17.1
Et0/0.40    40   100 P Standby 10.0.17.130     local           10.0.17.129
FS-R2#
*Jul 19 17:10:19.356: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Standby -> Active
*Jul 19 17:10:19.356: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Standby -> Active
*Jul 19 17:10:19.356: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Standby -> Active
*Jul 19 17:10:19.356: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Standby -> Active
FS-R2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   100 P Active  local           unknown         10.0.16.1
Et0/0.20    20   100 P Active  local           unknown         10.0.16.129
Et0/0.30    30   100 P Active  local           unknown         10.0.17.1
Et0/0.40    40   100 P Active  local           unknown         10.0.17.129
FS-R2#
*Jul 19 17:11:27.826: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Active -> Speak
FS-R2#
*Jul 19 17:11:28.999: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Active -> Speak
*Jul 19 17:11:29.610: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Active -> Speak
*Jul 19 17:11:29.914: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Active -> Speak
FS-R2#
*Jul 19 17:11:39.301: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Speak -> Standby
*Jul 19 17:11:39.606: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Speak -> Standby
FS-R2#
*Jul 19 17:11:41.440: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Speak -> Standby
*Jul 19 17:11:41.520: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Speak -> Standby
FS-R2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   100 P Standby 10.0.16.2       local           10.0.16.1
Et0/0.20    20   100 P Standby 10.0.16.130     local           10.0.16.129
Et0/0.30    30   100 P Standby 10.0.17.2       local           10.0.17.1
Et0/0.40    40   100 P Standby 10.0.17.130     local           10.0.17.129
FS-R2#
```
