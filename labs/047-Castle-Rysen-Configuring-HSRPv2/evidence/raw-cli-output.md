# Lab 047 - Raw CLI Output

```bash
Shelter-SW>en
Shelter-SW#co
*Jul 19 15:40:26.969: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Shelter-SW#conf t
*Jul 19 15:40:27.071: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 15:40:27.072: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 15:40:27.177: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Shelter-SW#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Shelter-SW(config)#
*Jul 19 15:40:27.277: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 19 15:40:27.277: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Shelter-SW(config)#vlan 20
Shelter-SW(config-vlan)#name Shelter-Logistics
Shelter-SW(config-vlan)#vlan 30
Shelter-SW(config-vlan)#name Shelter-Engineering
Shelter-SW(config-vlan)#vlan 40
Shelter-SW(config-vlan)#name Shelter-Security
Shelter-SW(config-vlan)#end
Shelter-SW#
*Jul 19 15:41:35.351: %SYS-5-CONFIG_I: Configured from console by console
Shelter-SW#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/3, Et1/0, Et1/1, Et1/2
                                                Et1/3
10   VLAN0010                         active    Et0/2
20   Shelter-Logistics                active    
30   Shelter-Engineering              active    
40   Shelter-Security                 active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Shelter-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1
Et0/1          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20,30,40
Et0/1          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/0          10,20,30,40
Et0/1          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20,30,40
Et0/1          10,20,30,40
Shelter-SW#


FS-R1>en
FS-R1#co
*Jul 19 15:43:21.017: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
FS-R1#conf t
*Jul 19 15:43:21.119: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 15:43:21.120: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 15:43:21.227: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
FS-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R1(config)#
*Jul 19 15:43:21.327: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 19 15:43:21.327: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
FS-R1(config)#interface ethernet0/0
FS-R1(config-if)#no shutdown
FS-R1(config-if)#int
FS-R1(config-if)#inteth
*Jul 19 15:43:41.832: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
FS-R1(config-if)#inteth
FS-R1(config-if)#inteth
*Jul 19 15:43:42.832: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
FS-R1(config-if)#inteth0/0.10
                  ^
% Invalid input detected at '^' marker.

FS-R1(config-if)#int
FS-R1(config-if)#inteth
FS-R1(config-if)#int   
FS-R1(config-if)#interface ethernet0/0.10
FS-R1(config-subif)#no ip address
FS-R1(config-subif)#ip address 10.0.16.2 255.255.255.224
FS-R1(config-subif)#interface ethernet0/0.20            
FS-R1(config-subif)#no ip address                       
FS-R1(config-subif)#ip address 10.0.16.130 255.255.255.224
FS-R1(config-subif)#interface ethernet0/0.30              
FS-R1(config-subif)#no ip address                         
FS-R1(config-subif)#ip address 10.0.17.2 255.255.255.224  
FS-R1(config-subif)#interface ethernet0/0.40            
FS-R1(config-subif)#no ip address                       
FS-R1(config-subif)#ip address 10.0.17.130 255.255.255.224
FS-R1(config-subif)#end
FS-R1#
*Jul 19 15:46:27.361: %SYS-5-CONFIG_I: Configured from console by console
FS-R1#show ip interface brief | include ethernet0/0
FS-R1#show ip interface brief | include Ethernet0/0
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/0.10         10.0.16.2       YES manual up                    up      
Ethernet0/0.20         10.0.16.130     YES manual up                    up      
Ethernet0/0.30         10.0.17.2       YES manual up                    up      
Ethernet0/0.40         10.0.17.130     YES manual up                    up      
FS-R1#


FS-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R1(config)#interface ethernet0/0.10
FS-R1(config-subif)#standby version 2
FS-R1(config-subif)#standby 10 ip 10.0.16.1
FS-R1(config-subif)#standby 10 priority 
*Jul 19 15:49:05.451: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Standby -> Active
FS-R1(config-subif)#standby 10 priority 105
FS-R1(config-subif)#standby 10 preempt
FS-R1(config-subif)#interface ethernet0/0.20
FS-R1(config-subif)#standby version 2
FS-R1(config-subif)#standby 20 ip 10.0.16.129
FS-R1(config-subif)#standby 20 priority 105  
FS-R1(config-subif)#standby 20 preempt     
*Jul 19 15:50:31.530: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Standby -> Active
FS-R1(config-subif)#standby 20 preempt
FS-R1(config-subif)#interface ethernet0/0.30
FS-R1(config-subif)#standby version 2        
FS-R1(config-subif)#standby 30 ip 10.0.17.1  
FS-R1(config-subif)#standby 30 priority 105
FS-R1(config-subif)#standby 30 preempt     
*Jul 19 15:51:50.483: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Standby -> Active
FS-R1(config-subif)#standby 30 preempt
FS-R1(config-subif)#interface ethernet0/0.40
FS-R1(config-subif)#standby version 2       
FS-R1(config-subif)#standby 40 ip 10.0.17.129
FS-R1(config-subif)#standby 40 priority 105  
FS-R1(config-subif)#standby 40 preempt     
FS-R1(config-subif)#end
FS-R1#
*Jul 19 15:52:52.800: %SYS-5-CONFIG_I: Configured from console by console
*Jul 19 15:52:53.305: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Standby -> Active
FS-R1#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   105 P Active  local           unknown         10.0.16.1
Et0/0.20    20   105 P Active  local           unknown         10.0.16.129
Et0/0.30    30   105 P Active  local           unknown         10.0.17.1
Et0/0.40    40   105 P Active  local           unknown         10.0.17.129
FS-R1#


FS-R2>en
FS-R2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R2(config)#interface ethernet
*Jul 19 15:55:04.662: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
FS-R2(config)#interface ethernet
*Jul 19 15:55:04.764: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 15:55:04.764: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jul 19 15:55:04.872: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
FS-R2(config)#interface ethernet0/0
*Jul 19 15:55:04.973: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jul 19 15:55:04.973: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
FS-R2(config)#interface ethernet0/0
FS-R2(config-if)#no shutdown
FS-R2(config-if)#
*Jul 19 15:55:15.587: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
FS-R2(config-if)#inter
*Jul 19 15:55:16.587: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
FS-R2(config-if)#interface ethernet0/0.10
FS-R2(config-subif)#ip address 10.0.16.3 255.255.255.224
FS-R2(config-subif)#standby version 2
FS-R2(config-subif)#standby 10 ip 10.0.16.1
FS-R2(config-subif)#standby 10 preempt
FS-R2(config-subif)#interface ethernet0/0.20            
FS-R2(config-subif)#standby 10 ip 10.0.16.1 
*Jul 19 15:56:26.761: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Speak -> Standby
FS-R2(config-subif)#ip address 10.0.16.131 255.255.255.224
FS-R2(config-subif)#standby version 2                     
FS-R2(config-subif)#standby 20 ip 10.0.16.129             
FS-R2(config-subif)#standby 20 preempt       
FS-R2(config-subif)#standby version 2        
*Jul 19 15:57:28.093: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Speak -> Standby
FS-R2(config-subif)#interface ethernet0/0.30              
FS-R2(config-subif)#ip address 10.0.17.3 255.255.255.224  
FS-R2(config-subif)#standby version 2                     
FS-R2(config-subif)#standby 30 ip 10.0.17.1             
FS-R2(config-subif)#standby 30 preempt     
FS-R2(config-subif)#interface ethernet0/0.40            
FS-R2(config-subif)#
*Jul 19 15:59:11.105: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Speak -> Standby
FS-R2(config-subif)#ip address 10.0.17.131 255.255.255.224
FS-R2(config-subif)#standby version 2                     
FS-R2(config-subif)#standby 40 ip 10.0.17.129             
FS-R2(config-subif)#standby 40 preempt                    
FS-R2(config-subif)#end
FS-R2#
*Jul 19 16:00:22.074: %SYS-5-CONFIG_I: Configured from console by console
*Jul 19 16:00:22.435: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Speak -> Standby
FS-R2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   100 P Standby 10.0.16.2       local           10.0.16.1
Et0/0.20    20   100 P Standby 10.0.16.130     local           10.0.16.129
Et0/0.30    30   100 P Standby 10.0.17.2       local           10.0.17.1
Et0/0.40    40   100 P Standby 10.0.17.130     local           10.0.17.129
FS-R2#


FS-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R1(config)#interface ethernet0/0
FS-R1(config-if)#shutdown 
FS-R1(config-if)#en
*Jul 19 16:01:37.307: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Active -> Init
*Jul 19 16:01:37.307: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Active -> Init
*Jul 19 16:01:37.307: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Active -> Init
*Jul 19 16:01:37.307: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Active -> Init
FS-R1(config-if)#end
FS-R1#
*Jul 19 16:01:39.304: %LINK-5-CHANGED: Interface Ethernet0/0, changed state to administratively down
FS-R1#
*Jul 19 16:01:40.212: %SYS-5-CONFIG_I: Configured from console by console
FS-R1#
*Jul 19 16:01:40.305: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
FS-R1#


FS-R2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   100 P Active  local           unknown         10.0.16.1
Et0/0.20    20   100 P Active  local           unknown         10.0.16.129
Et0/0.30    30   100 P Active  local           unknown         10.0.17.1
Et0/0.40    40   100 P Active  local           unknown         10.0.17.129
FS-R2#


Connecting to console for FS-Client10

Core Linux
fs-client10 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@fs-client10:~$ cisco@fs-client10:~$ sudo ifconfig eth0 10.0.16.10 netmask 
255.255.255.224 up
-sh: cisco@fs-client10:~$: not found
cisco@fs-client10:~$ cisco@fs-client10:~$ sudo route del default 2>/dev/null
cisco@fs-client10:~$ cisco@fs-client10:~$ sudo route add default gw 10.0.16.1 et
h0
-sh: cisco@fs-client10:~$: not found
cisco@fs-client10:~$ cisco@fs-client10:~$ ping -c 5 10.0.16.1
-sh: cisco@fs-client10:~$: not found
cisco@fs-client10:~$ 
cisco@fs-client10:~$ 
cisco@fs-client10:~$  sudo ifconfig eth0 10.0.16.10 netmask 255.255.255.224 up
cisco@fs-client10:~$ sudo ifconfig eth0 10.0.16.10 netmask 255.255.255.224 up
cisco@fs-client10:~$ sudo route del default 2>/dev/null
cisco@fs-client10:~$ sudo route add default gw 10.0.16.1 eth0
cisco@fs-client10:~$ ping -c 5 10.0.16.1
PING 10.0.16.1 (10.0.16.1): 56 data bytes
64 bytes from 10.0.16.1: seq=0 ttl=255 time=1.660 ms
64 bytes from 10.0.16.1: seq=1 ttl=255 time=0.732 ms
64 bytes from 10.0.16.1: seq=2 ttl=255 time=0.837 ms
64 bytes from 10.0.16.1: seq=3 ttl=255 time=1.011 ms
64 bytes from 10.0.16.1: seq=4 ttl=255 time=0.921 ms

--- 10.0.16.1 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.732/1.032/1.660 ms
cisco@fs-client10:~$ 


FS-R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
FS-R1(config)#interface ethernet0/0
FS-R1(config-if)#no shutdown
FS-R1(config-if)#end
*Jul 19 16:04:57.037: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
FS-R1(config-if)#end
FS-R1#
*Jul 19 16:04:57.145: %HSRP-5-STATECHANGE: Ethernet0/0.40 Grp 40 state Listen -> Active
*Jul 19 16:04:57.224: %HSRP-5-STATECHANGE: Ethernet0/0.10 Grp 10 state Listen -> Active
*Jul 19 16:04:57.256: %HSRP-5-STATECHANGE: Ethernet0/0.20 Grp 20 state Listen -> Active
*Jul 19 16:04:57.738: %HSRP-5-STATECHANGE: Ethernet0/0.30 Grp 30 state Listen -> Active
*Jul 19 16:04:57.945: %SYS-5-CONFIG_I: Configured from console by console
FS-R1#
*Jul 19 16:04:58.037: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
FS-R1#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Et0/0.10    10   105 P Active  local           10.0.16.3       10.0.16.1
Et0/0.20    20   105 P Active  local           10.0.16.131     10.0.16.129
Et0/0.30    30   105 P Active  local           unknown         10.0.17.1
Et0/0.40    40   105 P Active  local           10.0.17.131     10.0.17.129
FS-R1#
```
