# Lab 031 - Raw CLI Output

```bash

Fallout-SW1#show vtp   
*Jun 27 11:55:37.904: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 27 11:55:37.904: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Fallout-SW1#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : 
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0100
Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00
Local updater ID is 0.0.0.0 (no valid interface found)

Feature VLAN:
--------------
VTP Operating Mode                : Server
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 5
Configuration Revision            : 0
MD5 digest                        : 0x57 0xCD 0x40 0x65 0x63 0x59 0x47 0xBD 
                                    0x56 0x9D 0x4A 0x3E 0xA5 0x69 0x35 0xBC 
Fallout-SW1#
Fallout-SW1#
Fallout-SW1#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0   
1002 fddi  101002     1500  -      -      -        -    -        0      0   
1003 tr    101003     1500  -      -      -        -    -        0      0   
1004 fdnet 101004     1500  -      -      -        ieee -        0      0   
1005 trnet 101005     1500  -      -      -        ibm  -        0      0   

Remote SPAN VLANs
------------------------------------------------------------------------------


Primary Secondary Type              Ports
          
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
------- --------- ----------------- ------------------------------------------

Fallout-SW1#

Fallout-SW1#show interface trunk | begin Port

Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#vtp domain fallout
Changing VTP domain name from NULL to fallout
Fallout-SW1(config)#
*Jun 27 12:00:40.765: %SW_VLAN-6-VTP_DOMAIN_NAME_CHG: VTP domain name changed to fallout.
Fallout-SW1(config)#vtp mode server
Device mode already VTP Server for VLANS.
Fallout-SW1(config)#vlan 10
Fallout-SW1(config-vlan)#name MGMT-FALLOUT
Fallout-SW1(config-vlan)#vlan 20
Fallout-SW1(config-vlan)#name INTERNAL-COMMS
Fallout-SW1(config-vlan)#vlan 30
Fallout-SW1(config-vlan)#name VIDEO-SURVEILLANCE
Fallout-SW1(config-vlan)#vlan 40
Fallout-SW1(config-vlan)#name GUEST-ACCESS
Fallout-SW1(config-vlan)#end
Fallout-SW1#
*Jun 27 12:02:03.572: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW1#$rating Mode|Number of existing VLANs|Configuration Revision     
VTP Domain Name                 : fallout
VTP Operating Mode                : Server
Number of existing VLANs          : 9
Configuration Revision            : 4
Fallout-SW1#show vlan brief | include 10   |20   |30   |40
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
Fallout-SW1#

Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#int
Fallout-SW1(config)#interface eth
Fallout-SW1(config)#interface ethernet0/1
Fallout-SW1(config-if)#switchport trunk encapsulation dot1q
Fallout-SW1(config-if)#switchport mode trunk
Fallout-SW1(config-if)#
*Jun 27 12:04:32.316: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Fallout-SW1(config-if)#
*Jun 27 12:04:35.317: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Fallout-SW1(config-if)#description "Uplink to Fallout-RT1"
Fallout-SW1(config-if)#switchport trunk allowed vlan 10,20,30,40
Fallout-SW1(config-if)#exit
Fallout-SW1(config)#int
Fallout-SW1(config)#interface eth
Fallout-SW1(config)#interface ethernet0/2
Fallout-SW1(config-if)#description Link to Fallout-SW3
Fallout-SW1(config-if)#switchport trunk encapsulation dot1q
Fallout-SW1(config-if)#switchport mode trunk
Fallout-SW1(config-if)#switch
*Jun 27 12:07:25.075: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Fallout-SW1(config-if)#switchport trunk 
*Jun 27 12:07:28.074: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Fallout-SW1(config-if)#switchport trunk allowed vlan 10,20,30,40
Fallout-SW1(config-if)#exit
Fallout-SW1(config)#int eth0/3                               
Fallout-SW1(config-if)#description Link to Fallout-SW4 
Fallout-SW1(config-if)#switchport trunk encapsulation dot1q
Fallout-SW1(config-if)#switchport mode trunk
Fallout-SW1(config-if)#switch
*Jun 27 12:09:06.371: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down
Fallout-SW1(config-if)#switchport tr
*Jun 27 12:09:09.371: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to up
Fallout-SW1(config-if)#switchport trunk allowed vlan 10,20,30,40
Fallout-SW1(config-if)#exit
Fallout-SW1(config)#int eth1/0
Fallout-SW1(config-if)#description Link to Fallout-SW5
Fallout-SW1(config-if)#switchport trunk encapsulation dot1q
Fallout-SW1(config-if)#switchport mode trunk
Fallout-SW1(config-if)#switchp
*Jun 27 12:10:12.073: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to down
Fallout-SW1(config-if)#switchport tru
*Jun 27 12:10:15.073: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to up
Fallout-SW1(config-if)#switchport trunk allowed
*Jun 27 12:10:17.494: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/0 TDR=0, TRC=0
Fallout-SW1(config-if)#switchport trunk allowed vlan 10,20,30,40
Fallout-SW1(config-if)#end
Fallout-SW1#
Fallout-SW1#
*Jun 27 12:10:30.738: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW1#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1
Et0/3          on               802.1q         trunking      1
Et1/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20,30,40
Et0/2          10,20,30,40
Et0/3          10,20,30,40
Et1/0          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40
Et0/2          10,20,30,40
Et0/3          10,20,30,40
Et1/0          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40
Et0/2          10,20,30,40
Et0/3          10,20,30,40
Et1/0          10,20,30,40
Fallout-SW1#


Fallout-SW3>en
Fallout-SW3#
*Jun 27 12:12:01.162: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jun 27 12:12:01.265: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 27 12:12:01.265: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 27 12:12:01.375: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Fallout-SW3#
*Jun 27 12:12:01.475: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jun 27 12:12:01.475: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Fallout-SW3#$rating Mode|Number of existing VLANs|Configuration Revision     
VTP Domain Name                 : fallout
VTP Operating Mode                : Server
Number of existing VLANs          : 9
Configuration Revision            : 4
Fallout-SW3#
Fallout-SW3#show vlan brief | include 10  |20  |30  |40
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
Fallout-SW3#
Fallout-SW3#
Fallout-SW3#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          auto             n-802.1q       trunking      1

Port           Vlans allowed on trunk
Et0/1          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20,30,40
Fallout-SW3#



Fallout-SW4#show vlan brief | include 10  |20  |30  |40
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
Fallout-SW4#show interface tru
*Jun 27 12:25:44.849: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
Fallout-SW4#show interface trunk | begin port
Fallout-SW4#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          auto             n-802.1q       trunking      1

Port           Vlans allowed on trunk
Et0/1          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20,30,40
Fallout-SW4#


Fallout-SW5#show vlan brief | include 10  |20  |30  |40            
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
Fallout-SW5#
Fallout-SW5#
Fallout-SW5#show interface trunl | begin Port
                               ^
% Invalid input detected at '^' marker.

Fallout-SW5#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          auto             n-802.1q       trunking      1

Port           Vlans allowed on trunk
Et0/1          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20,30,40
Fallout-SW5#

Connecting to console for Fallout-SW3

Fallout-SW3>en
Fallout-SW3#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW3(config)#int eth0/3
Fallout-SW3(config-if)#description MGMT-CONSOLE
Fallout-SW3(config-if)#switchport mode access
Fallout-SW3(config-if)#switchport access vlan 10
Fallout-SW3(config-if)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet0/3 but will only
 have effect when the interface is in a non-trunking mode.
Fallout-SW3(config-if)#end
Fallout-SW3#sh
*Jun 27 12:29:29.510: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW3#show vlan brief | include 10  |et0/3
10   MGMT-FALLOUT                     active    Et0/3
Fallout-SW3#


Fallout-SW4#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW4(config)#int et
*Jun 27 12:30:14.718: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
Fallout-SW4(config)#int eth0/3
Fallout-SW4(config-if)#description VIDEO-NVR
Fallout-SW4(config-if)#description INTERNAL-
*Jun 27 12:30:44.897: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
Fallout-SW4(config-if)#description INTERNAL-WORKSTATION
Fallout-SW4(config-if)#switchport mode access
Fallout-SW4(config-if)#switchport access vlan 20
Fallout-SW4(config-if)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet0/3 but will only
 have effect when the interface is in a non-trunking mode.
Fallout-SW4(config-if)#end
Fallout-SW4#sho
*Jun 27 12:31:22.307: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW4#show vlan brief | include 20  |et0/3
20   INTERNAL-COMMS                   active    Et0/3
Fallout-SW4#

Fallout-SW5#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW5(config)#int eth0/3
Fallout-SW5(config-if)#description VIDEO-NVR
Fallout-SW5(config-if)#switchport mode access
Fallout-SW5(config-if)#switchport access vlan 30
Fallout-SW5(config-if)#spannning-tree portfast
                            ^
% Invalid input detected at '^' marker.

Fallout-SW5(config-if)#end
Fallout-SW5#
*Jun 27 12:33:00.344: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW5#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW5(config)#int eth0/3               
Fallout-SW5(config-if)#spanning-tree portfast 
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet0/3 but will only
 have effect when the interface is in a non-trunking mode.
Fallout-SW5(config-if)#end                   
Fallout-SW5#
*Jun 27 12:33:35.343: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW5#
Fallout-SW5#
Fallout-SW5#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW5(config)#int eth1/1
Fallout-SW5(config-if)#description GUEST-KIOSK
Fallout-SW5(config-if)#switchport mode access
Fallout-SW5(config-if)#switchport access vlan 40
Fallout-SW5(config-if)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet1/1 but will only
 have effect when the interface is in a non-trunking mode.
Fallout-SW5(config-if)#end
Fallout-SW5#
*Jun 27 12:34:41.134: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW5#show vlan brief | include 30  |40  |et0/3|et1/1
30   VIDEO-SURVEILLANCE               active    Et0/3
40   GUEST-ACCESS                     active    Et1/1
Fallout-SW5#


*Jun 27 12:36:24.151: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Fallout-RT1>en
Fallout-RT1#terminal length 0
Fallout-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-RT1(config)#int
Fallout-RT1(config)#interface eth
Fallout-RT1(config)#interface ethernet0/0
Fallout-RT1(config-if)#mo shutdown
                           ^
% Invalid input detected at '^' marker.

Fallout-RT1(config-if)#no shutdown
Fallout-RT1(config-if)#ex
*Jun 27 12:39:39.720: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Fallout-RT1(config-if)#exit
Fallout-RT1(config)#
*Jun 27 12:39:40.720: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Fallout-RT1(config)#int
Fallout-RT1(config)#interface eth
Fallout-RT1(config)#interface ethernet0/0.10
Fallout-RT1(config-subif)#encapsulation dot1q 10
Fallout-RT1(config-subif)#ip address 10.0.16.1 255.255.255.128
Fallout-RT1(config-subif)#exit
Fallout-RT1(config)#interface ethernet0/0.20            
Fallout-RT1(config-subif)#encapsulation dot1q 10              

%Configuration of multiple subinterfaces of the same main
interface with the same VID (10) is not permitted.
This VID is already configured on Ethernet0/0.10.

Fallout-RT1(config-subif)#encapsulation dot1q 20  
Fallout-RT1(config-subif)#ip address 10.0.16.129 255.255.255.128
Fallout-RT1(config-subif)#exit
Fallout-RT1(config)#interface ethernet0/0.30              
Fallout-RT1(config-subif)#encapsulation dot1q 30                
Fallout-RT1(config-subif)#ip address 10.0.17.1 255.255.255.128  
Fallout-RT1(config-subif)#exit
Fallout-RT1(config)#interface ethernet0/0.40            
Fallout-RT1(config-subif)#encapsulation dot1q 40              
Fallout-RT1(config-subif)#ip address 10.0.17.129 255.255.255.128
Fallout-RT1(config-subif)#exit
Fallout-RT1(config)#ip dhcp pool MGMT
Fallout-RT1(dhcp-config)#network 10.0.16.0 255.255.255.128
Fallout-RT1(dhcp-config)#default-router 10.0.16.1
Fallout-RT1(dhcp-config)#dns-server 1.1.1.1
Fallout-RT1(dhcp-config)#domain-name fallout.local
Fallout-RT1(dhcp-config)#exit
Fallout-RT1(config)#ip dhcp pool INTERNAL            
Fallout-RT1(dhcp-config)#network 10.0.16.128 255.255.255.128
Fallout-RT1(dhcp-config)#default-router 10.0.16.129         
Fallout-RT1(dhcp-config)#dns-server 1.1.1.1                 
Fallout-RT1(dhcp-config)#domain-name fallout.local          
Fallout-RT1(dhcp-config)#exit                               
Fallout-RT1(config)#ip dhcp pool VIDEO                 
Fallout-RT1(dhcp-config)#network 10.0.17.0 255.255.255.128  
Fallout-RT1(dhcp-config)#default-router 10.0.17.1         
Fallout-RT1(dhcp-config)#dns-server 1.1.1.1               
Fallout-RT1(dhcp-config)#domain-name fallout.local          
Fallout-RT1(dhcp-config)#exit                             
Fallout-RT1(config)#ip dhcp pool GUEST               
Fallout-RT1(dhcp-config)#network 10.0.17.128 255.255.255.128
Fallout-RT1(dhcp-config)#default-router 10.0.17.129         
Fallout-RT1(dhcp-config)#dns-server 1.1.1.1                 
Fallout-RT1(dhcp-config)#domain-name fallout.local          
Fallout-RT1(dhcp-config)#end                                
Fallout-RT1#
*Jun 27 12:46:34.679: %SYS-5-CONFIG_I: Configured from console by console
Fallout-RT1#
Fallout-RT1#
Fallout-RT1#show ip interface brief | include eth0/0
Fallout-RT1#show running-config | section ip dhcp pool
ip dhcp pool MGMT
 network 10.0.16.0 255.255.255.128
 default-router 10.0.16.1 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool INTERNAL
 network 10.0.16.128 255.255.255.128
 default-router 10.0.16.129 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool VIDEO
 network 10.0.17.0 255.255.255.128
 default-router 10.0.17.1 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool GUEST
 network 10.0.17.128 255.255.255.128
 default-router 10.0.17.129 
 dns-server 1.1.1.1 
 domain-name fallout.local
Fallout-RT1#
Fallout-RT1#
Fallout-RT1#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address      Client-ID/              Lease expiration        Type       State      Interface
                Hardware address/
                User name
Fallout-RT1#


Fallout-SW1>en
Fallout-SW1#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : fallout
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0100
Configuration last modified by 0.0.0.0 at 6-27-26 12:02:03
Local updater ID is 0.0.0.0 (no valid interface found)

Feature VLAN:
--------------
VTP Operating Mode                : Server
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 9
Configuration Revision            : 4
MD5 digest                        : 0x62 0x66 0x3B 0xE1 0xB1 0x22 0xBD 0x5D 
                                    0x29 0x0B 0x0D 0x8D 0x32 0xEC 0xEB 0x44 
Fallout-SW1#
*Jun 27 12:49:28.754: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/0 TDR=0, TRC=0
Fallout-SW1#

Fallout-SW1#
Fallout-SW1#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1
Et0/3          on               802.1q         trunking      1
Et1/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20,30,40
Et0/2          10,20,30,40
Et0/3          10,20,30,40
Et1/0          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40
Et0/2          10,20,30,40
Et0/3          10,20,30,40
Et1/0          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40
Et0/2          10,20,30,40
Et0/3          10,20,30,40
Et1/0          10,20,30,40
Fallout-SW1#
*Jun 27 12:50:36.766: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/0 TDR=0, TRC=0
Fallout-SW1#

```
