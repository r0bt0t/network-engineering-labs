# Lab 002 - Raw CLI Dump

```bash
enable
configure terminal
```

```bash
Switch(config)#hostname Cafe-01-SW1
Cafe-01-SW1(config)#banner motd ^Unauthorized access ends badly. Authorized Castle Rysen engineers only.^
Cafe-01-SW1(config)#enable secret C4stleRysen!
Cafe-01-SW1(config)#line con 0
Cafe-01-SW1(config-line)#password VaultAccessCafe-01-SW1(config-line)# ^C
Cafe-01-SW1(config-line)#password VaultAccess
Cafe-01-SW1(config-line)#login
Cafe-01-SW1(config)#service password-encryption
Cafe-01-SW1(config)#line vty 0 4
Cafe-01-SW1(config-line)#password ShelterAccess
Cafe-01-SW1(config-line)#login
Cafe-01-SW1(config-line)#transport input ssh
Cafe-01-SW1(config-line)#exit
Cafe-01-SW1(config)#interface vlan1
Cafe-01-SW1(config-if)#ip address 192.168.10.10 255.255.255.0
Cafe-01-SW1(config-if)#no shutdown
Cafe-01-SW1(config-if)#interface ethernet0/0
Cafe-01-SW1(config-if)#description Uplink-to-Core-Distribution
Cafe-01-SW1(config-if)#
Cafe-01-SW1#copy running-config startup-config
Destination filename [startup-config]? 
```

## Verification Commands

```bash
show ip interface brief
show running-config
```
