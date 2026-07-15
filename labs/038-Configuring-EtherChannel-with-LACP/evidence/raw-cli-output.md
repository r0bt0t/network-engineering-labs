# Lab 038 - Raw CLI Output

```bash
Cafe-SW01>enable
Cafe-SW01#
*Jul 14 19:53:26.806: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Jul 14 19:53:26.806: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
*Jul 14 19:53:26.806: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
Cafe-SW01#ter
*Jul 14 19:53:26.845: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul 14 19:53:26.947: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 14 19:53:26.948: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 14 19:53:27.052: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW01#termina
*Jul 14 19:53:27.152: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jul 14 19:53:27.152: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW01#terminal length 0
Cafe-SW01#show spanning-tree

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


Cafe-SW01#


Cafe-SW02>en
Cafe-SW02#terminal length 0
Cafe-SW02#s
*Jul 14 19:54:30.798: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW02#show s
*Jul 14 19:54:30.900: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 14 19:54:30.901: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 14 19:54:31.006: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW02#show spanni
*Jul 14 19:54:31.106: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jul 14 19:54:31.106: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW02#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    4097
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 
Et0/3               Desg FWD 100       128.4    P2p 


Cafe-SW02#

Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#interface range ethernet0/1 - 2
Cafe-SW01(config-if-range)#switchport trunk encapsulation dot1q
Cafe-SW01(config-if-range)#switchport mode trunk
Cafe-SW01(config-if-range)#sw
*Jul 14 19:56:03.825: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 14 19:56:03.826: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01(config-if-range)#switchport 
*Jul 14 19:56:06.826: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 14 19:56:06.827: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01(config-if-range)#switchport trunk allowed vlan all
Cafe-SW01(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Cafe-SW01(config-if-range)#exit
Cafe-SW01(config)#
*Jul 14 19:56:28.788: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 14 19:56:28.788: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01(config)#interface Port-channel1
*Jul 14 19:56:36.000: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
*Jul 14 19:56:36.443: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
Cafe-SW01(config)#interface Port-channel1
Cafe-SW01(config-if)#switchport trunk encapsulation dot1q
Cafe-SW01(config-if)#switchpor
*Jul 14 19:56:55.154: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 14 19:56:55.154: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01(config-if)#switchport mode trunk
Cafe-SW01(config-if)#switchport
*Jul 14 19:57:02.831: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
*Jul 14 19:57:02.907: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
Cafe-SW01(config-if)#switchport allo
*Jul 14 19:57:03.831: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
*Jul 14 19:57:03.907: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW01(config-if)#switchport trunk allowed vlan all
Cafe-SW01(config-if)#end
*Jul 14 19:57:18.920: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 14 19:57:18.921: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01(config-if)#end
Cafe-SW01#
*Jul 14 19:57:22.933: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW01#
*Jul 14 19:57:26.364: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
*Jul 14 19:57:26.468: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
Cafe-SW01#
*Jul 14 19:57:27.364: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 14 19:57:27.468: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01#

Cafe-SW02#
Cafe-SW02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW02(config)#interface range ethernet0/1 - 2
Cafe-SW02(config-if-range)#shutdown
Cafe-SW02(config-if-range)#
*Jul 14 19:58:43.612: %LINK-5-CHANGED: Interface Ethernet0/1, changed state to administratively down
*Jul 14 19:58:43.614: %LINK-5-CHANGED: Interface Ethernet0/2, changed state to administratively down
*Jul 14 19:58:44.612: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
Cafe-SW02(config-if-range)#
*Jul 14 19:58:44.615: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW02(config-if-range)#switchport trunk encapsulation dot1q
Cafe-SW02(config-if-range)#switchport mode trunk
Cafe-SW02(config-if-range)#switchport trunk allowed vlan al
Cafe-SW02(config-if-range)#switchport trunk allowed vlan all
Cafe-SW02(config-if-range)#channel-group 1 mode active      
Creating a port-channel interface Port-channel 1

Cafe-SW02(config-if-range)#no shutdown
Cafe-SW02(config-if-range)#exit
Cafe-SW02(config)#
*Jul 14 20:00:20.923: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
*Jul 14 20:00:20.924: %LINK-3-UPDOWN: Interface Ethernet0/2, changed state to up
Cafe-SW02(config)#
*Jul 14 20:00:22.925: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 14 20:00:22.926: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW02(config)#
*Jul 14 20:00:25.706: %LINK-3-UPDOWN: Interface Port-channel1, changed state to up
Cafe-SW02(config)#inter
*Jul 14 20:00:26.706: %LINEPROTO-5-UPDOWN: Line protocol on Interface Port-channel1, changed state to up
Cafe-SW02(config)#interface Port-channel1
Cafe-SW02(config-if)#switchport trunk encapsulation dot1q
Cafe-SW02(config-if)#switchport mode trunk
Cafe-SW02(config-if)#switchport trunk allowed vlan all
Cafe-SW02(config-if)#end
Cafe-SW02#
*Jul 14 20:01:07.749: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW02#

Cafe-SW01#
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

Cafe-SW01#show spanning-tree vlan 1

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
Et0/3               Desg FWD 100       128.4    P2p 
Po1                 Desg FWD 56        128.65   P2p 


Cafe-SW01#show interfaces port-channel1 status

Port         Name               Status       Vlan       Duplex  Speed Type
Po1                             connected    trunk        full   auto 10/100/1000BaseTX
Cafe-SW01#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Cafe-SW01#

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

Cafe-SW02#show spanning-tree vlan 1 

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    4097
             Address     aabb.cc00.0100
             Cost        56
             Port        65 (Port-channel1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/3               Desg FWD 100       128.4    P2p 
Po1                 Root FWD 56        128.65   P2p 


Cafe-SW02#show interfaces port-channel1 status

Port         Name               Status       Vlan       Duplex  Speed Type
Po1                             connected    trunk        full   auto 10/100/1000BaseTX
Cafe-SW02#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Cafe-SW02#
```
