# Lab 063 - Raw CLI Output

```bash
Cafe-Core-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Core-R1(config)#cdp run
Cafe-Core-R1(config)#end
Cafe-Core-R1#
*Aug 19 15:58:16.403: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Core-R1#show cdp
Global CDP information:
        Sending CDP packets every 60 seconds
        Sending a holdtime value of 180 seconds
        Sending CDPv2 advertisements is enabled
Cafe-Core-R1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID

Total cdp entries displayed : 0
Cafe-Core-R1#show cdp neighbors detail

Total cdp entries displayed : 0


Connecting to console for Cafe-Access-SW1

Cafe-Access-SW1>en
Cafe-Access-SW1#
*Aug 19 15:59:45.773: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-Access-SW1#co
*Aug 19 15:59:45.875: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 15:59:45.876: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 15:59:45.984: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-Access-SW1#conf 
*Aug 19 15:59:46.084: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 19 15:59:46.084: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-Access-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Access-SW1(config)#cdp run
Cafe-Access-SW1(config)#end
Cafe-Access-SW1#
*Aug 19 15:59:56.478: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Access-SW1#


Cafe-Core-R1#show cdp neighbors       
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-Access-SW1  Eth 0/0           176             R S I  Linux Uni Eth 0/0

Total cdp entries displayed : 1
Cafe-Core-R1#show cdp neighbors detail
-------------------------
Device ID: Cafe-Access-SW1
Entry address(es): 
  IP address: 192.168.21.2
Platform: Linux Unix,  Capabilities: Router Switch IGMP 
Interface: Ethernet0/0,  Port ID (outgoing port): Ethernet0/0
Holdtime : 171 sec

Version :
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX_L2-ADVENTERPRISEK9-M), Version 17.16.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 19-Dec-24 17:53 by mcpre

advertisement version: 2
Peer Source MAC: aabb.cc00.0100
VTP Management Domain: ''
Native VLAN: 1
Duplex: full
Management address(es): 
  IP address: 192.168.21.2

          
Total cdp entries displayed : 1
Cafe-Core-R1#


Cafe-Core-R1#telnet 192.168.21.2
Trying 192.168.21.2 ... Open


User Access Verification

Password: 
Cafe-Access-SW1>en
% No password set
Cafe-Access-SW1>


Cafe-Access-SW1#show cdp
Global CDP information:
        Sending CDP packets every 60 seconds
        Sending a holdtime value of 180 seconds
        Sending CDPv2 advertisements is enabled
Cafe-Access-SW1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-Lobby-AP1   Eth 1/0           157               R    Linux Uni Eth 0/0
Cafe-Core-R1     Eth 0/0           179               R    Linux Uni Eth 0/0

Total cdp entries displayed : 2
Cafe-Access-SW1#show cdp neighbors detail
-------------------------
Device ID: Cafe-Lobby-AP1
Entry address(es): 
  IP address: 192.168.50.2
Platform: Linux Unix,  Capabilities: Router 
Interface: Ethernet1/0,  Port ID (outgoing port): Ethernet0/0
Holdtime : 145 sec

Version :
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.16.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 19-Dec-24 17:54 by mcpre

advertisement version: 2
Peer Source MAC: aabb.cc00.0300
Duplex: full
Management address(es): 
  IP address: 192.168.50.2

-------------------------
Device ID: Cafe-Core-R1
Entry address(es): 
  IP address: 192.168.21.1
Platform: Linux Unix,  Capabilities: Router 
Interface: Ethernet0/0,  Port ID (outgoing port): Ethernet0/0
Holdtime : 167 sec

Version :
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.16.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 19-Dec-24 17:54 by mcpre

advertisement version: 2
Peer Source MAC: aabb.cc00.0200
Duplex: full
Management address(es): 
  IP address: 192.168.21.1


Total cdp entries displayed : 2
Cafe-Access-SW1#


Cafe-Access-SW1#
Cafe-Access-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Access-SW1(config)#interface Ethernet1/0
Cafe-Access-SW1(config-if)#no cdp transmit
                                   ^
% Invalid input detected at '^' marker.

Cafe-Access-SW1(config-if)#no cdp ?
  enable           Enable CDP on interface
  filter-tlv-list  Apply tlv list filter on interface
  log              Log messages generated by CDP
  tlv              Enable exchange of specific tlv information

Cafe-Access-SW1(config-if)#no cdp enable
Cafe-Access-SW1(config-if)#end
Cafe-Access-SW1#
*Aug 19 16:07:56.918: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Access-SW1#show running-config interface Ethernet1/0
Building configuration...

Current configuration : 150 bytes
!
interface Ethernet1/0
 description Guest services drop toward Cafe-Lobby-AP1
 switchport access vlan 20
 switchport mode access
 no cdp enable
end

Cafe-Access-SW1#show cdp interface Ethernet1/0
 CDP is not enabled on interface Ethernet1/0

Cafe-Access-SW1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-Lobby-AP1   Eth 1/0           58                R    Linux Uni Eth 0/0
Cafe-Core-R1     Eth 0/0           144               R    Linux Uni Eth 0/0

Total cdp entries displayed : 2
Cafe-Access-SW1#


Field-Relay-R01>
Field-Relay-R01>en
Field-Relay-R01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Field-Relay-R01(config)#
*Aug 19 16:11:42.439: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 19 16:11:42.541: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 16:11:42.542: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 16:11:42.651: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Field-Relay-R01(config)#
*Aug 19 16:11:42.751: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 19 16:11:42.751: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Field-Relay-R01(config)#run lldp
                         ^
% Invalid input detected at '^' marker.

Field-Relay-R01(config)#lldp run
Field-Relay-R01(config)#end
Field-Relay-R01#show
*Aug 19 16:12:09.157: %SYS-5-CONFIG_I: Configured from console by console
Field-Relay-R01#show lldp 

Global LLDP Information:
    Status: ACTIVE
    LLDP advertisements are sent every 30 seconds
    LLDP hold time advertised is 120 seconds
    LLDP interface reinitialisation delay is 2 seconds
Field-Relay-R01#show lldp neighbors
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID

Total entries displayed: 0

Field-Relay-R01#


Cafe-Access-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Access-SW1(config)#lldp run
*Aug 19 16:13:04.969: %SYS-6-TTY_EXPIRE_TIMER: (exec timer expired, tty 2 (192.168.21.1)), user 
Cafe-Access-SW1(config)#lldp run
Cafe-Access-SW1(config)#end
Cafe-Access-SW1#sh
*Aug 19 16:13:12.115: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Access-SW1#show lldp

Global LLDP Information:
    Status: ACTIVE
    LLDP advertisements are sent every 30 seconds
    LLDP hold time advertised is 120 seconds
    LLDP interface reinitialisation delay is 2 seconds
Cafe-Access-SW1#show lldp neighbors
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID
Field-Relay-R01     Et0/1          120        R               Et0/0

Total entries displayed: 1

Cafe-Access-SW1#


Cafe-Access-SW1#
Cafe-Access-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Access-SW1(config)#interface Ethernet0/1
Cafe-Access-SW1(config-if)#no lldp transmit
Cafe-Access-SW1(config-if)#end
Cafe-Access-SW1#
*Aug 19 16:15:32.781: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Access-SW1#show running-config interface Ethernet0/1
Building configuration...

Current configuration : 120 bytes
!
interface Ethernet0/1
 description Link to Field-Relay-R01 Ethernet0/0
 switchport mode access
 no lldp transmit
end

Cafe-Access-SW1#show lldp interface Ethernet0/1

Ethernet0/1:
    Tx: disabled
    Rx: enabled
    Tx state: INIT
    Rx state: WAIT FOR FRAME
    
Cafe-Access-SW1#show lldp neighbors
Capability codes:
    (R) Router, (B) Bridge, (T) Telephone, (C) DOCSIS Cable Device
    (W) WLAN Access Point, (P) Repeater, (S) Station, (O) Other

Device ID           Local Intf     Hold-time  Capability      Port ID
Field-Relay-R01     Et0/1          120        R               Et0/0

Total entries displayed: 1

Cafe-Access-SW1#
```
