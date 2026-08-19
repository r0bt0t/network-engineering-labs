# Lab 054 - Raw CLI Output

```bash
Connecting to console for Castle-Cafe-RTR

Castle-Cafe-RTR>en
Castle-Cafe-RTR#sho ip in
*Aug 17 11:41:33.464: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Castle-Cafe-RTR#sho ip int br
*Aug 17 11:41:33.567: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 11:41:33.567: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 11:41:33.672: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Castle-Cafe-RTR#sho ip int brief
*Aug 17 11:41:33.772: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 17 11:41:33.772: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Castle-Cafe-RTR#sho ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/0.20         10.0.18.33      YES TFTP   up                    up      
Ethernet0/1            10.0.16.1       YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#                
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#enshow ip interface brief | include ethernet0/0 |ethernet0/1
                  ^
% Invalid input detected at '^' marker.

Castle-Cafe-RTR#enshow ip interface brief | include ethernet0|et                                                         
Castle-Cafe-RTR#show ip int brief | include Ethernet0/0|Ethernet0/1
Ethernet0/0            unassigned      YES TFTP   up                    up      
Ethernet0/0.10         10.0.18.1       YES TFTP   up                    up      
Ethernet0/0.20         10.0.18.33      YES TFTP   up                    up      
Ethernet0/1            10.0.16.1       YES TFTP   up                    up      
Castle-Cafe-RTR#



Connecting to console for Cafe-SW1

Cafe-SW1>en
Cafe-SW1#show interface
*Aug 17 11:47:24.805: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Cafe-SW1#show interface t
*Aug 17 11:47:24.908: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 11:47:24.909: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 11:47:25.016: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW1#show interface t
*Aug 17 11:47:25.116: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 0 seconds).
*Aug 17 11:47:25.116: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW1#show interfaces trunk

Port           Mode             Encapsulation  Status        Native vlan  
Et0/0          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/0          10,20

Port           Vlans allowed and active in management domain
Et0/0          10,20

Port           Vlans in spanning tree forwarding state and not pruned
Et0/0          10,20
Cafe-SW1#


Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ip access-list extended CAFE-FILTER
Castle-Cafe-RTR(config-ext-nacl)#remark Allow patron Plex access$lex accesswhile shielding admin LAN        
Castle-Cafe-RTR(config-ext-nacl)#permit tcp 10.0.18.32 0.0.0.31 $ 0.0.0.31 10.0.18.0 0.0.0.31 eq 443        
Castle-Cafe-RTR(config-ext-nacl)#$ 0.0.0.31 10.0.18.0 0.0.0.31 eq 32400
Castle-Cafe-RTR(config-ext-nacl)#$ 0.0.0.31 10.0.18.0 0.0.0.31 eq 32469
Castle-Cafe-RTR(config-ext-nacl)#$ 0.0.0.31 10.0.18.0 0.0.0.31 eq 1900 
Castle-Cafe-RTR(config-ext-nacl)#$ 0.0.0.31 10.0.18.0 0.0.0.31 eq 5353
Castle-Cafe-RTR(config-ext-nacl)#deny ip 10.0.18.32 0.0.0.31 10.$0.18.32 0.0.0.31 10.0.18.0 0.0.0.31        
Castle-Cafe-RTR(config-ext-nacl)#permit ip any any
Castle-Cafe-RTR(config-ext-nacl)#exit
Castle-Cafe-RTR(config)#end
Castle-Cafe-RTR#
*Aug 17 11:52:19.183: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ip access-lists CAFE-FILTER
Extended IP access list CAFE-FILTER
    10 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 443
    20 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 32400
    30 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 32469
    40 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 1900
    50 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 5353
    60 deny ip 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31
    70 permit ip any any
Castle-Cafe-RTR#


cisco@patron-pc:~$ nc -vz -w 2 10.0.18.6 443
10.0.18.6 (10.0.18.6:443) open
cisco@patron-pc:~$ nc -vz -w 2 10.0.18.6 32400
10.0.18.6 (10.0.18.6:32400) open
cisco@patron-pc:~$ ping -c 3 10.0.18.6
PING 10.0.18.6 (10.0.18.6): 56 data bytes
64 bytes from 10.0.18.6: seq=0 ttl=63 time=1.356 ms
64 bytes from 10.0.18.6: seq=1 ttl=63 time=1.336 ms
64 bytes from 10.0.18.6: seq=2 ttl=63 time=1.431 ms

--- 10.0.18.6 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 1.336/1.374/1.431 ms
cisco@patron-pc:~$ 



Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#interface ethernet0/0.20
Castle-Cafe-RTR(config-subif)#ip access-group CAFE-FILTER in
Castle-Cafe-RTR(config-subif)#end
Castle-Cafe-RTR#
*Aug 17 12:58:55.846: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ip interface Ethernet0/0.20 | include access list
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is CAFE-FILTER
Castle-Cafe-RTR#



cisco@patron-pc:~$ nc -vz -w 2 10.0.18.6 443
10.0.18.6 (10.0.18.6:443) open
cisco@patron-pc:~$ nc -vz -w 2 10.0.18.6 32400
10.0.18.6 (10.0.18.6:32400) open
cisco@patron-pc:~$ ping -c 3 10.0.18.6
PING 10.0.18.6 (10.0.18.6): 56 data bytes

--- 10.0.18.6 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@patron-pc:~$ ping -c 3 10.0.18.4
PING 10.0.18.4 (10.0.18.4): 56 data bytes

--- 10.0.18.4 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@patron-pc:~$ 



Castle-Cafe-RTR#show ip access-lists CAFE-FILTER
Extended IP access list CAFE-FILTER
    10 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 443 (4 matches)
    20 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 32400 (4 matches)
    30 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 32469
    40 permit udp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 1900
    50 permit udp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 5353
    60 deny ip 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 (6 matches)
    70 permit ip any any (32 matches)
Castle-Cafe-RTR#


Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#interface ethernet0/0.20
Castle-Cafe-RTR(config-subif)#ip access-group CAFE-FILTER in
Castle-Cafe-RTR(config-subif)#end
Castle-Cafe-RTR#
*Aug 17 12:58:55.846: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#show ip interface Ethernet0/0.20 | include access list
  Outgoing Common access list is not set 
  Outgoing access list is not set
  Inbound Common access list is not set 
  Inbound  access list is CAFE-FILTER
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#show ip access-lists CAFE-FILTER
Extended IP access list CAFE-FILTER
    10 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 443 (4 matches)
    20 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 32400 (4 matches)
    30 permit tcp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 32469
    40 permit udp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 1900
    50 permit udp 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 eq 5353
    60 deny ip 10.0.18.32 0.0.0.31 10.0.18.0 0.0.0.31 (6 matches)
    70 permit ip any any (32 matches)
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#
Castle-Cafe-RTR#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Castle-Cafe-RTR(config)#ip access-list standard ADMIN-MGMT-ONLY
Castle-Cafe-RTR(config-std-nacl)#remark Restrict remote access t$rict remote access to trusted desks        
Castle-Cafe-RTR(config-std-nacl)#permit 10.0.18.0 0.0.0.31
Castle-Cafe-RTR(config-std-nacl)#permit 10.0.16.0 0.0.0.127
Castle-Cafe-RTR(config-std-nacl)#exit
Castle-Cafe-RTR(config)#line vty 0 4
Castle-Cafe-RTR(config-line)#access-class ADMIN-MGMT-ONLY in
Castle-Cafe-RTR(config-line)#transport input ssh telnet
Castle-Cafe-RTR(config-line)#end
Castle-Cafe-RTR#
*Aug 17 13:04:22.138: %SYS-5-CONFIG_I: Configured from console by console
Castle-Cafe-RTR#write memory
Building configuration...
[OK]
Castle-Cafe-RTR#show running-config | section line vty
line vty 0 4
 access-class ADMIN-MGMT-ONLY in
 password cisco
 login
 transport input telnet ssh
Castle-Cafe-RTR#




Cafe-SW1>en
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#ip
*Aug 17 13:05:30.948: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 17 13:05:31.050: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 13:05:31.051: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 13:05:31.159: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Cafe-SW1(config)#ip acces
*Aug 17 13:05:31.260: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 17 13:05:31.260: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Cafe-SW1(config)#ip access-list standard ADMIN-MGMT-ONLY
Cafe-SW1(config-std-nacl)#remark Restrict remote access to trusted desks
Cafe-SW1(config-std-nacl)#permit 10.0.18.0 0.0.0.31
Cafe-SW1(config-std-nacl)#permit 10.0.16.0 0.0.0.127
Cafe-SW1(config-std-nacl)#exit
Cafe-SW1(config)#line vty 0 4
Cafe-SW1(config-line)#access-class ADMIN-MGMT-ONLY in
Cafe-SW1(config-line)#transport input ssh telnet
Cafe-SW1(config-line)#end
Cafe-SW1#wri
*Aug 17 13:07:40.575: %SYS-5-CONFIG_I: Configured from console by console
Cafe-SW1#write memory
Building configuration...
[OK]
Cafe-SW1#



cisco@patron-pc:~$ telnet 10.0.18.3
telnet: can't connect to remote host (10.0.18.3): No route to host
cisco@patron-pc:~$ 



Connecting to console for Cafe-AdminPC

Core Linux
cafe-adminpc login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@cafe-adminpc:~$ cisco@patron-pc:~$ telnet 10.0.18.3
-sh: cisco@patron-pc:~$: not found
cisco@cafe-adminpc:~$ telnet: can't connect to remote host (10.0.18.3): No route
 to host
> cisco@patron-pc:~$ telnet 10.0.18.3
> 
> cisco
> telnet: can't connect to remote host (10.0.18.3): No route to> cisco@patron-pc:~$ telnet 10.0.18.3^C

cisco@cafe-adminpc:~$ telnet 10.0.18.3
Connected to 10.0.18.3

Entering character mode
Escape character is '^]'.



User Access Verification

Password:
```
