# Lab 070 - Raw CLI Output

```bash
In order to complete this lab I have had to add a couple of elements beyond the written scope of the lab
Firstly an ip route needed to be added to the Alpha and Bravo routers as shown below

ip route 10.22.255.1 255.255.255.255 172.22.0.2

I also had to turn the relevant interfaces on on the district router in order to allow connectivity to be established and had to add a secondary ip address to ethernet0/1.10 on district in order to give the plex server an interface to reference.

Lastly it should be noted that NTP adjacencies are unable to form and maintain a full relationship due to an issue with the emulator so all NTP steps are followed but outcomes are not expected to return accurate results


Username: 
% Username:  timeout expired!
Username: 
% Username:  timeout expired!
Username: fieldtech
Password: 
RTR-Shelter-Alpha#
*Aug 24 13:20:50.848: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: fieldtech] [Source: LOCAL] [localport: 0] at 13:20:50 UTC Mon Aug 24 2026
RTR-Shelter-Alpha#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Alpha(config)#no logging console
RTR-Shelter-Alpha(config)#line con 0
RTR-Shelter-Alpha(config-line)#exec-timeout 0 0
RTR-Shelter-Alpha(config-line)#end
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#show clock
*13:23:38.574 UTC Mon Aug 24 2026
RTR-Shelter-Alpha#show clock detail
*13:23:44.789 UTC Mon Aug 24 2026
Time source is hardware calendar
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Alpha(config)#clock timezone CRST -7
RTR-Shelter-Alpha(config)#end
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#clock set 11:40:00 12 September 2024
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#show clock detail
11:40:14.931 CRST Thu Sep 12 2024
Time source is user configuration
RTR-Shelter-Alpha#



Username: fieldtech
Password: 
RTR-Shelter-Bravo#
*Aug 24 13:21:32.483: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: fieldtech] [Source: LOCAL] [localport: 0] at 13:21:32 UTC Mon Aug 24 2026
RTR-Shelter-Bravo#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Bravo(config)#no loh
*Aug 24 13:21:38.695: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
RTR-Shelter-Bravo(config)#no loggin
*Aug 24 13:21:38.797: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 13:21:38.798: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 13:21:38.907: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
RTR-Shelter-Bravo(config)#no logging 
*Aug 24 13:21:39.007: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 24 13:21:39.008: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
RTR-Shelter-Bravo(config)#no logging console
RTR-Shelter-Bravo(config)#line con 0
RTR-Shelter-Bravo(config-line)#exec-timeout 0 0 
RTR-Shelter-Bravo(config-line)#end
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show clock
*13:24:52.672 UTC Mon Aug 24 2026
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show clock detail
*13:24:58.187 UTC Mon Aug 24 2026
Time source is hardware calendar
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Bravo(config)#clock timezone CRST -7
RTR-Shelter-Bravo(config)#end
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#clock set 11:40:00 12 September 2024
RTR-Shelter-Bravo#show clock detail
11:40:53.308 CRST Thu Sep 12 2024
Time source is user configuration
RTR-Shelter-Bravo#



Username: fieldtech
Password: 
RTR-District-01#
*Aug 24 13:22:12.731: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: fieldtech] [Source: LOCAL] [localport: 0] at 13:22:12 UTC Mon Aug 24 2026
RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#no logging console
RTR-District-01(config)#line con 0
RTR-District-01(config-line)#exec-timeout 0 0 
RTR-District-01(config-line)#end
RTR-District-01#
RTR-District-01#
RTR-District-01#show clock
*13:25:40.506 UTC Mon Aug 24 2026
RTR-District-01#
RTR-District-01#show clock detail
*13:25:46.022 UTC Mon Aug 24 2026
Time source is hardware calendar
RTR-District-01#
RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#clock timezone CRST -7
RTR-District-01(config)#end
RTR-District-01#
RTR-District-01#clock set 11:40:00 12 September 2024
RTR-District-01#
RTR-District-01#show clock detail
11:41:17.579 CRST Thu Sep 12 2024
Time source is user configuration
RTR-District-01#



RTR-Shelter-Alpha#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Alpha(config)#interface Loopback1
RTR-Shelter-Alpha(config-if)#ip address 1.1.1.1 255.255.255.255
RTR-Shelter-Alpha(config-if)#exit
RTR-Shelter-Alpha(config)#
RTR-Shelter-Alpha(config)#ntp source Loopback1
RTR-Shelter-Alpha(config)#ntp master 1
RTR-Shelter-Alpha(config)#end
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#show clock detail
11:42:49.568 CRST Thu Sep 12 2024
Time source is NTP
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#show ntp status
Clock is unsynchronized, stratum 1, reference is .LOCL.
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 3000 (1/100 of seconds), resolution is 4000
reference time is EA8DB4A7.6C083250 (11:42:47.422 CRST Thu Sep 12 2024)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 3939.40 msec, peer dispersion is 3938.29 msec
loopfilter state is 'FREQ' (Drift being measured), drift is 0.000000000 s/s
system poll interval is 16, last update was 9 sec ago.
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
*~127.127.1.1     .LOCL.           0      0     16     7  0.000   0.000 1938.4
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            172.22.0.1      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Loopback1              1.1.1.1         YES manual up                    up      
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Alpha(config)#ip route 10.22.255.1 255.255.255.255 172.22.0.2
RTR-Shelter-Alpha(config)#end
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is not set

      1.0.0.0/32 is subnetted, 1 subnets
C        1.1.1.1 is directly connected, Loopback1
      10.0.0.0/8 is variably subnetted, 3 subnets, 2 masks
S        10.22.10.0/24 [1/0] via 172.22.0.2
S        10.22.20.0/24 [1/0] via 172.22.0.2
S        10.22.255.1/32 [1/0] via 172.22.0.2
      172.22.0.0/16 is variably subnetted, 2 subnets, 2 masks
C        172.22.0.0/29 is directly connected, Ethernet0/0
L        172.22.0.1/32 is directly connected, Ethernet0/0
RTR-Shelter-Alpha#




RTR-Shelter-Bravo#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Bravo(config)#interface Loopback1
RTR-Shelter-Bravo(config-if)#ip address 2.2.2.2 255.255.255.255
RTR-Shelter-Bravo(config-if)#exit
RTR-Shelter-Bravo(config)#ntp source Loopback1
RTR-Shelter-Bravo(config)#ntp master 1
RTR-Shelter-Bravo(config)#end
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show clock detail
11:45:42.016 CRST Thu Sep 12 2024
Time source is NTP
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show ntp status
Clock is unsynchronized, stratum 1, reference is .LOCL.
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 2100 (1/100 of seconds), resolution is 4000
reference time is EA8DB550.48F5C358 (11:45:36.285 CRST Thu Sep 12 2024)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 7939.14 msec, peer dispersion is 7937.98 msec
loopfilter state is 'FREQ' (Drift being measured), drift is 0.000000000 s/s
system poll interval is 16, last update was 12 sec ago.
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
*~127.127.1.1     .LOCL.           0      9     16     3  0.000   0.000 3938.2
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            172.22.0.5      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Loopback1              2.2.2.2         YES manual up                    up      
Loopback10             198.51.100.10   YES TFTP   up                    up      
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Bravo(config)#ip route 10.22.255.1 255.255.255.255 172.22.0.2
RTR-Shelter-Bravo(config)#end
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is not set

      2.0.0.0/32 is subnetted, 1 subnets
C        2.2.2.2 is directly connected, Loopback1
      10.0.0.0/8 is variably subnetted, 3 subnets, 2 masks
S        10.22.10.0/24 [1/0] via 172.22.0.2
S        10.22.20.0/24 [1/0] via 172.22.0.2
S        10.22.255.1/32 [1/0] via 172.22.0.2
      172.22.0.0/16 is variably subnetted, 2 subnets, 2 masks
C        172.22.0.0/29 is directly connected, Ethernet0/0
L        172.22.0.5/32 is directly connected, Ethernet0/0
      198.51.100.0/32 is subnetted, 1 subnets
C        198.51.100.10 is directly connected, Loopback10
RTR-Shelter-Bravo#



RTR-District-01#ping 1.1.1.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 1.1.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-District-01#ping 2.2.2.2
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 2.2.2.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-District-01#
RTR-District-01#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            172.22.0.2      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
Ethernet0/1.10         10.22.10.1      YES TFTP   administratively down down    
Ethernet0/1.20         10.22.20.1      YES TFTP   administratively down down    
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
RTR-District-01#
RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#interface ethernet0/1
RTR-District-01(config-if)#no shutdown
RTR-District-01(config-if)#end
RTR-District-01#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            172.22.0.2      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/1.10         10.22.10.1      YES TFTP   up                    up      
Ethernet0/1.20         10.22.20.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
RTR-District-01#
RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#interface Loopback0
RTR-District-01(config-if)#ip address 10.22.255.1
% Incomplete command.

RTR-District-01(config-if)#ip address 10.22.255.1 255.255.255.255
RTR-District-01(config-if)#exit
RTR-District-01(config)#ntp server 1.1.1.1
RTR-District-01(config)#ntp server 2.2.2.2
RTR-District-01(config)#end         
RTR-District-01#
RTR-District-01#show clock detail
11:50:40.744 CRST Thu Sep 12 2024
Time source is NTP
RTR-District-01#
RTR-District-01#show ntp status
Clock is unsynchronized, stratum 16, no reference clock
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 5100 (1/100 of seconds), resolution is 4000
reference time is 00000000.00000000 (17:00:00.000 CRST Wed Dec 31 1899)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 0.77 msec, peer dispersion is 0.00 msec
loopfilter state is 'NSET' (Never set), drift is 0.000000000 s/s
system poll interval is 8, never updated.
RTR-District-01#
RTR-District-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~1.1.1.1         .INIT.          16     48     64     0  0.000   0.000 15937.
 ~2.2.2.2         .INIT.          16     39     64     0  0.000   0.000 15937.
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-District-01#
RTR-District-01#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area 
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, m - OMP
       n - NAT, Ni - NAT inside, No - NAT outside, Nd - NAT DIA
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       H - NHRP, G - NHRP registered, g - NHRP registration summary
       o - ODR, P - periodic downloaded static route, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR
       & - replicated local route overrides by connected

Gateway of last resort is 172.22.0.1 to network 0.0.0.0

S*    0.0.0.0/0 [1/0] via 172.22.0.1
      1.0.0.0/32 is subnetted, 1 subnets
S        1.1.1.1 [1/0] via 172.22.0.1
      2.0.0.0/32 is subnetted, 1 subnets
S        2.2.2.2 [1/0] via 172.22.0.5
      10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
C        10.22.10.0/24 is directly connected, Ethernet0/1.10
L        10.22.10.1/32 is directly connected, Ethernet0/1.10
C        10.22.20.0/24 is directly connected, Ethernet0/1.20
L        10.22.20.1/32 is directly connected, Ethernet0/1.20
C        10.22.255.1/32 is directly connected, Loopback0
      172.22.0.0/16 is variably subnetted, 2 subnets, 2 masks
C        172.22.0.0/29 is directly connected, Ethernet0/0
L        172.22.0.2/32 is directly connected, Ethernet0/0
S     198.51.100.0/24 [1/0] via 172.22.0.5
RTR-District-01#



RTR-Shelter-Alpha#show ntp status      
Clock is synchronized, stratum 1, reference is .LOCL.
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 118500 (1/100 of seconds), resolution is 4000
reference time is EA8DB927.6C083250 (12:01:59.422 CRST Thu Sep 12 2024)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 2.36 msec, peer dispersion is 1.20 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000000000 s/s
system poll interval is 16, last update was 12 sec ago.
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
*~127.127.1.1     .LOCL.           0      9     16   377  0.000   0.000  1.204
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-Shelter-Alpha#



RTR-Shelter-Bravo#show ntp status      
Clock is synchronized, stratum 1, reference is .LOCL.
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 104200 (1/100 of seconds), resolution is 4000
reference time is EA8DB950.48F5C358 (12:02:40.285 CRST Thu Sep 12 2024)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 2.31 msec, peer dispersion is 1.20 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000000000 s/s
system poll interval is 16, last update was 9 sec ago.
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
*~127.127.1.1     .LOCL.           0     15     16   377  0.000   0.000  1.204
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-Shelter-Bravo#



RTR-District-01#show ntp status      
Clock is unsynchronized, stratum 2, reference is 1.1.1.1        
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 80600 (1/100 of seconds), resolution is 4000
reference time is EA8DB949.3A9FBF18 (12:02:33.229 CRST Thu Sep 12 2024)
clock offset is 4721.5001 msec, root delay is 1.00 msec
root dispersion is 4728.47 msec, peer dispersion is 3.01 msec
loopfilter state is 'FREQ' (Drift being measured), drift is 0.000000000 s/s
system poll interval is 64, last update was 48 sec ago.
RTR-District-01#
RTR-District-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
*~1.1.1.1         .LOCL.           1     61     64    17  1.000 4721.50  3.017
x~2.2.2.2         .LOCL.           1     56     64     3  1.000 2157.50 64.463
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-District-01#



Username: fieldtech
Password: 
SW-District-Access#con
*Aug 24 13:22:52.518: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: fieldtech] [Source: LOCAL] [localport: 0] at 13:22:52 UTC Mon Aug 24 2026
SW-District-Access#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-District-Access(config)#no logging console
*Aug 24 13:23:00.636: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
SW-District-Access(config)#no logging console
SW-District-Access(config)#
*Aug 24 13:23:00.739: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 13:23:00.740: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 13:23:00.848: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
SW-District-Access(config)#line con 0
SW-District-Access(config-line)#exec-timeout 0 0 
SW-District-Access(config-line)#end
SW-District-Access#
SW-District-Access#
SW-District-Access#ping 1.1.1.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 1.1.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-District-Access#
SW-District-Access#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-District-Access(config)#end        
SW-District-Access#ping 10.22.10.1    
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.10.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-District-Access#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-District-Access(config)#ntp source 10.22.10.1
                                      ^
% Invalid input detected at '^' marker.

SW-District-Access(config)#ntp server 10.22.10.1
SW-District-Access(config)#end
SW-District-Access#
SW-District-Access#show clock detail
*13:46:01.033 UTC Mon Aug 24 2026
Time source is NTP
SW-District-Access#
SW-District-Access#show ntp status
Clock is unsynchronized, stratum 16, no reference clock
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 1900 (1/100 of seconds), resolution is 4000
reference time is 00000000.00000000 (00:00:00.000 UTC Mon Jan 1 1900)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 0.29 msec, peer dispersion is 0.00 msec
loopfilter state is 'NSET' (Never set), drift is 0.000000000 s/s
system poll interval is 8, never updated.
SW-District-Access#
SW-District-Access#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~10.22.10.1      .INIT.          16     25     64     0  0.000   0.000 15937.
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
SW-District-Access#



RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#ntp source Loopback0
RTR-District-01(config)#end
RTR-District-01#
RTR-District-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
*~1.1.1.1         .LOCL.           1     42     64   377  1.000 4722.50  3.329
x~2.2.2.2         .LOCL.           1     37     64    77  1.000 2157.50  3.273
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-District-01#



***Note that RTR-District-01 never seems to achieve full synch with the ntp servers and resets periodically meaning that downstream dependencies cannot form a ntp association with it. this appears to be a failing of the emulator***

RTR-District-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~1.1.1.1         .STEP.          16      0     64     0  0.000   0.000 16000.
 ~2.2.2.2         .STEP.          16      0     64     0  0.000   0.000 16000.
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
RTR-District-01#
RTR-District-01#show ntp status      
Clock is unsynchronized, stratum 16, no reference clock
nominal freq is 250.0000 Hz, actual freq is 249.8750 Hz, precision is 2**10
ntp uptime is 152800 (1/100 of seconds), resolution is 4016
reference time is 00000000.00000000 (17:00:00.000 CRST Wed Dec 31 1899)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 0.00 msec, peer dispersion is 0.00 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000499999 s/s
system poll interval is 64, never updated.
RTR-District-01#



RTR-Shelter-Alpha#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Alpha(config)#ip domain name castlerysen.local
RTR-Shelter-Alpha(config)#ip dns server
RTR-Shelter-Alpha(config)#ip host cafe1.castlerysen.local 172.22.0.2
RTR-Shelter-Alpha(config)#ip name-server 1.1.1.1
RTR-Shelter-Alpha(config)#ip name-server 8.8.8.8
RTR-Shelter-Alpha(config)#



RTR-Shelter-Bravo#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Bravo(config)#ip domain name castlerysen.local
RTR-Shelter-Bravo(config)#ip dns server
RTR-Shelter-Bravo(config)#ip host cafe1.castlerysen.local 172.22.0.2
RTR-Shelter-Bravo(config)#ip name-server 1.1.1.1
RTR-Shelter-Bravo(config)#ip name-server 8.8.8.8
RTR-Shelter-Bravo(config)#



RTR-Shelter-Alpha#show run | include ip name-server
ip name-server 1.1.1.1 8.8.8.8
RTR-Shelter-Alpha#show hosts
Default domain is castlerysen.local
Name servers are 1.1.1.1, 8.8.8.8
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------
 2.0.22.172.in-addr.arpa        10      IN      PTR     cafe1.castlerysen.local
 cafe1.castlerysen.local        10      IN      A       172.22.0.2

RTR-Shelter-Alpha#



RTR-Shelter-Bravo#
RTR-Shelter-Bravo#show run | include ip name-server
ip name-server 1.1.1.1 8.8.8.8
RTR-Shelter-Bravo#show hosts
Default domain is castlerysen.local
Name servers are 1.1.1.1, 8.8.8.8
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------
 2.0.22.172.in-addr.arpa        10      IN      PTR     cafe1.castlerysen.local
 cafe1.castlerysen.local        10      IN      A       172.22.0.2

RTR-Shelter-Bravo#



RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#interface Loopback100
RTR-District-01(config-if)#ip address 10.22.10.50 255.255.255.255
% 10.22.10.50 overlaps with Ethernet0/1.10
RTR-District-01(config-if)#no ip address 10.22.10.50 255.255.255.255
Invalid address
RTR-District-01(config-if)#no interface Loopback100                 
RTR-District-01(config)#exit
RTR-District-01#interface ethernet0/1.10
                 ^
% Invalid input detected at '^' marker.

RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#interface etherent0/1.10
                                       ^
% Invalid input detected at '^' marker.

RTR-District-01(config)#interface ethernet0/1.10
RTR-District-01(config-subif)#ip address 10.22.10.50 255.255.255.255 secondary
Bad mask /32 for address 10.22.10.50
RTR-District-01(config-subif)#ip address 10.22.10.50 255.255.255.0 secondary
RTR-District-01(config-subif)#exit
RTR-District-01(config)#
RTR-District-01(config)#end
RTR-District-01#
RTR-District-01#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            172.22.0.2      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/1.10         10.22.10.1      YES TFTP   up                    up      
Ethernet0/1.20         10.22.20.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Loopback0              10.22.255.1     YES manual up                    up      
RTR-District-01#show run interface ethernet0/1.10
Building configuration...

Current configuration : 173 bytes
!
interface Ethernet0/1.10
 description Admin VLAN Gateway
 encapsulation dot1Q 10
 ip address 10.22.10.50 255.255.255.0 secondary
 ip address 10.22.10.1 255.255.255.0
end

RTR-District-01#



RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#ip domain name castlerysen.local
RTR-District-01(config)#ip dns server
RTR-District-01(config)#ip name-server 1.1.1.1
RTR-District-01(config)#ip name-server 2.2.2.2
RTR-District-01(config)#ip host plex.castlerysen.local 10.22.10.50
RTR-District-01(config)#end
RTR-District-01#
RTR-District-01#ping plex
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.10.50, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-District-01#
RTR-District-01#ping cafe1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.22.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-District-01#



RTR-Shelter-Alpha#ping cafe1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.22.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#ping plex
% Unrecognized host or address, or protocol not running.

RTR-Shelter-Alpha#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Alpha(config)#ip name-server 10.22.255.1
RTR-Shelter-Alpha(config)#end
RTR-Shelter-Alpha#
RTR-Shelter-Alpha#ping plex
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.10.50, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Shelter-Alpha#



RTR-Shelter-Bravo(config)#ip name-server 10.22.255.1
RTR-Shelter-Bravo(config)#end
RTR-Shelter-Bravo#
RTR-Shelter-Bravo#ping cafe1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.22.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Shelter-Bravo#ping plex
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.10.50, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-Shelter-Bravo#



SW-District-Access#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-District-Access(config)#ip domain name castlerysen.local
SW-District-Access(config)#ip name-server 10.22.255.1
SW-District-Access(config)#end
SW-District-Access#
SW-District-Access#
SW-District-Access#show hosts
Default domain is castlerysen.local
Name servers are 10.22.255.1
NAME  TTL  CLASS   TYPE      DATA/ADDRESS
-----------------------------------------

SW-District-Access#ping plex.castlerysen.local
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.10.50, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
SW-District-Access#ping cafe1.castlerysen.local
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 172.22.0.2, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-District-Access#



RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#ip dhcp excluded-address 10.22.10.1 10.22.10.20
DHCPD: exclusion [10.22.10.1, 10.22.10.20] already exists.
RTR-District-01(config)#ip dhcp excluded-address 10.22.20.1 10.22.20.20
DHCPD: exclusion [10.22.20.1, 10.22.20.20] already exists.
RTR-District-01(config)#ip dhcp pool ADMIN-NET
RTR-District-01(dhcp-config)# network 10.22.10.0 255.255.255.0
RTR-District-01(dhcp-config)# default-router 10.22.10.1
RTR-District-01(dhcp-config)# domain-name castlerysen.local
RTR-District-01(dhcp-config)# dns-server 10.22.10.1
RTR-District-01(dhcp-config)# option 42 ip 10.22.255.1
RTR-District-01(dhcp-config)#exit
RTR-District-01(config)#ip dhcp pool PATRON-NET
RTR-District-01(dhcp-config)# network 10.22.20.0 255.255.255.0
RTR-District-01(dhcp-config)# default-router 10.22.20.1
RTR-District-01(dhcp-config)# domain-name castlerysen.local
RTR-District-01(dhcp-config)# dns-server 10.22.10.1
RTR-District-01(dhcp-config)# option 42 ip 10.22.255.1
RTR-District-01(dhcp-config)#exit
RTR-District-01(config)#end
RTR-District-01#
RTR-District-01#
RTR-District-01#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            172.22.0.2      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/1.10         10.22.10.1      YES TFTP   up                    up      
Ethernet0/1.20         10.22.20.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Loopback0              10.22.255.1     YES manual up                    up      
RTR-District-01#show dhcp lease
RTR-District-01#


SW-District-Access#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-District-Access(config)#interface Vlan1
SW-District-Access(config-if)# no ip address
SW-District-Access(config-if)# ip address dhcp
SW-District-Access(config-if)#exit
SW-District-Access(config)#end
SW-District-Access#
SW-District-Access#
SW-District-Access#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Vlan1                  unassigned      YES manual administratively down down    
Vlan10                 10.22.10.22     YES DHCP   up                    up      
SW-District-Access#show dhcp lease
Temp IP addr: 10.22.10.22  for peer on Interface: Vlan10
Temp  sub net mask: 255.255.255.0
   DHCP Lease server: 10.22.10.1, state: 5 Bound
   DHCP transaction id: 5F202E08
   Lease: 86400 secs,  Renewal: 43200 secs,  Rebind: 75600 secs
Temp default-gateway addr: 10.22.10.1
   Next timer fires after: 11:01:19
   Retry count: 0   Client-ID: cisco-aabb.cc80.0200-Vl10
   Client-ID hex dump: 636973636F2D616162622E636338302E
                       303230302D566C3130
   Hostname: SW-District-Access
SW-District-Access#



RTR-Shelter-Alpha#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Alpha(config)#username jeremy privilege 15 secret BeanR0ast!
RTR-Shelter-Alpha(config)#crypto key generate rsa modulus 2048
The name for the keys will be: RTR-Shelter-Alpha.castlerysen.local

% The key modulus size is 2048 bits
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

RTR-Shelter-Alpha(config)#ip ssh version 2
RTR-Shelter-Alpha(config)#line vty 0 4
RTR-Shelter-Alpha(config-line)# transport input ssh
RTR-Shelter-Alpha(config-line)# login local
RTR-Shelter-Alpha(config-line)#exit
RTR-Shelter-Alpha(config)#end
RTR-Shelter-Alpha#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
RTR-Shelter-Alpha#



RTR-Shelter-Bravo#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Shelter-Bravo(config)#username jeremy privilege 15 secret BeanR0ast!
RTR-Shelter-Bravo(config)#crypto key generate rsa modulus 2048
The name for the keys will be: RTR-Shelter-Bravo.castlerysen.local

% The key modulus size is 2048 bits
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

RTR-Shelter-Bravo(config)#ip ssh version 2
RTR-Shelter-Bravo(config)#line vty 0 4
RTR-Shelter-Bravo(config-line)# transport input ssh
RTR-Shelter-Bravo(config-line)# login local
RTR-Shelter-Bravo(config-line)#exit
RTR-Shelter-Bravo(config)#end
RTR-Shelter-Bravo#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
RTR-Shelter-Bravo#



RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#username jeremy privilege 15 secret BeanR0ast!
RTR-District-01(config)#crypto key generate rsa modulus 2048
The name for the keys will be: RTR-District-01.castlerysen.local

% The key modulus size is 2048 bits
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

RTR-District-01(config)#ip ssh version 2
RTR-District-01(config)#line vty 0 4
RTR-District-01(config-line)# transport input ssh
RTR-District-01(config-line)# login local
RTR-District-01(config-line)#exit
RTR-District-01(config)#end
RTR-District-01#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
RTR-District-01#



SW-District-Access#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-District-Access(config)#username jeremy privilege 15 secret BeanR0ast!
SW-District-Access(config)#crypto key generate rsa modulus 2048
The name for the keys will be: SW-District-Access.castlerysen.local

% The key modulus size is 2048 bits
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

SW-District-Access(config)#ip ssh version 2
SW-District-Access(config)#line vty 0 4
SW-District-Access(config-line)# transport input ssh
SW-District-Access(config-line)# login local
SW-District-Access(config-line)#exit
SW-District-Access(config)#end
SW-District-Access#copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
SW-District-Access#
SW-District-Access#



Connecting to console for Admin-Term

Core Linux
admin-term login: tc
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

tc@admin-term:~$ 
tc@admin-term:~$ ssh -l jeremy 172.22.0.1
The authenticity of host '172.22.0.1 (172.22.0.1)' can't be established.
RSA key fingerprint is SHA256:jmH1301OXRcpCpG6jxmFe+3MtBhUZxci//cS4C2xCu4.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '172.22.0.1' (RSA) to the list of known hosts.
(jeremy@172.22.0.1) Password: 
(jeremy@172.22.0.1) Password: 



RTR-Shelter-Alpha#
RTR-Shelter-Alpha#end

tc@admin-term:~$ 
tc@admin-term:~$ telnet 172.22.0.2
telnet: can't connect to remote host (172.22.0.2): Connection refused
tc@admin-term:~$ ssh -l jeremy 172.22.0.2
The authenticity of host '172.22.0.2 (172.22.0.2)' can't be established.
RSA key fingerprint is SHA256:oGvN5Anz7X6pAoC4ZXNrmxj32SC3OJzx9ycQdKn2Kl0.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '172.22.0.2' (RSA) to the list of known hosts.
(jeremy@172.22.0.2) Password: 
(jeremy@172.22.0.2) Password: 



RTR-District-01#
RTR-District-01#
RTR-District-01#
RTR-District-01#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            172.22.0.2      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/1.10         10.22.10.1      YES TFTP   up                    up      
Ethernet0/1.20         10.22.20.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
Loopback0              10.22.255.1     YES manual up                    up      
RTR-District-01#end




RTR-District-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-District-01(config)#interface Ethernet0/1.10
RTR-District-01(config-subif)# ip nat inside
RTR-District-01(config-subif)#exit
RTR-District-01(config)#interface Ethernet0/1.20
RTR-District-01(config-subif)# ip nat inside
RTR-District-01(config-subif)#exit
RTR-District-01(config)#interface Ethernet0/0
RTR-District-01(config-if)# ip nat outside
RTR-District-01(config-if)#exit
RTR-District-01(config)#access-list 1 permit 10.22.10.0 0.0.0.255
RTR-District-01(config)#access-list 1 permit 10.22.20.0 0.0.0.255
RTR-District-01(config)#$de source list 1 interface Ethernet0/0 overload     
RTR-District-01(config)#end
RTR-District-01#
RTR-District-01#
RTR-District-01#ping 198.51.100.10 source 10.22.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 198.51.100.10, timeout is 2 seconds:
Packet sent with a source address of 10.22.10.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-District-01#ping 198.51.100.10 source 10.22.20.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 198.51.100.10, timeout is 2 seconds:
Packet sent with a source address of 10.22.20.1 
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
RTR-District-01#show ip nat translations
Pro Inside global      Inside local       Outside local      Outside global
icmp 172.22.0.2:1024   10.22.10.1:6       198.51.100.10:6    198.51.100.10:1024
icmp 172.22.0.2:1025   10.22.20.1:7       198.51.100.10:7    198.51.100.10:1025
RTR-District-01#
```
