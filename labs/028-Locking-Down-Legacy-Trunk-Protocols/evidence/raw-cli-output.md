# Lab 028 - Raw CLI Output

```bash
Cafe-SW1>en
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#int
Cafe-SW1(config)#interface 
*Jun 24 20:21:04.987: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jun 24 20:21:05.089: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 20:21:05.089: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 20:21:05.193: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW1(config)#interface ethe
*Jun 24 20:21:05.294: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jun 24 20:21:05.294: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW1(config)#interface ethe
Cafe-SW1(config)#interface ethernet0/1
Cafe-SW1(config-if)#switchport dtp
                                ^
% Invalid input detected at '^' marker.

Cafe-SW1(config-if)#switchport dtp ?
% Unrecognized command
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#swit
*Jun 24 20:22:07.956: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW1(config-if)#switchport mode 
*Jun 24 20:22:10.957: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#switchport nonegotiate
Cafe-SW1(config-if)#end
Cafe-SW1#show 
*Jun 24 20:22:27.110: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20

Port           Vlans allowed and active in management domain
Et0/1          none

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          none
Cafe-SW1#show dtp interface eth
Cafe-SW1#show dtp interface ethernet 0/1
DTP information for Ethernet0/1:
  TOS/TAS/TNS:                              TRUNK/NONEGOTIATE/TRUNK
  TOT/TAT/TNT:                              802.1Q/802.1Q/802.1Q
  Neighbor address 1:                       AABBCC000310
  Neighbor address 2:                       000000000000
  Hello timer expiration (sec/state):       never/STOPPED
  Access timer expiration (sec/state):      never/STOPPED
  Negotiation timer expiration (sec/state): never/STOPPED
  Multidrop timer expiration (sec/state):   never/STOPPED
  FSM state:                                S6:TRUNK
  # times multi & trunk                     0
  Enabled:                                  yes
  In STP:                                   no

  Statistics
  ----------
  10 packets received (9 good)
  1 packets dropped
      1 nonegotiate, 0 bad version, 0 domain mismatches, 
      0 bad TLVs, 0 bad TAS, 0 bad TAT, 0 bad TOT, 0 other
  20 packets output (20 good)
      14 native, 6 software encap isl, 0 isl hardware native
  0 output errors
  0 trunk timeouts
  1 link ups, last link up on Wed Jun 24 2026, 20:20:14
  0 link downs

Cafe-SW1#


Connecting to console for Cafe-SW2

Cafe-SW2>
*Jun 24 20:22:07.957: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW2>
*Jun 24 20:22:10.957: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-SW2>en
Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#interface e
*Jun 24 20:23:17.818: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW2(config)#interface ether
*Jun 24 20:23:17.920: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 20:23:17.921: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 20:23:18.027: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW2(config)#interface ethernet
*Jun 24 20:23:18.127: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jun 24 20:23:18.127: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW2(config)#interface ethernet0/1
Cafe-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-SW2(config-if)#switchport mode trunk
Cafe-SW2(config-if)#switchport nonegotiate
Cafe-SW2(config-if)#end
Cafe-SW2#s
*Jun 24 20:24:14.668: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20

Port           Vlans allowed and active in management domain
Et0/1          none

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          none
Cafe-SW2#show dtp interface ethernet0/1
DTP information for Ethernet0/1:
  TOS/TAS/TNS:                              TRUNK/NONEGOTIATE/TRUNK
  TOT/TAT/TNT:                              802.1Q/802.1Q/802.1Q
  Neighbor address 1:                       AABBCC000110
  Neighbor address 2:                       000000000000
  Hello timer expiration (sec/state):       never/STOPPED
  Access timer expiration (sec/state):      never/STOPPED
  Negotiation timer expiration (sec/state): never/STOPPED
  Multidrop timer expiration (sec/state):   never/STOPPED
  FSM state:                                S6:TRUNK
  # times multi & trunk                     0
  Enabled:                                  yes
  In STP:                                   no

  Statistics
  ----------
  10 packets received (10 good)
  0 packets dropped
      0 nonegotiate, 0 bad version, 0 domain mismatches, 
      0 bad TLVs, 0 bad TAS, 0 bad TAT, 0 bad TOT, 0 other
  18 packets output (18 good)
      15 native, 3 software encap isl, 0 isl hardware native
  0 output errors
  0 trunk timeouts
  1 link ups, last link up on Wed Jun 24 2026, 20:20:27
  0 link downs
          
Cafe-SW2#


Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#int
Cafe-SW1(config)#interface eth
Cafe-SW1(config)#interface ethernet0/0
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#switch
*Jun 24 20:25:57.390: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Cafe-SW1(config-if)#switchport noneg
*Jun 24 20:26:00.391: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-SW1(config-if)#switchport nonegotiate
Cafe-SW1(config-if)#end
Cafe-SW1#show
*Jun 24 20:26:11.924: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20
Et0/1          10,20

Port           Vlans allowed and active in management domain
Et0/0          none
Et0/1          none

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          none
Et0/1          none
Cafe-SW1#show dtp interface ethernet0/0
DTP information for Ethernet0/0:
  TOS/TAS/TNS:                              TRUNK/NONEGOTIATE/TRUNK
  TOT/TAT/TNT:                              802.1Q/802.1Q/802.1Q
  Neighbor address 1:                       000000000000
  Neighbor address 2:                       000000000000
  Hello timer expiration (sec/state):       never/STOPPED
  Access timer expiration (sec/state):      never/STOPPED
  Negotiation timer expiration (sec/state): never/STOPPED
  Multidrop timer expiration (sec/state):   never/STOPPED
  FSM state:                                S6:TRUNK
  # times multi & trunk                     0
  Enabled:                                  yes
  In STP:                                   no

  Statistics
  ----------
  0 packets received (0 good)
  0 packets dropped
      0 nonegotiate, 0 bad version, 0 domain mismatches, 
      0 bad TLVs, 0 bad TAS, 0 bad TAT, 0 bad TOT, 0 other
  25 packets output (25 good)
      14 native, 11 software encap isl, 0 isl hardware native
  0 output errors
  0 trunk timeouts
  1 link ups, last link up on Wed Jun 24 2026, 20:20:14
  0 link downs
          
Cafe-SW1#


Cafe-RTR1>en
Cafe-RTR1#conf t
*Jun 24 20:28:04.199: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-RTR1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-RTR1(config)#
*Jun 24 20:28:04.302: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 20:28:04.303: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 20:28:04.410: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-RTR1(config)#
*Jun 24 20:28:04.510: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 24 20:28:04.510: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-RTR1(config)#interface ethernet0/0
Cafe-RTR1(config-if)#no shutdown
Cafe-RTR1(config-if)#end
Cafe-RTR1#
*Jun 24 20:28:24.861: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Cafe-RTR1#
*Jun 24 20:28:25.065: %SYS-5-CONFIG_I: Configured from console by console
Cafe-RTR1#show
*Jun 24 20:28:25.861: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-RTR1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/0.20         10.0.18.33      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Cafe-RTR1#


Cafe-SW1#
Cafe-SW1#
Cafe-SW1#show vtp status
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
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#vtp domain COOKIE
Changing VTP domain name from NULL to COOKIE
Cafe-SW1(config)#
*Jun 24 20:29:38.272: %SW_VLAN-6-VTP_DOMAIN_NAME_CHG: VTP domain name changed to COOKIE.
Cafe-SW1(config)#vtp mode transparent
Setting device to VTP Transparent mode for VLANS.
Cafe-SW1(config)#vlan 10
Cafe-SW1(config-vlan)#name ADMIN
Cafe-SW1(config-vlan)#exit
Cafe-SW1(config)#vlan 20
Cafe-SW1(config-vlan)#name PATRON
Cafe-SW1(config-vlan)#end
Cafe-SW1#
*Jun 24 20:30:20.876: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/2, Et0/3
10   ADMIN                            active    
20   PATRON                           active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW1#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : COOKIE
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0100
Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

Feature VLAN:
--------------
VTP Operating Mode                : Transparent
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 7
Configuration Revision            : 0
MD5 digest                        : 0x35 0xA7 0x25 0x3B 0xB8 0x81 0x67 0x82 
                                    0x7C 0xF1 0x81 0x9D 0xF7 0xE0 0x5D 0x3E 
Cafe-SW1#


Cafe-SW2>
Cafe-SW2>en
Cafe-SW2#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : COOKIE
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0300
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
*** MD5 digest checksum mismatch on trunk: Et0/1 ***
Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#vtp domain COOKIE
Domain name already set to COOKIE.
Cafe-SW2(config)#vtp mode transparent
Setting device to VTP Transparent mode for VLANS.
Cafe-SW2(config)#vlan 10
Cafe-SW2(config-vlan)#name ADMIN
Cafe-SW2(config-vlan)#exit
Cafe-SW2(config)#vlan 20
Cafe-SW2(config-vlan)#name PATRON
Cafe-SW2(config-vlan)#end
Cafe-SW2#sho
*Jun 24 20:37:47.400: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/2, Et0/3
10   ADMIN                            active    
20   PATRON                           active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW2#show vtp status
VTP Version capable             : 1 to 3
VTP version running             : 1
VTP Domain Name                 : COOKIE
VTP Pruning Mode                : Disabled (Operationally Disabled)
VTP Traps Generation            : Disabled
Device ID                       : aabb.cc80.0300
Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00

Feature VLAN:
--------------
VTP Operating Mode                : Transparent
Maximum VLANs supported locally   : 1005
Number of existing VLANs          : 7
Configuration Revision            : 0
MD5 digest                        : 0x35 0xA7 0x25 0x3B 0xB8 0x81 0x67 0x82 
                                    0x7C 0xF1 0x81 0x9D 0xF7 0xE0 0x5D 0x3E 
*** MD5 digest checksum mismatch on trunk: Et0/1 ***
Cafe-SW2#
```
