# Lab 065 - Raw CLI Output

```bash
RTR-Training-01>
RTR-Training-01>en
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#no logging con
*Aug 20 11:33:52.805: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
RTR-Training-01(config)#no logging console
*Aug 20 11:33:52.907: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 11:33:52.907: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 11:33:53.012: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
RTR-Training-01(config)#no logging console
RTR-Training-01(config)#clock timezone CRST -7
RTR-Training-01(config)#ntp master
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#clock set 11:32:30 12 September 2024
RTR-Training-01#
RTR-Training-01#show clock
11:32:34.410 CRST Thu Sep 12 2024
RTR-Training-01#
RTR-Training-01#show clock detail
11:32:40.525 CRST Thu Sep 12 2024
Time source is NTP
RTR-Training-01#
RTR-Training-01#show ntp status
Clock is unsynchronized, stratum 8, reference is 127.127.1.1    
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 3900 (1/100 of seconds), resolution is 4000
reference time is EA8DB24E.8E147C68 (11:32:46.555 CRST Thu Sep 12 2024)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 3939.29 msec, peer dispersion is 3938.29 msec
loopfilter state is 'FREQ' (Drift being measured), drift is 0.000000000 s/s
system poll interval is 16, last update was 3 sec ago.
RTR-Training-01#



RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#interface Loopback100
RTR-Training-01(config-if)#ip address 10.22.100.1 255.255.255.255
RTR-Training-01(config-if)#exit
RTR-Training-01(config)#ntp source Loopback100
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#
RTR-Training-01#show ip interface brief | include Loopback100
Loopback100            10.22.100.1     YES manual up                    up      
RTR-Training-01#
RTR-Training-01#show running-config | include ntp
ntp source Loopback100
ntp master
RTR-Training-01#
RTR-Training-01#show ntp status
Clock is unsynchronized, stratum 8, reference is 127.127.1.1    
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 25500 (1/100 of seconds), resolution is 4000
reference time is EA8DB31E.8E147C68 (11:36:14.555 CRST Thu Sep 12 2024)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 2.33 msec, peer dispersion is 1.20 msec
loopfilter state is 'FREQ' (Drift being measured), drift is 0.000000000 s/s
system poll interval is 16, last update was 10 sec ago.
RTR-Training-01#


Connecting to console for SW-Training-01

*Aug 20 11:33:21.342: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Aug 20 11:33:21.342: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
SW-Training-01>
SW-Training-01>
*Aug 20 11:33:21.342: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
SW-Training-01>
*Aug 20 11:33:32.302: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
SW-Training-01>
*Aug 20 11:34:02.303: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
SW-Training-01>
*Aug 20 11:36:32.304: %AMDP2_FE-6-EXCESSCOLL: Ethernet0/0 TDR=0, TRC=0
SW-Training-01>en
SW-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-Training-01(config)#no logging console
SW-Training-01(config)#
*Aug 20 11:40:21.437: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 20 11:40:21.540: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 11:40:21.541: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 11:40:21.648: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
SW-Training-01(config)#
SW-Training-01(config)#
SW-Training-01(config)#end
SW-Training-01#
SW-Training-01#
SW-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
SW-Training-01(config)#interface vlan 10
SW-Training-01(config-if)#ip address 10.0.18.11 255.255.255.0
SW-Training-01(config-if)#no shutdown
SW-Training-01(config-if)#exit
SW-Training-01(config)#ip default-gateway 10.0.18.1
SW-Training-01(config)#ip route 0.0.0.0 0.0.0.0 10.0.18.1
SW-Training-01(config)#clock timezone CRST -7
SW-Training-01(config)#ntp server 10.22.100.1
SW-Training-01(config)#end
SW-Training-01#
SW-Training-01#
SW-Training-01#ping 10.0.18.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.18.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-Training-01#
SW-Training-01#ping 10.22.100.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.22.100.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
SW-Training-01#
SW-Training-01#
SW-Training-01#show ntp status
Clock is unsynchronized, stratum 16, no reference clock
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**10
ntp uptime is 7200 (1/100 of seconds), resolution is 4000
reference time is 00000000.00000000 (17:00:00.000 CRST Wed Dec 31 1899)
clock offset is 0.0000 msec, root delay is 0.00 msec
root dispersion is 1.09 msec, peer dispersion is 0.00 msec
loopfilter state is 'NSET' (Never set), drift is 0.000000000 s/s
system poll interval is 8, never updated.
SW-Training-01#
SW-Training-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~10.22.100.1     .INIT.          16     19     64     0  0.000   0.000 15937.
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
SW-Training-01#
SW-Training-01#
SW-Training-01#show clock detail
*04:44:23.097 CRST Thu Aug 20 2026
Time source is NTP
SW-Training-01#
SW-Training-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~10.22.100.1     .INIT.          16     54     64     0  0.000   0.000 15937.
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
SW-Training-01#
SW-Training-01#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~10.22.100.1     .INIT.          16     35     64     0  0.000   0.000 15937.
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
SW-Training-01#


In this simulator build, the switch can reach 10.22.100.1 after the static default route is added, but NTP remains in .INIT. with reach 0 instead of synchronizing. Record that live status rather than waiting indefinitely for stratum 9.
```
