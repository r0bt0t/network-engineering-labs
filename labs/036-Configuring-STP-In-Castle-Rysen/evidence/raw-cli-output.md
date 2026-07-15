# Lab 036 - Raw CLI Output

```bash
Connecting to console for Cafe-SW1
Connected to CML terminalserver.

*Jul  7 14:50:56.734: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Jul  7 14:50:56.734: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
Cafe-SW1>
*Jul  7 14:50:56.734: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
Cafe-SW1>en
*Jul  7 14:51:08.441: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Cafe-SW1>en
Cafe-SW1#show i
*Jul  7 14:51:16.773: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW1#show in
*Jul  7 14:51:16.874: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:51:16.875: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:51:16.980: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW1#show i 
*Jul  7 14:51:17.080: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul  7 14:51:17.080: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  up                    up      
Ethernet1/1            unassigned      YES unset  up                    up      
Ethernet1/2            unassigned      YES unset  up                    up      
Ethernet1/3            unassigned      YES unset  up                    up      
Cafe-SW1#show vlan

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
 --More-- 
*Jul  7 14:51:38.444: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
 --More-- 
*Jul  7 14:52:08.447: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
          
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
------- --------- ----------------- ------------------------------------------

Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#vlan 10
Cafe-SW1(config-vlan)#
*Jul  7 14:52:38.449: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Cafe-SW1(config-vlan)#vlan 20
Cafe-SW1(config-vlan)#spanning-tree mode rapid-pvst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Cafe-SW1(config)#end
Cafe-SW1#
*Jul  7 14:53:13.916: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Cafe-SW1#sh
*Jul  7 14:53:14.016: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: none
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     0         0        0          8          8
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       0         0        0          8          8
Cafe-SW1#


Connecting to console for Cafe-SW2

Cafe-SW2>
*Jul  7 14:51:00.355: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Jul  7 14:51:00.355: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
Cafe-SW2>
*Jul  7 14:51:00.355: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
Cafe-SW2>en
Cafe-SW2#show vlan

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
 --More-- 
*Jul  7 14:52:00.404: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul  7 14:52:00.506: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:52:00.507: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:52:00.612: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
 --More-- 
*Jul  7 14:52:00.712: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul  7 14:52:00.712: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
          
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
------- --------- ----------------- ------------------------------------------

Cafe-SW2#
*Jul  7 14:52:40.397: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)# vlan 10
Cafe-SW2(config-vlan)#vlan 20
Cafe-SW2(config-vlan)#spanning-tree mode rapid-pvst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Cafe-SW2(config)#end
Cafe-SW2#sh
*Jul  7 14:54:37.742: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: none
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     1         0        0          7          8
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       1         0        0          7          8
Cafe-SW2#



Connecting to console for Fallout-SW1

Fallout-SW1>
*Jul  7 14:51:03.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW1>
*Jul  7 14:52:03.315: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW1>
*Jul  7 14:52:33.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW1>
*Jul  7 14:53:33.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW1>
*Jul  7 14:54:03.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW1>en
Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#v
*Jul  7 14:55:09.463: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Fallout-SW1(config)#vlan 
*Jul  7 14:55:09.565: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:55:09.565: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:55:09.672: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Fallout-SW1(config)#vlan 10
Fallout-SW1(config-vlan)#
*Jul  7 14:55:09.772: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul  7 14:55:09.772: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Fallout-SW1(config-vlan)#vlan 20
Fallout-SW1(config-vlan)#vlan 30
Fallout-SW1(config-vlan)#vlan 40
Fallout-SW1(config-vlan)#spanning-tree 
*Jul  7 14:55:33.317: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/2 TDR=0, TRC=0
Fallout-SW1(config-vlan)#spanning-tree mode rapid-pvst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW1(config)#end
Fallout-SW1#sho
*Jul  7 14:55:44.685: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW1#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: VLAN0001
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     0         0        0          8          8
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       0         0        0          8          8
Fallout-SW1#


Connecting to console for Fallout-SW2

Fallout-SW2>
*Jul  7 14:51:33.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Fallout-SW2>
*Jul  7 14:52:33.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Fallout-SW2>
*Jul  7 14:55:03.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Fallout-SW2>en
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#
*Jul  7 14:56:13.354: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul  7 14:56:13.456: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:56:13.456: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:56:13.563: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Fallout-SW2(config)#val
*Jul  7 14:56:13.663: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul  7 14:56:13.663: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Fallout-SW2(config)#vlan 10
Fallout-SW2(config-vlan)#vlan 20
Fallout-SW2(config-vlan)#vlan 30
Fallout-SW2(config-vlan)#vlan 40
Fallout-SW2(config-vlan)#spanning-tree mode rapid-pvst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW2(config)#end
Fallout-SW2#show s
*Jul  7 14:56:42.926: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW2#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: none
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     1         0        0          7          8
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       1         0        0          7          8
Fallout-SW2#


Connecting to console for Fallout-SW3

Fallout-SW3>
*Jul  7 14:51:03.875: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Jul  7 14:51:03.875: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
Fallout-SW3>
*Jul  7 14:51:03.876: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
Fallout-SW3>
*Jul  7 14:51:43.915: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Fallout-SW3>
*Jul  7 14:52:13.915: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Fallout-SW3>
*Jul  7 14:53:33.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW3>
*Jul  7 14:55:03.316: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW3>
*Jul  7 14:56:03.317: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW3>en
Fallout-SW3#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW3(config)#vlan 10
Fallout-SW3(config-vlan)#vlan 20
Fallout-SW3(config-vlan)#vlan 
*Jul  7 14:57:23.966: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul  7 14:57:24.067: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:57:24.068: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul  7 14:57:24.174: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Fallout-SW3(config-vlan)#vlan 30
*Jul  7 14:57:24.274: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul  7 14:57:24.274: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Fallout-SW3(config-vlan)#vlan 30
Fallout-SW3(config-vlan)#vlan 40
Fallout-SW3(config-vlan)#spanning-tree mode
*Jul  7 14:57:33.318: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW3(config-vlan)#spanning-tree mode rapid-pvst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW3(config)#end
Fallout-SW3#show span
*Jul  7 14:57:43.155: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW3#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: none
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     1         0        0          7          8
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       1         0        0          7          8
Fallout-SW3#


Cafe-SW1#
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#spanning-tree vlan 1
*Jul  7 14:58:33.318: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Cafe-SW1(config)#spanning-tree vlan 1,10,20 root primary
Cafe-SW1(config)#end
Cafe-SW1#
*Jul  7 14:58:50.497: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#
Cafe-SW1#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: none
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     0         0        0          8          8
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       0         0        0          8          8
Cafe-SW1#
*Jul  7 14:54:08.467: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/1 TDR=0, TRC=0
Cafe-SW1#
*Jul  7 14:55:33.317: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Cafe-SW1#
*Jul  7 14:56:33.317: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Cafe-SW1#
*Jul  7 14:57:08.480: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#spanning-tree vlan 1
*Jul  7 14:58:33.318: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Cafe-SW1(config)#spanning-tree vlan 1,10,20 root primary
Cafe-SW1(config)#end
Cafe-SW1#
*Jul  7 14:58:50.497: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show spanning-tree vlan 10

Spanning tree instance(s) for vlan 10 does not exist.

Cafe-SW1#show spanning-tree vlan 1 

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    24577
             Address     aabb.cc00.0300
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    24577  (priority 24576 sys-id-ext 1)
             Address     aabb.cc00.0300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 
Et0/3               Desg FWD 100       128.4    P2p 
Et1/0               Desg FWD 100       128.5    P2p 
Et1/1               Desg FWD 100       128.6    P2p 
Et1/2               Desg FWD 100       128.7    P2p 
Et1/3               Desg FWD 100       128.8    P2p 
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------


Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#spanning-tree vlan 1,10,20 root secondary
Cafe-SW2(config)#end
Cafe-SW2#sh
*Jul  7 15:01:08.360: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show spanning-tree vlan 10

Spanning tree instance(s) for vlan 10 does not exist.

Cafe-SW2#
*Jul  7 15:04:33.318: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Cafe-SW2#show spanning-tree vlan 1 

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    24577
             Address     aabb.cc00.0300
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    28673  (priority 28672 sys-id-ext 1)
             Address     aabb.cc00.0400
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 
Et0/3               Desg FWD 100       128.4    P2p 
Et1/0               Desg FWD 100       128.5    P2p 
Et1/1               Desg FWD 100       128.6    P2p 
Et1/2               Desg FWD 100       128.7    P2p 
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------

Et1/3               Desg FWD 100       128.8    P2p 


Fallout-SW1>en
Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#spanning-tree vlan 1,10,20,30,40 priority 4096
Fallout-SW1(config)#end
Fallout-SW1#
*Jul  7 15:06:32.952: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW1#show spanning-tree vlan 30

Spanning tree instance(s) for vlan 30 does not exist.

Fallout-SW1#show spanning-tree vlan 1 

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    4097
             Address     aabb.cc00.0100
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    4097   (priority 4096 sys-id-ext 1)
             Address     aabb.cc00.0100
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 
Et0/3               Desg FWD 100       128.4    P2p 
Et1/0               Desg FWD 100       128.5    P2p 
Et1/1               Desg FWD 100       128.6    P2p 
Et1/2               Desg FWD 100       128.7    P2p 
Et1/3               Desg FWD 100       128.8    P2p 
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------



Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#spanning-tree 
*Jul  7 15:07:34.022: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
Fallout-SW2(config)#spanning-tree vlan 1,10,20,30,40 priority 8192
Fallout-SW2(config)#end
Fallout-SW2#sh
*Jul  7 15:07:49.565: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW2#show spanning-tree vlan 30

Spanning tree instance(s) for vlan 30 does not exist.

Fallout-SW2#show spanning-tree vlan 1 

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    4097
             Address     aabb.cc00.0100
             Cost        100
             Port        7 (Ethernet1/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    8193   (priority 8192 sys-id-ext 1)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 
Et0/3               Desg FWD 100       128.4    P2p 
Et1/0               Desg FWD 100       128.5    P2p 
Et1/1               Desg FWD 100       128.6    P2p 
Et1/2               Root FWD 100       128.7    P2p 
Et1/3               Altn BLK 100       128.8    P2p 
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------



Fallout-SW2#


Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#int
Cafe-SW1(config)#interface eth
Cafe-SW1(config)#interface ethernet0/1
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#swi
*Jul  7 15:09:41.628: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW1(config-if)#switchport trun
*Jul  7 15:09:44.628: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-SW1(config-if)#switchport trunk allowed vlan 1,10,20
Cafe-SW1(config-if)#exit
Cafe-SW1(config)#interface ethernet0/2                
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q 
Cafe-SW1(config-if)#switchport mode trunk                
Cafe-SW1(config-if)#switchport trunk allowed vlan 1,10,20
*Jul  7 15:10:08.702: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW1(config-if)#switchport trunk allowed vlan 1,10,20
*Jul  7 15:10:11.702: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW1(config-if)#switchport trunk allowed vlan 1,10,20,30,40
Cafe-SW1(config-if)#end
Cafe-SW1#s
*Jul  7 15:10:23.042: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1,10,20
Et0/2          1,10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          1,10,20
Et0/2          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20
Et0/2          1,10,20
Cafe-SW1#


Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#int
Cafe-SW2(config)#interface eth 
Cafe-SW2(config)#interface ethernet0/1
Cafe-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-SW2(config-if)#switchport mode trunk
Cafe-SW2(config-if)#switchport a
*Jul  7 15:11:43.925: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Cafe-SW2(config-if)#switchport trunk allowed vlan 1,10,20
Cafe-SW2(config-if)#exit
Cafe-SW2(config)#interface ethernet0/2                
Cafe-SW2(config-if)#switchport trunk encapsulation dot1q 
Cafe-SW2(config-if)#switchport mode trunk                
Cafe-SW2(config-if)#switchport trunk allowed vlan 1,10,20
*Jul  7 15:12:16.765: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW2(config-if)#switchport trunk allowed vlan 1,10,20,30,40
*Jul  7 15:12:19.765: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW2(config-if)#switchport trunk allowed vlan 1,10,20,30,40
Cafe-SW2(config-if)#end
Cafe-SW2#sw
*Jul  7 15:12:23.987: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1,10,20
Et0/2          1,10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          1,10,20
Et0/2          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20
Et0/2          1,10,20
Cafe-SW2#


Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#int
Fallout-SW1(config)#interface eth
Fallout-SW1(config)#interface ethernet0/1
Fallout-SW1(config-if)#switchport trunk encapsulation dot1q
Fallout-SW1(config-if)#switchport mode trunk 
Fallout-SW1(config-if)#switchport trunk allowed vlan 1,10,20,30,40
Fallout-SW1(config-if)#exit
Fallout-SW1(config)#interface ethernet0/3                      
Fallout-SW1(config-if)#switchport trunk encapsulation dot1q       
Fallout-SW1(config-if)#switchport mode trunk                      
Fallout-SW1(config-if)#switchport trunk allowed vlan 1,10,20,30,40
*Jul  7 15:14:34.146: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down
Fallout-SW1(config-if)#switchport trunk allowed vlan 1,10,20,30,40
Fallout-SW1(config-if)#
*Jul  7 15:14:37.146: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to up
Fallout-SW1(config-if)#exit
Fallout-SW1(config)#interface range ethernet1/2 - 3            
Fallout-SW1(config-if-range)#switchport trunk encapsulation dot1q       
Fallout-SW1(config-if-range)#switchport mode trunk                      
Fallout-SW1(config-if-range)#switchport trunk allowed vlan 1,10,20,30,40
*Jul  7 15:15:13.157: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jul  7 15:15:13.159: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Fallout-SW1(config-if-range)#switchport trunk allowed vlan 1,10,20,30,40
*Jul  7 15:15:15.173: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW1(config-if-range)#switchport trunk allowed vlan 1,10,20,30,40
Fallout-SW1(config-if-range)#
*Jul  7 15:15:16.157: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
*Jul  7 15:15:16.159: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to up
Fallout-SW1(config-if-range)#spanning-tree link-type point-to-point     
Fallout-SW1(config-if-range)#end
Fallout-SW1#
*Jul  7 15:15:46.549: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW1#show inte
*Jul  7 15:15:47.751: %AMDP2_FE-6-EXCESSCOLL: Ethernet1/3 TDR=0, TRC=0
Fallout-SW1#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/3          on               802.1q         trunking      1
Et1/2          on               802.1q         trunking      1
Et1/3          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1,10,20,30,40
Et0/3          1,10,20,30,40
Et1/2          1,10,20,30,40
Et1/3          1,10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          1,10,20,30,40
Et0/3          1,10,20,30,40
Et1/2          1,10,20,30,40
Et1/3          1,10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20,30,40
Et0/3          1,10,20,30,40
Et1/2          1,10,20,30,40
Et1/3          1,10,20,30,40
Fallout-SW1#


Fallout-SW2#
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#int
Fallout-SW2(config)#interface eth
Fallout-SW2(config)#interface ethernet0/1
Fallout-SW2(config-if)#switchport trunk encapsulation dot1q 
Fallout-SW2(config-if)#switchport mode trunk
Fallout-SW2(config-if)#switchport trunk allowed vlan 1,10,20,30,40
Fallout-SW2(config-if)#exit
Fallout-SW2(config)#interface ethernet0/3                      
Fallout-SW2(config-if)#switchport trunk encapsulation dot1q       
Fallout-SW2(config-if)#switchport mode trunk                      
Fallout-SW2(config-if)#switchport trunk allowed vlan 1,10,20,30,40
Fallout-SW2(config-if)#
*Jul  7 15:17:34.032: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down
Fallout-SW2(config-if)#exit
*Jul  7 15:17:37.032: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to up
Fallout-SW2(config-if)#exit
Fallout-SW2(config)#interface range ethernet1/2 - 3            
Fallout-SW2(config-if-range)#switchport trunk encapsulation dot1q       
Fallout-SW2(config-if-range)#switchport mode trunk                      
Fallout-SW2(config-if-range)#switchport trunk allowed vlan 1,10,20,30,40
Fallout-SW2(config-if-range)#spanning-tree link-type point-to-point
Fallout-SW2(config-if-range)#end
Fallout-SW2#show spa
*Jul  7 15:18:28.599: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW2#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/3          on               802.1q         trunking      1
Et1/2          on               802.1q         trunking      1
Et1/3          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1,10,20,30,40
Et0/3          1,10,20,30,40
Et1/2          1,10,20,30,40
Et1/3          1,10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          1,10,20,30,40
Et0/3          1,10,20,30,40
Et1/2          1,10,20,30,40
Et1/3          1,10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20,30,40
Et0/3          1,10,20,30,40
Et1/2          1,10,20,30,40
Et1/3          none
Fallout-SW2#


Fallout-SW3>en 
Fallout-SW3#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW3(config)#interface range ethernet0/1 - 2
Fallout-SW3(config-if-range)#switchport trunk encapsulation dot1q
Fallout-SW3(config-if-range)#switchport mode trunk
Fallout-SW3(config-if-range)#switchport trunk allowed vlan 1,10,20,30,40
Fallout-SW3(config-if-range)#end
Fallout-SW3#sh
*Jul  7 15:20:22.702: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW3#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1,10,20,30,40
Et0/2          1,10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          1,10,20,30,40
Et0/2          1,10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20,30,40
Et0/2          none
Fallout-SW3#show spanning-tree vlan 30

VLAN0030
  Spanning tree enabled protocol rstp
  Root ID    Priority    4126
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32798  (priority 32768 sys-id-ext 30)
             Address     aabb.cc00.0500
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 


Fallout-SW3#


Cafe-SW1>en
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#interface range ethernet0/3, ethernet1/0 - 3
Cafe-SW1(config-if-range)#switchport mode access
Cafe-SW1(config-if-range)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast will be configured in 5 interfaces due to the range command 
 but will only have effect when the interfaces are in a non-trunking mode.
Cafe-SW1(config-if-range)#spanning-tree bpduguard enable
Cafe-SW1(config-if-range)#end
Cafe-SW1#show
*Jul  7 15:22:43.960: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0001 is designated forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 4097, address aabb.cc00.0100
   Designated bridge has priority 24577, address aabb.cc00.0300
   Designated port id is 128.4, designated path cost 100
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   The port is in the portfast mode
   Link type is point-to-point by default
   Bpdu guard is enabled
   BPDU: sent 1001, received 0
Cafe-SW1#


Fallout-SW3#
Fallout-SW3#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW3(config)#interface range ethernet0/0, ethernet0/3, ethernet1/0 - 3
Fallout-SW3(config-if-range)#switchport mode access
Fallout-SW3(config-if-range)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast will be configured in 6 interfaces due to the range command 
 but will only have effect when the interfaces are in a non-trunking mode.
Fallout-SW3(config-if-range)#spanning-tree bpduguard enable
Fallout-SW3(config-if-range)#end
Fallout-SW3#s
*Jul  7 15:24:40.919: %SYS-5-CONFIG_I: Configured from console by console
Fallout-SW3#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0001 is designated forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 4097, address aabb.cc00.0100
   Designated bridge has priority 32769, address aabb.cc00.0500
   Designated port id is 128.4, designated path cost 100
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   The port is in the portfast mode
   Link type is point-to-point by default
   Bpdu guard is enabled
   BPDU: sent 1054, received 0
Fallout-SW3#


Cafe-SW1#
Cafe-SW1#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    4106
             Address     aabb.cc00.0100
             Cost        100
             Port        3 (Ethernet0/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    24586  (priority 24576 sys-id-ext 10)
             Address     aabb.cc00.0300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Root FWD 100       128.3    P2p 


Cafe-SW1#



Cafe-SW2>
Cafe-SW2>en
Cafe-SW2#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    4106
             Address     aabb.cc00.0100
             Cost        200
             Port        3 (Ethernet0/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    28682  (priority 28672 sys-id-ext 10)
             Address     aabb.cc00.0400
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Altn BLK 100       128.2    P2p 
Et0/2               Root FWD 100       128.3    P2p 


Cafe-SW2#
```
