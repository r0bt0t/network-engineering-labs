# Lab 030 - Raw CLI Output

```bash
Connecting to console for Cafe-SW1
Connected to CML terminalserver.

Cafe-SW1>en
Cafe-SW1#s
*Jun 26 09:23:47.404: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW1#show 
*Jun 26 09:23:47.506: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 26 09:23:47.507: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 26 09:23:47.612: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW1#show vlan
*Jun 26 09:23:47.712: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jun 26 09:23:47.712: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et1/0, Et1/1
                                                Et1/2, Et1/3, Et2/0, Et2/1
                                                Et2/2, Et2/3, Et3/0, Et3/1
                                                Et3/2, Et3/3, Et4/0, Et4/1
                                                Et4/2, Et4/3, Et5/0, Et5/1
                                                Et5/2, Et5/3, Et6/0, Et6/1
                                                Et6/2, Et6/3
10   VLAN0010                         active    Et0/2
20   VLAN0020                         active    Et0/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#show interface t
*Jun 26 09:24:02.495: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-SW1#show interface trunk | begin Port  

Cafe-SW1#
*Jun 26 09:24:35.070: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0

Connecting to console for Cafe-SW2

Cafe-SW2>
*Jun 26 09:24:06.425: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/2 TDR=0, TRC=0
Cafe-SW2>
*Jun 26 09:25:02.236: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/2 TDR=0, TRC=0
Cafe-SW2>en
Cafe-SW2#show vlan 
*Jun 26 09:25:22.080: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW2#show vlan br
*Jun 26 09:25:22.183: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 26 09:25:22.184: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 26 09:25:22.290: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW2#show vlan brief
*Jun 26 09:25:22.390: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jun 26 09:25:22.390: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et1/0
                                                Et1/1, Et1/3, Et2/0, Et2/1
                                                Et2/2, Et2/3, Et3/0, Et3/1
                                                Et3/2, Et3/3, Et4/0, Et4/1
                                                Et4/2, Et4/3, Et5/0, Et5/1
                                                Et5/2, Et5/3, Et6/0, Et6/1
                                                Et6/2, Et6/3
10   VLAN0010                         active    Et0/3
20   VLAN0020                         active    Et1/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW2#
Cafe-SW2#show interface trunk | begin 
*Jun 26 09:25:33.384: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-SW2#show interface trunk | begin Port


Connecting to console for Cafe-RTR1

Cafe-RTR1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RTR1(config)#interface ethenet0/0
                                ^
% Invalid input detected at '^' marker.

Cafe-RTR1(config)#interface ethernet0/0
Cafe-RTR1(config-if)#no shutdown
Cafe-RTR1(config-if)#
*Jun 26 09:28:21.064: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Cafe-RTR1(config-if)#
*Jun 26 09:28:22.065: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-RTR1(config-if)#end 
Cafe-RTR1#
*Jun 26 09:28:25.877: %SYS-5-CONFIG_I: Configured from console by console
Cafe-RTR1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/0.20         10.0.18.33      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RTR1#
Cafe-RTR1#

Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#vlan 10
Cafe-SW1(config-vlan)#name ADMIN-FLOOR
*Jun 26 09:29:32.613: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW1(config-vlan)#name ADMIN-FLOOR
Cafe-SW1(config-vlan)#vlan 20
Cafe-SW1(config-vlan)#name PATRON-FLOOR
Cafe-SW1(config-vlan)#exit
Cafe-SW1(config)#interface ethernet0/0
*Jun 26 09:30:04.733: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/1 TDR=0, TRC=0
Cafe-SW1(config)#interface ethernet0/0
Cafe-SW1(config-if)#description Trunk to Cafe-RTR1
Cafe-SW1(config-if)#switch
*Jun 26 09:30:36.854: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#
*Jun 26 09:30:58.843: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Cafe-SW1(config-if)#sw
*Jun 26 09:31:01.843: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-SW1(config-if)#switchport trunk allowed vlan 10,2
*Jun 26 09:31:10.875: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Cafe-SW1(config-if)#switchport trunk allowed vlan 10,20
Cafe-SW1(config-if)#exit
Cafe-SW1(config)#interface ethernet0/1
Cafe-SW1(config-if)#description Trunk to 
*Jun 26 09:31:42.555: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW1(config-if)#description Trunk to Cafe-SW2
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#swi
*Jun 26 09:32:16.132: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW1(config-if)#switch
*Jun 26 09:32:16.636: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Cafe-SW1(config-if)#switchport trunk all
*Jun 26 09:32:19.132: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-SW1(config-if)#switchport trunk allowed vlan 10,20
Cafe-SW1(config-if)#exit
Cafe-SW1(config)#interface ethernet1/0
Cafe-SW1(config-if)#description Trunk to 
*Jun 26 09:33:05.391: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW1(config-if)#description Trunk to Cafe-01-WAP1
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#switchport mode tr
*Jun 26 09:33:36.536: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#switch
*Jun 26 09:33:39.641: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to down
Cafe-SW1(config-if)#switchport trunk 
*Jun 26 09:33:42.643: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to up
Cafe-SW1(config-if)#switchport trunk allowed vlan 10,20
Cafe-SW1(config-if)#end
Cafe-SW1#show int
*Jun 26 09:33:58.711: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1
Et0/1          on               802.1q         trunking      1
Et1/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20
Et0/1          10,20
Et1/0          10,20

Port           Vlans allowed and active in management domain
Et0/0          10,20
Et0/1          10,20
Et1/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20
Et0/1          10,20
Et1/0          none
Cafe-SW1#

Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#valn 10
                  ^
% Invalid input detected at '^' marker.

Cafe-SW2(config)#vlan 10
Cafe-SW2(config-vlan)#     
*Jun 26 09:35:18.133: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/1 TDR=0, TRC=0
Cafe-SW2(config-vlan)#name ADMIN-FLOOR
Cafe-SW2(config-vlan)#vlan 20
Cafe-SW2(config-vlan)#name PATRON-FLOOR
Cafe-SW2(config-vlan)#exit
Cafe-SW2(config)#
*Jun 26 09:35:48.133: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW2(config)#interface ethernet0/1
Cafe-SW2(config-if)#description Trunk to Cafe-SW1
Cafe-SW2(config-if)#switchpor
*Jun 26 09:36:19.976: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-SW2(config-if)#switchport mode trunk
Cafe-SW2(config-if)#switchport trunk allowed vlan 10,20
Cafe-SW2(config-if)#
*Jun 26 09:36:50.545: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW2(config-if)#exit
Cafe-SW2(config)#interface ethernet1/0
Cafe-SW2(config-if)#description Trunk to Cafe-01-WAP"
*Jun 26 09:37:23.490: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-SW2(config-if)#description Trunk to Cafe-01-WAP2
Cafe-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-SW2(config-if)#switchport mode trunk
Cafe-SW2(config-if)#switchpo
*Jun 26 09:37:51.965: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to down
Cafe-SW2(config-if)#switchport t
*Jun 26 09:37:54.966: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to upr
Cafe-SW2(config-if)#switchport trunk allowed vlan 10,20
Cafe-SW2(config-if)#end
Cafe-SW2#
*Jun 26 09:38:17.535: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et1/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20
Et1/0          10,20

Port           Vlans allowed and active in management domain
Et0/1          10,20
Et1/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20
Et1/0          10,20
Cafe-SW2#

Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#interface ethernet6/0
Cafe-SW2(config-if)#description Cafe-01-Plex
*Jun 26 09:39:49.270: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/1 TDR=0, TRC=0
Cafe-SW2(config-if)#description Cafe-01-Plex
Cafe-SW2(config-if)#switchport mode access
Cafe-SW2(config-if)#switchport access vlan 10
Cafe-SW2(config-if)#spanning-tree po
*Jun 26 09:40:22.578: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/1 TDR=0, TRC=0
Cafe-SW2(config-if)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet6/0 but will only
 have effect when the interface is in a non-trunking mode.
Cafe-SW2(config-if)#end
Cafe-SW2#show
*Jun 26 09:40:34.787: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show vlan brief | include et6/0
Cafe-SW2#

Connecting to console for Cafe-PLEX1
Escape character is '^]'.

Core Linux
Cafe-PLEX1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@Cafe-PLEX1:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:3F:19:9D  
          inet addr:10.0.18.6  Bcast:10.0.18.31  Mask:255.255.255.224
          inet6 addr: fe80::5054:ff:fe3f:199d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2 errors:0 dropped:0 overruns:0 frame:0
          TX packets:135 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:120 (120.0 B)  TX bytes:42226 (41.2 KiB)

cisco@Cafe-PLEX1:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.18.1       0.0.0.0         UG    0      0        0 eth0
10.0.18.0       0.0.0.0         255.255.255.224 U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@Cafe-PLEX1:~$ ping -c 5 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes
64 bytes from 10.0.18.1: seq=0 ttl=255 time=3.720 ms
64 bytes from 10.0.18.1: seq=1 ttl=255 time=1.097 ms
64 bytes from 10.0.18.1: seq=2 ttl=255 time=1.017 ms
64 bytes from 10.0.18.1: seq=3 ttl=255 time=1.034 ms
64 bytes from 10.0.18.1: seq=4 ttl=255 time=0.976 ms

--- 10.0.18.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.976/1.568/3.720 ms
cisco@Cafe-PLEX1:~$ 

Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#interface ran
*Jun 26 09:44:00.716: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/2 TDR=0, TRC=0
Cafe-SW1(config)#interface range ethernet1/1 - 3
Cafe-SW1(config-if-range)#description UNUSED-LOCKDOWN
Cafe-SW1(config-if-range)#switchport mode a
*Jun 26 09:44:39.706: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Cafe-SW1(config-if-range)#switchport mode access
Cafe-SW1(config-if-range)#switchport access vlan 1
Cafe-SW1(config-if-range)#shutdown
Cafe-SW1(config-if-range)#
*Jun 26 09:45:06.566: %LINK-5-CHANGED: Interface Ethernet1/1, changed state to administratively down
*Jun 26 09:45:06.568: %LINK-5-CHANGED: Interface Ethernet1/2, changed state to administratively down
*Jun 26 09:45:06.570: %LINK-5-CHANGED: Interface Ethernet1/3, changed state to administratively down
*Jun 26 09:45:07.566: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to down
Cafe-SW1(config-if-range)#
*Jun 26 09:45:07.568: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jun 26 09:45:07.570: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Cafe-SW1(config-if-range)#exit
Cafe-SW1(config)#interf
*Jun 26 09:45:19.603: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW1(config)#interface range ethernet2/0 - 3
Cafe-SW1(config-if-range)#description UNUSED-LOCKDOWN
Cafe-SW1(config-if-range)#switchport mode access
Cafe-SW1(config-if-range)#switchport access vlan 1
Cafe-SW1(config-if-range)#shutdown
Cafe-SW1(config-if-range)#exit
Cafe-SW1(config)#
*Jun 26 09:46:06.111: %LINK-5-CHANGED: Interface Ethernet2/0, changed state to administratively down
*Jun 26 09:46:06.112: %LINK-5-CHANGED: Interface Ethernet2/1, changed state to administratively down
*Jun 26 09:46:06.114: %LINK-5-CHANGED: Interface Ethernet2/2, changed state to administratively down
*Jun 26 09:46:06.116: %LINK-5-CHANGED: Interface Ethernet2/3, changed state to administratively down
*Jun 26 09:46:07.112: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/0, changed state to down
*Jun 26 09:46:07.112: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/1, changed state to down
Cafe-SW1(config)#
*Jun 26 09:46:07.114: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/2, changed state to down
*Jun 26 09:46:07.116: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/3, changed state to down
Cafe-SW1(config)#
*Jun 26 09:46:07.863: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-SW1(config)#interface range ethernet3/0 - 3
Cafe-SW1(config-if-range)#description UNUSED-LOCKDOWN    
Cafe-SW1(config-if-range)#switchport mode access         
Cafe-SW1(config-if-range)#switchport access vlan 1       
Cafe-SW1(config-if-range)#switchport access vlan 1
*Jun 26 09:46:55.433: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW1(config-if-range)#shutdown                       
Cafe-SW1(config-if-range)#switchport mode access  
*Jun 26 09:47:05.655: %LINK-5-CHANGED: Interface Ethernet3/0, changed state to administratively down
*Jun 26 09:47:05.656: %LINK-5-CHANGED: Interface Ethernet3/1, changed state to administratively down
*Jun 26 09:47:05.657: %LINK-5-CHANGED: Interface Ethernet3/2, changed state to administratively down
*Jun 26 09:47:05.659: %LINK-5-CHANGED: Interface Ethernet3/3, changed state to administratively down
*Jun 26 09:47:06.655: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet3/0, changed state to down
Cafe-SW1(config-if-range)#description UNUSED-LOCKDOWN
*Jun 26 09:47:06.656: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet3/1, changed state to down
*Jun 26 09:47:06.657: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet3/2, changed state to down
*Jun 26 09:47:06.659: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet3/3, changed state to down
Cafe-SW1(config-if-range)#exit                           
Cafe-SW1(config)#interface range ethernet4/0 - 3
Cafe-SW1(config-if-range)#description UNUSED-LOCKDOWN    
Cafe-SW1(config-if-range)#switchport mode access         
Cafe-SW1(config-if-range)#switchport access vlan 1       
Cafe-SW1(config-if-range)#shutdown                       
Cafe-SW1(config-if-range)#description UNUSED-LOCKDOWN
*Jun 26 09:47:56.471: %LINK-5-CHANGED: Interface Ethernet4/0, changed state to administratively down
*Jun 26 09:47:56.473: %LINK-5-CHANGED: Interface Ethernet4/1, changed state to administratively down
*Jun 26 09:47:56.474: %LINK-5-CHANGED: Interface Ethernet4/2, changed state to administratively down
*Jun 26 09:47:56.476: %LINK-5-CHANGED: Interface Ethernet4/3, changed state to administratively down
*Jun 26 09:47:57.471: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet4/0, changed state to down
Cafe-SW1(config-if-range)#exit                           
*Jun 26 09:47:57.473: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet4/1, changed state to down
*Jun 26 09:47:57.474: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet4/2, changed state to down
*Jun 26 09:47:57.476: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet4/3, changed state to down
Cafe-SW1(config-if-range)#exit
Cafe-SW1(config)#interface range ethernet5/0 - 3
Cafe-SW1(config-if-range)#description UNUSED-LOCKDOWN    
Cafe-SW1(config-if-range)#switchport mode access         
Cafe-SW1(config-if-range)#switchport access vlan 1       
Cafe-SW1(config-if-range)#shutdown                       
Cafe-SW1(config-if-range)#switchport access vlan 1
*Jun 26 09:48:32.864: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/0 TDR=0, TRC=0
Cafe-SW1(config-if-range)#exit                           
*Jun 26 09:48:34.865: %LINK-5-CHANGED: Interface Ethernet5/0, changed state to administratively down
*Jun 26 09:48:34.866: %LINK-5-CHANGED: Interface Ethernet5/1, changed state to administratively down
*Jun 26 09:48:34.868: %LINK-5-CHANGED: Interface Ethernet5/2, changed state to administratively down
*Jun 26 09:48:34.869: %LINK-5-CHANGED: Interface Ethernet5/3, changed state to administratively down
*Jun 26 09:48:35.865: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet5/0, changed state to down
Cafe-SW1(config-if-range)#exit
*Jun 26 09:48:35.866: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet5/1, changed state to down
*Jun 26 09:48:35.868: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet5/2, changed state to down
*Jun 26 09:48:35.869: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet5/3, changed state to down
Cafe-SW1(config-if-range)#exit
Cafe-SW1(config)#interface range ethernet6/0 - 3
Cafe-SW1(config-if-range)#description UNUSED-LOCKDOWN    
Cafe-SW1(config-if-range)#switchport mode access         
Cafe-SW1(config-if-range)#switchport access vlan 1       
Cafe-SW1(config-if-range)#shutdown                       
Cafe-SW1(config-if-range)#interface range ethernet6/0 - 3
*Jun 26 09:49:40.213: %LINK-5-CHANGED: Interface Ethernet6/0, changed state to administratively down
*Jun 26 09:49:40.215: %LINK-5-CHANGED: Interface Ethernet6/1, changed state to administratively down
*Jun 26 09:49:40.217: %LINK-5-CHANGED: Interface Ethernet6/2, changed state to administratively down
*Jun 26 09:49:40.217: %LINK-5-CHANGED: Interface Ethernet6/3, changed state to administratively down
*Jun 26 09:49:41.213: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/0, changed state to down
Cafe-SW1(config-if-range)#exit                           
*Jun 26 09:49:41.215: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/1, changed state to down
*Jun 26 09:49:41.217: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/2, changed state to down
*Jun 26 09:49:41.217: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/3, changed state to down
Cafe-SW1(config-if-range)#exit
Cafe-SW1(config)#end
Cafe-SW1#
*Jun 26 09:49:56.855: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show interfaces status | include disabled|Port
Port         Name               Status       Vlan       Duplex  Speed Type
Et1/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et1/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et1/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et2/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et2/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et2/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et2/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et3/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et3/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et3/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et3/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Port         Name               Status       Vlan       Duplex  Speed Type
Et4/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et4/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et4/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et4/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et5/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et5/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et5/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et5/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et6/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et6/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et6/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et6/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et1/1, Et1/2, Et1/3, Et2/0
                                                Et2/1, Et2/2, Et2/3, Et3/0
                                                Et3/1, Et3/2, Et3/3, Et4/0
                                                Et4/1, Et4/2, Et4/3, Et5/0
                                                Et5/1, Et5/2, Et5/3, Et6/0
                                                Et6/1, Et6/2, Et6/3
10   ADMIN-FLOOR                      active    Et0/2
20   PATRON-FLOOR                     active    Et0/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW1#


Cafe-SW2>
Cafe-SW2>en
Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#interface ethernet
*Jun 26 09:52:09.542: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/1 TDR=0, TRC=0
Cafe-SW2(config)#interface ethernet0/0
Cafe-SW2(config-if)#description UNUSED-LOCKDOWN
Cafe-SW2(config-if)#switchport mode access
Cafe-SW2(config-if)#switchport access vlan 1
Cafe-SW2(config-if)#shutdown
*Jun 26 09:52:57.375: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW2(config-if)#shutdown
Cafe-SW2(config-if)#exit
Cafe-SW2(config)#
*Jun 26 09:53:01.881: %LINK-5-CHANGED: Interface Ethernet0/0, changed state to administratively down
*Jun 26 09:53:02.881: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Cafe-SW2(config)#interface ethernet0/2      
Cafe-SW2(config-if)#description UNUSED-LOCKDOWN
Cafe-SW2(config-if)#switchport mode access     
Cafe-SW2(config-if)#switchport access vlan 1   
Cafe-SW2(config-if)#shutdown                   
Cafe-SW2(config-if)#exit                       
*Jun 26 09:54:03.751: %LINK-5-CHANGED: Interface Ethernet0/2, changed state to administratively down
Cafe-SW2(config-if)#exit
Cafe-SW2(config)#
*Jun 26 09:54:04.751: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW2(config)#interface ethernet0/2      
*Jun 26 09:54:16.509: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-SW2(config)#interface ethernet1/1
Cafe-SW2(config-if)#description UNUSED-LOCKDOWN
Cafe-SW2(config-if)#switchport mode access     
Cafe-SW2(config-if)#switchport access vlan 1   
Cafe-SW2(config-if)#shutdown                   
Cafe-SW2(config-if)#exit                       
*Jun 26 09:54:44.861: %LINK-5-CHANGED: Interface Ethernet1/1, changed state to administratively down
*Jun 26 09:54:45.861: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to down
Cafe-SW2(config-if)#exit
Cafe-SW2(config)#interface ethernet1/3      
*Jun 26 09:54:56.694: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/1 TDR=0, TRC=0
Cafe-SW2(config)#interface ethernet1/3
Cafe-SW2(config-if)#description UNUSED-LOCKDOWN
Cafe-SW2(config-if)#switchport mode access     
Cafe-SW2(config-if)#switchport access vlan 1   
Cafe-SW2(config-if)#shutdown                   
Cafe-SW2(config-if)#exit                       
*Jun 26 09:55:22.563: %LINK-5-CHANGED: Interface Ethernet1/3, changed state to administratively down
*Jun 26 09:55:23.563: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Cafe-SW2(config-if)#exit
Cafe-SW2(config)#
*Jun 26 09:55:36.697: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/1 TDR=0, TRC=0
Cafe-SW2(config)#interface ethernet2/0 - 3  
                                       ^
% Invalid input detected at '^' marker.

Cafe-SW2(config)#interface range ethernet2/0 - 3
Cafe-SW2(config-if-range)#description UNUSED-LOCKDOWN    
Cafe-SW2(config-if-range)#switchport mode access         
Cafe-SW2(config-if-range)#switchport mode access         
*Jun 26 09:56:35.456: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Cafe-SW2(config-if-range)#switchport access vlan 1
Cafe-SW2(config-if-range)#shutdown                       
Cafe-SW2(config-if-range)#interface ethernet2/0 - 3      
*Jun 26 09:56:45.480: %LINK-5-CHANGED: Interface Ethernet2/0, changed state to administratively down
*Jun 26 09:56:45.482: %LINK-5-CHANGED: Interface Ethernet2/1, changed state to administratively down
*Jun 26 09:56:45.483: %LINK-5-CHANGED: Interface Ethernet2/2, changed state to administratively down
*Jun 26 09:56:45.485: %LINK-5-CHANGED: Interface Ethernet2/3, changed state to administratively down
*Jun 26 09:56:46.480: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/0, changed state to down
Cafe-SW2(config-if-range)#exit                     
*Jun 26 09:56:46.482: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/1, changed state to down
*Jun 26 09:56:46.483: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/2, changed state to down
*Jun 26 09:56:46.486: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/3, changed state to down
Cafe-SW2(config-if-range)#exit
Cafe-SW2(config)#interface range ethernet3/0 - 3
Cafe-SW2(config-if-range)#description UNUSED-LOCKDOWN    
Cafe-SW2(config-if-range)#switchport mode access         
*Jun 26 09:57:11.455: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-SW2(config-if-range)#switchport mode access
Cafe-SW2(config-if-range)#switchport access vlan 1       
Cafe-SW2(config-if-range)#shutdown                       
Cafe-SW2(config-if-range)#exit                           
*Jun 26 09:57:25.890: %LINK-5-CHANGED: Interface Ethernet3/0, changed state to administratively down
*Jun 26 09:57:25.892: %LINK-5-CHANGED: Interface Ethernet3/1, changed state to administratively down
*Jun 26 09:57:25.893: %LINK-5-CHANGED: Interface Ethernet3/2, changed state to administratively down
*Jun 26 09:57:25.895: %LINK-5-CHANGED: Interface Ethernet3/3, changed state to administratively down
*Jun 26 09:57:26.890: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet3/0, changed state to down
Cafe-SW2(config-if-range)#exit
*Jun 26 09:57:26.892: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet3/1, changed state to down
*Jun 26 09:57:26.893: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet3/2, changed state to down
*Jun 26 09:57:26.895: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet3/3, changed state to down
Cafe-SW2(config-if-range)#exit
Cafe-SW2(config)#interface range ethernet4/0 - 3
Cafe-SW2(config-if-range)#description UNUSED-LOCKDOWN    
Cafe-SW2(config-if-range)#switchport mode access         
Cafe-SW2(config-if-range)#switchport access vlan 1       
Cafe-SW2(config-if-range)#shutdown                       
Cafe-SW2(config-if-range)#shutdown                       
*Jun 26 09:58:10.310: %LINK-5-CHANGED: Interface Ethernet4/0, changed state to administratively down
*Jun 26 09:58:10.312: %LINK-5-CHANGED: Interface Ethernet4/1, changed state to administratively down
*Jun 26 09:58:10.313: %LINK-5-CHANGED: Interface Ethernet4/2, changed state to administratively down
*Jun 26 09:58:10.314: %LINK-5-CHANGED: Interface Ethernet4/3, changed state to administratively down
*Jun 26 09:58:11.310: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet4/0, changed state to down
Cafe-SW2(config-if-range)#shutdown
*Jun 26 09:58:11.312: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet4/1, changed state to down
*Jun 26 09:58:11.313: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet4/2, changed state to down
*Jun 26 09:58:11.315: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet4/3, changed state to down
Cafe-SW2(config-if-range)#exit                    
Cafe-SW2(config)#interface range ethernet5/0 - 3
Cafe-SW2(config-if-range)#switchport mode access         
Cafe-SW2(config-if-range)#switchport access vlan 1       
Cafe-SW2(config-if-range)#shutdown                       
Cafe-SW2(config-if-range)#exit                           
*Jun 26 09:58:54.130: %LINK-5-CHANGED: Interface Ethernet5/0, changed state to administratively down
*Jun 26 09:58:54.131: %LINK-5-CHANGED: Interface Ethernet5/1, changed state to administratively down
*Jun 26 09:58:54.133: %LINK-5-CHANGED: Interface Ethernet5/2, changed state to administratively down
*Jun 26 09:58:54.134: %LINK-5-CHANGED: Interface Ethernet5/3, changed state to administratively down
*Jun 26 09:58:55.130: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet5/0, changed state to down
Cafe-SW2(config-if-range)#exit
*Jun 26 09:58:55.131: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet5/1, changed state to down
*Jun 26 09:58:55.133: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet5/2, changed state to down
*Jun 26 09:58:55.134: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet5/3, changed state to down
Cafe-SW2(config-if-range)#exit
Cafe-SW2(config)#interface range ethernet6/1 - 3
Cafe-SW2(config-if-range)#switchport mode access         
Cafe-SW2(config-if-range)#switchport access vlan 1       
Cafe-SW2(config-if-range)#shutdown                       
Cafe-SW2(config-if-range)#shutdown                       
*Jun 26 09:59:40.546: %LINK-5-CHANGED: Interface Ethernet6/1, changed state to administratively down
*Jun 26 09:59:40.548: %LINK-5-CHANGED: Interface Ethernet6/2, changed state to administratively down
*Jun 26 09:59:40.549: %LINK-5-CHANGED: Interface Ethernet6/3, changed state to administratively down
*Jun 26 09:59:41.546: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/1, changed state to down
Cafe-SW2(config-if-range)#shutdown
*Jun 26 09:59:41.548: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/2, changed state to down
*Jun 26 09:59:41.549: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/3, changed state to down
Cafe-SW2(config-if-range)#exit                    
Cafe-SW2(config)#end
Cafe-SW2#sho
*Jun 26 09:59:56.086: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show interfaces status | include disabled|Port
Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et0/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et1/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et1/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et2/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et2/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et2/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et2/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et3/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et3/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et3/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Port         Name               Status       Vlan       Duplex  Speed Type
Et3/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et4/0        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et4/1        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et4/2        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et4/3        UNUSED-LOCKDOWN    disabled     1            full   auto 10/100/1000BaseTX
Et5/0                           disabled     1            full   auto 10/100/1000BaseTX
Et5/1                           disabled     1            full   auto 10/100/1000BaseTX
Et5/2                           disabled     1            full   auto 10/100/1000BaseTX
Et5/3                           disabled     1            full   auto 10/100/1000BaseTX
Et6/1                           disabled     1            full   auto 10/100/1000BaseTX
Et6/2                           disabled     1            full   auto 10/100/1000BaseTX
Et6/3                           disabled     1            full   auto 10/100/1000BaseTX
Cafe-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/2, Et1/1, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
                                                Et3/0, Et3/1, Et3/2, Et3/3
                                                Et4/0, Et4/1, Et4/2, Et4/3
                                                Et5/0, Et5/1, Et5/2, Et5/3
                                                Et6/1, Et6/2, Et6/3
10   ADMIN-FLOOR                      active    Et0/3, Et6/0
20   PATRON-FLOOR                     active    Et1/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW2#
```
