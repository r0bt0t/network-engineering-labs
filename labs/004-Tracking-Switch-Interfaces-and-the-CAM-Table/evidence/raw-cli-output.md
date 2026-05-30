# Lab 004 - Raw CLI Dump

```bash
Switch6#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Switch6#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink-to-CoreSwitch
Et0/1                          up             up       AccessPoint1
Et0/2                          up             up       SensorPod-A
Et0/3                          admin down     down     Reserved-StackLink
Switch6#show interface status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        Uplink-to-CoreSwit connected    trunk        full   auto 10/100/1000BaseTX
Et0/1        AccessPoint1       connected    10           full   auto 10/100/1000BaseTX
Et0/2        SensorPod-A        connected    20           full   auto 10/100/1000BaseTX
Et0/3        Reserved-StackLink disabled     1            full   auto 10/100/1000BaseTX
Switch6#show mac address table
                         ^
% Invalid input detected at '^' marker.

Switch6#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.0058.297b    DYNAMIC     Et0/1
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  20    5254.0036.d8d6    DYNAMIC     Et0/2
  20    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0 
Total Mac Addresses for this criterion: 6
Switch6#show mac address-table|5a5a.1c1c.0d0d
                              ^
% Invalid input detected at '^' marker.

Switch6#show mac address-table | 5a5a.1c1c.0d0d
                                 ^
% Invalid input detected at '^' marker.

Switch6#show mac address-table | 5a5a.1c1c.0d0d
                                 ^
% Invalid input detected at '^' marker.

Switch6#show mac address-table address 5a5a.1c1c.0d0d 
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
Total Mac Addresses for this criterion: 1
```
