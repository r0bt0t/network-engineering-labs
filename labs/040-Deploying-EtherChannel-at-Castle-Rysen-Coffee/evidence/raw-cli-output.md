# Lab 040 - Raw CLI Output

```bash
Cafe-SW01>en
Cafe-SW01#
*Jul 15 20:37:49.830: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW01#
*Jul 15 20:37:49.932: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 15 20:37:49.932: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 15 20:37:50.037: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW01#t
*Jul 15 20:37:50.137: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jul 15 20:37:50.137: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW01#terminal length 0
Cafe-SW01#show running-config
Building configuration...

Current configuration : 978 bytes
!
! Last configuration change at 20:37:50 UTC Wed Jul 15 2026
!
version 17.16
service timestamps debug datetime msec
service timestamps log datetime msec
!
hostname Cafe-SW01
!
boot-start-marker
boot-end-marker
!
!
no aaa new-model
!
!
!
!
!
!
!
!
!
!
!
!
!
ip audit notify log
ip audit po max-events 100
ip cef
login on-success log
no ipv6 cef
!
!
!
!
!
!
!
!
!
!
!
memory free low-watermark processor 79497
!
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id
!
!
vlan internal allocation policy ascending
!
!
!
!
!
interface Ethernet0/0
!
interface Ethernet0/1
 description Cafe uplink to Cafe-SW02 (Link A)
!
interface Ethernet0/2
 description Cafe uplink to Cafe-SW02 (Link B)
!
interface Ethernet0/3
!
ip forward-protocol nd
ip forward-protocol udp
!
!
ip http server
ip http secure-server
ip ssh bulk-mode 131072
!
no logging btrace
!
!
!
control-plane
!
!
!
line con 0
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input telnet ssh
!
!
end

Cafe-SW01#
Cafe-SW01#show running-config interface ethernet0/1
Building configuration...

Current configuration : 76 bytes
!
interface Ethernet0/1
 description Cafe uplink to Cafe-SW02 (Link A)
end

Cafe-SW01#show running-config interface ethernet0/2
Building configuration...

Current configuration : 76 bytes
!
interface Ethernet0/2
 description Cafe uplink to Cafe-SW02 (Link B)
end

Cafe-SW01#show interface trunk
Cafe-SW01#show spanning-tree vlan 1

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
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
Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#interface range ethernet0/1 - 2
Cafe-SW01(config-if-range)#switchport trunk encapsulation dot1q
Cafe-SW01(config-if-range)#switchport mode trunk
Cafe-SW01(config-if-range)#
*Jul 15 20:41:07.849: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 15 20:41:07.851: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01(config-if-range)#switchpo
*Jul 15 20:41:10.849: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 15 20:41:10.852: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01(config-if-range)#switchport trunk allowed vlan all
Cafe-SW01(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Cafe-SW01(config-if-range)#ex
*Jul 15 20:41:38.718: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 15 20:41:38.719: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01(config-if-range)#exit
Cafe-SW01(config)#
*Jul 15 20:41:45.747: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
*Jul 15 20:41:46.417: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
Cafe-SW01(config)#interface Port-channel1 
Cafe-SW01(config-if)#switchport trunk encapsulation dot1q
Cafe-SW01(config-if)#
*Jul 15 20:42:25.532: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 15 20:42:25.532: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01(config-if)#switchport mode trunk
*Jul 15 20:42:32.757: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
*Jul 15 20:42:33.106: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
Cafe-SW01(config-if)#switchport mode trunk
Cafe-SW01(config-if)#
*Jul 15 20:42:33.758: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jul 15 20:42:34.106: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW01(config-if)#switchport trunk allowedvlan all
                                             ^
% Invalid input detected at '^' marker.

Cafe-SW01(config-if)#switchport trunk allowed vlan all
Cafe-SW01(config-if)#
*Jul 15 20:43:16.963: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jul 15 20:43:16.964: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW01(config-if)#end
Cafe-SW01#
*Jul 15 20:43:20.275: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW01#show 
*Jul 15 20:43:24.554: %ETC-5-L3DONTBNDL2: Et0/2 suspended: LACP currently not enabled on the remote port.
*Jul 15 20:43:24.754: %ETC-5-L3DONTBNDL2: Et0/1 suspended: LACP currently not enabled on the remote port.
Cafe-SW01#show e
*Jul 15 20:43:25.554: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
*Jul 15 20:43:25.754: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
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

Cafe-SW01#show interface trunk
Cafe-SW01#show spanning-tree vlan 1

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0100
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    P2p 
Et0/3               Desg FWD 100       128.4    P2p 


Cafe-SW02>
Cafe-SW02>en
Cafe-SW02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW02(config)#i
*Jul 15 20:46:03.463: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul 15 20:46:03.565: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 15 20:46:03.566: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 15 20:46:03.673: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW02(config)#interfa
*Jul 15 20:46:03.773: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 15 20:46:03.773: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW02(config)#interface range ethernet0/1 - 2
Cafe-SW02(config-if-range)#switchport trunk encapsulation dot1q
Cafe-SW02(config-if-range)#switchport mode trunk
Cafe-SW02(config-if-range)#switchport trunk allowed vlan all
Cafe-SW02(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Cafe-SW02(config-if-range)#exit
*Jul 15 20:47:29.579: %LINK-3-UPDOWN: Interface Port-channel1, changed state to up
Cafe-SW02(config-if-range)#exit
Cafe-SW02(config)#
*Jul 15 20:47:30.579: %LINEPROTO-5-UPDOWN: Line protocol on Interface Port-channel1, changed state to up
Cafe-SW02(config)#interface Port-channel1
Cafe-SW02(config-if)#switchport trunk encapsulation dot1q
Cafe-SW02(config-if)#switchport mode trunk
Cafe-SW02(config-if)#switchport trunk allowed vlan all
Cafe-SW02(config-if)#end
Cafe-SW02#
*Jul 15 20:48:22.000: %SYS-5-CONFIG_I: Configured from console by console
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

Cafe-SW02#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Cafe-SW02#show spanning-tree vlan 1

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
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

Shelter-SW01#terminal length 0
Shelter-SW01#show running-config interface ethernet1/2
Building configuration...

Current configuration : 82 bytes
!
interface Ethernet1/2
 description Shelter uplink to Shelter-SW02 (Link A)
end

Shelter-SW01#show running-config interface ethernet1/3
Building configuration...

Current configuration : 82 bytes
!
interface Ethernet1/3
 description Shelter uplink to Shelter-SW02 (Link B)
end

Shelter-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW01(config)#interface range ethernet1/2-3
Shelter-SW01(config-if-range)#switchport trunk encapsulation dot1q
Shelter-SW01(config-if-range)#switchport mode trunk
Shelter-SW01(config-if-range)#switch
*Jul 15 20:51:25.850: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jul 15 20:51:25.851: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Shelter-SW01(config-if-range)#switchport
*Jul 15 20:51:28.851: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
*Jul 15 20:51:28.851: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to up
Shelter-SW01(config-if-range)#switchport trunk allowed vlan all
Shelter-SW01(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Shelter-SW01(config-if-range)#exit
*Jul 15 20:51:56.727: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jul 15 20:51:56.728: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Shelter-SW01(config-if-range)#exit
Shelter-SW01(config)#interface Port-channel
*Jul 15 20:52:03.517: %ETC-5-L3DONTBNDL2: Et1/2 suspended: LACP currently not enabled on the remote port.
Shelter-SW01(config)#interface Port-channel
*Jul 15 20:52:04.568: %ETC-5-L3DONTBNDL2: Et1/3 suspended: LACP currently not enabled on the remote port.
Shelter-SW01(config)#interface Port-channel1
Shelter-SW01(config-if)#switchport trunk encapsulation dot1q
Shelter-SW01(config-if)#exit                                
*Jul 15 20:52:18.183: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
*Jul 15 20:52:18.184: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to up
Shelter-SW01(config-if)#switchport mode trunk            
Shelter-SW01(config-if)#
*Jul 15 20:52:25.040: %ETC-5-L3DONTBNDL2: Et1/2 suspended: LACP currently not enabled on the remote port.
*Jul 15 20:52:25.817: %ETC-5-L3DONTBNDL2: Et1/3 suspended: LACP currently not enabled on the remote port.
Shelter-SW01(config-if)#
*Jul 15 20:52:26.040: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Jul 15 20:52:26.818: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
Shelter-SW01(config-if)#switchport trunk allowed vlan all   
Shelter-SW01(config-if)#
*Jul 15 20:52:43.254: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to up
*Jul 15 20:52:43.254: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to up
Shelter-SW01(config-if)#end
Shelter-SW01#sh
*Jul 15 20:52:46.666: %SYS-5-CONFIG_I: Configured from console by console
Shelter-SW01#show etherchanne
*Jul 15 20:52:50.436: %ETC-5-L3DONTBNDL2: Et1/3 suspended: LACP currently not enabled on the remote port.
*Jul 15 20:52:50.485: %ETC-5-L3DONTBNDL2: Et1/2 suspended: LACP currently not enabled on the remote port.
Shelter-SW01#show etherchannel
*Jul 15 20:52:51.437: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
*Jul 15 20:52:51.485: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
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
1      Po1(SD)         LACP        Et1/2(s)        Et1/3(s)        

Shelter-SW01#show interface trunk
Shelter-SW01#show spanning-tree vlan 1

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0300
             This bridge is the root
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
Et0/3               Desg FWD 100       128.4    P2p 
Et1/0               Desg FWD 100       128.5    P2p 
Et1/1               Desg FWD 100       128.6    P2p 


Shelter-SW02#terminal length 0
Shelter-SW02#show running-config interface ethernet1/2
Building configuration...

Current configuration : 82 bytes
!
interface Ethernet1/2
 description Shelter uplink to Shelter-SW01 (Link A)
end

Shelter-SW02#show running-config interface ethernet1/3
Building configuration...

Current configuration : 82 bytes
!
interface Ethernet1/3
 description Shelter uplink to Shelter-SW01 (Link B)
end

Shelter-SW02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW02(config)#interface range ethernet1/2-3
Shelter-SW02(config-if-range)#switchport trunk encapsulation dot1q
Shelter-SW02(config-if-range)#switchport mode trunk
Shelter-SW02(config-if-range)#switchport trunk allowed vlan all
Shelter-SW02(config-if-range)#channel-group 1 mode active
Creating a port-channel interface Port-channel 1

Shelter-SW02(config-if-range)#exit
Shelter-SW02(config)#
*Jul 15 20:55:56.879: %LINK-3-UPDOWN: Interface Port-channel1, changed state to up
Shelter-SW02(config)#in
*Jul 15 20:55:57.879: %LINEPROTO-5-UPDOWN: Line protocol on Interface Port-channel1, changed state to up
Shelter-SW02(config)#interface Port-channel1
Shelter-SW02(config-if)#switchport trunk encapsulation dot1q
Shelter-SW02(config-if)#switchport mode trunk               
Shelter-SW02(config-if)#switchport trunk allowed vlan all   
Shelter-SW02(config-if)#end
Shelter-SW02#
*Jul 15 20:56:27.315: %SYS-5-CONFIG_I: Configured from console by console
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

Shelter-SW02#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Po1            on               802.1q         trunking      1

Port           Vlans allowed on trunk
Po1            1-4094

Port           Vlans allowed and active in management domain
Po1            1

Port           Vlans in spanning tree forwarding state and not pruned
Po1            1
Shelter-SW02#show spanning-tree vlan 1

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0300
             Cost        56
             Port        65 (Port-channel1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0400
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


Cafe-SW01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW01(config)#port-channel load-balance src-dst-mac
Cafe-SW01(config)#end
Cafe-SW01#sh
*Jul 15 20:58:52.087: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW01#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-mac

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination MAC address
  IPv6: Source XOR Destination MAC address

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


Cafe-SW02>
Cafe-SW02>en
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
*Jul 15 21:00:42.406: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW02#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-mac

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination MAC address
  IPv6: Source XOR Destination MAC address

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
```
