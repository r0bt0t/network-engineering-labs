# Lab 041 - Raw CLI Output

```bash
Connecting to console for Cafe-SW01

*Jul 16 20:19:10.731: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.

User Access Verification

Username: 
% Username:  timeout expired!
Username: castle
Password: 
Cafe-SW01#
*Jul 16 20:20:22.879: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: castle] [Source: LOCAL] [localport: 0] at 20:20:22 UTC Thu Jul 16 2026
Cafe-SW01#terminal length 0
Cafe-SW01#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        100
             Port        4 (Ethernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 
Et0/3               Root FWD 100       128.4    P2p 


Cafe-SW01#show spanning-tree interface ethernet0/1

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Desg FWD 100       128.2    P2p 
Cafe-SW01#show spanning-tree interface ethernet0/2

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Desg FWD 100       128.3    P2p 
Cafe-SW01#show interface trunk                    
Cafe-SW01#show interfaces trunk
Cafe-SW01#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
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

Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 0
Number of aggregators:           0

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------

Cafe-SW01#


Username: castle
Password: 
Cafe-SW02#
*Jul 16 20:25:00.704: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: castle] [Source: LOCAL] [localport: 0] at 20:25:00 UTC Thu Jul 16 2026
Cafe-SW02#
Cafe-SW02#
Cafe-SW02#terminal length 0
Cafe-SW02#show spaning-tree
                   ^
% Invalid input detected at '^' marker.

Cafe-SW02#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        200
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0400
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 
Et0/3               Desg FWD 100       128.4    P2p 


Cafe-SW02#show vlan

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
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

Cafe-SW02#show interfaces trunk
Cafe-SW02#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 0
Number of aggregators:           0

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------




Username: castle
Password: 
Shelter-SW01#
*Jul 16 20:27:22.280: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: castle] [Source: LOCAL] [localport: 0] at 20:27:22 UTC Thu Jul 16 2026
Shelter-SW01#
Shelter-SW01#
Shelter-SW01#terminal length 0
Shelter-SW01#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        100
             Port        4 (Ethernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 
Et0/3               Root FWD 100       128.4    P2p 
Et1/0               Desg FWD 100       128.5    P2p 
Et1/1               Desg FWD 100       128.6    P2p 
Et1/2               Desg FWD 100       128.7    P2p 
Et1/3               Desg FWD 100       128.8    P2p 


Shelter-SW01#show vlan

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
------- --------- ----------------- ------------------------------------------

Shelter-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 0
Number of aggregators:           0

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------

Shelter-SW01#show interfaces trunk
Shelter-SW01#


Shelter-SW02#terminal length 0
Shelter-SW02#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        200
             Port        7 (Ethernet1/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0500
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


Shelter-SW02#show vlan

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
------- --------- ----------------- ------------------------------------------

Shelter-SW02#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 0
Number of aggregators:           0

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------

Shelter-SW02#show interfaces trunk
Shelter-SW02#


Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#interface range ether
*Jul 16 20:32:00.867: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW01(config)#interface range ethernet
*Jul 16 20:32:00.969: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 16 20:32:00.970: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 16 20:32:01.078: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW01(config)#interface range ethernet
*Jul 16 20:32:01.178: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 16 20:32:01.178: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW01(config)#interface range ethernet0/1 - 2
Cafe-SW01(config-if-range)#switchport trunk encapsulation dot1q
Cafe-SW01(config-if-range)#switchport mode trunk
Cafe-SW01(config-if-range)#switchport
*Jul 16 20:32:44.339: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 16 20:32:44.340: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01(config-if-range)#switchport trunk 
*Jul 16 20:32:47.339: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 16 20:32:47.341: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01(config-if-range)#switchport trunk allowed vlan all
Cafe-SW01(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Cafe-SW01(config-if-range)#ex
*Jul 16 20:33:32.369: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 16 20:33:32.370: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01(config-if-range)#exit
Cafe-SW01(config)#interface Port-
*Jul 16 20:33:39.871: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
*Jul 16 20:33:39.925: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
Cafe-SW01(config)#interface Port-channel1
Cafe-SW01(config-if)#switchport trunk encapsulation dot1q
Cafe-SW01(config-if)#switchpo
*Jul 16 20:34:08.271: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 16 20:34:08.272: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01(config-if)#switchport mode trunk
Cafe-SW01(config-if)#switc
*Jul 16 20:34:15.236: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
*Jul 16 20:34:15.723: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
Cafe-SW01(config-if)#switchport
*Jul 16 20:34:16.236: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 16 20:34:16.724: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01(config-if)#switchport trunk allowed vlan all
Cafe-SW01(config-if)#end
Cafe-SW01#
*Jul 16 20:34:26.530: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 16 20:34:26.531: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01#
*Jul 16 20:34:27.437: %SYS-5-CONFIG_I: Configured from console by castle on console
Cafe-SW01#show etherchannel 
*Jul 16 20:34:33.343: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
*Jul 16 20:34:34.097: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
Cafe-SW01#show etherchannel su
*Jul 16 20:34:34.343: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 16 20:34:35.097: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SD)         LACP        Et0/1(s)        Et0/2(s)        

Cafe-SW01#


Cafe-SW02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW02(config)#interface range ethernet0
*Jul 16 20:35:57.882: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW02(config)#interface range ethernet0/1 
*Jul 16 20:35:57.984: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 16 20:35:57.985: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 16 20:35:58.095: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW02(config)#interface range ethernet0/1 - 2
*Jul 16 20:35:58.195: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 16 20:35:58.195: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW02(config)#interface range ethernet0/1 - 2
Cafe-SW02(config-if-range)#switchport trunk encapsulation dot1q
Cafe-SW02(config-if-range)#switchport mode trunk
Cafe-SW02(config-if-range)#switchport trunk allowed vlan all
Cafe-SW02(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Cafe-SW02(config-if-range)#exit
Cafe-SW02(config)#
*Jul 16 20:36:57.677: %LINK-3-UPDOWN: Interface Port-channel1, changed state to up
Cafe-SW02(config)#
*Jul 16 20:36:58.677: %LINEPROTO-5-UPDOWN: Line protocol on Interface Port-channel1, changed state to up
Cafe-SW02(config)#interface Port-channel1
Cafe-SW02(config-if)#switchport trunk encapsulation dot1q
Cafe-SW02(config-if)#switchport mode trunk               
Cafe-SW02(config-if)#switchport trunk allowed vlan all   
Cafe-SW02(config-if)#end
Cafe-SW02#
*Jul 16 20:37:26.371: %SYS-5-CONFIG_I: Configured from console by castle on console
Cafe-SW02#
Cafe-SW02#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(P)        Et0/2(P)        

Cafe-SW02#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        156
             Port        65 (Port-channel1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0400
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/3               Desg FWD 100       128.4    P2p 
Po1                 Root FWD 56        128.65   P2p 


Cafe-SW02#show spanning-tree interface ethernet0/1

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Root FWD 56        128.65   P2p 
Cafe-SW02#show spanning-tree interface ethernet0/2

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Root FWD 56        128.65   P2p 
Cafe-SW02#


Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(P)        Et0/2(P)        

Cafe-SW01#show spanning-tree interface ethernet0/1

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Desg FWD 56        128.65   P2p 
Cafe-SW01#show spanning-tree interface ethernet0/2

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Desg FWD 56        128.65   P2p 
Cafe-SW01#show spanning-tree                      

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        100
             Port        4 (Ethernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/3               Root FWD 100       128.4    P2p 
Po1                 Desg FWD 56        128.65   P2p 


Shelter-SW02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW02(config)#interface range ethernet1/2
*Jul 16 20:45:51.629: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Shelter-SW02(config)#interface range ethernet1/2 - 3
*Jul 16 20:45:51.731: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 16 20:45:51.732: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 16 20:45:51.843: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Shelter-SW02(config)#interface range ethernet1/2 - 3
Shelter-SW02(config-if-range)#
*Jul 16 20:45:51.943: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jul 16 20:45:51.943: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Shelter-SW02(config-if-range)#switchport trunk encapsulation dot1q
Shelter-SW02(config-if-range)#switchport mode trunk
Shelter-SW02(config-if-range)#switchport trunk allowed vlan all
Shelter-SW02(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Shelter-SW02(config-if-range)#exit
Shelter-SW02(config)#interr
*Jul 16 20:46:43.073: %LINK-3-UPDOWN: Interface Port-channel1, changed state to up
Shelter-SW02(config)#interface
*Jul 16 20:46:44.073: %LINEPROTO-5-UPDOWN: Line protocol on Interface Port-channel1, changed state to up
Shelter-SW02(config)#interface Port-channel1
Shelter-SW02(config-if)#switchport trunk encapsulation dot1q
Shelter-SW02(config-if)#switchport mode trunk               
Shelter-SW02(config-if)#switchport trunk allowed vlan all   
Shelter-SW02(config-if)#end
Shelter-SW02#
Shelter-SW02#
*Jul 16 20:47:06.127: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW02#
Shelter-SW02#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et1/2(P)        Et1/3(P)        

Shelter-SW02#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        156
             Port        65 (Port-channel1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0500
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
Po1                 Root FWD 56        128.65   P2p 
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------



Shelter-SW02#show spanning-tree interface ethernet1/2

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Root FWD 56        128.65   P2p 
Shelter-SW02#show spanning-tree interface ethernet1/3

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Root FWD 56        128.65   P2p 
Shelter-SW02#



Shelter-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW01(config)#interface range ethernet0/
*Jul 16 20:42:54.784: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul 16 20:42:54.887: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 16 20:42:54.888: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 16 20:42:54.998: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Shelter-SW01(config)#interface range ethernet0/
*Jul 16 20:42:55.098: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 16 20:42:55.098: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Shelter-SW01(config)#interface range ethernet1/2 - 3
Shelter-SW01(config-if-range)#switchport trunk encapsulation dot1q
Shelter-SW01(config-if-range)#switchport mode trunk
Shelter-SW01(config-if-range)#swit
*Jul 16 20:44:02.732: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jul 16 20:44:02.734: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Shelter-SW01(config-if-range)#switchpo  
*Jul 16 20:44:05.732: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
*Jul 16 20:44:05.735: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to up
Shelter-SW01(config-if-range)#switchport trunk allowed vlan all
Shelter-SW01(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Shelter-SW01(config-if-range)#e 
*Jul 16 20:44:34.423: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jul 16 20:44:34.425: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Shelter-SW01(config-if-range)#exit
Shelter-SW01(config)#interface
*Jul 16 20:44:41.451: %ETC-5-L3DONTBNDL2: Et1/2 suspended: LACP currently not enabled on the remote port.
*Jul 16 20:44:41.899: %ETC-5-L3DONTBNDL2: Et1/3 suspended: LACP currently not enabled on the remote port.
Shelter-SW01(config)#interface Port-channel1
Shelter-SW01(config-if)#switchport trunk encapsulation dot1q
Shelter-SW01(config-if)#switchport mode trunk               
*Jul 16 20:44:54.985: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
*Jul 16 20:44:54.985: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to up
Shelter-SW01(config-if)#switchport mode trunk
Shelter-SW01(config-if)#channel-group 1 mode active         
                         ^
% Invalid input detected at '^' marker.

Shelter-SW01(config-if)#channel-group 1 mode active         
*Jul 16 20:45:02.370: %ETC-5-L3DONTBNDL2: Et1/2 suspended: LACP currently not enabled on the remote port.
*Jul 16 20:45:02.668: %ETC-5-L3DONTBNDL2: Et1/3 suspended: LACP currently not enabled on the remote port.
Shelter-SW01(config-if)#switchport trunk allowed vlan all
*Jul 16 20:45:03.370: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jul 16 20:45:03.669: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Shelter-SW01(config-if)#switchport trunk allowed vlan all
Shelter-SW01(config-if)#
*Jul 16 20:45:06.728: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
*Jul 16 20:45:06.729: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to up
Shelter-SW01(config-if)#end
Shelter-SW01#
*Jul 16 20:45:10.847: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW01#
*Jul 16 20:45:13.789: %ETC-5-L3DONTBNDL2: Et1/3 suspended: LACP currently not enabled on the remote port.
*Jul 16 20:45:14.485: %ETC-5-L3DONTBNDL2: Et1/2 suspended: LACP currently not enabled on the remote port.
Shelter-SW01#
*Jul 16 20:45:14.789: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
*Jul 16 20:45:15.485: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
Shelter-SW01#
*Jul 16 20:46:40.142: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
*Jul 16 20:46:40.142: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to up
Shelter-SW01#
*Jul 16 20:46:43.072: %LINK-3-UPDOWN: Interface Port-channel1, changed state to up
Shelter-SW01#
*Jul 16 20:46:44.073: %LINEPROTO-5-UPDOWN: Line protocol on Interface Port-channel1, changed state to up
Shelter-SW01#
Shelter-SW01#
Shelter-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et1/2(P)        Et1/3(P)        

Shelter-SW01#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        100
             Port        4 (Ethernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 
Et0/3               Root FWD 100       128.4    P2p 
Et1/0               Desg FWD 100       128.5    P2p 
Et1/1               Desg FWD 100       128.6    P2p 
Po1                 Desg FWD 56        128.65   P2p 
          
Shelter-SW01#show spanning-tree interface ethernet1/2

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Desg FWD 56        128.65   P2p 
Shelter-SW01#show spanning-tree interface ethernet1/3

Vlan                Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
VLAN0001            Desg FWD 56        128.65   P2p 
Shelter-SW01#


Username: castle 
Password: 
Cafe-SW01#
*Jul 16 20:52:53.464: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: castle] [Source: LOCAL] [localport: 0] at 20:52:53 UTC Thu Jul 16 2026
Cafe-SW01#
Cafe-SW01#
Cafe-SW01#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-ip

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination IP address
  IPv6: Source XOR Destination IP address

Cafe-SW01#
Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#port-channel load-balance src-dst-mac
Cafe-SW01(config)#end
Cafe-SW01#
*Jul 16 20:55:46.669: %SYS-5-CONFIG_I: Configured from console by castle on console
Cafe-SW01#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-mac

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination MAC address
  IPv6: Source XOR Destination MAC address

Cafe-SW01#show spanning-tree summary
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
VLAN0001                     0         0        0          3          3
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       0         0        0          3          3
Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(P)        Et0/2(P)        


Username: castle
Password: 
Cafe-SW02#
Cafe-SW02#
Cafe-SW02#
*Jul 16 20:53:32.611: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: castle] [Source: LOCAL] [localport: 0] at 20:53:32 UTC Thu Jul 16 2026
Cafe-SW02#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-ip

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination IP address
  IPv6: Source XOR Destination IP address

Cafe-SW02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW02(config)#port-channel load-balance src-dst-mac
Cafe-SW02(config)#end
Cafe-SW02#
*Jul 16 20:56:28.438: %SYS-5-CONFIG_I: Configured from console by castle on console
Cafe-SW02#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-mac

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination MAC address
  IPv6: Source XOR Destination MAC address

Cafe-SW02#show spanning-tree summary
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
VLAN0001                     0         0        0          3          3
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       0         0        0          3          3
Cafe-SW02#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(P)        Et0/2(P)        

Cafe-SW02#

Shelter-SW01#
Shelter-SW01#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-ip

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination IP address
  IPv6: Source XOR Destination IP address

Shelter-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW01(config)#port-channel load-balance src-dst-mac
Shelter-SW01(config)#end
Shelter-SW01#
*Jul 16 20:56:40.314: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW01#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-mac

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination MAC address
  IPv6: Source XOR Destination MAC address

Shelter-SW01#
Shelter-SW01#show spanning-tree summary
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
VLAN0001                     0         0        0          7          7
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       0         0        0          7          7
Shelter-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et1/2(P)        Et1/3(P)        

Shelter-SW01#

Shelter-SW02#show etherchannel load-balance 
EtherChannel Load-Balancing Configuration:
        src-dst-ip

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination IP address
  IPv6: Source XOR Destination IP address

Shelter-SW02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW02(config)#port-channel load-balance src-dst-mac
Shelter-SW02(config)#end
Shelter-SW02#
*Jul 16 20:56:50.995: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW02#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-mac

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination MAC address
  IPv6: Source XOR Destination MAC address

Shelter-SW02#show spanning-tree summary
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
VLAN0001                     0         0        0          7          7
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       0         0        0          7          7
Shelter-SW02#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et1/2(P)        Et1/3(P)        

Shelter-SW02#



Cafe-SW01#
Cafe-SW01#show interfaces Port-channel1
Port-channel1 is up, line protocol is up (connected) 
  Hardware is EtherChannel, address is aabb.cc00.0220 (bia aabb.cc00.0220)
  MTU 1500 bytes, BW 20000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  Members in this channel: Et0/1 Et0/2 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:27:01, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     8 packets input, 468 bytes, 0 no buffer
     Received 8 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     2072 packets output, 164564 bytes, 0 underruns
     Output 2072 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Cafe-SW01#
Cafe-SW01#
Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#interface ethernet0/1
Cafe-SW01(config-if)#shutdown
Cafe-SW01(config-if)#end
Cafe-SW01#
*Jul 16 21:05:14.919: %LINK-5-CHANGED: Interface Ethernet0/1, changed state to administratively down
*Jul 16 21:05:15.726: %SYS-5-CONFIG_I: Configured from console by castle on console
Cafe-SW01#
*Jul 16 21:05:15.919: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(D)        Et0/2(P)        

Cafe-SW01#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-mac

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination MAC address
  IPv6: Source XOR Destination MAC address

Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#interface ethernet0/1
Cafe-SW01(config-if)#no shutdown
Cafe-SW01(config-if)#end
Cafe-SW01#
*Jul 16 21:08:51.168: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
Cafe-SW01#
*Jul 16 21:08:51.674: %SYS-5-CONFIG_I: Configured from console by castle on console
Cafe-SW01#
*Jul 16 21:08:53.170: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(P)        Et0/2(P)        

Cafe-SW01#


Shelter-SW01#
Shelter-SW01#show interfaces Port-channel1
Port-channel1 is up, line protocol is up (connected) 
  Hardware is EtherChannel, address is aabb.cc00.0331 (bia aabb.cc00.0331)
  MTU 1500 bytes, BW 20000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  Members in this channel: Et1/2 Et1/3 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:17:50, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     8 packets input, 468 bytes, 0 no buffer
     Received 8 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     1353 packets output, 109198 bytes, 0 underruns
     Output 1353 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Shelter-SW01#
Shelter-SW01#
Shelter-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW01(config)#interface ethernet1/2
Shelter-SW01(config-if)#shutdown
Shelter-SW01(config-if)#end
Shelter-SW01#
*Jul 16 21:05:48.409: %LINK-5-CHANGED: Interface Ethernet1/2, changed state to administratively down
Shelter-SW01#
*Jul 16 21:05:48.414: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW01#
*Jul 16 21:05:49.410: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
Shelter-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et1/2(D)        Et1/3(P)        

Shelter-SW01#show spanning-tree summary
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
VLAN0001                     0         0        0          7          7
---------------------- -------- --------- -------- ---------- ----------
1 vlan                       0         0        0          7          7
Shelter-SW01#
Shelter-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW01(config)#interface ethernet1/2
Shelter-SW01(config-if)#no shutdown
Shelter-SW01(config-if)#end
Shelter-SW01#
*Jul 16 21:10:29.507: %SYS-5-CONFIG_I: Configured from console by castle on console
Shelter-SW01#
*Jul 16 21:10:30.303: %LINK-3-UPDOWN: Interface Ethernet1/2, changed state to up
Shelter-SW01#
*Jul 16 21:10:32.306: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
Shelter-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et1/2(P)        Et1/3(P)        



Cafe-SW01#
Cafe-SW01#show interfaces Port-channel1
Port-channel1 is up, line protocol is up (connected) 
  Hardware is EtherChannel, address is aabb.cc00.0220 (bia aabb.cc00.0220)
  MTU 1500 bytes, BW 20000 Kbit/sec, DLY 1000 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
  input flow-control is off, output flow-control is unsupported 
  Members in this channel: Et0/1 Et0/2 
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:27:01, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     8 packets input, 468 bytes, 0 no buffer
     Received 8 broadcasts (0 multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input packets with dribble condition detected
     2072 packets output, 164564 bytes, 0 underruns
     Output 2072 broadcasts (0 multicasts)
     0 output errors, 0 collisions, 0 interface resets
     0 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out
Cafe-SW01#
Cafe-SW01#
Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#interface ethernet0/1
Cafe-SW01(config-if)#shutdown
Cafe-SW01(config-if)#end
Cafe-SW01#
*Jul 16 21:05:14.919: %LINK-5-CHANGED: Interface Ethernet0/1, changed state to administratively down
*Jul 16 21:05:15.726: %SYS-5-CONFIG_I: Configured from console by castle on console
Cafe-SW01#
*Jul 16 21:05:15.919: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(D)        Et0/2(P)        

Cafe-SW01#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-mac

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination MAC address
  IPv6: Source XOR Destination MAC address

Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#interface ethernet0/1
Cafe-SW01(config-if)#no shutdown
Cafe-SW01(config-if)#end
Cafe-SW01#
*Jul 16 21:08:51.168: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
Cafe-SW01#
*Jul 16 21:08:51.674: %SYS-5-CONFIG_I: Configured from console by castle on console
Cafe-SW01#
*Jul 16 21:08:53.170: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(P)        Et0/2(P)        

Cafe-SW01#
Cafe-SW01#
Cafe-SW01#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW01#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Cafe-SW01#show interfaces port-channel1 switchport
Name: Po1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
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

Protected: false
Appliance trust: none
Cafe-SW01#show running-config interface port-channel1
Building configuration...

Current configuration : 92 bytes
!
interface Port-channel1
 switchport trunk encapsulation dot1q
 switchport mode trunk
end

Cafe-SW01#show running-config interface ethernet0/1
Building configuration...

Current configuration : 154 bytes
!
interface Ethernet0/1
 description Uplink A to Cafe-SW02
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 1 mode active
end

Cafe-SW01#show running-config interface ethernet0/2
Building configuration...

Current configuration : 154 bytes
!
interface Ethernet0/2
 description Uplink B to Cafe-SW02
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 1 mode active
end

Cafe-SW01#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        100
             Port        4 (Ethernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/3               Root FWD 100       128.4    P2p 
Po1                 Desg FWD 56        128.65   P2p 


Cafe-SW01#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW01#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Cafe-SW01#show interfaces port-channel1 switchport
Name: Po1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
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

          
Cafe-SW01#how running-config interface port-channel1
           ^
% Invalid input detected at '^' marker.

Cafe-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(P)        Et0/2(P)        

Cafe-SW01#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        100
             Port        4 (Ethernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/3               Root FWD 100       128.4    P2p 
Po1                 Desg FWD 56        128.65   P2p 


Cafe-SW01#


Cafe-SW02# show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW02#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Cafe-SW02#show interfaces port-channel1 switchport
Name: Po1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
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

          
Cafe-SW02#how running-config interface port-channel1
           ^
% Invalid input detected at '^' marker.

Cafe-SW02#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et0/1(P)        Et0/2(P)        

Cafe-SW02#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        156
             Port        65 (Port-channel1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0400
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/3               Desg FWD 100       128.4    P2p 
Po1                 Root FWD 56        128.65   P2p 


Cafe-SW02#



Shelter-SW01#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW01#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Shelter-SW01#show interfaces port-channel1 switchport
Name: Po1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
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

          
Shelter-SW01#how running-config interface port-channel1
              ^
% Invalid input detected at '^' marker.

Shelter-SW01#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et1/2(P)        Et1/3(P)        

Shelter-SW01#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        100
             Port        4 (Ethernet0/3)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 
Et0/3               Root FWD 100       128.4    P2p 
Et1/0               Desg FWD 100       128.5    P2p 
Et1/1               Desg FWD 100       128.6    P2p 
Po1                 Desg FWD 56        128.65   P2p 
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------



Shelter-SW01#


Shelter-SW02#
Shelter-SW02#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW02#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Shelter-SW02#show interfaces port-channel1 switchport
Name: Po1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
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

Protected: false
Appliance trust: none
Shelter-SW02#show running-config interface port-channel1
Building configuration...

Current configuration : 92 bytes
!
interface Port-channel1
 switchport trunk encapsulation dot1q
 switchport mode trunk
end

Shelter-SW02#show running-config interface ethernet1/2
Building configuration...

Current configuration : 185 bytes
!
interface Ethernet1/2
 description Shelter uplink A to Shelter-SW01 (Guide Ethernet0/6)
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 1 mode active
end

Shelter-SW02#show running-config interface ethernet1/3
Building configuration...

Current configuration : 185 bytes
!
interface Ethernet1/3
 description Shelter uplink B to Shelter-SW01 (Guide Ethernet0/7)
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 1 mode active
end

Shelter-SW02#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        156
             Port        65 (Port-channel1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0500
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
Po1                 Root FWD 56        128.65   P2p 
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------



Shelter-SW02#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW02#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Shelter-SW02#show interfaces port-channel1 switchport
Name: Po1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
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

          
Shelter-SW02#how running-config interface port-channel1
              ^
% Invalid input detected at '^' marker.

Shelter-SW02#show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port

        A - formed by Auto LAG


Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)         LACP        Et1/2(P)        Et1/3(P)        

Shelter-SW02#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        156
             Port        65 (Port-channel1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0500
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
Po1                 Root FWD 56        128.65   P2p 
          
Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
```
