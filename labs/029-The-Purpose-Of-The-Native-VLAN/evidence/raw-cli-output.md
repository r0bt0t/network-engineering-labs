# Lab 029 - Raw CLI Output

```bash
Connecting to console for Cafe-SW1

Cafe-SW1>en
*Jun 26 08:19:21.615: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Jun 26 08:19:21.615: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
Cafe-SW1>en
Cafe-SW1#
*Jun 26 08:19:21.615: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
Cafe-SW1#show interface 
*Jun 26 08:19:31.652: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jun 26 08:19:31.754: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 26 08:19:31.755: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 26 08:19:31.859: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW1#show interface trun
*Jun 26 08:19:31.959: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jun 26 08:19:31.959: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW1#show interface trunk
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#show interfaces Ethernet0/1 switchport | include Admini$aces Ethernet0/1 switchport | include Administrative Mode|     $   
Name: Et0/1
Switchport: Enabled
Administrative Mode: dynamic auto
Operational Mode: static access
Administrative Trunking Encapsulation: negotiate
Operational Trunking Encapsulation: native
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
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
Trunking VLANs Enabled: ALL
Pruning VLANs Enabled: 2-1001
Capture Mode Disabled
Capture VLANs Allowed: ALL

Protected: false
Appliance trust: none
Cafe-SW1# 
Cafe-SW1#
Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1
10   VLAN0010                         active    Et0/2
20   VLAN0020                         active    Et0/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#show logging | include VLAN|Native
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#


Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#vlan 99
Cafe-SW1(config-vlan)#name MGMT-NATIVE
Cafe-SW1(config-vlan)#exit
Cafe-SW1(config)#interface ethernet0/1
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#switch
*Jun 26 08:22:24.730: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW1(config-if)#switchport 
*Jun 26 08:22:27.730: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-SW1(config-if)#switchport trunk native vlan 99
Cafe-SW1(config-if)#
*Jun 26 08:22:37.733: %SPANTREE-2-BLOCK_PVID_PEER: Blocking Ethernet0/1 on VLAN0001. Inconsistent peer vlan.
*Jun 26 08:22:37.733: %SPANTREE-2-BLOCK_PVID_LOCAL: Blocking Ethernet0/1 on VLAN0099. Inconsistent local vlan.
Cafe-SW1(config-if)#end
Cafe-SW1#
*Jun 26 08:22:40.172: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#
Cafe-SW1#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#show logging | include Native|mismatch
Cafe-SW1#


Cafe-SW2>
*Jun 26 08:19:25.515: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Jun 26 08:19:25.515: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
Cafe-SW2>
*Jun 26 08:19:25.515: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
Cafe-SW2>
*Jun 26 08:22:24.730: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW2>
*Jun 26 08:22:27.731: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-SW2>
*Jun 26 08:22:37.732: %SPANTREE-2-BLOCK_PVID_LOCAL: Blocking Ethernet0/1 on VLAN0001. Inconsistent local vlan.
Cafe-SW2>
*Jun 26 08:23:23.843: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (1), with Cafe-SW1 Ethernet0/1 (99).
Cafe-SW2>
*Jun 26 08:24:15.264: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (1), with Cafe-SW1 Ethernet0/1 (99).
Cafe-SW2>
Cafe-SW2>
Cafe-SW2>en
Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#
*Jun 26 08:24:55.594: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW2(config)#
*Jun 26 08:24:55.696: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 26 08:24:55.696: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 26 08:24:55.802: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW2(config)#
*Jun 26 08:24:55.902: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 26 08:24:55.902: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW2(config)#vlan 99
Cafe-SW2(config-vlan)#name MGMT-NATIVE
Cafe-SW2(config-vlan)#exit
Cafe-SW2(config)#
*Jun 26 08:25:14.190: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (1), with Cafe-SW1 Ethernet0/1 (99).
Cafe-SW2(config)#interfa
*Jun 26 08:25:15.754: %SPANTREE-2-BLOCK_PVID_PEER: Blocking Ethernet0/1 on VLAN0099. Inconsistent peer vlan.
Cafe-SW2(config)#interface ethernet0/1
Cafe-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-SW2(config-if)#switchport mode trunk
Cafe-SW2(config-if)#switchport trunk native vlan 99
Cafe-SW2(config-if)#end
Cafe-SW2#sh
*Jun 26 08:26:08.734: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show interface trunk | begin P
*Jun 26 08:26:18.758: %SPANTREE-2-UNBLOCK_CONSIST_PORT: Unblocking Ethernet0/1 on VLAN0099. Port consistency restored.
*Jun 26 08:26:18.758: %SPANTREE-2-UNBLOCK_CONSIST_PORT: Unblocking Ethernet0/1 on VLAN0001. Port consistency restored.
Cafe-SW2#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      99

Port           Vlans allowed on trunk
Et0/1          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20,99

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20,99
Cafe-SW2#
Cafe-SW2#show logging | include Native|mismatch
*Jun 26 08:23:23.843: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (1), with Cafe-SW1 Ethernet0/1 (99).
*Jun 26 08:24:15.264: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (1), with Cafe-SW1 Ethernet0/1 (99).
*Jun 26 08:25:14.190: %CDP-4-NATIVE_VLAN_MISMATCH: Native VLAN mismatch discovered on Ethernet0/1 (1), with Cafe-SW1 Ethernet0/1 (99).
Cafe-SW2#
```
