# Lab 032 - Raw CLI Output

```bash


Shelter-SW1#show vlan 

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
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


          
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
Primary Secondary Type              Ports
------- --------- ----------------- ------------------------------------------

Shelter-SW1#
*Jun 27 14:03:22.931: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/1 TDR=0, TRC=0
Shelter-SW1#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : 
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0200
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
Shelter-SW1#

Shelter-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW1(config)#vtp domain
*Jun 27 14:04:12.076: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Shelter-SW1(config)#vtp domain
*Jun 27 14:04:12.179: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 27 14:04:12.180: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 27 14:04:12.287: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Shelter-SW1(config)#vtp domain
*Jun 27 14:04:12.387: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 27 14:04:12.387: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Shelter-SW1(config)#vtp domain FALLOUT
Changing VTP domain name from NULL to FALLOUT
Shelter-SW1(config)#
*Jun 27 14:04:19.944: %SW_VLAN-6-VTP_DOMAIN_NAME_CHG: VTP domain name changed to FALLOUT.
Shelter-SW1(config)#vlan 10
Shelter-SW1(config-vlan)#name MGMT-FALLOUT
Shelter-SW1(config-vlan)#exit
Shelter-SW1(config)#vlan 20
Shelter-SW1(config-vlan)#name INTERNAL-COMMS
Shelter-SW1(config-vlan)#exit
Shelter-SW1(config)#vlan 30
Shelter-SW1(config-vlan)#name VIDEO-SURVEILLANCE
Shelter-SW1(config-vlan)#exit
Shelter-SW1(config)#vlan 40
Shelter-SW1(config-vlan)#name GUEST-ACCESS
Shelter-SW1(config-vlan)#exit
Shelter-SW1(config)#vlan 99
Shelter-SW1(config-vlan)#
*Jun 27 14:05:52.282: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/1 TDR=0, TRC=0
Shelter-SW1(config-vlan)#name MGMT-NATIVE
*Jun 27 14:06:22.358: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/1 TDR=0, TRC=0
Shelter-SW1(config-vlan)#name MGMT-NATIVE
Shelter-SW1(config-vlan)#exit
Shelter-SW1(config)#vtp mode ?
  client       Set the device to client mode.
  off          Set the device to off mode.
  server       Set the device to server mode.
  transparent  Set the device to transparent mode.

Shelter-SW1(config)#vtp mode transparent
Setting device to VTP Transparent mode for VLANS.
Shelter-SW1(config)#

Shelter-SW1#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
99   MGMT-NATIVE                      active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0   
10   enet  100010     1500  -      -      -        -    -        0      0   
20   enet  100020     1500  -      -      -        -    -        0      0   
30   enet  100030     1500  -      -      -        -    -        0      0   
40   enet  100040     1500  -      -      -        -    -        0      0   
          
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
99   enet  100099     1500  -      -      -        -    -        0      0   
1002 fddi  101002     1500  -      -      -        -    -        0      0   
1003 tr    101003     1500  -      -      -        -    -        0      0   
1004 fdnet 101004     1500  -      -      -        ieee -        0      0   
1005 trnet 101005     1500  -      -      -        ibm  -        0      0   

Remote SPAN VLANs
------------------------------------------------------------------------------


Primary Secondary Type              Ports
------- --------- ----------------- ------------------------------------------

Shelter-SW1#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : FALLOUT
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0200
Configuration last modified by 0.0.0.0 at 6-27-26 14:06:37

Feature VLAN:
--------------
VTP Operating Mode                : Transparent
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 10
Configuration Revision            : 0
MD5 digest                        : 0x70 0x46 0xE4 0xD9 0x68 0x3F 0xEA 0x2E 
                                    0xA7 0x16 0xA9 0xA9 0x88 0xEB 0x38 0x4F 
Shelter-SW1#


Shelter-SW2#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
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
------- --------- ----------------- ------------------------------------------
          
Shelter-SW2#
Shelter-SW2#
Shelter-SW2#show vtp status
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
Shelter-SW2#

Shelter-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW2(config)#vtp domain FALLOUT
Changing VTP domain name from NULL to FALLOUT
Shelter-SW2(config)#
*Jun 27 14:10:01.336: %SW_VLAN-6-VTP_DOMAIN_NAME_CHG: VTP domain name changed to FALLOUT.
Shelter-SW2(config)#vlan 10
Shelter-SW2(config-vlan)#name MGMT-FALLOUT
Shelter-SW2(config-vlan)#exit
Shelter-SW2(config)#vlan 20
Shelter-SW2(config-vlan)#name INTERNAL-COMMS
Shelter-SW2(config-vlan)#exit
Shelter-SW2(config)#vlan 30
Shelter-SW2(config-vlan)#name VIDEO-SURVEILLANCE
Shelter-SW2(config-vlan)#exit
Shelter-SW2(config)#vlan 40
Shelter-SW2(config-vlan)#name GUEST-ACCESS
Shelter-SW2(config-vlan)#exit
Shelter-SW2(config)#vlan 99
Shelter-SW2(config-vlan)#name MGMT-NATIVE
Shelter-SW2(config-vlan)#end
Shelter-SW2#
*Jun 27 14:11:40.078: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW2#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
99   MGMT-NATIVE                      active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0   
10   enet  100010     1500  -      -      -        -    -        0      0   
20   enet  100020     1500  -      -      -        -    -        0      0   
30   enet  100030     1500  -      -      -        -    -        0      0   
40   enet  100040     1500  -      -      -        -    -        0      0   
99   enet  100099     1500  -      -      -        -    -        0      0   
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

Shelter-SW2#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : FALLOUT
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0100
Configuration last modified by 0.0.0.0 at 6-27-26 14:11:40
Local updater ID is 0.0.0.0 (no valid interface found)

Feature VLAN:
--------------
VTP Operating Mode                : Server
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 10
Configuration Revision            : 5
MD5 digest                        : 0x70 0x46 0xE4 0xD9 0x68 0x3F 0xEA 0x2E 
                                    0xA7 0x16 0xA9 0xA9 0x88 0xEB 0x38 0x4F 
Shelter-SW2#

Shelter-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW2(config)#vtp mode transparent
Setting device to VTP Transparent mode for VLANS.
Shelter-SW2(config)#exit
Shelter-SW2#
*Jun 27 14:13:10.082: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW2#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : FALLOUT
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0100
Configuration last modified by 0.0.0.0 at 6-27-26 14:11:40

Feature VLAN:
--------------
VTP Operating Mode                : Transparent
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 10
Configuration Revision            : 0
MD5 digest                        : 0x70 0x46 0xE4 0xD9 0x68 0x3F 0xEA 0x2E 
                                    0xA7 0x16 0xA9 0xA9 0x88 0xEB 0x38 0x4F 
Shelter-SW2#

Shelter-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW1(config)#int eth0/1
Shelter-SW1(config-if)#
*Jun 27 14:14:23.018: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/1 TDR=0, TRC=0
Shelter-SW1(config-if)#
*Jun 27 14:16:53.043: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/1 TDR=0, TRC=0
Shelter-SW1(config-if)#description Trunk-to-Shelter-SW2
Shelter-SW1(config-if)#switchport trunk encapsulation dot1q
Shelter-SW1(config-if)#switchport mode trunk
Shelter-SW1(config-if)#
*Jun 27 14:17:39.900: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Shelter-SW1(config-if)#switch
*Jun 27 14:17:41.908: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Shelter-SW1(config-if)#switchport 
*Jun 27 14:17:42.901: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Shelter-SW1(config-if)#switchport trunk native vlan 99
Shelter-SW1(config-if)#switchpo
*Jun 27 14:17:53.055: %SPANTREE-2-BLOCK_PVID_PEER: Blocking Ethernet0/1 on VLAN0001. Inconsistent peer vlan.
*Jun 27 14:17:53.055: %SPANTREE-2-BLOCK_PVID_LOCAL: Blocking Ethernet0/1 on VLAN0099. Inconsistent local vlan.
Shelter-SW1(config-if)#switchport trunk allowed vlan 10,20,30,40,99
Shelter-SW1(config-if)#switchport nonegotiate
*Jun 27 14:18:22.118: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/1 TDR=0, TRC=0
Shelter-SW1(config-if)#switchport nonegotiate
Shelter-SW1(config-if)#no shutdown
Shelter-SW1(config-if)#end
Shelter-SW1#
*Jun 27 14:18:31.346: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW1#
Shelter-SW1#show interface tru
*Jun 27 14:18:50.637: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (99), with Shelter-SW2 Ethernet0/1 (1).
Shelter-SW1#show interface trunk | include eth0/1
Shelter-SW1#show interface trunk                 

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          10,20,30,40,99

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40
Shelter-SW1#
*Jun 27 14:19:22.914: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/2 TDR=0, TRC=0
Shelter-SW1#

Shelter-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW2(config)#int
Shelter-SW2(config)#interface eth
Shelter-SW2(config)#interface ethernet
*Jun 27 14:20:22.148: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (1), with Shelter-SW1 Ethernet0/1 (99).
Shelter-SW2(config)#interface ethernet0/1
Shelter-SW2(config-if)#description Trunk-to-Shelter
*Jun 27 14:20:41.126: %AMDP2_FE-6-EXCESSCOLL: Ethernet2/3 TDR=0, TRC=0
Shelter-SW2(config-if)#description Trunk-to-Shelter-SW1
Shelter-SW2(config-if)#switchport trunk encapsulation dot1q
Shelter-SW2(config-if)#switchport mode trunk
Shelter-SW2(config-if)#switchport trunk
*Jun 27 14:21:16.983: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (1), with Shelter-SW1 Ethernet0/1 (99).
Shelter-SW2(config-if)#switchport trunk native vlan 99
Shelter-SW2(config-if)#switchport trunk allowed vlan 10,20,30,40,
*Jun 27 14:21:35.177: %AMDP2_FE-6-EXCESSCOLL: Ethernet2/3 TDR=0, TRC=0
Shelter-SW2(config-if)#switchport trunk allowed vlan 10,20,30,40,99
Shelter-SW2(config-if)#
*Jun 27 14:21:37.919: %SPANTREE-2-UNBLOCK_CONSIST_PORT: Unblocking Ethernet0/1 on VLAN0099. Port consistency restored.
*Jun 27 14:21:37.919: %SPANTREE-2-UNBLOCK_CONSIST_PORT: Unblocking Ethernet0/1 on VLAN0001. Port consistency restored.
Shelter-SW2(config-if)#switchport nonegotiate
Shelter-SW2(config-if)#no shutdown 
Shelter-SW2(config-if)#end
Shelter-SW2#
*Jun 27 14:22:06.162: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW2#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          10,20,30,40,99

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40,99
Shelter-SW2#

Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW1(config)#int
Shelter-SW1(config)#interface eth
Shelter-SW1(config)#interface ethernet0/0
Shelter-SW1(config-if)#description Trunk-to-Shelter-RT1
Shelter-SW1(config-if)#switchport trunk encapsulation
% Incomplete command.

Shelter-SW1(config-if)#switchport mode trunk
Command rejected: An interface whose trunk encapsulation is "Auto" can not be configured to "trunk" mode.
Shelter-SW1(config-if)#switchport trunk native 
*Jun 27 14:23:52.256: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/1 TDR=0, TRC=0
Shelter-SW1(config-if)#switchport trunk native vlan 99
Shelter-SW1(config-if)#switchport trunk allowed vlan 10,20,30,40,99
Shelter-SW1(config-if)#switchport nonegotiate
Command rejected: Conflict between 'nonegotiate' and 'dynamic' status on this interface: Et0/0
Shelter-SW1(config-if)#no shutdown
Shelter-SW1(config-if)#end
Shelter-SW1#
*Jun 27 14:24:34.569: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW1#show interaface trunk
                      ^
% Invalid input detected at '^' marker.

Shelter-SW1#show interface trunk 

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          10,20,30,40,99

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40,99
Shelter-SW1#

Shelter-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW2(config)#int
Shelter-SW2(config)#interface eth
Shelter-SW2(config)#interface ethernet0/4
                                        ^
% Invalid input detected at '^' marker.

Shelter-SW2(config)#interface ethernet1/0
Shelter-SW2(config-if)#description Trunk to Shelter Access Point
Shelter-SW2(config-if)#switchport trunk encapsulation dot1q
Shelter-SW2(config-if)#switchport mode trunk
Shelter-SW2(config-if)#switchpo
*Jun 27 14:29:18.000: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to down
Shelter-SW2(config-if)#switchport 
*Jun 27 14:29:21.001: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to up
Shelter-SW2(config-if)#switchport trunk native vlan 99
Shelter-SW2(config-if)#switchport trunk allowed vlan 10,210
*Jun 27 14:29:50.285: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/0 TDR=0, TRC=0
Shelter-SW2(config-if)#switchport trunk allowed vlan 10,20 
Shelter-SW2(config-if)#switchport nonegotiate
Shelter-SW2(config-if)#no shutdown
Shelter-SW2(config-if)#end
Shelter-SW2#sh
*Jun 27 14:30:19.261: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW2#show trunk
                   ^
% Invalid input detected at '^' marker.

Shelter-SW2#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99
Et1/0          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          10,20,30,40,99
Et1/0          10,20

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40,99
Et1/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40,99
Et1/0          10,20
Shelter-SW2#

Shelter-SW2#show dtp
Global DTP information
        Sending DTP Hello packets every 30 seconds
        Dynamic Trunk timeout is 300 seconds
        12 interfaces using DTP
Shelter-SW2#show interfaces ethernet0/1 switchport
Name: Et0/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (MGMT-NATIVE)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 10,20,30,40,99
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
          
Shelter-SW2#how interfaces ethernet1/0 switchport
             ^
% Invalid input detected at '^' marker.

Shelter-SW2#show interfaces ethernet1/0 switchport
Name: Et1/0
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (MGMT-NATIVE)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 10,20
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Protected: false
Appliance trust: none
Shelter-SW2#

Shelter-SW1#show interfaces ethernet0/0 switchport
Name: Et0/0
Switchport: Enabled
Administrative Mode: dynamic auto
Operational Mode: static access
Administrative Trunking Encapsulation: negotiate
Operational Trunking Encapsulation: native
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (MGMT-NATIVE)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 10,20,30,40,99
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
          
Shelter-SW1#show interfaces ethernet0/1 switchport
Name: Et0/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (MGMT-NATIVE)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 10,20,30,40,99
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
          
Shelter-SW1#  

Shelter-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-RT1(config)#int
Shelter-RT1(config)#interface eth
Shelter-RT1(config)#interface ethernet0/0
Shelter-RT1(config-if)#description Trunk to Shelter-SW1
Shelter-RT1(config-if)#no ip address
Shelter-RT1(config-if)#no shutdown
Shelter-RT1(config-if)#interface eth
Shelter-RT1(config-if)#interface eth0/0.10
Shelter-RT1(config-subif)#description Gateway fpr VLAN 10
Shelter-RT1(config-subif)#encapsulation dot1q 10
Shelter-RT1(config-subif)#ip address 10.0.16.1 255.255.255.128
Shelter-RT1(config-subif)#int
Shelter-RT1(config-subif)#inteth
Shelter-RT1(config-subif)#inteth0/0.20
                           ^
% Invalid input detected at '^' marker.

Shelter-RT1(config-subif)#int
Shelter-RT1(config-subif)#intexit
                           ^
% Invalid input detected at '^' marker.

Shelter-RT1(config-subif)#exit
Shelter-RT1(config)#int
Shelter-RT1(config)#interface eth
Shelter-RT1(config)#interface ethernet0/0.20
Shelter-RT1(config-subif)#description Gateway fpr VLAN 20     
Shelter-RT1(config-subif)#encapsulation dot1q 10              

%Configuration of multiple subinterfaces of the same main
interface with the same VID (10) is not permitted.
This VID is already configured on Ethernet0/0.10.

Shelter-RT1(config-subif)#encapsulation dot1q 20
Shelter-RT1(config-subif)#ip address 10.0.16.129 255.255.255.128
Shelter-RT1(config-subif)#exit                                  
Shelter-RT1(config)#interface ethernet0/0.30              
Shelter-RT1(config-subif)#description Gateway fpr VLAN 30       
Shelter-RT1(config-subif)#encapsulation dot1q 30                
Shelter-RT1(config-subif)#ip address 10.0.17.1 255.255.255.128  
Shelter-RT1(config-subif)#exit                                  
Shelter-RT1(config)#interface ethernet0/0.40            
Shelter-RT1(config-subif)#description Gateway fpr VLAN 40     
Shelter-RT1(config-subif)#encapsulation dot1q 40              
Shelter-RT1(config-subif)#ip address 10.0.17.129 255.255.255.128
Shelter-RT1(config-subif)#exit
Shelter-RT1(config)#interface ethernet0/0.99              
Shelter-RT1(config-subif)#description native management gateway for VLAN 99
Shelter-RT1(config-subif)#encapsulation dot1q 99 native                    
Shelter-RT1(config-subif)#ip address 10.0.99.1 255.255.255.224             
Shelter-RT1(config-subif)#end
Shelter-RT1#
*Jun 27 14:44:59.786: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-RT1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-RT1(config)#ip dhcp excluded-address 10.0.16.1
Shelter-RT1(config)#ip dhcp excluded-address 10.0.16.129
Shelter-RT1(config)#ip dhcp excluded-address 10.0.17.129
Shelter-RT1(config)#ip dhcp excluded-address 10.0.17.1  
Shelter-RT1(config)#ip dhcp excluded-address 10.0.99.1
Shelter-RT1(config)#ip dhcp pool MGMT
Shelter-RT1(dhcp-config)#network 10.0.16.0 255.255.255.128
Shelter-RT1(dhcp-config)#default-router 10.0.16.1
Shelter-RT1(dhcp-config)#dns-server 1.1.1.1
Shelter-RT1(dhcp-config)#domain-name fallout.local
Shelter-RT1(dhcp-config)#ip dhcp pool INTERNAL             
Shelter-RT1(dhcp-config)#network 10.0.16.128 255.255.255.128
Shelter-RT1(dhcp-config)#default-router 10.0.16.129         
Shelter-RT1(dhcp-config)#dns-server 1.1.1.1                 
Shelter-RT1(dhcp-config)#domain-name fallout.local          
Shelter-RT1(dhcp-config)#ip dhcp pool VIDEO                 
Shelter-RT1(dhcp-config)#network 10.0.17.1 255.255.255.128  
Shelter-RT1(dhcp-config)#dns-server 1.1.1.1               
Shelter-RT1(dhcp-config)#domain-name fallout.local        
Shelter-RT1(dhcp-config)#ip dhcp pool GUEST               
Shelter-RT1(dhcp-config)#network 10.0.17.128 255.255.255.128
Shelter-RT1(dhcp-config)#default-router 10.0.17.129         
Shelter-RT1(dhcp-config)#dns-server 1.1.1.1                 
Shelter-RT1(dhcp-config)#domain-name fallout.local          
Shelter-RT1(dhcp-config)#ip dhcp pool MGMT-NATIVE           
Shelter-RT1(dhcp-config)#network 10.0.99.0 255.255.255.224  
Shelter-RT1(dhcp-config)#default-router 10.0.99.1         
Shelter-RT1(dhcp-config)#dns-server 1.1.1.1               
Shelter-RT1(dhcp-config)#domain-name fallout.local        
Shelter-RT1(dhcp-config)#no ip dhcp pool VIDEO
Shelter-RT1(config)#
Shelter-RT1(config)#ip dhcp pool VIDEO
Shelter-RT1(dhcp-config)# network 10.0.17.0 255.255.255.128
Shelter-RT1(dhcp-config)# default-router 10.0.17.1
Shelter-RT1(dhcp-config)# dns-server 1.1.1.1
Shelter-RT1(dhcp-config)# domain-name fallout.local
Shelter-RT1(dhcp-config)#
Shelter-RT1(dhcp-config)#end                       
Shelter-RT1#
*Jun 27 14:56:28.631: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-RT1#show running-config | section ip dhcp pool
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
ip dhcp pool GUEST
 network 10.0.17.128 255.255.255.128
 default-router 10.0.17.129 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool MGMT-NATIVE
 network 10.0.99.0 255.255.255.224
 default-router 10.0.99.1 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool VIDEO
 network 10.0.17.0 255.255.255.128
 default-router 10.0.17.1 
Shelter-RT1#show ip dhcp pool

Pool MGMT :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.16.1            10.0.16.1        - 10.0.16.126       0     / 1     / 126  

Pool INTERNAL :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.16.129          10.0.16.129      - 10.0.16.254       0     / 1     / 126  

Pool GUEST :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.17.129          10.0.17.129      - 10.0.17.254       0     / 1     / 126  

Pool MGMT-NATIVE :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 30
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.99.1            10.0.99.1        - 10.0.99.30        0     / 1     / 30   

Pool VIDEO :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.17.1            10.0.17.1        - 10.0.17.126       0     / 1     / 126  
Shelter-RT1#

Shelter-RT1#show running-config | section ip dhcp pool
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
ip dhcp pool GUEST
 network 10.0.17.128 255.255.255.128
 default-router 10.0.17.129 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool MGMT-NATIVE
 network 10.0.99.0 255.255.255.224
 default-router 10.0.99.1 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool VIDEO
 network 10.0.17.0 255.255.255.128
 default-router 10.0.17.1 
Shelter-RT1#show ip dhcp pool

Pool MGMT :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.16.1            10.0.16.1        - 10.0.16.126       0     / 1     / 126  

Pool INTERNAL :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.16.129          10.0.16.129      - 10.0.16.254       0     / 1     / 126  

Pool GUEST :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.17.129          10.0.17.129      - 10.0.17.254       0     / 1     / 126  

Pool MGMT-NATIVE :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 30
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.99.1            10.0.99.1        - 10.0.99.30        0     / 1     / 30   

Pool VIDEO :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.17.1            10.0.17.1        - 10.0.17.126       0     / 1     / 126  
Shelter-RT1#
Shelter-RT1#
Shelter-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.16.1       YES manual up                    up      
Ethernet0/0.20         10.0.16.129     YES manual up                    up      
Ethernet0/0.30         10.0.17.1       YES manual up                    up      
Ethernet0/0.40         10.0.17.129     YES manual up                    up      
Ethernet0/0.99         10.0.99.1       YES manual up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Shelter-RT1#show running-config | section interface Ethernet0/0
interface Ethernet0/0
 description Trunk to Shelter-SW1
 no ip address
interface Ethernet0/0.10
 description Gateway fpr VLAN 10
 encapsulation dot1Q 10
 ip address 10.0.16.1 255.255.255.128
interface Ethernet0/0.20
 description Gateway fpr VLAN 20
 encapsulation dot1Q 20
 ip address 10.0.16.129 255.255.255.128
interface Ethernet0/0.30
 description Gateway fpr VLAN 30
 encapsulation dot1Q 30
 ip address 10.0.17.1 255.255.255.128
interface Ethernet0/0.40
 description Gateway fpr VLAN 40
 encapsulation dot1Q 40
 ip address 10.0.17.129 255.255.255.128
interface Ethernet0/0.99
 description native management gateway for VLAN 99
 encapsulation dot1Q 99 native
 ip address 10.0.99.1 255.255.255.224
Shelter-RT1#how running-config | section ip dhcp pool
             ^
% Invalid input detected at '^' marker.

Shelter-RT1#show running-config | section ip dhcp pool
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
ip dhcp pool GUEST
 network 10.0.17.128 255.255.255.128
 default-router 10.0.17.129 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool MGMT-NATIVE
 network 10.0.99.0 255.255.255.224
 default-router 10.0.99.1 
 dns-server 1.1.1.1 
 domain-name fallout.local
ip dhcp pool VIDEO
 network 10.0.17.0 255.255.255.128
 default-router 10.0.17.1 
 dns-server 1.1.1.1 
 domain-name fallout.local
Shelter-RT1#show ip dhcp pool                                  

Pool MGMT :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.16.1            10.0.16.1        - 10.0.16.126       0     / 1     / 126  

Pool INTERNAL :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.16.129          10.0.16.129      - 10.0.16.254       0     / 1     / 126  

Pool GUEST :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.17.129          10.0.17.129      - 10.0.17.254       0     / 1     / 126  

Pool MGMT-NATIVE :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 30
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.99.1            10.0.99.1        - 10.0.99.30        0     / 1     / 30   

Pool VIDEO :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 0
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.17.1            10.0.17.1        - 10.0.17.126       0     / 1     / 126  
Shelter-RT1#

Shelter-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW2(config)#int
Shelter-SW2(config)#interface eth
Shelter-SW2(config)#interface ethernet0/2
Shelter-SW2(config-if)#description Shelter-Admin1 - vlan 10
Shelter-SW2(config-if)#switchport mode access
Shelter-SW2(config-if)#switchport access vlan 10
Shelter-SW2(config-if)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet0/2 but will only
 have effect when the interface is in a non-trunking mode.
Shelter-SW2(config-if)#no shutdown
Shelter-SW2(config-if)#interface ethernet0/3
Shelter-SW2(config-if)#description Shelter-Patron1 - VLAN 20
Shelter-SW2(config-if)#switchport mode access 
Shelter-SW2(config-if)#switchport access vlan 20
Shelter-SW2(config-if)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet0/3 but will only
 have effect when the interface is in a non-trunking mode.
Shelter-SW2(config-if)#no shutdown
Shelter-SW2(config-if)#end
Shelter-SW2#
*Jun 27 15:05:45.406: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW2#

Shelter-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW1(config)#interface ethernet0/5
                                        ^
% Invalid input detected at '^' marker.

Shelter-SW1(config)#
Shelter-SW1(config)#exit
Shelter-SW1#s
*Jun 27 15:09:28.273: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Ethernet1/0            unassigned      YES unset  up                    up      
Ethernet1/1            unassigned      YES unset  up                    up      
Ethernet1/2            unassigned      YES unset  up                    up      
Ethernet1/3            unassigned      YES unset  up                    up      
Ethernet2/0            unassigned      YES unset  up                    up      
Ethernet2/1            unassigned      YES unset  up                    up      
Ethernet2/2            unassigned      YES unset  up                    up      
Ethernet2/3            unassigned      YES unset  up                    up      
Shelter-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW1(config)#int
Shelter-SW1(config)#interface eth
Shelter-SW1(config)#interface ethernet0/2
Shelter-SW1(config-if)#description Virtualisation management uplink - VLAN 99
Shelter-SW1(config-if)#switchport mode access
Shelter-SW1(config-if)#switchport access vlan 99
Shelter-SW1(config-if)#spannning-tree portfast
                            ^
% Invalid input detected at '^' marker.

Shelter-SW1(config-if)#no shutdown
Shelter-SW1(config-if)#
*Jun 27 15:11:34.400: %LINK-3-UPDOWN: Interface Ethernet0/2, changed state to up
Shelter-SW1(config-if)#no shutdown
*Jun 27 15:11:35.401: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Shelter-SW1(config-if)#spanning-tree portfast 
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet0/2 but will only
 have effect when the interface is in a non-trunking mode.
Shelter-SW1(config-if)#end
Shelter-SW1#
*Jun 27 15:11:53.963: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Ethernet1/0            unassigned      YES unset  up                    up      
Ethernet1/1            unassigned      YES unset  up                    up      
Ethernet1/2            unassigned      YES unset  up                    up      
Ethernet1/3            unassigned      YES unset  up                    up      
Ethernet2/0            unassigned      YES unset  up                    up      
Ethernet2/1            unassigned      YES unset  up                    up      
Ethernet2/2            unassigned      YES unset  up                    up      
Ethernet2/3            unassigned      YES unset  up                    up      
Shelter-SW1#show ip interface      
Ethernet0/0 is up, line protocol is up
  Inbound  access list is not set
  Internet protocol processing disabled
Ethernet0/1 is up, line protocol is up
  Inbound  access list is not set
  Internet protocol processing disabled
Ethernet0/2 is up, line protocol is up
  Inbound  access list is not set
  Internet protocol processing disabled
Ethernet0/3 is administratively down, line protocol is down
  Inbound  access list is not set
  Internet protocol processing disabled
Ethernet1/0 is up, line protocol is up
  Inbound  access list is not set
  Internet protocol processing disabled
Ethernet1/1 is up, line protocol is up
  Inbound  access list is not set
  Internet protocol processing disabled
Ethernet1/2 is up, line protocol is up
  Inbound  access list is not set
  Internet protocol processing disabled
Ethernet1/3 is up, line protocol is up
  Inbound  access list is not set
          
Shelter-SW1#show ip interface brief | include description
Shelter-SW1#show ip interface | include description      
Shelter-SW1#conf t         
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW1(config)#$ange ethernet0/3, ethernet1/0 - 3, ethernet2/0 - 3       
Shelter-SW1(config-if-range)#description UNUSED-ADMINISTRATIVELY SHUTDOWN
Shelter-SW1(config-if-range)#switchport mode access
Shelter-SW1(config-if-range)#switchport access vlan 1
Shelter-SW1(config-if-range)#shutdown
Shelter-SW1(config-if-range)#
*Jun 27 15:16:32.135: %LINK-5-CHANGED: Interface Ethernet1/0, changed state to administratively down
*Jun 27 15:16:32.136: %LINK-5-CHANGED: Interface Ethernet1/1, changed state to administratively down
*Jun 27 15:16:32.137: %LINK-5-CHANGED: Interface Ethernet1/2, changed state to administratively down
*Jun 27 15:16:32.139: %LINK-5-CHANGED: Interface Ethernet1/3, changed state to administratively down
*Jun 27 15:16:32.140: %LINK-5-CHANGED: Interface Ethernet2/0, changed state to administratively down
*Jun 27 15:16:32.141: %LINK-5-CHANGED: Interface Ethernet2/1, changed state to administratively down
Shelter-SW1(config-if-range)#end
*Jun 27 15:16:32.143: %LINK-5-CHANGED: Interface Ethernet2/2, changed state to administratively down
*Jun 27 15:16:32.144: %LINK-5-CHANGED: Interface Ethernet2/3, changed state to administratively down
*Jun 27 15:16:33.135: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/0, changed state to down
*Jun 27 15:16:33.136: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to down
*Jun 27 15:16:33.137: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jun 27 15:16:33.139: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Shelter-SW1(config-if-range)#end
*Jun 27 15:16:33.140: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/0, changed state to down
*Jun 27 15:16:33.141: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/1, changed state to down
*Jun 27 15:16:33.143: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/2, changed state to down
*Jun 27 15:16:33.144: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/3, changed state to down
Shelter-SW1(config-if-range)#end
Shelter-SW1#
*Jun 27 15:16:34.748: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/3, Et1/0, Et1/1
                                                Et1/2, Et1/3, Et2/0, Et2/1
                                                Et2/2, Et2/3
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
99   MGMT-NATIVE                      active    Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW1#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        Trunk-to-Shelter-R connected    1            full   auto 10/100/1000BaseTX
Et0/1        Trunk-to-Shelter-S connected    trunk        full   auto 10/100/1000BaseTX
Et0/2        Virtualisation man connected    99           full   auto 10/100/1000BaseTX
Et0/3        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/0        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/1        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/2        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/3        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/0        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/1        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/2        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
          
Shelter-SW1#how interfaces description
             ^
% Invalid input detected at '^' marker.

Shelter-SW1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Trunk-to-Shelter-RT1
Et0/1                          up             up       Trunk-to-Shelter-SW2
Et0/2                          up             up       Virtualisation management uplink - VLAN 99
Et0/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/0                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/1                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/2                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/0                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/1                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/2                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Shelter-SW1#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          10,20,30,40,99

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40,99
Shelter-SW1#

Shelter-SW2#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          admin down     down     
Et0/1                          up             up       Trunk-to-Shelter-SW1
Et0/2                          up             up       Shelter-Admin1 - vlan 10
Et0/3                          up             up       Shelter-Patron1 - VLAN 20
Et1/0                          up             up       Trunk to Shelter Access Point
Et1/1                          up             up       
Et1/2                          up             up       
Et1/3                          up             up       
Et2/0                          up             up       
Et2/1                          up             up       
Et2/2                          up             up       
Et2/3                          up             up       
Shelter-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW2(config)#$ange ethernet0/0, ethernet1/1 - 3, ethernet2/0 - 3      
Shelter-SW2(config-if-range)#description UNUSED - ADMINISTRATIVELY SHUTDOWN
Shelter-SW2(config-if-range)#switchport mode access
Shelter-SW2(config-if-range)#switchport access vlan 1
Shelter-SW2(config-if-range)#shutdown
Shelter-SW2(config-if-range)#
*Jun 27 15:21:51.707: %LINK-5-CHANGED: Interface Ethernet1/1, changed state to administratively down
*Jun 27 15:21:51.708: %LINK-5-CHANGED: Interface Ethernet1/2, changed state to administratively down
*Jun 27 15:21:51.709: %LINK-5-CHANGED: Interface Ethernet1/3, changed state to administratively down
*Jun 27 15:21:51.711: %LINK-5-CHANGED: Interface Ethernet2/0, changed state to administratively down
*Jun 27 15:21:51.713: %LINK-5-CHANGED: Interface Ethernet2/1, changed state to administratively down
*Jun 27 15:21:51.713: %LINK-5-CHANGED: Interface Ethernet2/2, changed state to administratively down
Shelter-SW2(config-if-range)#end
*Jun 27 15:21:51.715: %LINK-5-CHANGED: Interface Ethernet2/3, changed state to administratively down
*Jun 27 15:21:52.707: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to down
*Jun 27 15:21:52.708: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jun 27 15:21:52.709: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
*Jun 27 15:21:52.711: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/0, changed state to down
*Jun 27 15:21:52.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/1, changed state to down
Shelter-SW2(config-if-range)#end
Shelter-SW2#
*Jun 27 15:21:52.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/2, changed state to down
*Jun 27 15:21:52.715: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet2/3, changed state to down
Shelter-SW2#
*Jun 27 15:21:53.916: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW2#
Shelter-SW2#
Shelter-SW2#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et0/1                          up             up       Trunk-to-Shelter-SW1
Et0/2                          up             up       Shelter-Admin1 - vlan 10
Et0/3                          up             up       Shelter-Patron1 - VLAN 20
Et1/0                          up             up       Trunk to Shelter Access Point
Et1/1                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et1/2                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et1/3                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/0                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/1                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/2                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/3                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Shelter-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
10   MGMT-FALLOUT                     active    Et0/2
20   INTERNAL-COMMS                   active    Et0/3
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
99   MGMT-NATIVE                      active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW2#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et0/1        Trunk-to-Shelter-S connected    trunk        full   auto 10/100/1000BaseTX
Et0/2        Shelter-Admin1 - v connected    10           full   auto 10/100/1000BaseTX
Et0/3        Shelter-Patron1 -  connected    20           full   auto 10/100/1000BaseTX
Et1/0        Trunk to Shelter A connected    trunk        full   auto 10/100/1000BaseTX
Et1/1        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et1/2        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et1/3        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/0        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/1        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/2        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
          
Shelter-SW2#how interfaces trunk
             ^
% Invalid input detected at '^' marker.

Shelter-SW2#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99
Et1/0          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          10,20,30,40,99
Et1/0          10,20

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40,99
Et1/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40,99
Et1/0          10,20
Shelter-SW2#


Connecting to console for Shelter-Admin1

Core Linux
shelter-admin1 login: castle
Password: 
Login incorrect
login[638]: invalid password for 'UNKNOWN' on 'ttyS0'
shelter-admin1 login: castle
Password: 
Login incorrect
login[638]: invalid password for 'UNKNOWN' on 'ttyS0'
shelter-admin1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@shelter-admin1:~$ ipconfig /renew
-sh: ipconfig: not found
cisco@shelter-admin1:~$ ifconfig /renew
ifconfig: /renew: error fetching interface information: Device not found
cisco@shelter-admin1:~$ ipconfig
-sh: ipconfig: not found
cisco@shelter-admin1:~$ ping 10.0.16.1
PING 10.0.16.1 (10.0.16.1): 56 data bytes
ping: sendto: Network is unreachable
cisco@shelter-admin1:~$ 

Shelter-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW1(config)#int
Shelter-SW1(config)#interface eth
Shelter-SW1(config)#interface ethernet0/0
Shelter-SW1(config-if)#description Trunk to Shelter-RT1
Shelter-SW1(config-if)#switchport trunk encapsulation dot1q
Shelter-SW1(config-if)#switchport mode trunk
Shelter-SW1(config-if)#switchpo
*Jun 27 15:33:05.828: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Shelter-SW1(config-if)#switchport 
*Jun 27 15:33:08.829: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Shelter-SW1(config-if)#switchport trunk native vlan 99
Shelter-SW1(config-if)#switchport trunk allowed vlan 10,20,30,40,99
Shelter-SW1(config-if)#switchport nonegotiate
Shelter-SW1(config-if)#no shutdown
Shelter-SW1(config-if)#end
Shelter-SW1#
*Jun 27 15:34:01.594: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW1#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      99
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99

Port           Vlans allowed and active in management domain
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99
Shelter-SW1#show interfaces ethernet0/0 switchport
Name: Et0/0
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (MGMT-NATIVE)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 10,20,30,40,99
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Protected: false
Appliance trust: none
Shelter-SW1#

cisco@shelter-admin1:~$ ifconfig
eth0      Link encap:Ethernet  HWaddr 52:54:00:4A:25:E6  
          inet addr:10.0.16.2  Bcast:10.0.16.127  Mask:255.255.255.128
          inet6 addr: fe80::5054:ff:fe4a:25e6/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:386 errors:0 dropped:1 overruns:0 frame:0
          TX packets:590 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:131468 (128.3 KiB)  TX bytes:197020 (192.4 KiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

cisco@shelter-admin1:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.16.1       0.0.0.0         UG    0      0        0 eth0
10.0.16.0       0.0.0.0         255.255.255.128 U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@shelter-admin1:~$ sudo udhcpc -i eth0
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.0.16.2, server 10.0.16.1
udhcpc: lease of 10.0.16.2 obtained from 10.0.16.1, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 1.1.1.1
cisco@shelter-admin1:~$ ifconfig
eth0      Link encap:Ethernet  HWaddr 52:54:00:4A:25:E6  
          inet addr:10.0.16.2  Bcast:10.0.16.127  Mask:255.255.255.128
          inet6 addr: fe80::5054:ff:fe4a:25e6/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:388 errors:0 dropped:1 overruns:0 frame:0
          TX packets:592 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:132172 (129.0 KiB)  TX bytes:197704 (193.0 KiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

cisco@shelter-admin1:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.16.1       0.0.0.0         UG    0      0        0 eth0
10.0.16.0       0.0.0.0         255.255.255.128 U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@shelter-admin1:~$ ping 10.0.16.1
PING 10.0.16.1 (10.0.16.1): 56 data bytes
64 bytes from 10.0.16.1: seq=0 ttl=255 time=2.397 ms
64 bytes from 10.0.16.1: seq=1 ttl=255 time=1.432 ms
64 bytes from 10.0.16.1: seq=2 ttl=255 time=1.476 ms
64 bytes from 10.0.16.1: seq=3 ttl=255 time=1.461 ms
64 bytes from 10.0.16.1: seq=4 ttl=255 time=1.433 ms
64 bytes from 10.0.16.1: seq=5 ttl=255 time=1.500 ms
64 bytes from 10.0.16.1: seq=6 ttl=255 time=1.501 ms
64 bytes from 10.0.16.1: seq=7 ttl=255 time=1.514 ms
64 bytes from 10.0.16.1: seq=8 ttl=255 time=1.564 ms
64 bytes from 10.0.16.1: seq=9 ttl=255 time=1.495 ms
^C
--- 10.0.16.1 ping statistics ---
10 packets transmitted, 10 packets received, 0% packet loss
round-trip min/avg/max = 1.432/1.577/2.397 ms
cisco@shelter-admin1:~$ ping 10.0.16.129
PING 10.0.16.129 (10.0.16.129): 56 data bytes
64 bytes from 10.0.16.129: seq=0 ttl=255 time=1.456 ms
64 bytes from 10.0.16.129: seq=1 ttl=255 time=1.531 ms
64 bytes from 10.0.16.129: seq=2 ttl=255 time=1.592 ms
64 bytes from 10.0.16.129: seq=3 ttl=255 time=1.559 ms
64 bytes from 10.0.16.129: seq=4 ttl=255 time=1.547 ms
64 bytes from 10.0.16.129: seq=5 ttl=255 time=1.627 ms
64 bytes from 10.0.16.129: seq=6 ttl=255 time=1.515 ms
64 bytes from 10.0.16.129: seq=7 ttl=255 time=1.501 ms
64 bytes from 10.0.16.129: seq=8 ttl=255 time=1.395 ms
64 bytes from 10.0.16.129: seq=9 ttl=255 time=1.517 ms
^C
--- 10.0.16.129 ping statistics ---
10 packets transmitted, 10 packets received, 0% packet loss
round-trip min/avg/max = 1.395/1.524/1.627 ms
cisco@shelter-admin1:~$ 

Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@shelter-patron1:~$ sudo udhcpc -i eth0
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.0.16.130, server 10.0.16.129
udhcpc: lease of 10.0.16.130 obtained from 10.0.16.129, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 1.1.1.1
cisco@shelter-patron1:~$ ifconfig
eth0      Link encap:Ethernet  HWaddr 52:54:00:A4:AE:1D  
          inet addr:10.0.16.130  Bcast:10.0.16.255  Mask:255.255.255.128
          inet6 addr: fe80::5054:ff:fea4:ae1d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:389 errors:0 dropped:2 overruns:0 frame:0
          TX packets:592 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:132232 (129.1 KiB)  TX bytes:197704 (193.0 KiB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

cisco@shelter-patron1:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.0.16.129     0.0.0.0         UG    0      0        0 eth0
10.0.16.128     0.0.0.0         255.255.255.128 U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@shelter-patron1:~$ ping -c 5 10.0.16.129
PING 10.0.16.129 (10.0.16.129): 56 data bytes
64 bytes from 10.0.16.129: seq=0 ttl=255 time=2.237 ms
64 bytes from 10.0.16.129: seq=1 ttl=255 time=1.349 ms
64 bytes from 10.0.16.129: seq=2 ttl=255 time=1.322 ms
64 bytes from 10.0.16.129: seq=3 ttl=255 time=1.529 ms
64 bytes from 10.0.16.129: seq=4 ttl=255 time=1.372 ms

--- 10.0.16.129 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.322/1.561/2.237 ms
cisco@shelter-patron1:~$ ping -c 5 10.0.17.129
PING 10.0.17.129 (10.0.17.129): 56 data bytes
64 bytes from 10.0.17.129: seq=0 ttl=255 time=1.296 ms
64 bytes from 10.0.17.129: seq=1 ttl=255 time=1.439 ms
64 bytes from 10.0.17.129: seq=2 ttl=255 time=1.253 ms
64 bytes from 10.0.17.129: seq=3 ttl=255 time=1.158 ms
64 bytes from 10.0.17.129: seq=4 ttl=255 time=1.349 ms

--- 10.0.17.129 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.158/1.299/1.439 ms
cisco@shelter-patron1:~$ ping <Shelter-Admin1-IP>
-sh: syntax error: unexpected newline
cisco@shelter-patron1:~$ ping -c 5 10.0.16.1
PING 10.0.16.1 (10.0.16.1): 56 data bytes
64 bytes from 10.0.16.1: seq=0 ttl=255 time=1.322 ms
64 bytes from 10.0.16.1: seq=1 ttl=255 time=1.418 ms
64 bytes from 10.0.16.1: seq=2 ttl=255 time=1.535 ms
64 bytes from 10.0.16.1: seq=3 ttl=255 time=1.458 ms
64 bytes from 10.0.16.1: seq=4 ttl=255 time=1.509 ms

--- 10.0.16.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.322/1.448/1.535 ms
cisco@shelter-patron1:~$ ping -c 5 10.0.16.0
PING 10.0.16.0 (10.0.16.0): 56 data bytes

--- 10.0.16.0 ping statistics ---
5 packets transmitted, 0 packets received, 100% packet loss
cisco@shelter-patron1:~$ 

Shelter-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3, Et1/0, Et1/1, Et1/2
                                                Et1/3, Et2/0, Et2/1, Et2/2
                                                Et2/3
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
99   MGMT-NATIVE                      active    Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW1#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : FALLOUT
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0200
Configuration last modified by 0.0.0.0 at 6-27-26 14:06:37

Feature VLAN:
--------------
VTP Operating Mode                : Transparent
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 10
Configuration Revision            : 0
MD5 digest                        : 0x70 0x46 0xE4 0xD9 0x68 0x3F 0xEA 0x2E 
                                    0xA7 0x16 0xA9 0xA9 0x88 0xEB 0x38 0x4F 
Shelter-SW1#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      99
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99

Port           Vlans allowed and active in management domain
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99
Shelter-SW1#show interfaces ethernet0/0 switchport
Name: Et0/0
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (MGMT-NATIVE)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 10,20,30,40,99
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
          
Shelter-SW1#how interfaces ethernet0/1 switchport
             ^
% Invalid input detected at '^' marker.

Shelter-SW1#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        Trunk to Shelter-R connected    trunk        full   auto 10/100/1000BaseTX
Et0/1        Trunk-to-Shelter-S connected    trunk        full   auto 10/100/1000BaseTX
Et0/2        Virtualisation man connected    99           full   auto 10/100/1000BaseTX
Et0/3        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/0        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/1        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/2        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/3        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/0        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/1        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/2        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
          
Shelter-SW1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Trunk to Shelter-RT1
Et0/1                          up             up       Trunk-to-Shelter-SW2
Et0/2                          up             up       Virtualisation management uplink - VLAN 99
Et0/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/0                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/1                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/2                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/0                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/1                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/2                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Shelter-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3, Et1/0, Et1/1, Et1/2
                                                Et1/3, Et2/0, Et2/1, Et2/2
                                                Et2/3
10   MGMT-FALLOUT                     active    
20   INTERNAL-COMMS                   active    
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
99   MGMT-NATIVE                      active    Et0/2
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW1#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : FALLOUT
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0200
Configuration last modified by 0.0.0.0 at 6-27-26 14:06:37

Feature VLAN:
--------------
VTP Operating Mode                : Transparent
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 10
Configuration Revision            : 0
MD5 digest                        : 0x70 0x46 0xE4 0xD9 0x68 0x3F 0xEA 0x2E 
                                    0xA7 0x16 0xA9 0xA9 0x88 0xEB 0x38 0x4F 
Shelter-SW1#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      99
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99

Port           Vlans allowed and active in management domain
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20,30,40,99
Et0/1          10,20,30,40,99
Shelter-SW1#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        Trunk to Shelter-R connected    trunk        full   auto 10/100/1000BaseTX
Et0/1        Trunk-to-Shelter-S connected    trunk        full   auto 10/100/1000BaseTX
Et0/2        Virtualisation man connected    99           full   auto 10/100/1000BaseTX
Et0/3        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/0        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/1        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/2        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et1/3        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/0        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/1        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
Et2/2        UNUSED-ADMINISTRAT disabled     1            full   auto 10/100/1000BaseTX
          
Shelter-SW1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Trunk to Shelter-RT1
Et0/1                          up             up       Trunk-to-Shelter-SW2
Et0/2                          up             up       Virtualisation management uplink - VLAN 99
Et0/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/0                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/1                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/2                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et1/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/0                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/1                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/2                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Et2/3                          admin down     down     UNUSED-ADMINISTRATIVELY SHUTDOWN
Shelter-SW1#

Shelter-SW2#
*Jun 27 15:49:14.596: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: castle] [Source: LOCAL] [localport: 0] at 15:49:14 UTC Sat Jun 27 2026
Shelter-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
10   MGMT-FALLOUT                     active    Et0/2
20   INTERNAL-COMMS                   active    Et0/3
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
99   MGMT-NATIVE                      active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW2#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : FALLOUT
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0100
Configuration last modified by 0.0.0.0 at 6-27-26 14:11:40

Feature VLAN:
--------------
VTP Operating Mode                : Transparent
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 10
Configuration Revision            : 0
MD5 digest                        : 0x70 0x46 0xE4 0xD9 0x68 0x3F 0xEA 0x2E 
                                    0xA7 0x16 0xA9 0xA9 0x88 0xEB 0x38 0x4F 
Shelter-SW2#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99
Et1/0          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          10,20,30,40,99
Et1/0          10,20

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40,99
Et1/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40,99
Et1/0          10,20
Shelter-SW2#show interfaces ethernet0/1 switchport
Name: Et0/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (MGMT-NATIVE)
Administrative Native VLAN tagging: disabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: 10,20,30,40,99
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
          
Shelter-SW2#how interfaces ethernet1/0 switchport
             ^
% Invalid input detected at '^' marker.

Shelter-SW2#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et0/1        Trunk-to-Shelter-S connected    trunk        full   auto 10/100/1000BaseTX
Et0/2        Shelter-Admin1 - v connected    10           full   auto 10/100/1000BaseTX
Et0/3        Shelter-Patron1 -  connected    20           full   auto 10/100/1000BaseTX
Et1/0        Trunk to Shelter A connected    trunk        full   auto 10/100/1000BaseTX
Et1/1        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et1/2        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et1/3        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/0        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/1        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/2        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
          
Shelter-SW2#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et0/1                          up             up       Trunk-to-Shelter-SW1
Et0/2                          up             up       Shelter-Admin1 - vlan 10
Et0/3                          up             up       Shelter-Patron1 - VLAN 20
Et1/0                          up             up       Trunk to Shelter Access Point
Et1/1                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et1/2                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et1/3                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/0                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/1                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/2                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/3                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Shelter-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
10   MGMT-FALLOUT                     active    Et0/2
20   INTERNAL-COMMS                   active    Et0/3
30   VIDEO-SURVEILLANCE               active    
40   GUEST-ACCESS                     active    
99   MGMT-NATIVE                      active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW2#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : FALLOUT
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0100
Configuration last modified by 0.0.0.0 at 6-27-26 14:11:40

Feature VLAN:
--------------
VTP Operating Mode                : Transparent
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 10
Configuration Revision            : 0
MD5 digest                        : 0x70 0x46 0xE4 0xD9 0x68 0x3F 0xEA 0x2E 
                                    0xA7 0x16 0xA9 0xA9 0x88 0xEB 0x38 0x4F 
Shelter-SW2#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99
Et1/0          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          10,20,30,40,99
Et1/0          10,20

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40,99
Et1/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40,99
Et1/0          10,20
Shelter-SW2#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et0/1        Trunk-to-Shelter-S connected    trunk        full   auto 10/100/1000BaseTX
Et0/2        Shelter-Admin1 - v connected    10           full   auto 10/100/1000BaseTX
Et0/3        Shelter-Patron1 -  connected    20           full   auto 10/100/1000BaseTX
Et1/0        Trunk to Shelter A connected    trunk        full   auto 10/100/1000BaseTX
Et1/1        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et1/2        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et1/3        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/0        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/1        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
Et2/2        UNUSED - ADMINISTR disabled     1            full   auto 10/100/1000BaseTX
          
Shelter-SW2#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et0/1                          up             up       Trunk-to-Shelter-SW1
Et0/2                          up             up       Shelter-Admin1 - vlan 10
Et0/3                          up             up       Shelter-Patron1 - VLAN 20
Et1/0                          up             up       Trunk to Shelter Access Point
Et1/1                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et1/2                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et1/3                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/0                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/1                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/2                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Et2/3                          admin down     down     UNUSED - ADMINISTRATIVELY SHUTDOWN
Shelter-SW2#

Shelter-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.16.1       YES manual up                    up      
Ethernet0/0.20         10.0.16.129     YES manual up                    up      
Ethernet0/0.30         10.0.17.1       YES manual up                    up      
Ethernet0/0.40         10.0.17.129     YES manual up                    up      
Ethernet0/0.99         10.0.99.1       YES manual up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Shelter-RT1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.16.1       YES manual up                    up      
Ethernet0/0.20         10.0.16.129     YES manual up                    up      
Ethernet0/0.30         10.0.17.1       YES manual up                    up      
Ethernet0/0.40         10.0.17.129     YES manual up                    up      
Ethernet0/0.99         10.0.99.1       YES manual up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Shelter-RT1#show running-config | section interface Ethernet0/0
interface Ethernet0/0
 description Trunk to Shelter-SW1
 no ip address
interface Ethernet0/0.10
 description Gateway fpr VLAN 10
 encapsulation dot1Q 10
 ip address 10.0.16.1 255.255.255.128
interface Ethernet0/0.20
 description Gateway fpr VLAN 20
 encapsulation dot1Q 20
 ip address 10.0.16.129 255.255.255.128
interface Ethernet0/0.30
 description Gateway fpr VLAN 30
 encapsulation dot1Q 30
 ip address 10.0.17.1 255.255.255.128
interface Ethernet0/0.40
 description Gateway fpr VLAN 40
 encapsulation dot1Q 40
 ip address 10.0.17.129 255.255.255.128
interface Ethernet0/0.99
 description native management gateway for VLAN 99
 encapsulation dot1Q 99 native
 ip address 10.0.99.1 255.255.255.224
Shelter-RT1#how running-config | section ip dhcp pool
             ^
% Invalid input detected at '^' marker.

Shelter-RT1#show ip dhcp pool

Pool MGMT :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 1
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.16.3            10.0.16.1        - 10.0.16.126       1     / 1     / 126  

Pool INTERNAL :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 126
 Leased addresses               : 1
 Excluded addresses             : 1
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.0.16.131          10.0.16.129      - 10.0.16.254       1     / 1     / 126  

          
Shelter-RT1#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address      Client-ID/              Lease expiration        Type       State      Interface
                Hardware address/
                User name
10.0.16.2       0152.5400.4a25.e6       Jun 28 2026 03:36 PM    Automatic  Active     Ethernet0/0.10
10.0.16.130     0152.5400.a4ae.1d       Jun 28 2026 03:40 PM    Automatic  Active     Ethernet0/0.20
Shelter-RT1#


```
