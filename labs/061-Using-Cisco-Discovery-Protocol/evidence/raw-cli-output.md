# Lab 061 - Raw CLI Output

```bash
Connecting to console for Cafe-Core-R1

Cafe-Core-R1>en
Cafe-Core-R1#show cdp
Global CDP information:
        Sending CDP packets every 60 seconds
        Sending a holdtime value of 180 seconds
        Sending CDPv2 advertisements is enabled
Cafe-Core-R1#show cdp 
*Aug 19 15:17:24.930: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-Core-R1#show cdp n
*Aug 19 15:17:25.032: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 15:17:25.033: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 19 15:17:25.138: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-Core-R1#show cdp neighb
*Aug 19 15:17:25.238: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 19 15:17:25.238: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-Core-R1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-Access-SW1  Eth 0/0           151             R S I  Linux Uni Eth 0/0

Total cdp entries displayed : 1
Cafe-Core-R1#


onnecting to console for Cafe-Core-R1

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
Cafe-Access-SW1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-Lobby-AP1   Eth 1/0           128               R    Linux Uni Eth 0/0
Cafe-Core-R1     Eth 0/0           153               R    Linux Uni Eth 0/0

Total cdp entries displayed : 2
Cafe-Access-SW1>show cdp neighbors detail
-------------------------
Device ID: Cafe-Lobby-AP1
Entry address(es): 
  IP address: 192.168.50.2
Platform: Linux Unix,  Capabilities: Router 
Interface: Ethernet1/0,  Port ID (outgoing port): Ethernet0/0
Holdtime : 121 sec

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
Holdtime : 146 sec

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
Cafe-Access-SW1>



Cafe-Access-SW1>en
Cafe-Access-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-Access-SW1(config)#int ethernet1/0
Cafe-Access-SW1(config-if)#no cdp enable
Cafe-Access-SW1(config-if)#end
Cafe-Access-SW1#
*Aug 19 15:26:01.287: %SYS-5-CONFIG_I: Configured from console by console
Cafe-Access-SW1#show running-config interface Ethernet1/0
Building configuration...

Current configuration : 174 bytes
!
interface Ethernet1/0
 description Guest services drop toward Cafe-Lobby-AP1 (lab step: Ethernet0/4)
 switchport access vlan 20
 switchport mode access
 no cdp enable
end

Cafe-Access-SW1#
Cafe-Access-SW1#
Cafe-Access-SW1#show cdp interface Ethernet1/0
 CDP is not enabled on interface Ethernet1/0

Cafe-Access-SW1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-Lobby-AP1   Eth 1/0           100               R    Linux Uni Eth 0/0
Cafe-Core-R1     Eth 0/0           133               R    Linux Uni Eth 0/0

Total cdp entries displayed : 2
Cafe-Access-SW1#


Cafe-Access-SW1#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Cafe-Core-R1     Eth 0/0           173               R    Linux Uni Eth 0/0

Total cdp entries displayed : 1
Cafe-Access-SW1#
```
