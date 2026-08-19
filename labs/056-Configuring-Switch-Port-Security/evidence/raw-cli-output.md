# Lab 056 - Raw CLI Output

```bash
Cafe-01-SW1#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  up                    up      
Ethernet1/0            unassigned      YES unset  up                    up      
Ethernet1/1            unassigned      YES unset  up                    up      
Ethernet1/2            unassigned      YES unset  up                    up      
Ethernet1/3            unassigned      YES unset  up                    up      
Ethernet2/0            unassigned      YES unset  up                    up      
Ethernet2/1            unassigned      YES unset  up                    up      
Ethernet2/2            unassigned      YES unset  up                    up      
Ethernet2/3            unassigned      YES unset  up                    up      
Ethernet3/0            unassigned      YES unset  up                    up      
Ethernet3/1            unassigned      YES unset  up                    up      
Ethernet3/2            unassigned      YES unset  up                    up      
Ethernet3/3            unassigned      YES unset  up                    up      
Ethernet4/0            unassigned      YES unset  up                    up      
Ethernet4/1            unassigned      YES unset  up                    up      
Ethernet4/2            unassigned      YES unset  up                    up      
Ethernet4/3            unassigned      YES unset  up                    up      
Ethernet5/0            unassigned      YES unset  up                    up      
 --More-- 
*Aug 18 13:22:24.150: %AMDP2_FE-6-EXCESSCOLL: Ethernet5/0 TDR=0, TRC=0
Ethernet5/1            unassigned      YES unset  up                    up      
Ethernet5/2            unassigned      YES unset  up                    up      
Ethernet5/3            unassigned      YES unset  up                    up      
Ethernet6/0            unassigned      YES unset  up                    up      
Ethernet6/1            unassigned      YES unset  up                    up      
Ethernet6/2            unassigned      YES unset  up                    up      
Ethernet6/3            unassigned      YES unset  up                    up      
Cafe-01-SW1#show mac address-table interface Ethernet0/3
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.001b.1e8e    DYNAMIC     Et0/3
Total Mac Addresses for this criterion: 1
Cafe-01-SW1#
*Aug 18 13:23:02.010: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-01-SW1#show interface Ethernet0/3 status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/3        Admin Workstation  connected    10           full   auto 10/100/1000BaseTX
Cafe-01-SW1#
*Aug 18 13:23:33.306: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1#


Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#int
Cafe-01-SW1(config)#interface Eth
Cafe-01-SW1(config)#interface Ethernet0/3
Cafe-01-SW1(config-if)#switchport mode access
Cafe-01-SW1(config-if)#switchport p
*Aug 18 13:25:09.236: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1(config-if)#switchport port-security
Cafe-01-SW1(config-if)#exit
Cafe-01-SW1(config)#exit
Cafe-01-SW1#
*Aug 18 13:25:19.868: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#


Connecting to console for Cafe-Admin-PC

Core Linux
Admin-PC login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@Admin-PC:~$ ping -c 3 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes

--- 10.0.18.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@Admin-PC:~$ 



Cafe-01-SW1#show port-security int
Cafe-01-SW1#show port-security interface Eth
Cafe-01-SW1#show port-security interface Ethernet 0/3
Port Security              : Enabled
Port Status                : Secure-up
Violation Mode             : Shutdown
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 1
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 5254.001b.1e8e:10
Security Violation Count   : 0

Cafe-01-SW1#
*Aug 18 13:27:20.125: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1#show mac address-table int
Cafe-01-SW1#show mac address-table interface eth
Cafe-01-SW1#show mac address-table interface ethernet 0/3
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.001b.1e8e    STATIC      Et0/3 
Total Mac Addresses for this criterion: 1
Cafe-01-SW1#
*Aug 18 13:27:51.941: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/2 TDR=0, TRC=0
Cafe-01-SW1#



Linux Console Quick Reference
Tasks 2 and 3 require you to change the MAC address on Cafe-Admin-PC, which runs a Linux console. The commands below are not CCNA exam material — they are simulation tools needed to trigger port security behavior in the lab environment. The Cisco switch commands are the learning objective. Use the hint blocks freely for the Linux syntax; there is no penalty for opening them.

Command	What it does
ifconfig eth0	Display the current IP and MAC address of eth0
sudo ifconfig eth0 down	Administratively disable the network interface
sudo ifconfig eth0 hw ether AA:BB:CC:DD:EE:FF	Set a new MAC address on eth0
sudo ifconfig eth0 up	Bring the interface back online
sudo ifconfig eth0 10.0.18.10 netmask 255.255.255.224 up	Reassign the IP address and bring the interface up
sudo route add default gw 10.0.18.1 eth0	Restore the default gateway so traffic can leave the subnet
ping -c 3 10.0.18.1	Send three ICMP pings to generate frames on the wire


cisco@Admin-PC:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:1B:1E:8E  
          inet addr:10.0.18.10  Bcast:10.0.18.31  Mask:255.255.255.224
          inet6 addr: fe80::5054:ff:fe1b:1e8e/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1 errors:0 dropped:1 overruns:0 frame:0
          TX packets:78 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:60 (60.0 B)  TX bytes:21204 (20.7 KiB)

cisco@Admin-PC:~$ sudo ifconfig eth0 down
cisco@Admin-PC:~$ sudo ifconfig eth0 hw ether 02:11:22:33:44:55
cisco@Admin-PC:~$ sudo ifconfig eth0 up
cisco@Admin-PC:~$ sudo ifconfig eth0 10.0.18.10 netmask 255.255.255.224 up
cisco@Admin-PC:~$ sudo route add default gw 10.0.18.1 eth0
cisco@Admin-PC:~$ ping -c 3 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes

--- 10.0.18.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@Admin-PC:~$ 


Cafe-01-SW1#show port-security
Secure Port  MaxSecureAddr  CurrentAddr  SecurityViolation  Security Action
                (Count)       (Count)          (Count)
---------------------------------------------------------------------------
      Et0/3              1            0                  1         Shutdown
---------------------------------------------------------------------------
Total Addresses in System (excluding one mac per port)     : 0
Max Addresses limit in System (excluding one mac per port) : 4096
Cafe-01-SW1#show port-security in
*Aug 18 13:33:15.332: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/3 TDR=0, TRC=0
Cafe-01-SW1#show port-security interface eth
Cafe-01-SW1#show port-security interface ethernet 0/3
Port Security              : Enabled
Port Status                : Secure-shutdown
Violation Mode             : Shutdown
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 0
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 0211.2233.4455:10
Security Violation Count   : 1

Cafe-01-SW1#show int
Cafe-01-SW1#show interfaces eth
Cafe-01-SW1#show interfaces ethernet
*Aug 18 13:33:51.468: %AMDP2_FE-6-EXCESSCOLL: Ethernet3/3 TDR=0, TRC=0
Cafe-01-SW1#show interface eth      
Cafe-01-SW1#show interface ethernet0/3 status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/3        Admin Workstation  err-disabled 10           full   auto 10/100/1000BaseTX
Cafe-01-SW1#



cisco@Admin-PC:~$ sudo ifconfig eth0 down
cisco@Admin-PC:~$ sudo ifconfig eth0 hw ethr 52:54:00:1B:1E:8E
BusyBox v1.36.1 (2024-01-28 10:23:59 UTC) multi-call binary.

Usage: ifconfig [-a] [IFACE] [ADDRESS]

Configure a network interface

        [add ADDRESS[/PREFIXLEN]]
        [del ADDRESS[/PREFIXLEN]]
        [[-]broadcast [ADDRESS]] [[-]pointopoint [ADDRESS]]
        [netmask ADDRESS] [dstaddr ADDRESS]
        [outfill NN] [keepalive NN]
        [hw ether|infiniband ADDRESS] [metric NN] [mtu NN]
        [[-]trailers] [[-]arp] [[-]allmulti]
        [multicast] [[-]promisc] [txqueuelen NN] [[-]dynamic]
        [mem_start NN] [io_addr NN] [irq NN]
        [up|down] ...
cisco@Admin-PC:~$ sudo ifconfig eth0 up
cisco@Admin-PC:~$ sudo ifconfig eth0 10.0.18.10 netmask 255.255.255.224 up
cisco@Admin-PC:~$ sudo route add default gw 10.0.18.1 eth0
cisco@Admin-PC:~$ 


Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#int
Cafe-01-SW1(config)#interface eth
Cafe-01-SW1(config)#interface ethernet
*Aug 18 13:37:37.379: %AMDP2_FE-6-EXCESSCOLL: Ethernet3/2 TDR=0, TRC=0
Cafe-01-SW1(config)#interface ethernet0/3
Cafe-01-SW1(config-if)#shut
Cafe-01-SW1(config-if)#shutdown 
Cafe-01-SW1(config-if)#no shutd
*Aug 18 13:37:49.708: %LINK-5-CHANGED: Interface Ethernet0/3, changed state to administratively down
Cafe-01-SW1(config-if)#no shutd
Cafe-01-SW1(config-if)#no shutdown 
Cafe-01-SW1(config-if)#end
Cafe-01-SW1#
*Aug 18 13:37:54.922: %LINK-3-UPDOWN: Interface Ethernet0/3, changed state to up
*Aug 18 13:37:55.429: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#
*Aug 18 13:37:55.922: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to up
Cafe-01-SW1#show port-security int
Cafe-01-SW1#show port-security interface eth
Cafe-01-SW1#show port-security interface ethernet 0/3
Port Security              : Enabled
Port Status                : Secure-up
Violation Mode             : Shutdown
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 0
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 0
Last Source Address:Vlan   : 0211.2233.4455:10
Security Violation Count   : 1

Cafe-01-SW1#
*Aug 18 13:38:09.769: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/0 TDR=0, TRC=0
Cafe-01-SW1#show ip interface brief | include eth
Cafe-01-SW1#show ip interface brief | include eth
*Aug 18 13:38:41.856: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/0 TDR=0, TRC=0
Cafe-01-SW1#show ip interface brief | include ethernet0/3
Cafe-01-SW1#show ip interface brief | include Ethernet0/3
*Aug 18 13:39:13.640: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/0 TDR=0, TRC=0
Cafe-01-SW1#show ip interface brief | include Ethernet0/3
Ethernet0/3            unassigned      YES unset  up                    up      
Cafe-01-SW1#



Cafe-01-SW1#
Cafe-01-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Cafe-01-SW1(config)#int
Cafe-01-SW1(config)#interface eth
Cafe-01-SW1(config)#interface ethernet0/3
Cafe-01-SW1(config-if)#switchport port-security violation restrict
Cafe-01-SW1(config-if)#switchport port-security                   
*Aug 18 13:40:18.117: %AMDP2_FE-6-EXCESSCOLL: Ethernet4/0 TDR=0, TRC=0
Cafe-01-SW1(config-if)#switchport port-security mac-address sticky
Cafe-01-SW1(config-if)#end
Cafe-01-SW1#
*Aug 18 13:40:30.454: %SYS-5-CONFIG_I: Configured from console by console
Cafe-01-SW1#show port-security interface Ethernet0/3
Port Security              : Enabled
Port Status                : Secure-up
Violation Mode             : Restrict
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 1
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 1
Last Source Address:Vlan   : 0211.2233.4455:10
Security Violation Count   : 1

Cafe-01-SW1#show running-config
*Aug 18 13:40:49.507: %AMDP2_FE-6-EXCESSCOLL: Ethernet3/3 TDR=0, TRC=0
Cafe-01-SW1#show running-config interface Ethernet0/3
Building configuration...

Current configuration : 311 bytes
!
interface Ethernet0/3
 description Admin Workstation
 switchport access vlan 10
 switchport mode access
 switchport port-security violation restrict
 switchport port-security mac-address sticky
 switchport port-security mac-address sticky 0211.2233.4455
 switchport port-security
 spanning-tree portfast
end

Cafe-01-SW1#show port-security address
               Secure Mac Address Table
-------------------------------------------------------------------------------
Vlan    Mac Address       Type                          Ports   Remaining Age
                                                                   (mins)    
----    -----------       ----                          -----   -------------
  10    0211.2233.4455    SecureSticky                  Et0/3        -
-------------------------------------------------------------------------------
Total Addresses in System (excluding one mac per port)     : 0
Max Addresses limit in System (excluding one mac per port) : 4096
Cafe-01-SW1#
*Aug 18 13:41:24.008: %AMDP2_FE-6-EXCESSCOLL: Ethernet6/0 TDR=0, TRC=0
Cafe-01-SW1#



cisco@Admin-PC:~$ sudo ifconfig eth0 down
cisco@Admin-PC:~$ sudo ifconfig eth0 hw ether 02:22:33:44:55:66
cisco@Admin-PC:~$ sudo ifconfig eth0 up
cisco@Admin-PC:~$ sudo ifconfig eth0 10.0.18.10 netmask 255.255.255.224 up
cisco@Admin-PC:~$ sudo route add default gw 10.0.18.1 eth0
cisco@Admin-PC:~$ ping -c 3 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes

--- 10.0.18.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@Admin-PC:~$ 


Cafe-01-SW1#show port-security interface Ethernet0/3
Port Security              : Enabled
Port Status                : Secure-up
Violation Mode             : Restrict
Aging Time                 : 0 mins
Aging Type                 : Absolute
SecureStatic Address Aging : Disabled
Maximum MAC Addresses      : 1
Total MAC Addresses        : 1
Configured MAC Addresses   : 0
Sticky MAC Addresses       : 1
Last Source Address:Vlan   : 0222.3344.5566:10
Security Violation Count   : 29

Cafe-01-SW1#show interface Ethernet0/3 status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/3        Admin Workstation  connected    10           full   auto 10/100/1000BaseTX
Cafe-01-SW1#


cisco@Admin-PC:~$ 
cisco@Admin-PC:~$ sudo ifconfig eth0 down
cisco@Admin-PC:~$ sudo ifconfig eth0 hw ether 52:54:00:08:BF:A1
cisco@Admin-PC:~$ sudo ifconfig eth0 up
cisco@Admin-PC:~$ sudo ifconfig eth0 10.0.18.10 netmask 255.255.255.224 up
cisco@Admin-PC:~$ sudo route add default gw 10.0.18.1 eth0
cisco@Admin-PC:~$
```
