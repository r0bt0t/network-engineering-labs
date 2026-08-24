# Lab 066 - Raw CLI Output

```bash
RTR-Training-01>
RTR-Training-01>en
RTR-Training-01#termnal length 0
                    ^
% Invalid input detected at '^' marker.

RTR-Training-01#termnal length 0
*Aug 20 12:43:22.488: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
RTR-Training-01#termnal length 0
*Aug 20 12:43:22.591: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 12:43:22.591: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 12:43:22.695: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
RTR-Training-01#termnal length 0
*Aug 20 12:43:22.795: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 20 12:43:22.795: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
RTR-Training-01#terminal length 0
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#no logging console
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#
RTR-Training-01#show ip interface brief | include Ethernet0/0|Ethernet0/1
Ethernet0/0            10.22.30.1      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
RTR-Training-01#
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#interface Ethernet0/1
RTR-Training-01(config-if)#ip address 203.0.113.54 255.255.255.252
RTR-Training-01(config-if)#no shutdown
RTR-Training-01(config-if)#exit
RTR-Training-01(config)#ip name-server 203.0.113.53
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#ping 203.0.113.53
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 203.0.113.53, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Training-01#
RTR-Training-01#ping cisco.com   
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 198.51.100.10, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Training-01#


RTR-Training-01#
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#ip domain name castlerysen.local
RTR-Training-01(config)#ip dns server
RTR-Training-01(config)#ip host roaster.castlerysen.local 10.22.88.15
RTR-Training-01(config)#ip host orders.castlerysen.local 10.22.88.25 
RTR-Training-01(config)#ip host archive.castlerysen.local 10.22.88.45
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#
RTR-Training-01#ping roaster
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.88.15, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Training-01#
RTR-Training-01#
RTR-Training-01#ping archive.castlerysen.local
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.88.45, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Training-01#
RTR-Training-01#
RTR-Training-01#ping orders
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.88.25, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Training-01#
RTR-Training-01#show hosts
Default domain is castlerysen.local
Name servers are 203.0.113.53
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------
 15.88.22.10.in-addr.arpa       10      IN      PTR     roaster.castlerysen.local
 25.88.22.10.in-addr.arpa       10      IN      PTR     orders.castlerysen.local
 45.88.22.10.in-addr.arpa       10      IN      PTR     archive.castlerysen.local
 archive.castlerysen.local      10      IN      A       10.22.88.45
 orders.castlerysen.local       10      IN      A       10.22.88.25
 roaster.castlerysen.local      10      IN      A       10.22.88.15



SW-Training-01#show ip interface brief | include VLAN 10
SW-Training-01#
SW-Training-01#show interfaces status | include Et0/1
Et0/1        Uplink to RTR-Trai connected    10           full   auto 10/100/1000BaseTX
SW-Training-01#show ip interface brief | include Vlan10 
Vlan10                 10.22.30.11     YES TFTP   up                    up      
SW-Training-01#
SW-Training-01#
SW-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-Training-01(config)#interface vlan 10
SW-Training-01(config-if)#ip address 10.22.30.11 255.255.255.0
SW-Training-01(config-if)#no shutdown
SW-Training-01(config-if)#exit
SW-Training-01(config)#ip default-gateway 10.22.30.1
SW-Training-01(config)#ip route 0.0.0.0 0.0.0.0 10.22.30.1
SW-Training-01(config)#ip domain name castlerysen.local
SW-Training-01(config)#ip name-server 10.22.30.1
SW-Training-01(config)#end
SW-Training-01#
SW-Training-01#ping orders
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.88.25, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-Training-01#
SW-Training-01#
SW-Training-01#ping archive
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.88.45, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-Training-01#
SW-Training-01#show hosts
Default domain is castlerysen.local
Name servers are 10.22.30.1
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------
 archive.castlerysen.local      0       IN      A       10.22.88.45

SW-Training-01#ping orders 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.88.25, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-Training-01#ping roaster 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.88.15, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-Training-01#
SW-Training-01#show hosts
Default domain is castlerysen.local
Name servers are 10.22.30.1
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------
 roaster.castlerysen.local      5       IN      A       10.22.88.15

SW-Training-01#


On this switch image, show hosts confirms the domain and name server but does not keep the resolved orders and archive entries in the displayed table. Use the ping destination address and success rate as the verification.
```
