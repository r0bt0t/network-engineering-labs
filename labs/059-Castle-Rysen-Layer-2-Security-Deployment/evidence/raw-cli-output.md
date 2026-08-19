# Lab 059 - Raw CLI Output

```bash
Connecting to console for Cafe-Edge-R1

Cafe-Edge-R1>
Cafe-Edge-R1>en
Cafe-Edge-R1#show ip in
*Aug 18 16:28:30.590: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-Edge-R1#show ip interfac
*Aug 18 16:28:30.692: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 16:28:30.693: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 16:28:30.797: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-Edge-R1#show ip interface
*Aug 18 16:28:30.897: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 18 16:28:30.897: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-Edge-R1#show ip interface brief | include Ethernet0/0
Ethernet0/0            unassigned      YES unset  administratively down down    
Ethernet0/0.10         10.1.10.1       YES TFTP   administratively down down    
Ethernet0/0.20         10.1.20.1       YES TFTP   administratively down down    
Cafe-Edge-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Edge-R1(config)#interface ethernet0/0
Cafe-Edge-R1(config-if)#no shutdown
Cafe-Edge-R1(config-if)#end
Cafe-Edge-R1#
*Aug 18 16:29:09.016: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Aug 18 16:29:09.922: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Edge-R1#s
*Aug 18 16:29:10.016: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-Edge-R1#show ip interface brioef | include ethernet0/0
                                  ^
% Invalid input detected at '^' marker.

Cafe-Edge-R1#show ip interface brief | include ethernet0/0 
Cafe-Edge-R1#show ip interface brief | include Ethernet0/0
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.1.10.1       YES TFTP   up                    up      
Ethernet0/0.20         10.1.20.1       YES TFTP   up                    up      
Cafe-Edge-R1#


Connecting to console for Cafe-01-SW1

*Aug 18 16:28:23.873: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW1>
Cafe-01-SW1>
*Aug 18 16:29:07.021: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1>en
Cafe-01-SW1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-01-SW2      Eth 0/1           123             R S I  Linux Uni Eth 0/1
Cafe-Edge-R1     Eth 6/0           159               R    Linux Uni Eth 0/0

Total cdp entries displayed : 2
Cafe-01-SW1#
*Aug 18 16:30:26.391: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-01-SW1#
*Aug 18 16:30:26.494: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 16:30:26.494: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 16:30:26.600: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-01-SW1#
*Aug 18 16:30:26.700: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 18 16:30:26.700: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-01-SW1#show interface status | include Et0/1|Et0/2|Et0/3|Et1/0|Et6/0
Et0/1        Trunk to Cafe-01-S connected    1            full   auto 10/100/1000BaseTX
Et0/2        Reserve Trunk to C connected    1            full   auto 10/100/1000BaseTX
Et0/3        Admin Workstation  connected    10           full   auto 10/100/1000BaseTX
Et1/0        Uplink to Cafe-01- connected    1            full   auto 10/100/1000BaseTX
Et6/0        Uplink to Cafe-Edg connected    1            full   auto 10/100/1000BaseTX
Cafe-01-SW1#
*Aug 18 16:30:45.115: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW1#show vlan brief | include Et0/3|Et1/1|Et5/3|Et6/0
                                                Et6/0, Et6/1, Et6/2, Et6/3
10   VLAN0010                         active    Et0/3
20   VLAN0020                         active    Et1/1, Et1/2, Et1/3, Et2/0
                                                Et5/1, Et5/2, Et5/3
Cafe-01-SW1#



Connecting to console for Cafe-01-SW2

Cafe-01-SW2>
Cafe-01-SW2>
*Aug 18 16:28:37.382: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2>
*Aug 18 16:29:10.017: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2>
*Aug 18 16:29:41.387: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2>
*Aug 18 16:30:17.391: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/1 TDR=0, TRC=0
Cafe-01-SW2>
*Aug 18 16:30:50.183: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2>en
Cafe-01-SW2#show cdp 
*Aug 18 16:31:10.880: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-01-SW2#show cdp n
*Aug 18 16:31:10.982: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 16:31:10.982: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 18 16:31:11.089: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-01-SW2#show cdp neighb
*Aug 18 16:31:11.189: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 18 16:31:11.189: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-01-SW2#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-01-SW1      Eth 0/1           123             R S I  Linux Uni Eth 0/1

Total cdp entries displayed : 1
Cafe-01-SW2#
*Aug 18 16:31:23.250: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2#show interface status | include Et0/1|Et0/2|Et1/0|Et1/1|Et5/3
Et0/1        Uplink to Cafe-01- connected    1            full   auto 10/100/1000BaseTX
Et0/2        Cafe-01-PC (Patron connected    20           full   auto 10/100/1000BaseTX
Et1/0        Cafe-01-Plex Admin connected    10           full   auto 10/100/1000BaseTX
Et1/1        Patron Access Drop connected    20           full   auto 10/100/1000BaseTX
Et5/3        Patron Access Drop connected    20           full   auto 10/100/1000BaseTX
Cafe-01-SW2#show vlan brief | include Et0/2|Et1/0|Et1/1|Et5/3
10   VLAN0010                         active    Et1/0
20   VLAN0020                         active    Et0/2, Et1/1, Et1/2, Et1/3
                                                Et5/0, Et5/1, Et5/2, Et5/3
Cafe-01-SW2#


Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#$ Ethernet3/0 - 3 , Ethernet4/0 - 3 , Ethernet5/0 - 3    
Cafe-01-SW1(config-if-range)#switchport mode access
Cafe-01-SW1(config-if-range)#switchport port-security
Cafe-01-SW1(config-if-range)#switchport port-security maximum 1
Cafe-01-SW1(config-if-range)#no switchport port-security mac-address st
*Aug 18 16:33:13.514: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW1(config-if-range)#no switchport port-security mac-address sticky
Cafe-01-SW1(config-if-range)#exit
Cafe-01-SW1(config)#interface ethernet0/3
Cafe-01-SW1(config-if)#switchport mode access
Cafe-01-SW1(config-if)#switchpor
*Aug 18 16:33:43.666: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-01-SW1(config-if)#switchport port-security
Cafe-01-SW1(config-if)#switchport port-security maximum 1
Cafe-01-SW1(config-if)#switchport port-security mac-address sticky
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#end
Cafe-01-SW1#
*Aug 18 16:34:14.347: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#show port-security interface Ethernet0/3
Port Security              : Enabled
Port Status                : Secure-up
Violation Mode             : Shutdown
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 0
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 0000.0000.0000:0
Security Violation Count   : 0

Cafe-01-SW1#show port-security
Secure Port  MaxSecureAddr  CurrentAddr  SecurityViolation  Security Action
                (Count)       (Count)          (Count)
---------------------------------------------------------------------------
      Et0/3              1            0                  0         Shutdown
      Et1/1              1            0                  0         Shutdown
      Et1/2              1            0                  0         Shutdown
      Et1/3              1            0                  0         Shutdown
      Et2/0              1            0                  0         Shutdown
      Et2/1              1            0                  0         Shutdown
      Et2/2              1            0                  0         Shutdown
      Et2/3              1            0                  0         Shutdown
      Et3/0              1            0                  0         Shutdown
      Et3/1              1            0                  0         Shutdown
      Et3/2              1            0                  0         Shutdown
      Et3/3              1            0                  0         Shutdown
      Et4/0              1            0                  0         Shutdown
      Et4/1              1            0                  0         Shutdown
      Et4/2              1            0                  0         Shutdown
      Et4/3              1            0                  0         Shutdown
      Et5/0              1            0                  0         Shutdown
      Et5/1              1            0                  0         Shutdown
      Et5/2              1            0                  0         Shutdown
      Et5/3              1            0                  0         Shutdown
---------------------------------------------------------------------------
Total Addresses in System (excluding one mac per port)     : 0
Max Addresses limit in System (excluding one mac per port) : 4096
Cafe-01-SW1#show running-config interface Ethernet0/3
Building configuration...

Current configuration : 211 bytes
!
interface Ethernet0/3
 description Admin Workstation Drop
 switchport access vlan 10
 switchport mode access
 switchport port-security mac-address sticky
 switchport port-security
 spanning-tree portfast
end

Cafe-01-SW1#


Cafe-01-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW2(config)#interface Ethernet0/2
Cafe-01-SW2(config-if)#switchport mode access
Cafe-01-SW2(config-if)#
*Aug 18 16:37:36.046: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/3 TDR=0, TRC=0
Cafe-01-SW2(config-if)#switchport port-security
Cafe-01-SW2(config-if)#switchport port-security maximum 1
Cafe-01-SW2(config-if)#no switchport port-security mac-address
*Aug 18 16:38:08.335: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config-if)#no switchport port-security mac-address sticky
Cafe-01-SW2(config-if)#exit
Cafe-01-SW2(config)#$ Ethernet3/0 - 3 , Ethernet4/0 - 3 , Ethernet5/0 - 3    
Cafe-01-SW2(config-if-range)#switchport mode access                        
Cafe-01-SW2(config-if-range)#no switchport port-security mac-address sticky
*Aug 18 16:38:39.216: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/2 TDR=0, TRC=0
Cafe-01-SW2(config-if-range)#switchport port-security                      
Cafe-01-SW2(config-if-range)#switchport port-security maximum 1            
Cafe-01-SW2(config-if-range)#no switchport port-security mac-address sticky
Cafe-01-SW2(config-if-range)#exit
Cafe-01-SW2(config)#interface Ethernet1/0 
Cafe-01-SW2(config-if)#switchport mode access                        
*Aug 18 16:39:20.520: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config-if)#switchport mode access
Cafe-01-SW2(config-if)#switchport port-security                      
Cafe-01-SW2(config-if)#switchport port-security maximum 1            
Cafe-01-SW2(config-if)#no switchport port-security mac-address sticky
Cafe-01-SW2(config-if)#exit
Cafe-01-SW2(config)#end
Cafe-01-SW2#
*Aug 18 16:39:38.673: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW2#show port-security interface Ethernet
*Aug 18 16:39:56.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2#show port-security interface Ethernet1/0
Port Security              : Enabled
Port Status                : Secure-up
Violation Mode             : Shutdown
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 1
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 5254.0079.6aa1:10
Security Violation Count   : 0

Cafe-01-SW2#show port-security interface Ethernet0/2
Port Security              : Enabled
Port Status                : Secure-up
Violation Mode             : Shutdown
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 1
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 5254.0008.3643:20
Security Violation Count   : 0

Cafe-01-SW2#show port-security                      
Secure Port  MaxSecureAddr  CurrentAddr  SecurityViolation  Security Action
                (Count)       (Count)          (Count)
---------------------------------------------------------------------------
      Et0/2              1            1                  0         Shutdown
      Et1/0              1            1                  0         Shutdown
      Et1/1              1            0                  0         Shutdown
      Et1/2              1            0                  0         Shutdown
      Et1/3              1            0                  0         Shutdown
      Et2/0              1            0                  0         Shutdown
      Et2/1              1            0                  0         Shutdown
      Et2/2              1            0                  0         Shutdown
      Et2/3              1            0                  0         Shutdown
      Et3/0              1            0                  0         Shutdown
      Et3/1              1            0                  0         Shutdown
      Et3/2              1            0                  0         Shutdown
      Et3/3              1            0                  0         Shutdown
      Et4/0              1            0                  0         Shutdown
      Et4/1              1            0                  0         Shutdown
      Et4/2              1            0                  0         Shutdown
      Et4/3              1            0                  0         Shutdown
      Et5/0              1            0                  0         Shutdown
      Et5/1              1            0                  0         Shutdown
      Et5/2              1            0                  0         Shutdown
      Et5/3              1            0                  0         Shutdown
---------------------------------------------------------------------------
Total Addresses in System (excluding one mac per port)     : 0
Max Addresses limit in System (excluding one mac per port) : 4096
Cafe-01-SW2#


Cafe-01-SW1#
Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#ip dhcp snooping 
Cafe-01-SW1(config)#ip dhcp snooping vlan 1,10,20
*Aug 18 16:41:14.233: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/2 TDR=0, TRC=0
Cafe-01-SW1(config)#ip dhcp snooping vlan 1,10,20
Cafe-01-SW1(config)#no ip dhcp snooping information option
Cafe-01-SW1(config)#interface ethernet6/0
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk
Cafe-01-SW1(config-if)#ip dh
*Aug 18 16:42:05.066: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/0, changed state to down
Cafe-01-SW1(config-if)#ip dhcp snooping
*Aug 18 16:42:08.067: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet6/0, changed state to up
Cafe-01-SW1(config-if)#ip dhcp snooping trust
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#interface ethernet0/1                 
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk               
Cafe-01-SW1(config-if)#ip dhcp snooping trust              
*Aug 18 16:42:39.157: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-01-SW1(config-if)#ip dhcp snooping trust
Cafe-01-SW1(config-if)#
*Aug 18 16:42:41.606: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-01-SW1(config-if)#exi
*Aug 18 16:42:42.159: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#
*Aug 18 16:43:16.163: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-01-SW1(config)#$ Ethernet3/0 - 3 , Ethernet4/0 - 3 , Ethernet5/0 - 3    
Cafe-01-SW1(config-if-range)#ip dhcp snooping limit rate 5
Cafe-01-SW1(config-if-range)#exit
Cafe-01-SW1(config)#interface Ethernet
*Aug 18 16:44:06.264: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/1 TDR=0, TRC=0
Cafe-01-SW1(config)#interface Ethernet1/0
Cafe-01-SW1(config-if)#ip dhcp snooping limit rate 20
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#end
Cafe-01-SW1#
*Aug 18 16:44:26.423: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#show ip dhcp snooping
*Aug 18 16:44:36.381: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Cafe-01-SW1#show ip dhcp snooping
Switch DHCP snooping is enabled
Switch DHCP gleaning is disabled
DHCP snooping is configured on following VLANs:
1,10,20
DHCP snooping is operational on following VLANs:
1,10,20
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
Ethernet1/0                      no         no              20        
  Custom circuit-ids:
Ethernet1/1                      no         no              5         
  Custom circuit-ids:
Ethernet1/2                      no         no              5         
  Custom circuit-ids:
Ethernet1/3                      no         no              5         
  Custom circuit-ids:
Ethernet2/0                      no         no              5         
  Custom circuit-ids:
Ethernet2/1                      no         no              5         
  Custom circuit-ids:
Ethernet2/2                      no         no              5         
  Custom circuit-ids:
Ethernet2/3                      no         no              5         
  Custom circuit-ids:
Ethernet3/0                      no         no              5         
  Custom circuit-ids:
Ethernet3/1                      no         no              5         
  Custom circuit-ids:
Ethernet3/2                      no         no              5         
          
Cafe-01-SW1#how interfaces trunk
             ^
% Invalid input detected at '^' marker.

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


Cafe-01-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW2(config)#ip dhc
*Aug 18 16:45:34.956: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config)#ip dhcp snooping
Cafe-01-SW2(config)#ip dhcp snooping vlan 1,10,20
Cafe-01-SW2(config)#no ip dhcp snooping information 
*Aug 18 16:46:06.238: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config)#no ip dhcp snooping information option
Cafe-01-SW2(config)#interface ethernet0/1
*Aug 18 16:46:40.727: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config)#interface ethernet0/1
Cafe-01-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW2(config-if)#switchport mode trunk
Cafe-01-SW2(config-if)#ip dh
*Aug 18 16:47:18.828: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config-if)#ip dhcp snooping trust
Cafe-01-SW2(config-if)#exit
Cafe-01-SW2(config)#interface ethernet0/2
Cafe-01-SW2(config-if)#ip dh
*Aug 18 16:47:52.717: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config-if)#ip dhcp snooping limit rate 5
Cafe-01-SW2(config-if)#exit
Cafe-01-SW2(config)#
*Aug 18 16:48:27.673: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/2 TDR=0, TRC=0
Cafe-01-SW2(config)#$ Ethernet3/0 - 3 , Ethernet4/0 - 3 , Ethernet5/0 - 3    
Cafe-01-SW2(config-if-range)#ip dhcp snooping limit rate 20
Cafe-01-SW2(config-if-range)#exit
Cafe-01-SW2(config)#
*Aug 18 16:48:58.681: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config)#end
Cafe-01-SW2#
*Aug 18 16:49:01.892: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW2#show ip dhcp snooping binding
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
Total number of bindings: 0

Cafe-01-SW2#show ip dhcp snooping        
Switch DHCP snooping is enabled
Switch DHCP gleaning is disabled
DHCP snooping is configured on following VLANs:
1,10,20
DHCP snooping is operational on following VLANs:
1,10,20
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
Ethernet0/2                      no         no              5         
  Custom circuit-ids:
Ethernet1/1                      no         no              20        
  Custom circuit-ids:
Ethernet1/2                      no         no              20        
  Custom circuit-ids:
Ethernet1/3                      no         no              20        
  Custom circuit-ids:
Ethernet2/0                      no         no              20        
  Custom circuit-ids:
Ethernet2/1                      no         no              20        
  Custom circuit-ids:
Ethernet2/2                      no         no              20        
  Custom circuit-ids:
Ethernet2/3                      no         no              20        
  Custom circuit-ids:
Ethernet3/0                      no         no              20        
  Custom circuit-ids:
Ethernet3/1                      no         no              20        
  Custom circuit-ids:
Ethernet3/2                      no         no              20        
Interface                  Trusted    Allow option    Rate limit (pps)
-----------------------    -------    ------------    ----------------   
  Custom circuit-ids:
Ethernet3/3                      no         no              20        
  Custom circuit-ids:
Ethernet4/0                      no         no              20        
  Custom circuit-ids:
Ethernet4/1                      no         no              20        
  Custom circuit-ids:
Ethernet4/2                      no         no              20        
  Custom circuit-ids:
Ethernet4/3                      no         no              20        
  Custom circuit-ids:
Ethernet5/0                      no         no              20        
  Custom circuit-ids:
Ethernet5/1                      no         no              20        
  Custom circuit-ids:
Ethernet5/2                      no         no              20        
  Custom circuit-ids:
Ethernet5/3                      no         no              20        
  Custom circuit-ids:
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
eth0      Link encap:Ethernet  HWaddr 52:54:00:08:36:43  
          inet addr:10.1.20.11  Bcast:10.1.20.255  Mask:255.255.255.0
          inet6 addr: fe80::5054:ff:fe08:3643/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:6 errors:0 dropped:1 overruns:0 frame:0
          TX packets:115 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:1488 (1.4 KiB)  TX bytes:35366 (34.5 KiB)

cisco@cafe-01-pc:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.1.20.1       0.0.0.0         UG    0      0        0 eth0
10.1.20.0       0.0.0.0         255.255.255.0   U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@cafe-01-pc:~$ 


Connecting to console for Cafe-01-Plex

Core Linux
cafe-01-plex login: 
Core Linux
cafe-01-plex login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-01-plex:~$ sudo ifconfig eth0 0.0.0.0
cisco@cafe-01-plex:~$ sudo udhcpc -i eth0 -n -q
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.1.10.11, server 10.1.10.1
udhcpc: lease of 10.1.10.11 obtained from 10.1.10.1, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 1.1.1.1
cisco@cafe-01-plex:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:79:6A:A1  
          inet addr:10.1.10.11  Bcast:10.1.10.255  Mask:255.255.255.0
          inet6 addr: fe80::5054:ff:fe79:6aa1/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:6 errors:0 dropped:1 overruns:0 frame:0
          TX packets:115 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:1488 (1.4 KiB)  TX bytes:35366 (34.5 KiB)

cisco@cafe-01-plex:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.1.10.1       0.0.0.0         UG    0      0        0 eth0
10.1.10.0       0.0.0.0         255.255.255.0   U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
cisco@cafe-01-plex:~$ 


Cafe-Edge-R1#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address      Client-ID/              Lease expiration        Type       State      Interface
                Hardware address/
                User name
10.1.10.11      0152.5400.796a.a1       Aug 19 2026 04:50 PM    Automatic  Active     Ethernet0/0.10
10.1.20.11      0152.5400.0836.43       Aug 19 2026 04:50 PM    Automatic  Active     Ethernet0/0.20
Cafe-Edge-R1#


Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#ip arp inspection vlan 1,10,20
*Aug 18 16:52:34.309: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Cafe-01-SW1(config)#ip arp inspection vlan 1,10,20
Cafe-01-SW1(config)#ip arp inspection validate src-mac dst-mac ip
Cafe-01-SW1(config)#interface ethernet6/0
*Aug 18 16:53:09.903: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Cafe-01-SW1(config)#interface ethernet6/0
Cafe-01-SW1(config-if)#ip arp inspection trust
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#interface ethernet0/1                        
Cafe-01-SW1(config-if)#ip arp inspection trust
Cafe-01-SW1(config-if)#exit                   
Cafe-01-SW1(config)#interface ethernet1    
*Aug 18 16:53:50.023: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-01-SW1(config)#interface ethernet1/0
Cafe-01-SW1(config-if)#ip arp inspection trust
Cafe-01-SW1(config-if)#exit                   
Cafe-01-SW1(config)#end
Cafe-01-SW1#
*Aug 18 16:54:01.040: %SYS-5-CONFIG_I: Configured from console by console
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
Cafe-01-SW1#show ip arp inspection vla    
*Aug 18 16:54:20.118: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-01-SW1#show ip arp inspection interfaces

 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et0/0            Untrusted               15                 1
 Et0/1            Trusted               None               N/A
 Et0/2            Untrusted               15                 1
 Et0/3            Untrusted               15                 1
 Et1/0            Trusted               None               N/A
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
Cafe-01-SW2(config)#ip arp inspection c
*Aug 18 16:55:06.296: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/2 TDR=0, TRC=0
Cafe-01-SW2(config)#ip arp inspection vlan 1,10,20
Cafe-01-SW2(config)#ip arp inspection validate src-mac dst-mac ip
Cafe-01-SW2(config)#i
*Aug 18 16:55:39.185: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config)#interface ethernet0/1
Cafe-01-SW2(config-if)#ip arp inspection trust
Cafe-01-SW2(config-if)#exit
*Aug 18 16:56:09.759: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2(config-if)#exit
Cafe-01-SW2(config)#interface ethernet1/0  
Cafe-01-SW2(config-if)#ip arp inspection trust
Cafe-01-SW2(config-if)#exit                   
Cafe-01-SW2(config)#end
Cafe-01-SW2#
*Aug 18 16:56:27.813: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW2#show ip arp inspection vlan 1
*Aug 18 16:56:40.448: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/3 TDR=0, TRC=0
Cafe-01-SW2#show ip arp inspection vlan 10

Source Mac Validation      : Enabled
Destination Mac Validation : Enabled
IP Address Validation      : Enabled

 Vlan     Configuration    Operation   ACL Match          Static ACL
 ----     -------------    ---------   ---------          ----------
   10     Enabled          Active                         

 Vlan     ACL Logging      DHCP Logging      Probe Logging
 ----     -----------      ------------      -------------
   10     Deny             Deny              Off          
Cafe-01-SW2#show ip arp inspection interfaces

 Interface        Trust State     Rate (pps)    Burst Interval
 ---------------  -----------     ----------    --------------
 Et0/0            Untrusted               15                 1
 Et0/1            Trusted               None               N/A
 Et0/2            Untrusted               15                 1
 Et0/3            Untrusted               15                 1
 Et1/0            Trusted               None               N/A
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
 Et6/0            Untrusted               15                 1
 Et6/1            Untrusted               15                 1
 Et6/2            Untrusted               15                 1
 Et6/3            Untrusted               15                 1
Cafe-01-SW2#


cisco@cafe-01-pc:~$ sudo arp -d 10.1.20.1
arp: SIOCDARP(pub): No such file or directory
cisco@cafe-01-pc:~$ ping -c 3 10.1.20.1
PING 10.1.20.1 (10.1.20.1): 56 data bytes

--- 10.1.20.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@cafe-01-pc:~$ ! On Cafe-01-Plex
-sh: On: not found
cisco@cafe-01-pc:~$ sudo arp -d 10.1.10.1
arp: SIOCDARP(priv): Network is unreachable
cisco@cafe-01-pc:~$ ping -c 3 10.1.10.1


Cafe-01-PC may fail to ping 10.1.20.1 with 100% packet loss after DAI is enabled because the live switch snooping binding table remains empty.
```
