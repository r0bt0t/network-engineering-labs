# Lab 026 - Raw CLI Output

```bash
Cafe-SW1>en
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#vlan 10
Cafe-SW1(config-vlan)#name
*Jun 24 16:32:39.187: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW1(config-vlan)#name 
*Jun 24 16:32:39.290: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 16:32:39.290: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 16:32:39.396: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW1(config-vlan)#name AD<
*Jun 24 16:32:39.496: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Jun 24 16:32:39.496: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW1(config-vlan)#name ADMIN_DEVICES
Cafe-SW1(config-vlan)#exit
Cafe-SW1(config)#vlan 20
Cafe-SW1(config-vlan)#name PATRON_DEVICES
Cafe-SW1(config-vlan)#exit
Cafe-SW1(config)#interface range et
Cafe-SW1(config)#interface range ethernet0/1-2
Cafe-SW1(config-if-range)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if-range)#switchport mode trunk
Cafe-SW1(config-if-range)#
*Jun 24 16:33:55.101: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Jun 24 16:33:55.102: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
Cafe-SW1(config-if-range)#end
Cafe-SW1#
*Jun 24 16:33:58.102: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Jun 24 16:33:58.102: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Cafe-SW1#
*Jun 24 16:33:58.111: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show interface trunk 

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1-4094
Et0/2          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20
Et0/2          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1
Et0/2          1
Cafe-SW1#

Cafe-SW2>en
Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#
*Jun 24 16:34:42.405: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jun 24 16:34:42.507: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 16:34:42.507: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Jun 24 16:34:42.614: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW2(config)#
*Jun 24 16:34:42.714: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Jun 24 16:34:42.714: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW2(config)#vlan 10
Cafe-SW2(config-vlan)#name ADMIN_DEVICES
Cafe-SW2(config-vlan)#exit
Cafe-SW2(config)#vlan 20
Cafe-SW2(config-vlan)#name PATRON_DEVICES
Cafe-SW2(config-vlan)#exit
Cafe-SW2(config)#int
Cafe-SW2(config)#interface range e
Cafe-SW2(config)#interface range ethernet 0/1-2
Cafe-SW2(config-if-range)#switchport trunk encapsulation dot1q
Cafe-SW2(config-if-range)#switchport mode trunk
Cafe-SW2(config-if-range)#end
Cafe-SW2#
*Jun 24 16:36:01.391: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1-4094
Et0/2          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20
Et0/2          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20
Et0/2          none
Cafe-SW2#


Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#int
Cafe-SW1(config)#interface e
Cafe-SW1(config)#interface eth
Cafe-SW1(config)#interface ethernet0/3
Cafe-SW1(config-if)#switchport mode access
Cafe-SW1(config-if)#switchport access vlan 10
Cafe-SW1(config-if)#end
Cafe-SW1#show 
*Jun 24 16:37:33.718: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0
10   ADMIN_DEVICES                    active    Et0/3
20   PATRON_DEVICES                   active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW1#

Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#int
Cafe-SW2(config)#interface eth
Cafe-SW2(config)#interface ethernet0/3
Cafe-SW2(config-if)#switchport mode access
Cafe-SW2(config-if)#switchport access vlan 10
Cafe-SW2(config-if)#end
Cafe-SW2#show 
*Jun 24 16:38:43.792: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0
10   ADMIN_DEVICES                    active    Et0/3
20   PATRON_DEVICES                   active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW2#


Core Linux
cafe-admin1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-admin1:~$ sudo ifconfig eth0 10.0.18.2 netmask 255.255.255.224 up
cisco@cafe-admin1:~$ sudo route del default 2>/dev/null
cisco@cafe-admin1:~$ sudo route add default gw 10.0.18.1 eth0
cisco@cafe-admin1:~$ 



Core Linux
cafe-client1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-client1:~$ sudo ifconfig eth0 10.0.18.3 netmask 255.255.255.224 up
cisco@cafe-client1:~$ sudo route del default 2>/dev/null
cisco@cafe-client1:~$ sudo route add default gw 10.0.18.1 eth0
cisco@cafe-client1:~$ 


cisco@cafe-admin1:~$ ping -c 5 10.0.18.3
PING 10.0.18.3 (10.0.18.3): 56 data bytes
64 bytes from 10.0.18.3: seq=0 ttl=64 time=2.060 ms
64 bytes from 10.0.18.3: seq=1 ttl=64 time=1.304 ms
64 bytes from 10.0.18.3: seq=2 ttl=64 time=1.334 ms
64 bytes from 10.0.18.3: seq=3 ttl=64 time=1.275 ms
64 bytes from 10.0.18.3: seq=4 ttl=64 time=1.339 ms

--- 10.0.18.3 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.275/1.462/2.060 ms
cisco@cafe-admin1:~$ 

Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#int
Cafe-SW2(config)#interface  eth
Cafe-SW2(config)#interface  ethernet0/3
Cafe-SW2(config-if)#switchport access vlan 20
Cafe-SW2(config-if)#end
Cafe-SW2#sho
*Jun 24 16:43:40.987: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0
10   ADMIN_DEVICES                    active    
20   PATRON_DEVICES                   active    Et0/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW2#

cisco@cafe-client1:~$ 
cisco@cafe-client1:~$ sudo ifconfig eth0 10.0.18.34 netmask 255.255.255.224 up
cisco@cafe-client1:~$ sudo route del default 2>/dev/null
cisco@cafe-client1:~$ sudo route add default gw 10.0.18.33 eth0
cisco@cafe-client1:~$ 


cisco@cafe-admin1:~$ 
cisco@cafe-admin1:~$ ping -c 5 10.0.18.34
PING 10.0.18.34 (10.0.18.34): 56 data bytes

--- 10.0.18.34 ping statistics ---
5 packets transmitted, 0 packets received, 100% packet loss
cisco@cafe-admin1:~$ 


Cafe-SW1#
Cafe-SW1#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1-4094
Et0/2          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20
Et0/2          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20
Et0/2          1,10,20
Cafe-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0
10   ADMIN_DEVICES                    active    Et0/3
20   PATRON_DEVICES                   active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW1#

Cafe-SW2#
Cafe-SW2#show interface trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          1-4094
Et0/2          1-4094

Port           Vlans allowed and active in management domain
Et0/1          1,10,20
Et0/2          1,10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          1,10,20
Et0/2          none
Cafe-SW2#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0
10   ADMIN_DEVICES                    active    
20   PATRON_DEVICES                   active    Et0/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
Cafe-SW2#
```
