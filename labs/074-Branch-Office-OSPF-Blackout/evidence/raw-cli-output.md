# Lab 074 - Raw CLI Evidence

## Purpose

This file contains CLI evidence captured from the PingMyNetwork Sandbox for Lab 074 - The Branch Office OSPF Blackout.

Evidence was captured from both:

1. The deliberately broken starting state
2. The corrected and fully operational network

This provides a record of the symptoms presented to the learner and the verification performed after all three OSPF faults were corrected.

---

# Broken Starting State

## R2-WAN Interface Status

```text
R2-WAN>en
R2-WAN#show ip interface brief
Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0         unassigned      YES NVRAM  administratively down down
GigabitEthernet0/1         10.0.12.2       YES NVRAM  up                    up
GigabitEthernet0/2         10.0.23.1       YES NVRAM  up                    up
GigabitEthernet0/3         unassigned      YES NVRAM  administratively down down
```

The two routed transit interfaces are both operational.

This confirms that the initial failure is not caused by a physical or administratively disabled interface.

---

## R2-WAN OSPF Neighbours

```text
R2-WAN#show ip ospf neighbor
```

No neighbours were displayed.

At the deliberately broken starting state, R2-WAN therefore has no active OSPF adjacencies.

---

## R2-WAN OSPF Routes

```text
R2-WAN#show ip route ospf
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is not set
```

No routes were being learned through OSPF.

---

# Deliberate Fault Evidence

## Fault 1 - R1-HQ OSPF Area Mismatch

```text
R1-HQ#show running-config | section router ospf
router ospf 1
 router-id 1.1.1.1
 passive-interface GigabitEthernet0/0
 network 10.0.12.0 0.0.0.3 area 1
 network 192.168.10.0 0.0.0.255 area 0
```

The `10.0.12.0/30` transit link has deliberately been placed into Area 1 on R1-HQ.

R2-WAN expects the same link to operate in Area 0.

---

## Fault 2 and Fault 3 - R3-Branch

```text
R3-BRANCH#show running-config | section router ospf
router ospf 1
 router-id 3.3.3.3
 passive-interface GigabitEthernet0/0
 passive-interface GigabitEthernet0/2
 network 10.0.23.0 0.0.0.3 area 0
```

Two deliberate faults are visible here.

### Fault 2

```text
passive-interface GigabitEthernet0/2
```

G0/2 connects R3-Branch to R2-WAN.

Making this interface passive prevents OSPF Hello packets from being exchanged and stops the neighbour relationship from forming.

### Fault 3

The following expected statement is absent:

```text
network 192.168.30.0 0.0.0.255 area 0
```

The Branch LAN is therefore not being advertised into OSPF.

---

# Fault Correction

## Correcting R3-Branch

```text
R3-BRANCH#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R3-BRANCH(config)# router ospf 1
R3-BRANCH(config-router)#no passive-interface g0/2
*Oct 19 18:11:54.212: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on GigabitEthernet0/2 from LOADING to FULL, Loading Done
R3-BRANCH(config-router)#network 192.168.30.0 0.0.0.255 area 0
R3-BRANCH(config-router)#end
*Oct 19 18:12:18.557: %SYS-5-CONFIG_I: Configured from console by console
```

Removing the incorrect passive-interface configuration immediately allowed R3-Branch to form a FULL OSPF adjacency with R2-WAN.

The Branch LAN was then restored to OSPF.

---

## Correcting R1-HQ

Before the correction, IOS repeatedly reported an OSPF area mismatch:

```text
R1-HQ#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
*Oct 19 18:05:09.841: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 10.0.12.2, GigabitEthernet0/1
R1-HQ(config)#router ospf 1
*Oct 19 18:05:19.841: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 10.0.12.2, GigabitEthernet0/1
*Oct 19 18:05:29.841: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 10.0.12.2, GigabitEthernet0/1
*Oct 19 18:05:39.841: %OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 10.0.12.2, GigabitEthernet0/1
```

The Area 1 network statement was then removed and replaced with the correct Area 0 statement:

