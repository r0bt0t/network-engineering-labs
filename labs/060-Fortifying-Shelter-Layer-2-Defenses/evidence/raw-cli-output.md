# Lab 060 - Raw CLI Output

```bash
Connecting to console for Cafe-01-SW1

Cafe-01-SW1>en
Cafe-01-SW1#show interfaces status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0                           connected    1            full   auto 10/100/1000BaseTX
Et0/1        Trunk to Cafe-01-S connected    1            full   auto 10/100/1000BaseTX
Et0/2                           connected    1            full   auto 10/100/1000BaseTX
Et0/3        Admin Workstation  connected    10           full   auto 10/100/1000BaseTX
Et1/0        Operations Kiosk D connected    10           full   auto 10/100/1000BaseTX
Et1/1        Patron Seating Dro connected    20           full   auto 10/100/1000BaseTX
Et1/2        Patron Seating Dro connected    20           full   auto 10/100/1000BaseTX
Et1/3        Patron Seating Dro connected    20           full   auto 10/100/1000BaseTX
Et2/0        Patron Seating Dro connected    20           full   auto 10/100/1000BaseTX
Et6/0        Uplink to Cafe-Edg connected    1            full   auto 10/100/1000BaseTX

Cafe-01-SW1#show cdp neighbors detail
-------------------------
Device ID: Cafe-01-SW2
Interface: Ethernet0/1,  Port ID (outgoing port): Ethernet0/1
Peer Source MAC: aabb.cc00.0610
Native VLAN: 1
Duplex: full

Total cdp entries displayed : 1

Cafe-01-SW1#show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/2, Et2/1 ...
10   VLAN0010                         active    Et0/3, Et1/0
20   VLAN0020                         active    Et1/1, Et1/2, Et1/3, Et2/0

Cafe-01-SW1#show interfaces trunk
Cafe-01-SW1#
(empty - no trunks configured yet)


Connecting to console for Cafe-Edge-R1

Cafe-Edge-R1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  administratively down down
Ethernet0/0.10         10.1.10.1       YES TFTP   administratively down down
Ethernet0/0.20         10.1.20.1       YES TFTP   administratively down down

Cafe-Edge-R1#show running-config interface Ethernet0/0.10
interface Ethernet0/0.10
 description Admin VLAN Gateway
 encapsulation dot1Q 10
 ip address 10.1.10.1 255.255.255.0

Cafe-Edge-R1#show running-config interface Ethernet0/0.20
interface Ethernet0/0.20
 description Patron VLAN Gateway
 encapsulation dot1Q 20
 ip address 10.1.20.1 255.255.255.0

Cafe-Edge-R1#show ip dhcp pool
Pool Admin :
 10.1.10.1        - 10.1.10.254       0     / 10    / 254
Pool Patron :
 10.1.20.1        - 10.1.20.254       0     / 10    / 254

Cafe-Edge-R1#configure terminal
Cafe-Edge-R1(config)#interface Ethernet0/0
Cafe-Edge-R1(config-if)# no shutdown
Cafe-Edge-R1(config-if)#interface Ethernet0/0.10
Cafe-Edge-R1(config-subif)# no shutdown
Cafe-Edge-R1(config-subif)#interface Ethernet0/0.20
Cafe-Edge-R1(config-subif)# no shutdown
Cafe-Edge-R1(config-subif)#end
*Aug 19 09:22:34.567: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Aug 19 09:22:35.566: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up

Cafe-Edge-R1#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up
Ethernet0/0.10         10.1.10.1       YES TFTP   up                    up
Ethernet0/0.20         10.1.20.1       YES TFTP   up                    up

Cafe-Edge-R1#show running-config | section dhcp
ip dhcp excluded-address 10.1.10.1 10.1.10.10
ip dhcp excluded-address 10.1.20.1 10.1.20.10
ip dhcp pool Admin
 network 10.1.10.0 255.255.255.0
 default-router 10.1.10.1
 dns-server 1.1.1.1
ip dhcp pool Patron
 network 10.1.20.0 255.255.255.0
 default-router 10.1.20.1
 dns-server 1.1.1.1


Connecting to console for Cafe-01-SW2

Cafe-01-SW2#show interfaces status
Port         Name               Status       Vlan       Duplex  Speed Type
Et0/1        Uplink to Cafe-01- connected    1            full   auto 10/100/1000BaseTX
Et0/2        Patron Workstation connected    20           full   auto 10/100/1000BaseTX
Et1/0        Operations Kiosk D connected    10           full   auto 10/100/1000BaseTX
Et1/1        Patron Seating Dro connected    20           full   auto 10/100/1000BaseTX
Et1/2        Patron Seating Dro connected    20           full   auto 10/100/1000BaseTX

Cafe-01-SW2#show cdp neighbors detail
-------------------------
Device ID: Cafe-01-SW1
Interface: Ethernet0/1,  Port ID (outgoing port): Ethernet0/1
Peer Source MAC: aabb.cc00.0510

Cafe-01-SW2#show vlan brief
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Et0/0, Et0/1, Et0/3, Et1/3
10   VLAN0010                         active    Et1/0
20   VLAN0020                         active    Et0/2, Et1/1, Et1/2


Cafe-Edge-R1#show ip interface brief
Ethernet0/0            unassigned      YES unset  up                    up
Ethernet0/0.10         10.1.10.1       YES TFTP   up                    up
Ethernet0/0.20         10.1.20.1       YES TFTP   up                    up


Connecting to console for Cafe-Admin-PC

admin@Cafe-Admin-PC:~$ ping -c 4 10.1.10.1
PING 10.1.10.1 (10.1.10.1): 56 data bytes
4 packets transmitted, 4 packets received, 0% packet loss
admin@Cafe-Admin-PC:~$ ping -c 4 10.1.20.1
4 packets transmitted, 4 packets received, 0% packet loss


Connecting to console for Cafe-Patron-PC

patron@Cafe-Patron-PC:~$ ping -c 4 10.1.10.1
4 packets transmitted, 4 packets received, 0% packet loss
patron@Cafe-Patron-PC:~$ ping -c 4 10.1.20.1
4 packets transmitted, 4 packets received, 0% packet loss


Cafe-01-SW1#conf t
Cafe-01-SW1(config)#interface ethernet0/1
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk
Cafe-01-SW1(config-if)#switchport trunk allowed vlan 10,20
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#interface ethernet6/0
Cafe-01-SW1(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW1(config-if)#switchport mode trunk
Cafe-01-SW1(config-if)#switchport trunk allowed vlan 10,20
Cafe-01-SW1(config-if)#end

Cafe-01-SW2#conf t
Cafe-01-SW2(config)#interface ethernet0/1
Cafe-01-SW2(config-if)#switchport trunk encapsulation dot1q
Cafe-01-SW2(config-if)#switchport mode trunk
Cafe-01-SW2(config-if)#switchport trunk allowed vlan 10,20
Cafe-01-SW2(config-if)#end

Cafe-01-SW1#show interfaces trunk
Port           Mode             Encapsulation  Status        Native vlan
Et0/1          on               802.1q         trunking      1
Et6/0          on               802.1q         trunking      1
Port           Vlans allowed on trunk
Et0/1          10,20
Et6/0          10,20

Cafe-01-SW2#show interfaces trunk
Port           Mode             Encapsulation  Status        Native vlan
Et0/1          on               802.1q         trunking      1
Et0/1          10,20


Cafe-01-SW1#enable
Cafe-01-SW1#configure terminal
Cafe-01-SW1(config)#interface Ethernet0/3
Cafe-01-SW1(config-if)# switchport mode access
Cafe-01-SW1(config-if)# switchport access vlan 10
Cafe-01-SW1(config-if)# switchport port-security
Cafe-01-SW1(config-if)# switchport port-security maximum 1
Cafe-01-SW1(config-if)# switchport port-security violation restrict
Cafe-01-SW1(config-if)# switchport port-security mac-address sticky
Cafe-01-SW1(config-if)#end

Cafe-01-SW1#show port-security interface Ethernet0/3
Port Status                : Secure-up
Total MAC Addresses        : 0
Sticky MAC Addresses       : 0
Security Violation Count   : 0

admin@Cafe-Admin-PC:~$ ping -c 4 10.1.10.1
4 packets transmitted, 4 packets received, 0% packet loss

Cafe-01-SW1#show port-security interface Ethernet0/3
Total MAC Addresses        : 1
Sticky MAC Addresses       : 1
Last Source Address:Vlan   : 5254.0010.a52a:10
Security Violation Count   : 0

Cafe-01-SW1#show port-security address
Vlan    Mac Address       Type                          Ports   Remaining Age
  10    5254.0010.a52a    SecureSticky                  Et0/3        -


Cafe-01-SW1(config)#interface range Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet2/0
Cafe-01-SW1(config-if-range)# switchport mode access
Cafe-01-SW1(config-if-range)# switchport access vlan 20
Cafe-01-SW1(config-if-range)# switchport port-security
Cafe-01-SW1(config-if-range)# switchport port-security maximum 1
Cafe-01-SW1(config-if-range)# switchport port-security violation restrict
Cafe-01-SW1(config-if-range)#end

Cafe-01-SW1#show port-security
Secure Port  MaxSecureAddr  CurrentAddr  SecurityViolation  Security Action
      Et0/3              1            1                  0         Restrict
      Et1/1              1            0                  0         Restrict
      Et1/2              1            0                  0         Restrict
      Et1/3              1            0                  0         Restrict
      Et2/0              1            0                  0         Restrict


Cafe-01-SW2#configure terminal
Cafe-01-SW2(config)#interface Ethernet0/2
Cafe-01-SW2(config-if)# switchport mode access
Cafe-01-SW2(config-if)# switchport access vlan 20
Cafe-01-SW2(config-if)# switchport port-security
Cafe-01-SW2(config-if)# switchport port-security maximum 1
Cafe-01-SW2(config-if)# switchport port-security violation restrict
Cafe-01-SW2(config-if)#end
Cafe-01-SW2#conf t
Cafe-01-SW2(config)#interface Ethernet1/0
Cafe-01-SW2(config-if)# switchport mode access
Cafe-01-SW2(config-if)# switchport access vlan 10
Cafe-01-SW2(config-if)# switchport port-security
Cafe-01-SW2(config-if)# switchport port-security maximum 1
Cafe-01-SW2(config-if)# switchport port-security violation restrict
Cafe-01-SW2(config-if)# switchport port-security mac-address sticky
Cafe-01-SW2(config-if)#end
Cafe-01-SW2(config)#interface range Ethernet1/1, Ethernet1/2
Cafe-01-SW2(config-if-range)# switchport mode access
Cafe-01-SW2(config-if-range)# switchport access vlan 20
Cafe-01-SW2(config-if-range)# switchport port-security
Cafe-01-SW2(config-if-range)# switchport port-security maximum 1
Cafe-01-SW2(config-if-range)# switchport port-security violation restrict
Cafe-01-SW2(config-if-range)#end

Cafe-01-SW2#show port-security
Secure Port  MaxSecureAddr  CurrentAddr  SecurityViolation  Security Action
      Et0/2              1            1                  0         Restrict
      Et1/0              1            0                  0         Restrict
      Et1/1              1            0                  0         Restrict
      Et1/2              1            0                  0         Restrict


Cafe-01-SW1#configure terminal
Cafe-01-SW1(config)#ip dhcp snooping
Cafe-01-SW1(config)#ip dhcp snooping vlan 10,20
Cafe-01-SW1(config)#interface Ethernet0/1
Cafe-01-SW1(config-if)# ip dhcp snooping trust
Cafe-01-SW1(config)#interface Ethernet6/0
Cafe-01-SW1(config-if)# ip dhcp snooping trust
Cafe-01-SW1(config-if)#end

Cafe-01-SW2#configure terminal
Cafe-01-SW2(config)#ip dhcp snooping
Cafe-01-SW2(config)#ip dhcp snooping vlan 10,20
Cafe-01-SW2(config)#interface Ethernet0/1
Cafe-01-SW2(config-if)# ip dhcp snooping trust
Cafe-01-SW2(config-if)#end

Cafe-01-SW1#show ip dhcp snooping
Switch DHCP snooping is enabled
DHCP snooping is operational on following VLANs: 10,20
Ethernet0/1                      yes        yes             unlimited
Ethernet6/0                      yes        yes             unlimited


Cafe-01-SW1(config)#interface range Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet2/0
Cafe-01-SW1(config-if-range)# ip dhcp snooping limit rate 5
Cafe-01-SW1(config-if-range)#exit
Cafe-01-SW1(config)#interface Ethernet1/0
Cafe-01-SW1(config-if)# ip dhcp snooping limit rate 20
Cafe-01-SW1(config-if)#end

Cafe-01-SW2(config)#interface range Ethernet0/2, Ethernet1/1, Ethernet1/2
Cafe-01-SW2(config-if-range)# ip dhcp snooping limit rate 5
Cafe-01-SW2(config-if-range)#end

Cafe-01-SW1#show ip dhcp snooping
Ethernet1/0                      no         no              20
Ethernet1/1                      no         no              5
Ethernet1/2                      no         no              5
Ethernet1/3                      no         no              5
Ethernet2/0                      no         no              5

Cafe-01-SW2#show ip dhcp snooping
Ethernet0/2                      no         no              5
Ethernet1/1                      no         no              5
Ethernet1/2                      no         no              5


patron@Cafe-Patron-PC:~$ udhcpc -i eth0
udhcpc: socket: Operation not permitted
patron@Cafe-Patron-PC:~$ ifconfig eth0 down && ifconfig eth0 up
ifconfig: SIOCSIFFLAGS: Operation not permitted
patron@Cafe-Patron-PC:~$ sudo udhcpc -i eth0
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.1.20.11, server 10.1.20.1
udhcpc: lease of 10.1.20.11 obtained from 10.1.20.1, lease time 86400
adding dns 1.1.1.1

Cafe-01-SW1#show ip dhcp snooping binding
Total number of bindings: 0

Cafe-01-SW2#show ip dhcp snooping binding
Total number of bindings: 0

patron@Cafe-Patron-PC:~$ sudo udhcpc -i eth0 -R
udhcpc: lease of 10.1.20.11 obtained from 10.1.20.1, lease time 86400

Cafe-01-SW1#show ip dhcp snooping binding
Total number of bindings: 0
Cafe-01-SW2#show ip dhcp snooping binding
Total number of bindings: 0

Cafe-01-SW1#show ip dhcp snooping statistics
 Packets Forwarded                                     = 0
 Packets Dropped                                       = 0
 Packets Dropped From untrusted ports                  = 0

Cafe-01-SW2#show ip dhcp snooping statistics
 Packets Forwarded                                     = 0
 Packets Dropped                                       = 0
 Packets Dropped From untrusted ports                  = 0

Cafe-01-SW2#debug ip dhcp snooping event
DHCP Snooping Event debugging is on
Cafe-01-SW2#debug ip dhcp snooping packet
DHCP Snooping Packet debugging is on
(no packet-level debug output observed during a confirmed live client renewal)

Cafe-01-SW2#show ip dhcp snooping database
Agent URL :
Total Attempts       :        0   Startup Failures :        0
Successful Writes    :        0   Failed Writes    :        0


Cafe-01-SW1#configure terminal
Cafe-01-SW1(config)#ip arp inspection vlan 10,20
Cafe-01-SW1(config)#interface Ethernet0/1
Cafe-01-SW1(config-if)# ip arp inspection trust
Cafe-01-SW1(config)#interface Ethernet6/0
Cafe-01-SW1(config-if)# ip arp inspection trust
Cafe-01-SW1(config-if)#end

Cafe-01-SW2#configure terminal
Cafe-01-SW2(config)#ip arp inspection vlan 10,20
Cafe-01-SW2(config)#interface Ethernet0/1
Cafe-01-SW2(config-if)# ip arp inspection trust
Cafe-01-SW2(config-if)#end

Cafe-01-SW1#show ip arp inspection vlan 10,20
 Vlan     Configuration    Operation
   10     Enabled          Active
   20     Enabled          Active

Cafe-01-SW1#show ip arp inspection interfaces
 Et0/1            Trusted               None               N/A
 Et6/0            Trusted               None               N/A
 (all other interfaces Untrusted, 15 pps, 1s burst)

Cafe-01-SW2#show ip arp inspection interfaces
 Et0/1            Trusted               None               N/A
 (all other interfaces Untrusted, 15 pps, 1s burst)


admin@Cafe-Admin-PC:~$ ping -c 4 10.1.10.1
4 packets transmitted, 4 packets received, 0% packet loss

patron@Cafe-Patron-PC:~$ ping -c 4 10.1.20.1
PING 10.1.20.1 (10.1.20.1): 56 data bytes
--- 10.1.20.1 ping statistics ---
4 packets transmitted, 0 packets received, 100% packet loss

Cafe-01-SW1#show ip arp inspection statistics vlan 10,20
 Vlan      Forwarded        Dropped     DHCP Drops      ACL Drops
   10              0              3              3              0
   20              0              0              0              0

Cafe-01-SW2#show ip arp inspection statistics vlan 10,20
 Vlan      Forwarded        Dropped     DHCP Drops      ACL Drops
   10              0              0              0              0
   20              0              3              3              0


admin@Cafe-Admin-PC:~$ ifconfig
eth0      HWaddr 52:54:00:46:46:4F
          inet addr:10.1.10.11  Bcast:10.1.10.255  Mask:255.255.255.0

Cafe-01-SW1#show port-security address
  10    5254.0046.464f    SecureSticky                  Et0/3        -

Cafe-01-SW2#show port-security address
  20    5254.00fc.9d30    SecureDynamic                 Et0/2        -


Cafe-01-SW1#configure terminal
Cafe-01-SW1(config)#arp access-list ADMIN-ARP
Cafe-01-SW1(config-arp-nacl)# permit ip host 10.1.10.11 mac host 5254.0046.464f
Cafe-01-SW1(config)#arp access-list PATRON-ARP
Cafe-01-SW1(config-arp-nacl)# permit ip host 10.1.20.11 mac host 5254.00fc.9d30
Cafe-01-SW1(config)#ip arp inspection filter ADMIN-ARP vlan 10
Cafe-01-SW1(config)#ip arp inspection filter PATRON-ARP vlan 20
Cafe-01-SW1(config)#end

Cafe-01-SW2#configure terminal
Cafe-01-SW2(config)#arp access-list ADMIN-ARP
Cafe-01-SW2(config-arp-nacl)# permit ip host 10.1.10.11 mac host 5254.0046.464f
Cafe-01-SW2(config)#arp access-list PATRON-ARP
Cafe-01-SW2(config-arp-nacl)# permit ip host 10.1.20.11 mac host 5254.00fc.9d30
Cafe-01-SW2(config)#ip arp inspection filter ADMIN-ARP vlan 10
Cafe-01-SW2(config)#ip arp inspection filter PATRON-ARP vlan 20
Cafe-01-SW2(config)#end

Cafe-01-SW1#show ip arp inspection statistics vlan 10,20
 Vlan      Forwarded        Dropped     DHCP Drops      ACL Drops
   10              2              3              3              0
 Vlan   DHCP Permits    ACL Permits
   10              0              1

Cafe-01-SW2#show ip arp inspection statistics vlan 10,20
 Vlan      Forwarded        Dropped     DHCP Drops      ACL Drops
   20              2              3              3              0
 Vlan   DHCP Permits    ACL Permits
   20              0              1

admin@Cafe-Admin-PC:~$ ping -c 4 10.1.10.1
4 packets transmitted, 4 packets received, 0% packet loss

patron@Cafe-Patron-PC:~$ ping -c 4 10.1.20.1
PING 10.1.20.1 (10.1.20.1): 56 data bytes
64 bytes from 10.1.20.1: seq=0 ttl=255 time=2.835 ms
4 packets transmitted, 4 packets received, 0% packet loss


Cafe-01-SW1#enable
Cafe-01-SW1#configure terminal
Cafe-01-SW1(config)#interface Ethernet0/3
Cafe-01-SW1(config-if)# no switchport port-security mac-address sticky 5254.0046.464f
Cafe-01-SW1(config-if)# switchport port-security mac-address 0000.dead.beef
Cafe-01-SW1(config-if)#end

Cafe-01-SW1#show port-security address
  10    0000.dead.beef    SecureConfigured              Et0/3        -
  10    5254.0046.464f    SecureSticky                  Et0/3        -
(stale duplicate entry - summary counters below were authoritative)

Cafe-01-SW1#show port-security interface Ethernet0/3
Configured MAC Addresses   : 1
Sticky MAC Addresses       : 0
Security Violation Count   : 0

admin@Cafe-Admin-PC:~$ ping -c 4 10.1.10.1
4 packets transmitted, 4 packets received, 0% packet loss
(real MAC still permitted - stale entry confirmed active)

Cafe-01-SW1#configure terminal
Cafe-01-SW1(config)#interface Ethernet0/3
Cafe-01-SW1(config-if)# no switchport port-security
Cafe-01-SW1(config-if)# switchport port-security
Cafe-01-SW1(config-if)# switchport port-security maximum 1
Cafe-01-SW1(config-if)# switchport port-security violation restrict
Cafe-01-SW1(config-if)# switchport port-security mac-address 0000.dead.beef
Cafe-01-SW1(config-if)#end

Cafe-01-SW1#show port-security address
  10    0000.dead.beef    SecureConfigured              Et0/3        -
(clean single entry confirmed)

admin@Cafe-Admin-PC:~$ ping -c 4 10.1.10.1
PING 10.1.10.1 (10.1.10.1): 56 data bytes
--- 10.1.10.1 ping statistics ---
4 packets transmitted, 0 packets received, 100% packet loss

Cafe-01-SW1#show port-security interface Ethernet0/3
Port Status                : Secure-up
Violation Mode             : Restrict
Total MAC Addresses        : 1
Configured MAC Addresses   : 1
Security Violation Count   : 7


Cafe-01-SW1#enable
Cafe-01-SW1#configure terminal
Cafe-01-SW1(config)#interface Ethernet0/3
Cafe-01-SW1(config-if)# no switchport port-security mac-address 0000.dead.beef
Cafe-01-SW1(config-if)# switchport port-security mac-address sticky
Cafe-01-SW1(config-if)#end

admin@Cafe-Admin-PC:~$ ping -c 4 10.1.10.1
PING 10.1.10.1 (10.1.10.1): 56 data bytes
4 packets transmitted, 4 packets received, 0% packet loss

Cafe-01-SW1#show port-security interface Ethernet0/3
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 1
Last Source Address:Vlan   : 5254.0046.464f:10
Security Violation Count   : 7


Cafe-01-SW1#clear port-security interface Ethernet0/3
                    ^
% Invalid input detected at '^' marker.
Cafe-01-SW1#clear port-security all interface Ethernet0/3
                    ^
% Invalid input detected at '^' marker.
Cafe-01-SW1#clear port-security sticky interface Ethernet0/3
                    ^
% Invalid input detected at '^' marker.
Cafe-01-SW1#clear port-security ?
% Unrecognized command
(command family not supported on this platform - violation counter left at historical value of 7)
```
