# Lab 025 - Raw CLI Output

```bash
CafeSwitch01>en
CafeSwitch01#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
                                                Et3/0, Et3/1, Et3/2, Et3/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
CafeSwitch01#
CafeSwitch01#
CafeSwitch01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
CafeSwitch01(config)#vlan 10
CafeSwitch01(config-vlan)#name ADMIN_DEVICES
CafeSwitch01(config-vlan)#exit
CafeSwitch01(config)#vlan 20
CafeSwitch01(config-vlan)#name PATRON_DEVICES
CafeSwitch01(config-vlan)#end
CafeSwitch01#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
                                                Et3/0, Et3/1, Et3/2, Et3/3
10   ADMIN_DEVICES                    active    
20   PATRON_DEVICES                   active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
CafeSwitch01#

CafeSwitch02>en
CafeSwitch02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
CafeSwitch02(config)#vlan 10
CafeSwitch02(config-vlan)#name ADMIN_DEVICES
CafeSwitch02(config-vlan)#exit
CafeSwitch02(config)#vlan 20
CafeSwitch02(config-vlan)#name PATRON_DEVICES
CafeSwitch02(config-vlan)#end
CafeSwitch02#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1, Et2/2, Et2/3
                                                Et3/0, Et3/1, Et3/2, Et3/3
10   ADMIN_DEVICES                    active    
20   PATRON_DEVICES                   active    
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
CafeSwitch02#


CafeSwitch01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
CafeSwitch01(config)#interface range ethernet2/2 - 3, ethernet3/0 - 3
CafeSwitch01(config-if-range)#switchport mode access
CafeSwitch01(config-if-range)#switchport access vlan 20
CafeSwitch01(config-if-range)#end
CafeSwitch01#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et0/3
                                                Et1/0, Et1/1, Et1/2, Et1/3
                                                Et2/0, Et2/1
10   ADMIN_DEVICES                    active    
20   PATRON_DEVICES                   active    Et2/2, Et2/3, Et3/0, Et3/1
                                                Et3/2, Et3/3
1002 fddi-default                     act/unsup 
1003 token-ring-default               act/unsup 
1004 fddinet-default                  act/unsup 
1005 trnet-default                    act/unsup 
CafeSwitch01#
```
