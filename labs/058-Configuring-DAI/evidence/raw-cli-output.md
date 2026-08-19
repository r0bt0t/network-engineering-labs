# Lab 058 - Raw CLI Output

```bash
Connecting to console for Cafe-Edge-R1

Cafe-Edge-R1>
Cafe-Edge-R1>en
Cafe-Edge-R1#show ip in
*Aug 18 15:51:19.703: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-Edge-R1#show ip interf
*Aug 18 15:51:19.806: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:51:19.807: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:51:19.911: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-Edge-R1#show ip interface 
*Aug 18 15:51:20.011: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 18 15:51:20.011: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-Edge-R1#show ip interface brief | include Ethernet0/0
Ethernet0/0            unassigned      YES unset  administratively down down    
Ethernet0/0.10         10.1.10.1       YES TFTP   administratively down down    
Ethernet0/0.20         10.1.20.1       YES TFTP   administratively down down    
Cafe-Edge-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Edge-R1(config)#interface Ethernet0/0
Cafe-Edge-R1(config-if)#no shutdown
Cafe-Edge-R1(config-if)#end
Cafe-Edge-R1#
*Aug 18 15:52:00.958: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Cafe-Edge-R1#s
*Aug 18 15:52:01.664: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Edge-R1#show i
*Aug 18 15:52:01.959: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-Edge-R1#show ip interface brief | include Ethernet0/0
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.1.10.1       YES TFTP   up                    up      
Ethernet0/0.20         


Connecting to console for Cafe-01-SW1
Connected to CML terminalserver.

Cafe-01-SW1>
*Aug 18 15:51:17.200: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1>
*Aug 18 15:51:50.780: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1>
*Aug 18 15:52:24.224: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/2 TDR=0, TRC=0
Cafe-01-SW1>en
Cafe-01-SW1#c
*Aug 18 15:52:55.352: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-01-SW1#conf 
*Aug 18 15:52:57.518: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#
*Aug 18 15:52:57.620: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:52:57.621: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:52:57.727: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-01-SW1(config)#
*Aug 18 15:52:57.827: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 18 15:52:57.827: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-01-SW1(config)#int
Cafe-01-SW1(config)#interface Ethernet6/0
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk
Cafe-01-SW1(config-if)#i
*Aug 18 15:53:26.730: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1(config-if)#ip dh
*Aug 18 15:53:27.731: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/0, changed state to down
Cafe-01-SW1(config-if)#ip dhcp snoopin
*Aug 18 15:53:30.732: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/0, changed state to up
Cafe-01-SW1(config-if)#ip dhcp snooping trust
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#interface Ethernet0/1               
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk               
Cafe-01-SW1(config-if)#ip dhcp snooping trust              
*Aug 18 15:53:51.895: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-01-SW1(config-if)#ip dhcp snooping trust
Cafe-01-SW1(config-if)#
*Aug 18 15:53:54.896: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-01-SW1(config-if)#
*Aug 18 15:53:56.858: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/1 TDR=0, TRC=0
Cafe-01-SW1(config-if)#end
Cafe-01-SW1#show 
*Aug 18 15:54:00.424: %SYS-5-CONFIG_I: Configured from console by console
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
   remote-id: aabb.cc00.0100 (MAC)
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


Connecting to console for Cafe-01-SW2

Cafe-01-SW2>
Cafe-01-SW2>
*Aug 18 15:53:51.896: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-01-SW2>
*Aug 18 15:53:54.897: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-01-SW2>en 
Cafe-01-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW2(config)#interf
*Aug 18 15:55:00.801: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 18 15:55:00.903: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:55:00.903: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 15:55:01.010: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-01-SW2(config)#interface 
*Aug 18 15:55:01.110: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 18 15:55:01.110: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-01-SW2(config)#interface Ethernet0/1
Cafe-01-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW2(config-if)#switchport mode trunk
Cafe-01-SW2(config-if)#ip dhcp snooping trust
Cafe-01-SW2(config-if)#end
Cafe-01-SW2#show 
*Aug 18 15:55:39.334: %SYS-5-CONFIG_I: Configured from console by console
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
   remote-id: aabb.cc00.0200 (MAC)
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


Connecting to console for Cafe-01-PC
Connected to CML terminalserver.

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
eth0      Link encap:Ethernet  HWaddr 52:54:00:12:E0:8D  
          inet addr:10.1.20.11  Bcast:10.1.20.255  Mask:255.255.255.0
          inet6 addr: fe80::5054:ff:fe12:e08d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:5 errors:0 dropped:1 overruns:0 frame:0
          TX packets:41 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:1428 (1.3 KiB)  TX bytes:10854 (10.5 KiB)

cisco@cafe-01-pc:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.1.20.1       0.0.0.0         UG    0      0        0 eth0
10.1.20.0       0.0.0.0         255.255.255.0   U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@cafe-01-pc:~$ 



Cafe-Edge-R1#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address      Client-ID/              Lease expiration        Type       State      Interface
                Hardware address/
                User name
10.1.20.11      0152.5400.12e0.8d       Aug 19 2026 03:56 PM    Automatic  Active     Ethernet0/0.20
Cafe-Edge-R1#


Cafe-01-SW2#show ip dhcp snooping binding
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
Total number of bindings: 0

Cafe-01-SW2#


Cafe-01-SW2 shows Total number of bindings: 0. The IOSvL2 switch image used in this CML lab does not populate the DHCP snooping binding table even though the DHCP exchange completes successfully. This is a known virtual environment limitation, not a configuration error. On production hardware the binding table would display an entry like this:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
5254.005C.1250      10.1.20.11       86400       dhcp-snooping  20    Ethernet0/2
Total number of bindings: 1
DAI relies on this table to decide whether an ARP packet is legitimate. With zero bindings, DAI will drop every ARP request from Cafe-01-PC on the untrusted access port. Task 3 applies a static ARP access-list as a workaround so DAI has an explicit permit entry to validate against.


Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#interface ethernet6/0
*Aug 18 16:00:32.756: %AMDP2_FE-6-EXCESSCOLL: Ethernet3/3 TDR=0, TRC=0
Cafe-01-SW1(config)#interface ethernet6/0
Cafe-01-SW1(config-if)#ip arp inspection trust
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#interface ethernet0/1
Cafe-01-SW1(config-if)#ip arp inspection 
*Aug 18 16:01:10.683: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/0 TDR=0, TRC=0
Cafe-01-SW1(config-if)#ip arp inspection trust
Cafe-01-SW1(config-if)#end
Cafe-01-SW1#show i
*Aug 18 16:01:14.968: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#show ip arp inspection interfaces

 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et0/0            Untrusted               15                 1
 Et0/1            Trusted               None               N/A
 Et0/2            Untrusted               15                 1
 Et0/3            Untrusted               15                 1
 Et1/0            Untrusted               15                 1
 Et1/1            Untrusted               15                 1
 Et1/2            Untrusted               15                 1
 Et1/3            Untrusted               15                 1
 Et2/0            Untrusted               15                 1
 Et2/1            Untrusted               15                 1
 Et2/2            Untrusted               15                 1
 Et2/3            Untrusted               15                 1
 Et3/0            Untrusted               15                 1
 Et3/1            Untrusted               15                 1
 Et3/2            Untrusted               15                 1
 Et3/3            Untrusted               15                 1
 Et4/0            Untrusted               15                 1
 Et4/1            Untrusted               15                 1
 Et4/2            Untrusted               15                 1
 Et4/3            Untrusted               15                 1
          
 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et5/0            Untrusted               15                 1
 Et5/1            Untrusted               15                 1
 Et5/2            Untrusted               15                 1
 Et5/3            Untrusted               15                 1
 Et6/0            Trusted               None               N/A
 Et6/1            Untrusted               15                 1
 Et6/2            Untrusted               15                 1
 Et6/3            Untrusted               15                 1
Cafe-01-SW1#


Cafe-01-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW2(config)#interface ethernet0/1
Cafe-01-SW2(config-if)#ip arp inspection trust
Cafe-01-SW2(config-if)#end
Cafe-01-SW2#show ip a
*Aug 18 16:02:23.949: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW2#show ip arp inspection interfaces

 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et0/0            Untrusted               15                 1
 Et0/1            Trusted               None               N/A
 Et0/2            Untrusted               15                 1
 Et0/3            Untrusted               15                 1
Cafe-01-SW2#


Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#ip arp inspection vlan 10,20
Cafe-01-SW1(config)#ip ar
*Aug 18 16:03:26.688: %AMDP2_FE-6-EXCESSCOLL: Ethernet3/3 TDR=0, TRC=0
Cafe-01-SW1(config)#ip arp inspection validate src-mac dst-mac ip
Cafe-01-SW1(config)#end
Cafe-01-SW1#
*Aug 18 16:03:50.651: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#show ip arp inspe
*Aug 18 16:03:58.670: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/2 TDR=0, TRC=0
Cafe-01-SW1#show ip arp inspection vlan 10

Source Mac Validation      : Enabled
Destination Mac Validation : Enabled
IP Address Validation      : Enabled

 Vlan     Configuration    Operation   ACL Match          Static ACL
 ----     -------------    ---------   ---------          ----------
   10     Enabled          Active                         

 Vlan     ACL Logging      DHCP Logging      Probe Logging
 ----     -----------      ------------      -------------
   10     Deny             Deny              Off          
Cafe-01-SW1#show ip arp inspection vlan 20

Source Mac Validation      : Enabled
Destination Mac Validation : Enabled
IP Address Validation      : Enabled

 Vlan     Configuration    Operation   ACL Match          Static ACL
 ----     -------------    ---------   ---------          ----------
   20     Enabled          Active                         

 Vlan     ACL Logging      DHCP Logging      Probe Logging
 ----     -----------      ------------      -------------
   20     Deny             Deny              Off          
Cafe-01-SW1#show ip arp inspection interfaces

 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et0/0            Untrusted               15                 1
 Et0/1            Trusted               None               N/A
 Et0/2            Untrusted               15                 1
 Et0/3            Untrusted               15                 1
 Et1/0            Untrusted               15                 1
 Et1/1            Untrusted               15                 1
 Et1/2            Untrusted               15                 1
 Et1/3            Untrusted               15                 1
 Et2/0            Untrusted               15                 1
 Et2/1            Untrusted               15                 1
 Et2/2            Untrusted               15                 1
 Et2/3            Untrusted               15                 1
 Et3/0            Untrusted               15                 1
 Et3/1            Untrusted               15                 1
 Et3/2            Untrusted               15                 1
 Et3/3            Untrusted               15                 1
 Et4/0            Untrusted               15                 1
 Et4/1            Untrusted               15                 1
 Et4/2            Untrusted               15                 1
 Et4/3            Untrusted               15                 1
          
 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et5/0            Untrusted               15                 1
 Et5/1            Untrusted               15                 1
 Et5/2            Untrusted               15                 1
 Et5/3            Untrusted               15                 1
 Et6/0            Trusted               None               N/A
 Et6/1            Untrusted               15                 1
 Et6/2            Untrusted               15                 1
 Et6/3            Untrusted               15                 1
Cafe-01-SW1#


Cafe-01-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW2(config)#ip arp inspection vlan 10,20
Cafe-01-SW2(config)#ip arp inspection validate src-mac dst-mac ip
Cafe-01-SW2(config)#end
Cafe-01-SW2#sh
*Aug 18 16:05:26.465: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW2#show ip arp inspection vlan 10

Source Mac Validation      : Enabled
Destination Mac Validation : Enabled
IP Address Validation      : Enabled

 Vlan     Configuration    Operation   ACL Match          Static ACL
 ----     -------------    ---------   ---------          ----------
   10     Enabled          Inactive                       

 Vlan     ACL Logging      DHCP Logging      Probe Logging
 ----     -----------      ------------      -------------
   10     Deny             Deny              Off          
Cafe-01-SW2#show ip arp inspection vlan 20

Source Mac Validation      : Enabled
Destination Mac Validation : Enabled
IP Address Validation      : Enabled

 Vlan     Configuration    Operation   ACL Match          Static ACL
 ----     -------------    ---------   ---------          ----------
   20     Enabled          Active                         

 Vlan     ACL Logging      DHCP Logging      Probe Logging
 ----     -----------      ------------      -------------
   20     Deny             Deny              Off          
Cafe-01-SW2#show ip arp inspection interfaces

 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et0/0            Untrusted               15                 1
 Et0/1            Trusted               None               N/A
 Et0/2            Untrusted               15                 1
 Et0/3            Untrusted               15                 1
Cafe-01-SW2#



Cafe-01-SW2#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW2(config)#arp access-list DAI-PERMIT-PC
Cafe-01-SW2(config-arp-nacl)#$host 10.1.20.11 mac host 5254.0012.E08D        
Cafe-01-SW2(config-arp-nacl)#exit
Cafe-01-SW2(config)#ip arp inspection filter DAI-PERMIT-PC vlan 20
Cafe-01-SW2(config)#end
Cafe-01-SW2#
*Aug 18 16:09:14.474: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW2#show arp access-list
ARP access list DAI-PERMIT-PC
    permit ip host 10.1.20.11 mac host 5254.0012.e08d 

Cafe-01-SW2#show ip arp inspection vlan 20

Source Mac Validation      : Enabled
Destination Mac Validation : Enabled
IP Address Validation      : Enabled

 Vlan     Configuration    Operation   ACL Match          Static ACL
 ----     -------------    ---------   ---------          ----------
   20     Enabled          Active      DAI-PERMIT-PC      No 

 Vlan     ACL Logging      DHCP Logging      Probe Logging
 ----     -----------      ------------      -------------
   20     Deny             Deny              Off          
Cafe-01-SW2#


cisco@cafe-01-pc:~$ sudo arp -d 10.1.20.1
arp: SIOCDARP(pub): No such file or directory
cisco@cafe-01-pc:~$ ping -c 3 10.1.20.1
PING 10.1.20.1 (10.1.20.1): 56 data bytes
64 bytes from 10.1.20.1: seq=0 ttl=255 time=3.021 ms
64 bytes from 10.1.20.1: seq=1 ttl=255 time=1.352 ms
64 bytes from 10.1.20.1: seq=2 ttl=255 time=1.283 ms

--- 10.1.20.1 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 1.283/1.885/3.021 ms
cisco@cafe-01-pc:~$ arp -n


Cafe-01-SW2#
Cafe-01-SW2#show ip arp inspection statistics

 Vlan      Forwarded        Dropped     DHCP Drops      ACL Drops
 ----      ---------        -------     ----------      ---------
   10              0              0              0              0
   20              2              0              0              0

 Vlan   DHCP Permits    ACL Permits  Probe Permits   Source MAC Failures
 ----   ------------    -----------  -------------   -------------------
   10              0              0              0                     0
   20              0              1              0                     0

 Vlan   Dest MAC Failures   IP Validation Failures   Invalid Protocol Data
 ----   -----------------   ----------------------   ---------------------
   10                   0                        0                       0
   20                   0                        0                       0
Cafe-01-SW2#



Cafe-01-SW1#
Cafe-01-SW1#show ip arp inspection interfaces

 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et0/0            Untrusted               15                 1
 Et0/1            Trusted               None               N/A
 Et0/2            Untrusted               15                 1
 Et0/3            Untrusted               15                 1
 Et1/0            Untrusted               15                 1
 Et1/1            Untrusted               15                 1
 Et1/2            Untrusted               15                 1
 Et1/3            Untrusted               15                 1
 Et2/0            Untrusted               15                 1
 Et2/1            Untrusted               15                 1
 Et2/2            Untrusted               15                 1
 Et2/3            Untrusted               15                 1
 Et3/0            Untrusted               15                 1
 Et3/1            Untrusted               15                 1
 Et3/2            Untrusted               15                 1
 Et3/3            Untrusted               15                 1
 Et4/0            Untrusted               15                 1
 Et4/1            Untrusted               15                 1
 Et4/2            Untrusted               15                 1
 Et4/3            Untrusted               15                 1
          
 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et5/0            Untrusted               15                 1
 Et5/1            Untrusted               15                 1
 Et5/2            Untrusted               15                 1
 Et5/3            Untrusted               15                 1
 Et6/0            Trusted               None               N/A
 Et6/1            Untrusted               15                 1
 Et6/2            Untrusted               15                 1
 Et6/3            Untrusted               15                 1
Cafe-01-SW1#show ip arp inspection statisti  
*Aug 18 16:11:30.954: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-01-SW1#show ip arp inspection statistics

 Vlan      Forwarded        Dropped     DHCP Drops      ACL Drops
 ----      ---------        -------     ----------      ---------
   10              0              0              0              0
   20              2              0              0              0

 Vlan   DHCP Permits    ACL Permits  Probe Permits   Source MAC Failures
 ----   ------------    -----------  -------------   -------------------
   10              0              0              0                     0
   20              0              0              0                     0

 Vlan   Dest MAC Failures   IP Validation Failures   Invalid Protocol Data
 ----   -----------------   ----------------------   ---------------------
   10                   0                        0                       0
   20                   0                        0                       0
Cafe-01-SW1#
```
