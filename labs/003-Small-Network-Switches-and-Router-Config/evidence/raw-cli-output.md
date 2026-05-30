# Lab 003 - Raw CLI Dump

```bash
Switch1>en
Switch1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch1(config)#hostname DS-07-SW1                                                         
DS-07-SW1(config)#banner motd ^Castle Rysen Ops: Authorised engineers only.^
DS-07-SW1(config)#enable secret CrC0ffee!

Switch2>en
Switch2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch2(config)#hostname DS-07-SW2
DS-07-SW2(config)#banner motd ^Castle Rysen Ops: Authorised Engineers only.^
DS-07-SW2(config)#enable secret CrC0ffee!

Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname DS-07-RTR1
DS-07-RTR1(config)#banner motd ^Castle Rysen Ops: Authorised engineers only.^
DS-07-RTR1(config)#enable secret CrC0ffee!
```

---

```bash
DS-07-SW1(config)#line con 0
DS-07-SW1(config-line)#password VaultAccess
DS-07-SW1(config-line)#login
DS-07-SW1(config-line)#exit
DS-07-SW1(config)#service password encryption
                                   ^
% Invalid input detected at '^' marker.

DS-07-SW1(config)#service password-encryption
DS-07-SW1(config)#username admin secret ShelterAccess
DS-07-SW1(config)#line vty 0 4
DS-07-SW1(config-line)#login local
DS-07-SW1(config-line)#transport input ssh
DS-07-SW1(config-line)#exit
DS-07-SW1(config)#ip ssh version 2
DS-07-SW1(config)#exec-timeout 10 0
                    ^
% Invalid input detected at '^' marker.

DS-07-SW1(config)#line vty 0 4
DS-07-SW1(config-line)#exec-timeout 10 0
DS-07-SW1(config-line)#exit
DS-07-SW1(config)#interface vlan1
DS-07-SW1(config-if)#ip address 192.168.10.11 255.255.255.0
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#exit
DS-07-SW1(config)#ip default-gateway 192.168.10.1
DS-07-SW1(config)#ip domain name castle.local
DS-07-SW1(config)#crypto key generate rsa
The name for the keys will be: DS-07-SW1.castle.local
Choose the size of the key modulus in the range of 2048 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [2048]: 2048
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

DS-07-SW1(config)#interface en0/3
                             ^
% Invalid input detected at '^' marker.

DS-07-SW1(config)#interface et0/3
DS-07-SW1(config-if)#description Uplink-to-Router
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#interface e0/2
DS-07-SW1(config-if)#description WAP1-Feed
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#interface e0/1
DS-07-SW1(config-if)#description Link-to-DS-07-SW2
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#interface e0/0
DS-07-SW1(config-if)#description 2nd-Link-to-DS-07-SW2
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#^Z
DS-07-SW1#write memory
Building configuration...
[OK]
DS-07-SW1#

DS-07-SW2(config)#line con 0
DS-07-SW2(config-line)#password VaultAccess
DS-07-SW2(config-line)#login
DS-07-SW2(config-line)#exit
DS-07-SW2(config)#service password encryption
                                   ^
% Invalid input detected at '^' marker.

DS-07-SW2(config)#service password-encryption
DS-07-SW2(config)#username admin secret ShelterAccess
DS-07-SW2(config)#line vty 0 4
DS-07-SW2(config-line)#login local
DS-07-SW2(config-line)#transport input ssh
DS-07-SW2(config-line)#exec-timeout 10 0
DS-07-SW2(config-line)#exit
DS-07-SW2(config)#ip ssh version 2
DS-07-SW2(config)#ip domain name castle.local
DS-07-SW2(config)#crypto key generate rsa
The name for the keys will be: DS-07-SW2.castle.local
Choose the size of the key modulus in the range of 2048 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [2048]: 2048
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

DS-07-SW2(config)#interface vlan1
DS-07-SW2(config-if)#ip address 192.168.10.12 255.255.255.0
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#exit
DS-07-SW2(config)#ip default-gateway 192.168.10.1
DS-07-SW2(config)#interface e0/0
DS-07-SW2(config-if)#description Link-to-DS-07-SW1
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#interface e0/1
DS-07-SW2(config-if)#description 2nd-Link-to-DS-07-SW1
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#interface e0/2
DS-07-SW2(config-if)#description WAP2-link
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#interface e0/3
DS-07-SW2(config-if)#description Drop-to-Server
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#exit
DS-07-SW2(config)#exit
DS-07-SW2#write memory
Building configuration...
[OK]
DS-07-SW2#

Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname DS-07-RTR1
DS-07-RTR1(config)#banner motd ^Castle Rysen Ops: Authorised engineers only.^
DS-07-RTR1(config)#enable secret CrC0ffee!
DS-07-RTR1(config)#line con 0
DS-07-RTR1(config-line)#password VaultAccess
DS-07-RTR1(config-line)#login
DS-07-RTR1(config-line)#exit
DS-07-RTR1(config)#service password-encryption
DS-07-RTR1(config)#username admin secret ShelterAccess
DS-07-RTR1(config)#ip ssh version 2
DS-07-RTR1(config)#ip domain name castle.local
DS-07-RTR1(config)#crypto key generate rsa
The name for the keys will be: DS-07-RTR1.castle.local
Choose the size of the key modulus in the range of 2048 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [2048]: 2048
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

DS-07-RTR1(config)#line vty 0 4
DS-07-RTR1(config-line)#login local
DS-07-RTR1(config-line)#transport input ssh
DS-07-RTR1(config-line)#exec-timeout 10 0
DS-07-RTR1(config-line)#exit
DS-07-RTR1(config)#interface e0/0
DS-07-RTR1(config-if)#description Link-to-DS-07-SW1
DS-07-RTR1(config-if)#no shutdown
DS-07-RTR1(config-if)#inteface vlan1
                       ^
% Invalid input detected at '^' marker.

DS-07-RTR1(config-if)#interface vlan1
                                 ^
% Invalid input detected at '^' marker.

DS-07-RTR1(config)#interface vlan1
                              ^
% Invalid input detected at '^' marker.

DS-07-RTR1(config)#interface e0/0
DS-07-RTR1(config-if)#ip address 192.168.10.1
% Incomplete command.

DS-07-RTR1(config-if)#ip address 192.168.10.1 255.255.255.0
DS-07-RTR1(config-if)#^Z
DS-07-RTR1#write memory
Building configuration...
[OK]

DS-07-SW1#ping 192.168.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.1, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
DS-07-SW1#ping 192.168.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
DS-07-SW1#

DS-07-SW2#ping 192.168.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.1, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
DS-07-SW2#ping 192.168.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
DS-07-SW2#
```
