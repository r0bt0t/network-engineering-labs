# Lab 069 - Raw CLI Output

```bash
Connecting to console for RTR-FS-01

RTR-FS-01>
RTR-FS-01>en
RTR-FS-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-FS-01(config)#no logging console
RTR-FS-01(config)#end
RTR-FS-01#
RTR-FS-01#
RTR-FS-01#show ip interface brief | include Ethernet0/0
Ethernet0/0            172.22.0.1      YES TFTP   up                    up      
RTR-FS-01#
RTR-FS-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-FS-01(config)#ip domain name castlerysen.local
RTR-FS-01(config)#ip dns server
RTR-FS-01(config)#ip host cafe.castlerysen.local 172.22.0.2
RTR-FS-01(config)#ip name-server 1.1.1.1
RTR-FS-01(config)#ip name-server 8.8.8.8
RTR-FS-01(config)#interface Loopback1
RTR-FS-01(config-if)#ip address 1.1.1.1 255.255.255.255
RTR-FS-01(config-if)#exit
RTR-FS-01(config)#end
RTR-FS-01#
RTR-FS-01#ping cafe.castlerysen.local
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.22.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-FS-01#
RTR-FS-01#show hosts
Default domain is castlerysen.local
Name servers are 1.1.1.1, 8.8.8.8
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------
 2.0.22.172.in-addr.arpa        10      IN      PTR     cafe.castlerysen.local
 cafe.castlerysen.local 10      IN      A       172.22.0.2

RTR-FS-01#



Connecting to console for RTR-FS-02

RTR-FS-02>
RTR-FS-02>en
RTR-FS-02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-FS-02(config)#no logging console
*Aug 20 14:21:52.781: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
RTR-FS-02(config)#no logging console
RTR-FS-02(config)#end
RTR-FS-02#
RTR-FS-02#show ip int brief | include Ethernet0/0
Ethernet0/0            172.22.0.5      YES TFTP   up                    up      
RTR-FS-02#
RTR-FS-02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-FS-02(config)#ip domain name castlerysen.local
RTR-FS-02(config)#ip dns server
RTR-FS-02(config)#ip host cafe1.castlerysen.local 172.22.0.2
RTR-FS-02(config)#ip name-server 1.1.1.1
RTR-FS-02(config)#ip name-server 8.8.8.8
RTR-FS-02(config)#interface Loopbace1
                                   ^
% Invalid input detected at '^' marker.

RTR-FS-02(config)#ip address 2.2.2.2 255.255.255.255
                            ^
% Invalid input detected at '^' marker.

RTR-FS-02(config)#interface Loopback1               
RTR-FS-02(config-if)#ip address 2.2.2.2 255.255.255.255
RTR-FS-02(config-if)#exit
RTR-FS-02(config)#end
RTR-FS-02#
RTR-FS-02#ping cafe1.castlerysen.local
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.22.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-FS-02#
RTR-FS-02#show hosts
Default domain is castlerysen.local
Name servers are 1.1.1.1, 8.8.8.8
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------
 2.0.22.172.in-addr.arpa        10      IN      PTR     cafe1.castlerysen.local
 cafe1.castlerysen.local        10      IN      A       172.22.0.2

RTR-FS-02#


Connecting to console for RTR-CAF-01

RTR-CAF-01>
RTR-CAF-01>en
RTR-CAF-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-CAF-01(config)#no log
*Aug 20 14:22:06.399: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 20 14:22:06.501: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 14:22:06.502: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 14:22:06.608: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
RTR-CAF-01(config)#no logging 
*Aug 20 14:22:06.708: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 20 14:22:06.708: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
RTR-CAF-01(config)#no logging console
RTR-CAF-01(config)#end
RTR-CAF-01#
RTR-CAF-01#
RTR-CAF-01#show ip int brief | include Ethernet0/1
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/1.10         10.22.10.1      YES TFTP   administratively down down    
Ethernet0/1.20         10.22.20.1      YES TFTP   administratively down down    
RTR-CAF-01#
RTR-CAF-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-CAF-01(config)#interface Ethernet0/1
RTR-CAF-01(config-if)#no shutdown
RTR-CAF-01(config-if)#end
RTR-CAF-01#show ip interface brief | include Ethernet0/1
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/1.10         10.22.10.1      YES TFTP   up                    up      
Ethernet0/1.20         10.22.20.1      YES TFTP   up                    up      
RTR-CAF-01#
RTR-CAF-01#
RTR-CAF-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-CAF-01(config)#end
RTR-CAF-01#show interface brief | include Ethernet0/0
                           ^
% Invalid input detected at '^' marker.

RTR-CAF-01#show ip interface brief | include Ethernet0/0
Ethernet0/0            172.22.0.2      YES TFTP   up                    up      
RTR-CAF-01#
RTR-CAF-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-CAF-01(config)#ip domain name castlerysen.local
RTR-CAF-01(config)#ip dns server
RTR-CAF-01(config)#ip host plex.castlerysen.local 10.22.10.50
RTR-CAF-01(config)#ip name-server 1.1.1.1
RTR-CAF-01(config)#ip name-server 8.8.8.8
RTR-CAF-01(config)#no ip name-server 8.8.8.8
RTR-CAF-01(config)#ip name-server 2.2.2.2
RTR-CAF-01(config)#end
RTR-CAF-01#
RTR-CAF-01#ping plex.castlerysen.local
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.10.50, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
RTR-CAF-01#
RTR-CAF-01#show hosts
Default domain is castlerysen.local
Name servers are 1.1.1.1, 2.2.2.2
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------
 50.10.22.10.in-addr.arpa       10      IN      PTR     plex.castlerysen.local
 plex.castlerysen.local 10      IN      A       10.22.10.50

RTR-CAF-01#



RTR-FS-01>en
RTR-FS-01#show clock
*14:38:05.469 UTC Thu Aug 20 2026
RTR-FS-01#
RTR-FS-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-FS-01(config)#clock timezone MST -7
RTR-FS-01(config)#ntp master 1
RTR-FS-01(config)#ntp source Loopback1
RTR-FS-01(config)#end
RTR-FS-01#
RTR-FS-01#show ntp status
Clock is unsynchronized, stratum 1, reference is .LOCL.
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 1800 (1/100 of seconds), resolution is 4000
reference time is EE318FFD.D8937710 (07:38:53.846 MST Thu Aug 20 2026)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 3939.29 msec, peer dispersion is 3938.29 msec
loopfilter state is 'FREQ' (Drift being measured), drift is 0.000000000 s/s
system poll interval is 16, last update was 3 sec ago.
RTR-FS-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
*~127.127.1.1     .LOCL.           0     14     16     3  0.000   0.000 3938.2
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-FS-01#



RTR-FS-02>en
RTR-FS-02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-FS-02(config)#clock timezone MST -7
RTR-FS-02(config)#ntp master 1
RTR-FS-02(config)#ntp source Loopback1
RTR-FS-02(config)#end
RTR-FS-02#
RTR-FS-02#show ntp status
Clock is unsynchronized, stratum 1, reference is .LOCL.
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 1900 (1/100 of seconds), resolution is 4000
reference time is EE319052.D0E56280 (07:40:18.816 MST Thu Aug 20 2026)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 3939.29 msec, peer dispersion is 3938.29 msec
loopfilter state is 'FREQ' (Drift being measured), drift is 0.000000000 s/s
system poll interval is 16, last update was 3 sec ago.
RTR-FS-02#
RTR-FS-02#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
*~127.127.1.1     .LOCL.           0     12     16     3  0.000   0.000 3938.2
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-FS-02#



RTR-CAF-01#
RTR-CAF-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-CAF-01(config)#ntp server 1.1.1.1
RTR-CAF-01(config)#ntp server 2.2.2.2
RTR-CAF-01(config)#interface Loopback0
RTR-CAF-01(config-if)#ip address 10.22.255.1 255.255.255.255
RTR-CAF-01(config-if)#exit
RTR-CAF-01(config)#ntp source Loopback0
RTR-CAF-01(config)#ntp master 2
RTR-CAF-01(config)#end
RTR-CAF-01#
RTR-CAF-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~1.1.1.1         .INIT.          16     50     64     0  0.000   0.000 15937.
*~127.127.1.1     .LOCL.           1      8     16     1  0.000   0.000 7937.9
 ~2.2.2.2         .INIT.          16     43     64     0  0.000   0.000 15937.
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-CAF-01#
RTR-CAF-01#show ntp status
Clock is unsynchronized, stratum 2, reference is 127.127.1.1    
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 7200 (1/100 of seconds), resolution is 4000
reference time is EE31910F.55810710 (14:43:27.334 UTC Thu Aug 20 2026)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 3939.31 msec, peer dispersion is 3938.29 msec
loopfilter state is 'FREQ' (Drift being measured), drift is 0.000000000 s/s
system poll interval is 16, last update was 4 sec ago.
RTR-CAF-01#


RTR-CAF-01#
RTR-CAF-01#
RTR-CAF-01#show running-config | section ip dhcp
ip dhcp excluded-address 10.22.10.1 10.22.10.20
ip dhcp excluded-address 10.22.20.1 10.22.20.20
ip dhcp pool ADMIN-NET
 network 10.22.10.0 255.255.255.0
 default-router 10.22.10.1 
ip dhcp pool PATRON-NET
 network 10.22.20.0 255.255.255.0
 default-router 10.22.20.1 
RTR-CAF-01#
RTR-CAF-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-CAF-01(config)#ip dhcp pool ADMIN-NET
RTR-CAF-01(dhcp-config)#domain-name castlerysen.local
RTR-CAF-01(dhcp-config)#dns-server 10.22.10.1
RTR-CAF-01(dhcp-config)#option 42 ip 10.22.255.1
RTR-CAF-01(dhcp-config)#exit
RTR-CAF-01(config)#ip dhcp pool PATRON-NET      
RTR-CAF-01(dhcp-config)#domain-name castlerysen.local
RTR-CAF-01(dhcp-config)#dns-server 10.22.10.1        
RTR-CAF-01(dhcp-config)#option 42 ip 10.22.255.1     
RTR-CAF-01(dhcp-config)#end
RTR-CAF-01#
RTR-CAF-01#show running-config | section ip dhcp
ip dhcp excluded-address 10.22.10.1 10.22.10.20
ip dhcp excluded-address 10.22.20.1 10.22.20.20
ip dhcp pool ADMIN-NET
 network 10.22.10.0 255.255.255.0
 default-router 10.22.10.1 
 domain-name castlerysen.local
 dns-server 10.22.10.1 
 option 42 ip 10.22.255.1 
ip dhcp pool PATRON-NET
 network 10.22.20.0 255.255.255.0
 default-router 10.22.20.1 
 domain-name castlerysen.local
 dns-server 10.22.10.1 
 option 42 ip 10.22.255.1 
RTR-CAF-01#
RTR-CAF-01#show ip dhcp pool

Pool ADMIN-NET :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 254
 Leased addresses               : 1
 Excluded addresses             : 20
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.22.10.22          10.22.10.1       - 10.22.10.254      1     / 20    / 254  

Pool PATRON-NET :
 Utilization mark (high/low)    : 100 / 0
 Subnet size (first/next)       : 0 / 0 
 Total addresses                : 254
 Leased addresses               : 0
 Excluded addresses             : 20
 Pending event                  : none
 1 subnet is currently in the pool :
 Current index        IP address range                    Leased/Excluded/Total
 10.22.20.1           10.22.20.1       - 10.22.20.254      0     / 20    / 254  
RTR-CAF-01#


Connecting to console for Cafe-Admin-PC

Core Linux
cafe-admin-pc login: tc
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

tc@cafe-admin-pc:~$ sudo udhcpc -i eth0 -n -q
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 10.22.10.21, server 10.22.10.1
udhcpc: lease of 10.22.10.21 obtained from 10.22.10.1, lease time 86400
deleting routers
route: SIOCDELRT: No such process
adding dns 10.22.10.1
tc@cafe-admin-pc:~$ ifconfig eth0
eth0      Link encap:Ethernet  HWaddr 52:54:00:A7:FD:78  
          inet addr:10.22.10.21  Bcast:10.22.10.255  Mask:255.255.255.0
          inet6 addr: fe80::5054:ff:fea7:fd78/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:14 errors:0 dropped:1 overruns:0 frame:0
          TX packets:91 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:2008 (1.9 KiB)  TX bytes:27158 (26.5 KiB)

tc@cafe-admin-pc:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.22.10.1      0.0.0.0         UG    0      0        0 eth0
10.22.10.0      0.0.0.0         255.255.255.0   U     0      0        0 eth0
127.0.0.1       0.0.0.0         255.255.255.255 UH    0      0        0 lo
tc@cafe-admin-pc:~$ cat /etc/resolv.conf
search castlerysen.local
nameserver 10.22.10.1
tc@cafe-admin-pc:~$ 



RTR-CAF-01#show ip dhcp binding
Bindings from all pools not associated with VRF:
IP address      Client-ID/              Lease expiration        Type       State      Interface
                Hardware address/
                User name
10.22.10.21     0152.5400.a7fd.78       Aug 21 2026 02:50 PM    Automatic  Active     Ethernet0/1.10
RTR-CAF-01#



RTR-CAF-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-CAF-01(config)#int
RTR-CAF-01(config)#interface Eth
RTR-CAF-01(config)#interface Ethernet0/1.10
RTR-CAF-01(config-subif)#ip nat inside
RTR-CAF-01(config-subif)#exit
RTR-CAF-01(config)#interface Ethernet0/1.20
RTR-CAF-01(config-subif)#ip nat inside           
RTR-CAF-01(config-subif)#exit
RTR-CAF-01(config)#interface Ethernet0/0   
RTR-CAF-01(config-if)#ip nat outside
RTR-CAF-01(config-if)#exit
RTR-CAF-01(config)#access-list 10 permit 10.22.10.0 0.0.0.255
RTR-CAF-01(config)#access-list 10 permit 10.22.20.0 0.0.0.255
RTR-CAF-01(config)#$de source list 10 interface Ethernet0/0 overload         
RTR-CAF-01(config)#end
RTR-CAF-01#
RTR-CAF-01#ping 198.51.100.10 source 10.22.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 198.51.100.10, timeout is 2 seconds:
Packet sent with a source address of 10.22.10.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-CAF-01#
RTR-CAF-01#show ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
icmp 172.22.0.2:1024   10.22.10.1:2       198.51.100.10:2    198.51.100.10:1024
RTR-CAF-01#



RTR-FS-01>en
RTR-FS-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-FS-01(config)#username jeremy privilege 15 secret BeanR0ast!
RTR-FS-01(config)#crypto key generate rsa modulus 2048                     
The name for the keys will be: RTR-FS-01.castlerysen.local

% The key modulus size is 2048 bits
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

RTR-FS-01(config)#ip ssh version 2
RTR-FS-01(config)#line vty 0 4
RTR-FS-01(config-line)#transport input ssh
RTR-FS-01(config-line)#login local
RTR-FS-01(config-line)#exit
RTR-FS-01(config)#end
RTR-FS-01#


RTR-FS-02>en
RTR-FS-02#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-FS-02(config)#username jeremy privilege 15 secret BeanR0ast!
RTR-FS-02(config)#cryptoi key generate rsa modulus 2048
                        ^
% Invalid input detected at '^' marker.

RTR-FS-02(config)#ip ssh version 2
Please create EC or RSA keys to enable SSH (and of atleast 2048 bits for SSH v2 in case of RSA).
RTR-FS-02(config)#line vty 0 4
RTR-FS-02(config-line)#exit
RTR-FS-02(config)#crypto key generate rsa modulus 2048 
The name for the keys will be: RTR-FS-02.castlerysen.local

% The key modulus size is 2048 bits
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 1 seconds)

RTR-FS-02(config)#line vty 0 4                        
RTR-FS-02(config-line)#transport input ssh
RTR-FS-02(config-line)#login local
RTR-FS-02(config-line)#end
RTR-FS-02#


RTR-CAF-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-CAF-01(config)#username jeremy privilege 15 secret BeanR0ast!
RTR-CAF-01(config)#crypto key generate rsa modulus 2048
The name for the keys will be: RTR-CAF-01.castlerysen.local

% The key modulus size is 2048 bits
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 1 seconds)

RTR-CAF-01(config)#ip ssh version 2
RTR-CAF-01(config)#line vty 0 4
RTR-CAF-01(config-line)#transport input ssh
RTR-CAF-01(config-line)#login local
RTR-CAF-01(config-line)#end
RTR-CAF-01#


RTR-CAF-01#
RTR-CAF-01#ssh -l jeremy 1.1.1.1
Password: 



RTR-FS-01#show users
    Line       User       Host(s)              Idle       Location
   0 con 0                idle                 00:04:39   
*  2 vty 0     jeremy     idle                 00:00:00 cafe.castlerysen.local

  Interface    User               Mode         Idle     Peer Address

RTR-FS-01#exit

[Connection to 1.1.1.1 closed by foreign host]
RTR-CAF-01#
RTR-CAF-01#telnet 1.1.1.1
Trying 1.1.1.1 ... 
% Connection refused by remote host

RTR-CAF-01#
```
