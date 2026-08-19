# Lab 057 - Raw CLI Output

```bash
Cafe-Edge-R1>
Cafe-Edge-R1>en
Cafe-Edge-R1#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Edge-R1(config)#interface Ethernet0/0
Cafe-Edge-R1(config-if)#no shutdown
Cafe-Edge-R1(config-if)#end
Cafe-Edge-R1#show ip interface brief | include Ethernet0/0
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.1.10.1       YES TFTP   up                    up      
Ethernet0/0.20         10.1.20.1       YES TFTP   up                    up      
Cafe-Edge-R1#show ip dhcp binding
*Aug 18 15:17:29.966: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Edge-R1#show ip dhcp binding
*Aug 18 15:17:31.961: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Aug 18 15:17:32.731: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-Edge-R1#show ip dhcp binding
*Aug 18 15:17:32.833: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:17:32.833: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:17:32.938: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:17:32.961: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-Edge-R1#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address      Client-ID/              Lease expiration        Type       State      Interface
                Hardware address/
                User name
Cafe-Edge-R1#
*Aug 18 15:17:33.038: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 18 15:17:33.038: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-Edge-R1#




Cafe-01-SW1>
Cafe-01-SW1>
*Aug 18 15:17:52.220: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW1>en
Cafe-01-SW1#show interfaces trunk
Cafe-01-SW1#
*Aug 18 15:18:16.055: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 18 15:18:16.157: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:18:16.158: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:18:16.264: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-01-SW1#
*Aug 18 15:18:16.364: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 18 15:18:16.364: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-01-SW1#show interfaces
*Aug 18 15:18:23.263: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1#show interfaces ethernet0/0
Ethernet0/0 is up, line protocol is up (connected) 
  Hardware is Ethernet, address is aabb.cc00.0400 (bia aabb.cc00.0400)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:01, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     83 packets output, 8410 bytes, 0 underruns
     Output 83 broadcasts (77 multicasts)
     1 output errors, 1 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Cafe-01-SW1#show interfaces ethernet0/1
Ethernet0/1 is up, line protocol is up (connected) 
  Hardware is Ethernet, address is aabb.cc00.0410 (bia aabb.cc00.0410)
  Description: Trunk to Cafe-01-SW2
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:01, output 00:00:01, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 1000 bits/sec, 1 packets/sec
     29 packets input, 5344 bytes, 0 no buffer
     Received 25 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     90 packets output, 9122 bytes, 0 underruns
     Output 90 broadcasts (84 multicasts)
     1 output errors, 1 collisions, 1 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Cafe-01-SW1#show interfaces ethernet0/1
*Aug 18 15:18:53.839: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1#show interfaces ethernet6/0
Ethernet6/0 is up, line protocol is up (connected) 
  Hardware is Ethernet, address is aabb.cc00.0406 (bia aabb.cc00.0406)
  Description: Uplink to Cafe-Edge-R1 (Guide Ethernet0/24)
  MTU 1500 bytes, BW 10000 Kbit/sec, DLY 1000 usec, 
     reliability 229/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:09, output 00:00:00, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     29 packets input, 2214 bytes, 0 no buffer
     Received 14 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     92 packets output, 9362 bytes, 0 underruns
     Output 92 broadcasts (92 multicasts)
     31 output errors, 31 collisions, 1 interface resets
     7 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Cafe-01-SW1#
*Aug 18 15:19:27.226: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1#
*Aug 18 15:19:57.226: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/1 TDR=0, TRC=0
Cafe-01-SW1#
*Aug 18 15:20:27.226: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#interface ethernet0/1
Cafe-01-SW1(config-if)#switchport 
*Aug 18 15:20:57.233: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/1 TDR=0, TRC=0
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk
Cafe-01-SW1(config-if)#
*Aug 18 15:21:22.193: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-01-SW1(config-if)#switchport mod
*Aug 18 15:21:25.192: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-01-SW1(config-if)#switchport mode trunk allowed
*Aug 18 15:21:29.117: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/1 TDR=0, TRC=0
Cafe-01-SW1(config-if)#switchport trunk allowed vlan 
*Aug 18 15:22:02.224: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/2 TDR=0, TRC=0
Cafe-01-SW1(config-if)#switchport trunk allowed vlan 10,20
Cafe-01-SW1(config-if)#no shutd
*Aug 18 15:22:33.186: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/2 TDR=0, TRC=0
Cafe-01-SW1(config-if)#no shutdown
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#interface ethernet6/0
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk               
Cafe-01-SW1(config-if)#no shutdown                         
*Aug 18 15:23:02.861: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/0, changed state to down
Cafe-01-SW1(config-if)#switchport trunk allowed vlan 10,20
*Aug 18 15:23:03.266: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1(config-if)#switchport trunk allowed vlan 10,20
Cafe-01-SW1(config-if)#no shutdown                         
*Aug 18 15:23:05.862: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/0, changed state to up
Cafe-01-SW1(config-if)#no shutdown
Cafe-01-SW1(config-if)#exit                                
Cafe-01-SW1(config)#end
Cafe-01-SW1#sh
*Aug 18 15:23:17.915: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et6/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20
Et6/0          10,20

Port           Vlans allowed and active in management domain
Et0/1          10,20
Et6/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20
Et6/0          10,20
Cafe-01-SW1#
*Aug 18 15:23:37.227: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/1 TDR=0, TRC=0
Cafe-01-SW1#
*Aug 18 15:24:07.229: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-01-SW1#
*Aug 18 15:24:42.223: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Cafe-01-SW1#
*Aug 18 15:25:12.224: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/1 TDR=0, TRC=0
Cafe-01-SW1#
*Aug 18 15:25:42.224: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-01-SW1#


Connecting to console for Cafe-01-SW2

Cafe-01-SW2>
Cafe-01-SW2>
*Aug 18 15:21:22.193: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-01-SW2>
*Aug 18 15:21:25.195: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-01-SW2>en
Cafe-01-SW2#conf t
*Aug 18 15:23:49.163: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 18 15:23:49.265: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:23:49.266: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:23:49.374: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-01-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW2(config)#
*Aug 18 15:23:49.474: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 18 15:23:49.474: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-01-SW2(config)#interface ethernet0/1
Cafe-01-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW2(config-if)#switchport mode trunk
Cafe-01-SW2(config-if)#switchport trunk allowed vlan 10,20
Cafe-01-SW2(config-if)#no shutdown
Cafe-01-SW2(config-if)#end
Cafe-01-SW2#
*Aug 18 15:24:52.913: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW2#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20

Port           Vlans allowed and active in management domain
Et0/1          20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          20
Cafe-01-SW2#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/3
20   VLAN0020                         active    Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0   
20   enet  100020     1500  -      -      -        -    -        0      0   
1002 fddi  101002     1500  -      -      -        -    -        0      0   
1003 tr    101003     1500  -      -      -        -    -        0      0   
1004 fdnet 101004     1500  -      -      -        ieee -        0      0   
1005 trnet 101005     1500  -      -      -        ibm  -        0      0   

Remote SPAN VLANs
------------------------------------------------------------------------------


          
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
Primary Secondary Type              Ports
------- --------- ----------------- ------------------------------------------

Cafe-01-SW2#


Connecting to console for Cafe-01-PC

Core Linux
cafe-01-pc login: 
Core Linux
cafe-01-pc login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-01-pc:~$ sudo ifconfig eth0 0.0.0.0
cisco@cafe-01-pc:~$ sudo udhcpc -i eth0 -n -q
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.1.20.11, server 10.1.20.1
udhcpc: lease of 10.1.20.11 obtained from 10.1.20.1, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 1.1.1.1
cisco@cafe-01-pc:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:AC:84:39  
          inet addr:10.1.20.11  Bcast:10.1.20.255  Mask:255.255.255.0
          inet6 addr: fe80::5054:ff:feac:8439/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:7 errors:0 dropped:2 overruns:0 frame:0
          TX packets:60 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:1548 (1.5 KiB)  TX bytes:16828 (16.4 KiB)

cisco@cafe-01-pc:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.1.20.1       0.0.0.0         UG    0      0        0 eth0
10.1.20.0       0.0.0.0         255.255.255.0   U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@cafe-01-pc:~$ 



Cafe-01-SW2#
Cafe-01-SW2#show interface Ethernet0/2 status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/2        Cafe-01-PC         connected    20           full   auto 10/100/1000BaseTX
Cafe-01-SW2#show vlan brief | include Et0/2
20   VLAN0020                         active    Et0/2
Cafe-01-SW2#



Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#ip dhcp snooping
Cafe-01-SW1(config)#ip dhcp snooping vlan 10,20
Cafe-01-SW1(config)#no ip dhcp snooping information option
Cafe-01-SW1(config)#
*Aug 18 15:28:59.783: %AMDP2_FE-6-EXCESSCOLL: Ethernet3/3 TDR=0, TRC=0
Cafe-01-SW1(config)#end
Cafe-01-SW1#
*Aug 18 15:29:03.693: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#show running-config | include ip dhcp snooping
ip dhcp snooping vlan 10,20
no ip dhcp snooping information option
ip dhcp snooping
Cafe-01-SW1#show ip dhcp snooping
Switch DHCP snooping is enabled
Switch DHCP gleaning is disabled
DHCP snooping is configured on following VLANs:
10,20
DHCP snooping is operational on following VLANs:
10,20
 Proxy bridge is configured on following VLANs:
none
 Proxy bridge is operational on following VLANs:
none
DHCP snooping is configured on the following L3 Interfaces:

Insertion of option 82 is disabled
   circuit-id default format: vlan-mod-port
   remote-id: aabb.cc00.0400 (MAC)
Option 82 on untrusted port is not allowed
Verification of hwaddr field is enabled
Verification of giaddr field is enabled
DHCP snooping trust/rate is configured on the following Interfaces:

Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
Cafe-01-SW1#
*Aug 18 15:29:31.271: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-01-SW1#



Cafe-01-SW1#
Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#int
Cafe-01-SW1(config)#interface Ethernet6/0
*Aug 18 15:30:32.223: %AMDP2_FE-6-EXCESSCOLL: Ethernet3/3 TDR=0, TRC=0
Cafe-01-SW1(config)#interface Ethernet6/0
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk
Cafe-01-SW1(config-if)#ip dhcp snooping trust
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#
*Aug 18 15:31:05.921: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW1(config)#interface Ethernet0/1               
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk               
Cafe-01-SW1(config-if)#ip dhcp snooping trust              
Cafe-01-SW1(config-if)#end                                 
Cafe-01-SW1#
*Aug 18 15:31:34.203: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et6/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20
Et6/0          10,20

Port           Vlans allowed and active in management domain
Et0/1          10,20
Et6/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20
Et6/0          10,20
Cafe-01-SW1#
*Aug 18 15:31:42.223: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/0 TDR=0, TRC=0
Cafe-01-SW1#show ip dhcp snooping
Switch DHCP snooping is enabled
Switch DHCP gleaning is disabled
DHCP snooping is configured on following VLANs:
10,20
DHCP snooping is operational on following VLANs:
10,20
 Proxy bridge is configured on following VLANs:
none
 Proxy bridge is operational on following VLANs:
none
DHCP snooping is configured on the following L3 Interfaces:

Insertion of option 82 is disabled
   circuit-id default format: vlan-mod-port
   remote-id: aabb.cc00.0400 (MAC)
Option 82 on untrusted port is not allowed
Verification of hwaddr field is enabled
Verification of giaddr field is enabled
DHCP snooping trust/rate is configured on the following Interfaces:

Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
Ethernet0/1                      yes        yes             unlimited
Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
  Custom circuit-ids:
Ethernet6/0                      yes        yes             unlimited
  Custom circuit-ids:
Cafe-01-SW1#



Cafe-01-SW2#
Cafe-01-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW2(config)#ip dhcp snooping
Cafe-01-SW2(config)#ip dhcp snooping vlan 10,20
Cafe-01-SW2(config)#no ip dhcp snooping information option
Cafe-01-SW2(config)#interface Ethernet0/1
Cafe-01-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW2(config-if)#switchport mode trunk
Cafe-01-SW2(config-if)#ip dhcp snooping trust
Cafe-01-SW2(config-if)#end
Cafe-01-SW2#show in
*Aug 18 15:33:57.422: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW2#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20

Port           Vlans allowed and active in management domain
Et0/1          20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          20
Cafe-01-SW2#show ip dhcp snooping
Switch DHCP snooping is enabled
Switch DHCP gleaning is disabled
DHCP snooping is configured on following VLANs:
10,20
DHCP snooping is operational on following VLANs:
20
 Proxy bridge is configured on following VLANs:
none
 Proxy bridge is operational on following VLANs:
none
DHCP snooping is configured on the following L3 Interfaces:

Insertion of option 82 is disabled
   circuit-id default format: vlan-mod-port
   remote-id: aabb.cc00.0500 (MAC)
Option 82 on untrusted port is not allowed
Verification of hwaddr field is enabled
Verification of giaddr field is enabled
DHCP snooping trust/rate is configured on the following Interfaces:

Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
Ethernet0/1                      yes        yes             unlimited
Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
  Custom circuit-ids:
Cafe-01-SW2#



cisco@cafe-01-pc:~$ sudo ifconfig eth0 0.0.0.0
cisco@cafe-01-pc:~$ sudo udhcpc -i eth0 -n -q
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.1.20.11, server 10.1.20.1
udhcpc: lease of 10.1.20.11 obtained from 10.1.20.1, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 1.1.1.1
cisco@cafe-01-pc:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:AC:84:39  
          inet addr:10.1.20.11  Bcast:10.1.20.255  Mask:255.255.255.0
          inet6 addr: fe80::5054:ff:feac:8439/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:9 errors:0 dropped:2 overruns:0 frame:0
          TX packets:63 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:2232 (2.1 KiB)  TX bytes:17582 (17.1 KiB)

cisco@cafe-01-pc:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.1.20.1       0.0.0.0         UG    0      0        0 eth0
10.1.20.0       0.0.0.0         255.255.255.0   U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@cafe-01-pc:~$ ping -c 3 10.1.20.1
PING 10.1.20.1 (10.1.20.1): 56 data bytes
64 bytes from 10.1.20.1: seq=0 ttl=255 time=2.698 ms
64 bytes from 10.1.20.1: seq=1 ttl=255 time=1.585 ms
64 bytes from 10.1.20.1: seq=2 ttl=255 time=1.487 ms

--- 10.1.20.1 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 1.487/1.923/2.698 ms
cisco@cafe-01-pc:~$ 


Cafe-Edge-R1#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address      Client-ID/              Lease expiration        Type       State      Interface
                Hardware address/
                User name
10.1.20.11      0152.5400.ac84.39       Aug 19 2026 03:34 PM    Automatic  Active     Ethernet0/0.20
Cafe-Edge-R1#


Cafe-01-SW2#show ip dhcp snooping binding
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
Total number of bindings: 0

Cafe-01-SW2#show ip dhcp snooping        
Switch DHCP snooping is enabled
Switch DHCP gleaning is disabled
DHCP snooping is configured on following VLANs:
10,20
DHCP snooping is operational on following VLANs:
20
 Proxy bridge is configured on following VLANs:
none
 Proxy bridge is operational on following VLANs:
none
DHCP snooping is configured on the following L3 Interfaces:

Insertion of option 82 is disabled
   circuit-id default format: vlan-mod-port
   remote-id: aabb.cc00.0500 (MAC)
Option 82 on untrusted port is not allowed
Verification of hwaddr field is enabled
Verification of giaddr field is enabled
DHCP snooping trust/rate is configured on the following Interfaces:

Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
Ethernet0/1                      yes        yes             unlimited
Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
  Custom circuit-ids:
Cafe-01-SW2#show ip dhcp snooping statistics
 Packets Forwarded                                     = 0
 Packets Dropped                                       = 0
 Packets Dropped From untrusted ports                  = 0
Cafe-01-SW2#


Cafe-01-SW1#
Cafe-01-SW1#show ip dhcp snooping binding
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
Total number of bindings: 0

Cafe-01-SW1#show ip dhcp snooping binding
*Aug 18 15:36:55.686: %AMDP2_FE-6-EXCESSCOLL: Ethernet3/3 TDR=0, TRC=0
Cafe-01-SW1#show ip dhcp snooping        
Switch DHCP snooping is enabled
Switch DHCP gleaning is disabled
DHCP snooping is configured on following VLANs:
10,20
DHCP snooping is operational on following VLANs:
10,20
 Proxy bridge is configured on following VLANs:
none
 Proxy bridge is operational on following VLANs:
none
DHCP snooping is configured on the following L3 Interfaces:

Insertion of option 82 is disabled
   circuit-id default format: vlan-mod-port
   remote-id: aabb.cc00.0400 (MAC)
Option 82 on untrusted port is not allowed
Verification of hwaddr field is enabled
Verification of giaddr field is enabled
DHCP snooping trust/rate is configured on the following Interfaces:

Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
Ethernet0/1                      yes        yes             unlimited
Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
  Custom circuit-ids:
Ethernet6/0                      yes        yes             unlimited
  Custom circuit-ids:
Cafe-01-SW1#show interfaces trunk     

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et6/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20
Et6/0          10,20

Port           Vlans allowed and active in management domain
Et0/1          10,20
Et6/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20
Et6/0          10,20
Cafe-01-SW1#
```
