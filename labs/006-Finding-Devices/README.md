# Lab 006 - Finding Devices

## Objective
1. A user with the IP address of 192.168.1.18 has been complaining of slow internet access.
USING SWITCH ACCESS ONLY, locate this device's MAC address down to the switch and port level in this network. 

2. The IP address 192.168.1.11 has been identified as causing a security breach.
Locate this device in the network so malware scanes can be run.

---

## Devices Used
- Switch SW1 / SW2 / SW3 / SW4 / SW5 / SW6
- PC1 / PC2 / PC3 / PC4 / PC5 / PC6 / PC7 / PC8
- Server SV1 / SV2

---

## Configuration Steps

```bash
Switch>en
Switch#ping 192.168.1.18

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.18, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 0/0/0 ms

Switch#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.1.3             -   00D0.58BA.EC62  ARPA   Vlan1
Internet  192.168.1.18            0   0005.5E5D.B43C  ARPA   Vlan1
Switch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0001.64eb.5401    DYNAMIC     Fa0/1
   1    0005.5e5d.b43c    DYNAMIC     Fa0/1
   1    0030.f204.9503    DYNAMIC     Fa0/2
Switch#show interface fa0/1
FastEthernet0/1 is up, line protocol is up (connected)
  Hardware is Lance, address is 00e0.f917.4d01 (bia 00e0.f917.4d01)
 BW 100000 Kbit, DLY 100 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s
  input flow-control is off, output flow-control is off
  ARP type: ARPA, ARP Timeout 00:04:00
  Last input 00:00:08, output 00:00:05, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue :0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     956 packets input, 193351 bytes, 0 no buffer
     Received 956 broadcasts, 0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     0 watchdog, 0 multicast, 0 pause input
     0 input packets with dribble condition detected
     2357 packets output, 263570 bytes, 0 underruns
     0 output errors, 0 collisions, 10 interface resets
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier
     0 output buffer failures, 0 output buffers swapped out

Switch# show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone
Device ID    Local Intrfce   Holdtme    Capability   Platform    Port ID
Switch       Fas 0/2          121            S       2960        Fas 0/3
Switch       Fas 0/1          121            S       2960        Fas 0/1
Switch#

Switch>
Switch>en
Switch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0060.3e1c.4902    DYNAMIC     Fa0/3
   1    00e0.a30d.a801    DYNAMIC     Fa0/2
   1    00e0.b0d6.4402    DYNAMIC     Fa0/4
   1    00e0.f917.4d01    DYNAMIC     Fa0/1
Switch#ping 192.168.1.18

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.18, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 0/0/0 ms

Switch#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.1.1             -   000C.CF02.70D0  ARPA   Vlan1
Internet  192.168.1.18            0   0005.5E5D.B43C  ARPA   Vlan1
Switch#ping 192.168.1.18

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.18, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 0/3/14 ms

Switch#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.1.1             -   000C.CF02.70D0  ARPA   Vlan1
Internet  192.168.1.18            6   0005.5E5D.B43C  ARPA   Vlan1
Switch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0005.5e5d.b43c    DYNAMIC     Fa0/2
   1    000d.bd18.9083    DYNAMIC     Fa0/4
   1    0060.3e1c.4902    DYNAMIC     Fa0/3
   1    00e0.a30d.a801    DYNAMIC     Fa0/2
   1    00e0.b0d6.4402    DYNAMIC     Fa0/4
   1    00e0.f917.4d01    DYNAMIC     Fa0/1
Switch#

Switch>
Switch>show mac addresss-table
                       ^
% Invalid input detected at '^' marker.
	
Switch>en
Switch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0001.64eb.5402    DYNAMIC     Fa0/1
   1    0005.5e5d.b43c    DYNAMIC     Fa0/4
   1    000c.cf02.70d0    DYNAMIC     Fa0/1
   1    000d.bd18.9083    DYNAMIC     Fa0/1
   1    0030.f204.9504    DYNAMIC     Fa0/2

```

### Explanation
- First I ping the IP to find the MAC of the slow device
- I then check the CAM table to see which port this connection was found
- Can see multiple connections through same port so must move to next switch in the network and repeat
- Search is narrowed to the final switch showing only one device (our device) showing on one port and so can see the device is PC 4

---

## Configuration Steps Part 2

```bash
Switch#
Switch#ping 192.168.1.11

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.11, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 0/0/1 ms

Switch#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.1.4             -   00D0.FFC4.BDA8  ARPA   Vlan1
Internet  192.168.1.11            0   0005.5E3C.0DC1  ARPA   Vlan1
Switch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0001.64eb.5402    DYNAMIC     Fa0/1
   1    0005.5e3c.0dc1    DYNAMIC     Fa0/1
   1    0030.f204.9504    DYNAMIC     Fa0/2
Switch#

Switch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0005.5e3c.0dc1    DYNAMIC     Fa0/3
   1    0060.3e1c.4902    DYNAMIC     Fa0/3
   1    00d0.ffc4.bda8    DYNAMIC     Fa0/2
   1    00e0.a30d.a801    DYNAMIC     Fa0/2
   1    00e0.b0d6.4402    DYNAMIC     Fa0/4
   1    00e0.f917.4d01    DYNAMIC     Fa0/1
Switch#

Switch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----

   1    0001.64eb.5403    DYNAMIC     Fa0/2
   1    0005.5e3c.0dc1    DYNAMIC     Fa0/4
   1    0030.f204.9501    DYNAMIC     Fa0/1
   1    00d0.ffc4.bda8    DYNAMIC     Fa0/2
Switch#

```

### Explanation Part 2
- This time I reversed the same process by pinging the infected devices IP address table first from the switch I was working on
- Then checked ARP table for the MAC address and then confirmed the connected port using `show mac address-table` 
- I then checked the CAM tables on two further switches to narrow doen the search to PC6 which will now be scanned for malware

---

## Troubleshooting

### Issue 1
What went wrong?
- The provided exercise files did not have switches correctly numbered so `show cdp neighbors` only gave me a list of same named devices with no identifying characteristics

### Diagnosis
How you found the problem.
- By using the `show cdp neighbors` command

### Fix
How you resolved it.
- Had to check CAM table on multiple switches manually
---

## Key Learnings
- What you learned
    - How to locate devices on a LAN starting only with IP addressing
- What improved
    - Understanding of ARP and CAM tables
- What to remember next time
    - STAY CALM AND PATIENTLY WORK THROUGH THE DATA 🕵️‍♂️

---

## Improvements for Next Time
- What you would do differently
    - I imagine the lack of updated hostnames is a real world happening so although not desirable, I think the learning was good. I'm happy with my approach on this one