```text
R1-HQ(config-router)#no network 10.0.12.0 0.0.0.3 area 1
R1-HQ(config-router)#network 10.0.12.0 0.0.0.3 area 0
*Oct 19 18:05:56.754: %OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on GigabitEthernet0/1 from LOADING to FULL, Loading Done
R1-HQ(config-router)#end
```

The OSPF adjacency immediately progressed to `FULL`.

---

# Corrected OSPF Configuration

## R1-HQ

```text
R1-HQ#show running-config | section router ospf
router ospf 1
 router-id 1.1.1.1
 passive-interface GigabitEthernet0/0
 network 10.0.12.0 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
```

---

## R2-WAN

```text
router ospf 1
 router-id 2.2.2.2
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.23.0 0.0.0.3 area 0
```

---

## R3-Branch

```text
R3-BRANCH#show running-config | section router ospf
router ospf 1
 router-id 3.3.3.3
 passive-interface GigabitEthernet0/0
 network 10.0.23.0 0.0.0.3 area 0
 network 192.168.30.0 0.0.0.255 area 0
```

---

# Final OSPF Neighbour Verification

```text
R2-WAN#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
3.3.3.3           1   FULL/DR         00:00:31    10.0.23.2       GigabitEthernet0/2
1.1.1.1           1   FULL/BDR        00:00:31    10.0.12.1       GigabitEthernet0/1
```

Both expected neighbour relationships are now in the `FULL` state.

---

# Final OSPF Route Verification

```text
R2-WAN#show ip route ospf
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, * - candidate default, U - per-user static route
       o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
       a - application route
       + - replicated route, % - next hop override, p - overrides from PfR

Gateway of last resort is not set

O     192.168.10.0/24 [110/2] via 10.0.12.1, 00:06:57, GigabitEthernet0/1
O     192.168.30.0/24 [110/2] via 10.0.23.2, 00:00:38, GigabitEthernet0/2
```

R2-WAN now learns both remote LANs through OSPF.

---

# End-to-End Verification

## HQ to Branch

```text
C:\>ping 192.168.30.10

Pinging 192.168.30.10 with 32 bytes of data:

Reply from 192.168.30.10: bytes=32 time=77ms TTL=125
Reply from 192.168.30.10: bytes=32 time=26ms TTL=125
Reply from 192.168.30.10: bytes=32 time=35ms TTL=125
Reply from 192.168.30.10: bytes=32 time=36ms TTL=125

Ping statistics for 192.168.30.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 26ms, Maximum = 77ms, Average = 44ms
```

Result:

```text
4 sent
4 received
0 lost
```

---

## Branch to HQ

```text
C:\>ping 192.168.10.10

Pinging 192.168.10.10 with 32 bytes of data:

Reply from 192.168.10.10: bytes=32 time=88ms TTL=125
Reply from 192.168.10.10: bytes=32 time=28ms TTL=125
Reply from 192.168.10.10: bytes=32 time=27ms TTL=125
Reply from 192.168.10.10: bytes=32 time=27ms TTL=125

Ping statistics for 192.168.10.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 27ms, Maximum = 88ms, Average = 43ms
```

Result:

```text
4 sent
4 received
0 lost
```

---

# Final Evidence Summary

The captured evidence demonstrates the complete troubleshooting lifecycle.

### Broken State

- Transit interfaces remained `up/up`.
- R2-WAN had no OSPF neighbours.
- R2-WAN had no OSPF-learned routes.
- R1-HQ had an Area 1 / Area 0 mismatch.
- R3-Branch had its WAN-facing interface configured as passive.
- The Branch LAN was missing from the OSPF configuration.

### Correction

- IOS identified the area mismatch through `%OSPF-4-ERRRCV` messages.
- Correcting the area allowed the R1-HQ / R2-WAN adjacency to reach `FULL`.
- Removing the incorrect passive-interface configuration allowed the R2-WAN / R3-Branch adjacency to reach `FULL`.
- Restoring the Branch LAN network statement allowed `192.168.30.0/24` to be advertised.

### Final State

- Both OSPF adjacencies reached `FULL`.
- R2-WAN learned both user LANs through OSPF.
- HQ successfully reached the Branch LAN.
- Branch successfully reached the HQ LAN.
- Both end-to-end ping tests completed with 0% packet loss.

The lab was therefore successfully restored to the intended operational state.