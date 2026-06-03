# Raw CLI Output - Lab 010 Configuring Switch Interfaces

```bash
Connecting to console for Cafe-SW1


User Access Verification

Username: cisco
Password: 
Cafe-SW1>en
Password: 
Cafe-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW1(config)#


Connecting to console for Cafe-SW2


User Access Verification

Username: 
% Username:  timeout expired!
Username: cisco
Password: 
Cafe-SW2>en
Password: 
Cafe-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-SW2(config)#


Cafe-SW1(config)#interface et0/0
Cafe-SW1(config-if)#description "## Cafe-SW2 Uplink"
Cafe-SW1(config-if)#interface et0/1
Cafe-SW1(config-if)#description "## BaristaPOS" 
Cafe-SW1(config-if)#
Cafe-SW1(config-if)#exit
Cafe-SW1(config)#show interfaces description
                   ^
% Invalid input detected at '^' marker.

Cafe-SW1(config)#show interfaces description^Z                   ^
% Invalid input detected at '^' marker.

Cafe-SW1#^Z
Cafe-SW1#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       "## Cafe-SW2 Uplink"
Et0/1                          up             up       "## BaristaPOS"
Et0/2                          up             up       
Et0/3                          up             up       
Et1/0                          admin down     down     
Et1/1                          admin down     down     
Et1/2                          admin down     down     
Et1/3                          admin down     down     
Vl42                           admin down     down     
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#


Cafe-SW2(config)#interface et0/0
Cafe-SW2(config-if)#description "## Cafe-SW1 Uplink"
Cafe-SW2(config-if)#interface et0/1
Cafe-SW2(config-if)#description "## Camera Feed"
Cafe-SW2(config-if)#interface et0/3
Cafe-SW2(config-if)#description "## Thermostat"
Cafe-SW2(config-if)#^Z
Cafe-SW2#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       "## Cafe-SW1 Uplink"
Et0/1                          up             up       "## Camera Feed"
Et0/2                          up             up       
Et0/3                          up             up       "## Thermostat"
Et1/0                          admin down     down     
Et1/1                          admin down     down     
Et1/2                          admin down     down     
Et1/3                          admin down     down     
Vl42                           admin down     down     
Cafe-SW2#

Cafe-SW1(config)#interface et0/0
Cafe-SW1(config-if)#duplex full
Cafe-SW1(config-if)#^Z
Cafe-SW1#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        "## Cafe-SW2 Uplin connected    1            full   auto 10/100/1000BaseTX
Et0/1        "## BaristaPOS"    connected    1            full   auto 10/100/1000BaseTX
Et0/2                           connected    1            full   auto 10/100/1000BaseTX
Et0/3                           connected    1            full   auto 10/100/1000BaseTX
Et1/0                           disabled     1            full   auto 10/100/1000BaseTX
Et1/1                           disabled     1            full   auto 10/100/1000BaseTX
Et1/2                           disabled     1            full   auto 10/100/1000BaseTX
Et1/3                           disabled     1            full   auto 10/100/1000BaseTX
Cafe-SW1#

Cafe-SW2(config)#interface et0/0
Cafe-SW2(config-if)#duplex full
Cafe-SW2(config-if)#interface et0/1
Cafe-SW2(config-if)#duplex full    
Cafe-SW2(config-if)#interface et0/3
Cafe-SW2(config-if)#duplex full    
Cafe-SW2(config-if)#^Z
Cafe-SW2#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        "## Cafe-SW1 Uplin connected    1            full   auto 10/100/1000BaseTX
Et0/1        "## Camera Feed"   connected    1            full   auto 10/100/1000BaseTX
Et0/2                           connected    1            full   auto 10/100/1000BaseTX
Et0/3        "## Thermostat"    connected    1            full   auto 10/100/1000BaseTX
Et1/0                           disabled     1            full   auto 10/100/1000BaseTX
Et1/1                           disabled     1            full   auto 10/100/1000BaseTX
Et1/2                           disabled     1            full   auto 10/100/1000BaseTX
Et1/3                           disabled     1            full   auto 10/100/1000BaseTX
Cafe-SW2#

Cafe-SW1#show interfaces ethernet0/0 | include duplex|collisions|reset|error|C$
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 output errors, 0 collisions, 1 interface resets
Cafe-SW1#
Cafe-SW1#show interfaces ethernet0/1 | include duplex|collisions|reset|error|C$
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 output errors, 0 collisions, 1 interface resets

Cafe-SW2#show interfaces ethernet0/0 | include duplex|collisions|reset|error|C$
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 output errors, 0 collisions, 1 interface resets
Cafe-SW2#$aces ethernet0/1 | include duplex|collisions|reset|error|CRC
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 output errors, 0 collisions, 1 interface resets
Cafe-SW2#$aces ethernet0/3 | include duplex|collisions|reset|error|CRC
  Full-duplex, Auto-speed, media type is 10/100/1000BaseTX
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 output errors, 0 collisions, 1 interface resets
Cafe-SW2#

Cafe-SW1(config)#vlan 42
Cafe-SW1(config-vlan)#name MGMT
Cafe-SW1(config-vlan)#interface vlan 42
Cafe-SW1(config-if)#description "## MGMT"
Cafe-SW1(config-if)#ip address 192.168.42.1 255.255.255.0
Cafe-SW1(config-if)#no shutdown
Cafe-SW1(config-if)#exit
Cafe-SW1(config)#ip default-gateway 192.168.42.254
Cafe-SW1(config)#^Z
Cafe-SW1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  administratively down down    
Ethernet1/1            unassigned      YES unset  administratively down down    
Ethernet1/2            unassigned      YES unset  administratively down down    
Ethernet1/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.1    YES manual down                  down    
Cafe-SW1#

Cafe-SW2(config)#vlan 42
Cafe-SW2(config-vlan)#name MGMT
Cafe-SW2(config-vlan)#interface vlan 42
Cafe-SW2(config-if)#description "## MGMT"
Cafe-SW2(config-if)#ip address 192.168.42.2 255.255.255.0
Cafe-SW2(config-if)#no shutdown
Cafe-SW2(config-if)#exit
Cafe-SW2(config)#ip default-gateway 192.168.42.254
Cafe-SW2(config)#^Z
Cafe-SW2#show ip interface brief 
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  administratively down down    
Ethernet1/1            unassigned      YES unset  administratively down down    
Ethernet1/2            unassigned      YES unset  administratively down down    
Ethernet1/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.2    YES manual down                  down    
Cafe-SW2#

Cafe-SW1(config)#interface et0/0
Cafe-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-SW1(config-if)#switchport mode trunk
Cafe-SW1(config-if)#switchport trunk allowed vlan add 42
Cafe-SW1(config-if)#no shutdown
Cafe-SW1(config-if)#exit
Cafe-SW1(config)#^Z
Cafe-SW1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  administratively down down    
Ethernet1/1            unassigned      YES unset  administratively down down    
Ethernet1/2            unassigned      YES unset  administratively down down    
Ethernet1/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.1    YES manual up                    up      
Cafe-SW1#

Cafe-SW2(config)#interface et0/0
Cafe-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-SW2(config-if)#switchport mode trunk
Cafe-SW2(config-if)#switchport trunk allowed vlan add 42
Cafe-SW2(config-if)#no shutdown
Cafe-SW2(config-if)#^Z
Cafe-SW2#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  administratively down down    
Ethernet1/1            unassigned      YES unset  administratively down down    
Ethernet1/2            unassigned      YES unset  administratively down down    
Ethernet1/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.2    YES manual up                    up      
Cafe-SW2#

Cafe-SW1#ping 192.168.42.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.2, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
Cafe-SW1#ping 192.168.42.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-SW1#

Cafe-SW2#ping 192.168.42.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.42.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
Cafe-SW2#

Cafe-SW1#show interface status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        "## Cafe-SW2 Uplin connected    trunk        full   auto 10/100/1000BaseTX
Et0/1        "## BaristaPOS"    connected    1            full   auto 10/100/1000BaseTX
Et0/2                           connected    1            full   auto 10/100/1000BaseTX
Et0/3                           connected    1            full   auto 10/100/1000BaseTX
Et1/0                           disabled     1            full   auto 10/100/1000BaseTX
Et1/1                           disabled     1            full   auto 10/100/1000BaseTX
Et1/2                           disabled     1            full   auto 10/100/1000BaseTX
Et1/3                           disabled     1            full   auto 10/100/1000BaseTX
Cafe-SW1#
Cafe-SW1#
Cafe-SW1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  administratively down down    
Ethernet1/1            unassigned      YES unset  administratively down down    
Ethernet1/2            unassigned      YES unset  administratively down down    
Ethernet1/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.1    YES manual up                    up      
Cafe-SW1#

Cafe-SW2#show interface status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        "## Cafe-SW1 Uplin connected    trunk        full   auto 10/100/1000BaseTX
Et0/1        "## Camera Feed"   connected    1            full   auto 10/100/1000BaseTX
Et0/2                           connected    1            full   auto 10/100/1000BaseTX
Et0/3        "## Thermostat"    connected    1            full   auto 10/100/1000BaseTX
Et1/0                           disabled     1            full   auto 10/100/1000BaseTX
Et1/1                           disabled     1            full   auto 10/100/1000BaseTX
Et1/2                           disabled     1            full   auto 10/100/1000BaseTX
Et1/3                           disabled     1            full   auto 10/100/1000BaseTX
Cafe-SW2#
Cafe-SW2#
Cafe-SW2#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  administratively down down    
Ethernet1/1            unassigned      YES unset  administratively down down    
Ethernet1/2            unassigned      YES unset  administratively down down    
Ethernet1/3            unassigned      YES unset  administratively down down    
Vlan42                 192.168.42.2    YES manual up                    up      
Cafe-SW2#
```
