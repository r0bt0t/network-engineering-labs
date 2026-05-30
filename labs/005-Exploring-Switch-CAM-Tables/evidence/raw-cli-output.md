# Lab 005 - Raw CLI Dump

```bash
Connecting to console for PC1

Core Linux
pc1 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@pc1:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:5E:61:BD  
          inet addr:192.168.1.50  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::5054:ff:fe5e:61bd/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:5 errors:0 dropped:1 overruns:0 frame:0
          TX packets:21 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:1428 (1.3 KiB)  TX bytes:4054 (3.9 KiB)

cisco@pc1:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 eth0
cisco@pc1:~$ 


Connecting to console for PC2

Core Linux
pc2 login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@pc2:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:EB:72:52  
          inet addr:192.168.1.51  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fe80::5054:ff:feeb:7252/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:22 errors:0 dropped:1 overruns:0 frame:0
          TX packets:37 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:7242 (7.0 KiB)  TX bytes:9254 (9.0 KiB)

cisco@pc2:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 eth0
cisco@pc2:~$ 
```

---

```bash
cisco@pc1:~$ ping 192.168.1.51
PING 192.168.1.51 (192.168.1.51): 56 data bytes
64 bytes from 192.168.1.51: seq=25 ttl=64 time=0.844 ms
64 bytes from 192.168.1.51: seq=26 ttl=64 time=0.923 ms
64 bytes from 192.168.1.51: seq=27 ttl=64 time=0.862 ms
64 bytes from 192.168.1.51: seq=28 ttl=64 time=0.830 ms
64 bytes from 192.168.1.51: seq=29 ttl=64 time=0.914 ms
^C
--- 192.168.1.51 ping statistics ---
30 packets transmitted, 30 packets received, 0% packet loss
round-trip min/avg/max = 0.811/0.909/1.541 ms
cisco@pc1:~$ arp -a
? (192.168.1.51) at 52:54:00:eb:72:52 [ether]  on eth0
cisco@pc1:~$ 

Switch6>en
Switch6#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch6(config)#show mac address-table
                  ^
% Invalid input detected at '^' marker.

Switch6(config)#^Z
Switch6#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.005e.61bd    DYNAMIC     Et0/1
  10    5254.00eb.7252    DYNAMIC     Et0/2
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  10    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0 
Total Mac Addresses for this criterion: 6
Switch6#

Switch6#clear mac address-table dynamic
Switch6#show mac address-table         
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  10    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0 
Total Mac Addresses for this criterion: 4
Switch6#

cisco@pc1:~$ ping -c 5 192.168.1.51
PING 192.168.1.51 (192.168.1.51): 56 data bytes
64 bytes from 192.168.1.51: seq=0 ttl=64 time=0.823 ms
64 bytes from 192.168.1.51: seq=1 ttl=64 time=0.927 ms
64 bytes from 192.168.1.51: seq=2 ttl=64 time=0.786 ms
64 bytes from 192.168.1.51: seq=3 ttl=64 time=0.871 ms
64 bytes from 192.168.1.51: seq=4 ttl=64 time=0.827 ms

--- 192.168.1.51 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.786/0.846/0.927 ms
cisco@pc1:~$ 

Switch6#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.005e.61bd    DYNAMIC     Et0/1
  10    5254.00eb.7252    DYNAMIC     Et0/2
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  10    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0 
Total Mac Addresses for this criterion: 6
Switch6#
```
