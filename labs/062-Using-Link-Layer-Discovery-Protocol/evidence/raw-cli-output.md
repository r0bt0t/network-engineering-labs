# Lab 062 - Raw CLI Output

```bash
S01>en
S01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
S01(config)#lldp run
S01(config)#end
*Aug 19 15:39:53.059: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 19 15:39:53.161: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 15:39:53.161: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 15:39:53.266: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
S01(config)#end
S01#
*Aug 19 15:39:53.366: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 19 15:39:53.366: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
S01#
*Aug 19 15:39:54.488: %SYS-5-CONFIG_I: Configured from console by console
S01#show lldp

Global LLDP Information:
    Status: ACTIVE
    LLDP advertisements are sent every 30 seconds
    LLDP hold time advertised is 120 seconds
    LLDP interface reinitialisation delay is 2 seconds
S01#show lldp neighbors
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID

Total entries displayed: 0

S01#



Connecting to console for R01

R01>en
R01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R01(config)#lldp run
R01(config)#
*Aug 19 15:41:12.564: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
R01(config)#end
*Aug 19 15:41:12.666: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 15:41:12.667: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 15:41:12.774: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
R01(config)#end
R01#
*Aug 19 15:41:12.875: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 19 15:41:12.875: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
R01#
*Aug 19 15:41:14.567: %SYS-5-CONFIG_I: Configured from console by console
R01#show lldp neighbours
                     ^
% Invalid input detected at '^' marker.

R01#show lldp neighbors  
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID
S01                 Et0/0          120        B,R             Et0/0

Total entries displayed: 1

R01#show lldp neighbors detail
------------------------------------------------
Local Intf: Et0/0
Local Intf service instance: -
Chassis id: aabb.cc00.0100
Port id: Et0/0
Port Description: Link to R01
System Name: S01

System Description: 
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX_L2-ADVENTERPRISEK9-M), Version 17.16.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 19-Dec-24 17:53 by m

Time remaining: 94 seconds
System Capabilities: B,R
Enabled Capabilities: B,R
Management Addresses:
    IP: 10.21.0.2
Auto Negotiation - supported, enabled
Physical media capabilities:
    1000baseT(FD)
Media Attachment Unit type - not advertised
Vlan ID: 1
Peer Source MAC: aabb.cc00.0100
          
          
Total entries displayed: 1
          
R01#


S01#
S01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
S01(config)#interface Ethernet0/0
S01(config-if)#no lldp transmit
S01(config-if)#end
S01#
*Aug 19 15:43:34.014: %SYS-5-CONFIG_I: Configured from console by console
S01#show running-config interface Ethernet0/0
Building configuration...

Current configuration : 72 bytes
!
interface Ethernet0/0
 description Link to R01
 no lldp transmit
end

S01#show lldp interface Ethernet0/0          

Ethernet0/0:
    Tx: disabled
    Rx: enabled
    Tx state: INIT
    Rx state: WAIT FOR FRAME
    
S01#show lldp neighbors            
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID
R01                 Et0/0          120        R               Et0/0

Total entries displayed: 1

S01#


R01#
R01#show lldp neighbors
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID

Total entries displayed: 0

R01#

```
