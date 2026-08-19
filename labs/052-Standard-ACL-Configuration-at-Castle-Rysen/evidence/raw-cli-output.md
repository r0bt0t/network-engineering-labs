# Lab 052 - Raw CLI Output

```bash
Castle-Cafe-RTR#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  administratively down down    
Ethernet0/0.10         10.0.18.1       YES TFTP   administratively down down    
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#inte  
Castle-Cafe-RTR(config)#interface eth
Castle-Cafe-RTR(config)#interface ethernet0/0
Castle-Cafe-RTR(config-if)#no shutdown
Castle-Cafe-RTR(config-if)#
*Aug 17 10:29:28.853: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
Castle-Cafe-RTR(config-if)#
*Aug 17 10:29:29.853: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up


Cafe-SW>en
Cafe-SW#show interfaces trunk
Cafe-SW#
*Aug 17 10:30:23.634: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW#
*Aug 17 10:30:23.736: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 10:30:23.737: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 10:30:23.844: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW#
*Aug 17 10:30:23.944: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 17 10:30:23.945: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW#show ipint brief
               ^
% Invalid input detected at '^' marker.

Cafe-SW#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Cafe-SW#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW(config)#interface ethernet0/0
Cafe-SW(config-if)#switchport trunk encapsulation dot1q
Cafe-SW(config-if)#switchport mode trunk
Cafe-SW(config-if)#switch
*Aug 17 10:32:22.192: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Cafe-SW(config-if)#switchport trunk 
*Aug 17 10:32:25.193: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Cafe-SW(config-if)#switchport trunk allowed vlan 10
Cafe-SW(config-if)#spanning-tree portfast trunk
Cafe-SW(config-if)#end
Cafe-SW#
*Aug 17 10:32:53.074: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10

Port           Vlans allowed and active in management domain
Et0/0          10

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10
Cafe-SW#


Castle-Cafe-RTR#
Castle-Cafe-RTR#show running-config | section vty 
line vty 0 4
 access-class 50 in
 password CastleRysen!
 login
 transport input ssh
Castle-Cafe-RTR#line vty 5 15
                  ^
% Invalid input detected at '^' marker.

Castle-Cafe-RTR#show running-config | section line vty
line vty 0 4
 access-class 50 in
 password CastleRysen!
 login
 transport input ssh
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#line vty 0 4
Castle-Cafe-RTR(config-line)#no access-class 50 in
Castle-Cafe-RTR(config-line)#exit
Castle-Cafe-RTR(config)#line vty 5 15
                                 ^
% Invalid input detected at '^' marker.

Castle-Cafe-RTR(config)#end 
Castle-Cafe-RTR#
*Aug 17 10:40:35.700: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show running-config | section line vty
line vty 0 4
 password CastleRysen!
 login
 transport input ssh
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#no access-list 50
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#


Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ip access-list standard PC1-FILTER
Castle-Cafe-RTR(config-std-nacl)#remark Deny Cafe-PC1 streaming traffic
Castle-Cafe-RTR(config-std-nacl)#deny host 10.0.18.2
Castle-Cafe-RTR(config-std-nacl)#permit 10.0.18.0 0.0.0.255
Castle-Cafe-RTR(config-std-nacl)#exit
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Aug 17 10:43:43.898: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show access-lists PC1-FILTER
Standard IP access list PC1-FILTER
    10 deny   10.0.18.2
    20 permit 10.0.18.0, wildcard bits 0.0.0.255
Castle-Cafe-RTR#


Connecting to console for Cafe-PC1
Connected to CML terminalserver.

Core Linux
Cafe-PC1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@Cafe-PC1:~$ ping -c 3 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes
64 bytes from 10.0.18.1: seq=0 ttl=255 time=1.578 ms
64 bytes from 10.0.18.1: seq=1 ttl=255 time=0.611 ms
64 bytes from 10.0.18.1: seq=2 ttl=255 time=0.603 ms

--- 10.0.18.1 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.603/0.930/1.578 ms
cisco@Cafe-PC1:~$ ^C

cisco@Cafe-PC1:~$ 


Castle-Cafe-RTR#
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#interface ethernet0/0.10
Castle-Cafe-RTR(config-subif)#ip access-group PC1-FILTER in
Castle-Cafe-RTR(config-subif)#end
Castle-Cafe-RTR#
*Aug 17 10:46:38.951: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#

cisco@Cafe-PC1:~$ ping -c 3 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes

--- 10.0.18.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@Cafe-PC1:~$ 


Connecting to console for Cafe-PC2

Core Linux
Cafe-PC2 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@Cafe-PC2:~$ ping -c 3 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes
64 bytes from 10.0.18.1: seq=0 ttl=255 time=1.543 ms
64 bytes from 10.0.18.1: seq=1 ttl=255 time=0.622 ms
64 bytes from 10.0.18.1: seq=2 ttl=255 time=0.582 ms

--- 10.0.18.1 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.582/0.915/1.543 ms
cisco@Cafe-PC2:~$ 


Castle-Cafe-RTR#show access-lists PC1-FILTER
Standard IP access list PC1-FILTER
    10 deny   10.0.18.2 (6 matches)
    20 permit 10.0.18.0, wildcard bits 0.0.0.255 (6 matches)
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#interface ethernet0/0.10
Castle-Cafe-RTR(config-subif)#no ip access-group PC1-FILTER in
Castle-Cafe-RTR(config-subif)#end
Castle-Cafe-RTR#
*Aug 17 10:49:52.647: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show access-lists PC1-FILTER
Standard IP access list PC1-FILTER
    10 deny   10.0.18.2 (6 matches)
    20 permit 10.0.18.0, wildcard bits 0.0.0.255 (6 matches)
Castle-Cafe-RTR#
```
