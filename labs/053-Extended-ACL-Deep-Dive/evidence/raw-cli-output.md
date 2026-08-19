# Lab 053 - Raw CLI Output

```bash
Skill 18 • Lesson 03 Lab — Extended ACL Deep Dive
Mission Briefing
Castle Rysen’s bunker simulator has spun up R18-L3 with two lifeline terminals: PC-A at the Roastery floor (10.18.30.10/24 on Ethernet0/0) and PC-B in the Quality Lab (10.18.40.20/24 on Ethernet0/1). Jeremy needs you to prove you can sculpt an extended access list that protects the network without starving the survivors of healthy traffic. You’ll practice isolating echo probes while keeping business-critical flows alive — because in the field, precision beats brute force.

Training Objectives
For this deployment to be successful, you must complete the following:

Confirm the current connectivity map between R18-L3, PC-A, and PC-B before introducing policy.
Build a named extended access list that selectively permits and denies ICMP alongside an IP catch-all safeguard.
Apply the filter near the traffic source and verify that policy counters reflect the intended behavior.
Task 0 — Map the Baseline
Verify the network is wide open before you tighten the screws so you know exactly what changes once the filter lands.

Steps:

On R18-L3, reach privileged EXEC mode and note the prompt so you’re ready to adjust policy.
Review the Ethernet interfaces to confirm which link faces PC-A (10.18.30.10) and which reaches PC-B (10.18.40.20).
Log in to PC-A and PC-B with cisco / cisco, then send quick echo tests to validate that traffic currently flows without restrictions.
Task 1 — Craft the Extended ACL
Shape the policy named S18-L03-FILTER so it favors essential ties between the labs while clipping stray echo traffic from PC-A.

Steps:

Enter configuration mode on R18-L3 and start building the named extended access list S18-L03-FILTER.
Insert a statement that explicitly allows echo requests from PC-A (10.18.30.10) to reach PC-B (10.18.40.20).
Add the follow-up entries that deny other echo traffic from PC-A while keeping all remaining IP protocols available for the team.
Task 2 — Deploy and Verify the Filter
Anchor the policy where PC-A traffic first hits the router and prove the matches behave as designed.

Steps:

Move into the configuration context of Ethernet0/0 on R18-L3, the interface that receives traffic from PC-A.
Apply the S18-L03-FILTER access list inbound so unwanted echoes are stopped closest to their source.
Re-test from PC-A, confirming pings to PC-B succeed while attempts to either router interface fail, then review the ACL counters to ensure the correct statements show hits.
Completion Check
PC-A successfully echoes PC-B, while echo attempts from PC-A to 10.18.30.1 and 10.18.40.1 time out.
The catch-all permit ip any any remains in the ACL so IP traffic other than the denied echo requests is not blocked.
show ip access-lists S18-L03-FILTER on R18-L3 reports hits on sequence 10 and 20, confirming the policy is matching as designed.



----------------------------------------------------------------------------------------------------------------------------------


Raw CLI Output



Connecting to console for R18-L3

R18-L3>en
R18-L3#show ip interface
*Aug 17 11:25:43.912: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
R18-L3#show ip interface bri
*Aug 17 11:25:44.014: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 11:25:44.015: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 17 11:25:44.120: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
R18-L3#show ip interface brief
*Aug 17 11:25:44.220: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 17 11:25:44.220: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
R18-L3#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            10.18.30.1      YES TFTP   up                    up      
Ethernet0/1            10.18.40.1      YES TFTP   up                    up      
Ethernet0/2            unassigned      YES unset  administratively down down    
Ethernet0/3            unassigned      YES unset  administratively down down    
R18-L3#


Connecting to console for PC-A

Core Linux
pc-a login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-")           www.tinycorelinux.net

cisco@pc-a:~$ ping -c 3 10.0.18.1
PING 10.0.18.1 (10.0.18.1): 56 data bytes

--- 10.0.18.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@pc-a:~$ 10.18.30.1
-sh: 10.18.30.1: not found
cisco@pc-a:~$ ping -c 3 10.18.30.1
PING 10.18.30.1 (10.18.30.1): 56 data bytes
64 bytes from 10.18.30.1: seq=0 ttl=255 time=0.597 ms
64 bytes from 10.18.30.1: seq=1 ttl=255 time=0.584 ms
64 bytes from 10.18.30.1: seq=2 ttl=255 time=0.537 ms

--- 10.18.30.1 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.537/0.572/0.597 ms
cisco@pc-a:~$ 
cisco@pc-a:~$ 
cisco@pc-a:~$ ping -c 3 10.18.40.20
PING 10.18.40.20 (10.18.40.20): 56 data bytes
64 bytes from 10.18.40.20: seq=0 ttl=63 time=1.304 ms
64 bytes from 10.18.40.20: seq=1 ttl=63 time=0.836 ms
64 bytes from 10.18.40.20: seq=2 ttl=63 time=0.830 ms

--- 10.18.40.20 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.830/0.990/1.304 ms
cisco@pc-a:~$ 


Connecting to console for PC-B

Core Linux
pc-b login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-")           www.tinycorelinux.net

cisco@pc-b:~$ ping -c 3 10.18.40.1
PING 10.18.40.1 (10.18.40.1): 56 data bytes
64 bytes from 10.18.40.1: seq=0 ttl=255 time=0.596 ms
64 bytes from 10.18.40.1: seq=1 ttl=255 time=0.630 ms
64 bytes from 10.18.40.1: seq=2 ttl=255 time=0.650 ms

--- 10.18.40.1 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.596/0.625/0.650 ms
cisco@pc-b:~$ 



R18-L3#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R18-L3(config)#ip access-list extended S18-L03-FILTER
R18-L3(config-ext-nacl)#10 permit icmp host 10.18.30.10 host 10.18.40.20 echo
R18-L3(config-ext-nacl)#20 deny icmp host 10.18.30.10 any echo
R18-L3(config-ext-nacl)#30 permit ip any any
R18-L3(config-ext-nacl)#end
R18-L3#
*Aug 17 11:30:38.136: %SYS-5-CONFIG_I: Configured from console by console
R18-L3#show ip access-lists S18-L03-FILTER
Extended IP access list S18-L03-FILTER
    10 permit icmp host 10.18.30.10 host 10.18.40.20 echo
    20 deny icmp host 10.18.30.10 any echo
    30 permit ip any any
R18-L3#



R18-L3#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R18-L3(config)# interface ethernet0/0
R18-L3(config-if)#ip access-group S18-L03-FILTER in
R18-L3(config-if)#end
R18-L3#


cisco@pc-a:~$ ping -c 3 10.18.40.20
PING 10.18.40.20 (10.18.40.20): 56 data bytes
64 bytes from 10.18.40.20: seq=0 ttl=63 time=0.692 ms
64 bytes from 10.18.40.20: seq=1 ttl=63 time=0.892 ms
64 bytes from 10.18.40.20: seq=2 ttl=63 time=0.744 ms

--- 10.18.40.20 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.692/0.776/0.892 ms
cisco@pc-a:~$ 
cisco@pc-a:~$ 
cisco@pc-a:~$ ping -c 3 10.18.30.1
PING 10.18.30.1 (10.18.30.1): 56 data bytes

--- 10.18.30.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@pc-a:~$ 
cisco@pc-a:~$ 
cisco@pc-a:~$ 
cisco@pc-a:~$ ping -c 3 10.18.40.1
PING 10.18.40.1 (10.18.40.1): 56 data bytes

--- 10.18.40.1 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
cisco@pc-a:~$ 


R18-L3#show ip access-lists S18-L03-FILTER
Extended IP access list S18-L03-FILTER
    10 permit icmp host 10.18.30.10 host 10.18.40.20 echo (3 matches)
    20 deny icmp host 10.18.30.10 any echo (6 matches)
    30 permit ip any any (24 matches)
R18-L3#
```
