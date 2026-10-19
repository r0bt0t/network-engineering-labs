# Lab 074 - The Branch Office OSPF Blackout

## Objective

Design and build an original CCNA-level troubleshooting lab using the PingMyNetwork Sandbox.

The aim was to create a small but realistic OSPF troubleshooting scenario in which the learner is presented with a network that has:

- Correct IPv4 addressing
- Operational physical interfaces
- A clearly defined intended design
- No end-to-end connectivity because of deliberately introduced OSPF configuration faults

The learner must diagnose and correct the problems using verification and troubleshooting commands rather than simply following configuration instructions.

This lab was also created for submission to the PingMyNetwork Sandbox Challenge.

A secondary objective was to move beyond completing pre-built networking labs and experience the process of designing a troubleshooting exercise for somebody else to solve.

---

## Scenario

An overnight configuration change has left the Branch office unable to communicate with HQ.

All physical interfaces and IPv4 addressing are correct.

The network should use single-area OSPF Area 0 to provide connectivity between the HQ and Branch LANs.

Three OSPF configuration faults have been introduced.

### Learner Tasks

- Diagnose and correct the OSPF configuration.
- Do not change the existing IPv4 addressing.
- Do not use static routes.
- Restore full end-to-end connectivity.
- Verify that the expected OSPF neighbour relationships form.
- Verify that the required remote networks appear in the routing tables.

### Success Condition

`PC-HQ` at `192.168.10.10` must be able to successfully ping `PC-Branch` at `192.168.30.10`.

---

## Devices Used

| Device | Role |
|---|---|
| PC-HQ | HQ end device |
| R1-HQ | HQ router |
| R2-WAN | Transit/WAN router |
| R3-Branch | Branch router |
| PC-Branch | Branch end device |

The lab was created using the **PingMyNetwork Sandbox**.

---

## Addressing Plan

| Device | Interface | IPv4 Address | Prefix |
|---|---|---:|---:|
| PC-HQ | F0 | 192.168.10.10 | /24 |
| R1-HQ | G0/0 | 192.168.10.1 | /24 |
| R1-HQ | G0/1 | 10.0.12.1 | /30 |
| R2-WAN | G0/1 | 10.0.12.2 | /30 |
| R2-WAN | G0/2 | 10.0.23.1 | /30 |
| R3-Branch | G0/2 | 10.0.23.2 | /30 |
| R3-Branch | G0/0 | 192.168.30.1 | /24 |
| PC-Branch | F0 | 192.168.30.10 | /24 |

### Default Gateways

| Host | Default Gateway |
|---|---:|
| PC-HQ | 192.168.10.1 |
| PC-Branch | 192.168.30.1 |

---

## Interface / Port Plan

```text
PC-HQ F0
   |
   |
R1-HQ G0/0

R1-HQ G0/1
   |
   | 10.0.12.0/30
   |
R2-WAN G0/1

R2-WAN G0/2
   |
   | 10.0.23.0/30
   |
R3-Branch G0/2

R3-Branch G0/0
   |
   |
PC-Branch F0
```

### Network Summary

| Network | Purpose |
|---|---|
| 192.168.10.0/24 | HQ LAN |
| 10.0.12.0/30 | R1-HQ to R2-WAN transit |
| 10.0.23.0/30 | R2-WAN to R3-Branch transit |
| 192.168.30.0/24 | Branch LAN |

---

## Final Topology

The topology was deliberately kept small so that the challenge could focus on OSPF troubleshooting rather than topology complexity.

The PingMyNetwork workspace also includes:

- The lab title
- The troubleshooting scenario
- Learner instructions
- The complete addressing table
- Subnet labels for each network segment
- The required success condition

![Lab 074 - The Branch Office OSPF Blackout - Complete Working Topology](Images/Complete%20and%20working.png)

---

# Configuration and Build Process

## 1. Building a Known-Good Network

Before introducing any troubleshooting faults, the complete network was configured and tested in a known-good state.

This was an important part of the design process.

A troubleshooting lab should begin from a configuration that has already been proven to work. Otherwise it can become difficult to distinguish between:

- Deliberately introduced faults
- Accidental configuration mistakes
- Simulator or platform behaviour
- Addressing errors
- Routing protocol errors

The intended OSPF design used:

- OSPF process ID `1`
- Single-area OSPF Area `0`
- Manually configured router IDs
- Passive interfaces towards end-device LANs
- Active OSPF neighbour relationships across the routed transit links

---

## 2. R1-HQ Working OSPF Configuration

R1-HQ provides connectivity to the HQ LAN and forms an OSPF neighbour relationship with R2-WAN.

```text
router ospf 1
 router-id 1.1.1.1
 passive-interface GigabitEthernet0/0
 network 10.0.12.0 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
```

`GigabitEthernet0/0` is passive because the HQ LAN needs to be advertised into OSPF, but no OSPF-speaking router exists on that interface.

---

## 3. R2-WAN Working OSPF Configuration

R2-WAN acts as the transit router between the HQ and Branch sites.

```text
router ospf 1
 router-id 2.2.2.2
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.23.0 0.0.0.3 area 0
```

Both routed interfaces participate fully in OSPF because R2-WAN must form neighbour relationships with both R1-HQ and R3-Branch.

---

## 4. R3-Branch Working OSPF Configuration

R3-Branch provides connectivity to the Branch LAN and forms an OSPF neighbour relationship with R2-WAN.

```text
router ospf 1
 router-id 3.3.3.3
 passive-interface GigabitEthernet0/0
 network 10.0.23.0 0.0.0.3 area 0
 network 192.168.30.0 0.0.0.255 area 0
```

`GigabitEthernet0/0` is passive because it faces the Branch LAN rather than another OSPF router.

---

# Initial Validation of the Working Network

Before introducing deliberate faults, the network was tested to confirm that:

- All required interfaces were operational.
- R1-HQ formed an OSPF adjacency with R2-WAN.
- R2-WAN formed an OSPF adjacency with R3-Branch.
- The HQ LAN was advertised into OSPF.
- The Branch LAN was advertised into OSPF.
- Remote networks appeared in the routing tables.
- PC-HQ could communicate with PC-Branch.

Useful commands included:

```text
show ip interface brief
show ip ospf neighbor
show ip route ospf
show running-config | section router ospf
show ip ospf interface
show ip protocols
ping
```

The intended neighbour relationships were:

```text
R1-HQ <-> R2-WAN       FULL
R2-WAN <-> R3-Branch   FULL
```

The end-to-end connectivity test was:

```text
PC-HQ> ping 192.168.30.10
```

This succeeded before the deliberate faults were introduced.

---

# Genuine Troubleshooting During the Build

Two genuine configuration mistakes were encountered while initially constructing the network.

These were corrected before the deliberate troubleshooting faults were introduced.

This became a useful part of the lab-building process because it reinforced the importance of establishing a known-good state before intentionally breaking a network.

---

## Build Issue 1 - Incorrect IP Address on R2-WAN

R2-WAN was initially configured incorrectly.

`GigabitEthernet0/1`, which connects towards R1-HQ, had mistakenly been given:

```text
ip address 10.0.23.1 255.255.255.252
```

The intended addressing was:

```text
R1-HQ G0/1
10.0.12.1/30

R2-WAN G0/1
10.0.12.2/30
```

while the second transit network should have been:

```text
R2-WAN G0/2
10.0.23.1/30

R3-Branch G0/2
10.0.23.2/30
```

The error became apparent when the following direct ping failed:

```text
R1-HQ#ping 10.0.12.2
```

Because R1-HQ and R2-WAN should have been directly connected, this test did not require OSPF.

The failed ping therefore indicated that the problem existed below the routing protocol.

The problem was investigated using:

```text
show ip interface brief
show running-config interface GigabitEthernet0/1
ping 10.0.12.2
```

The corrected R2-WAN interface configuration became:

```text
interface GigabitEthernet0/1
 description LINK-TO-R1-HQ
 ip address 10.0.12.2 255.255.255.252
 no shutdown

interface GigabitEthernet0/2
 description LINK-TO-R3-BRANCH
 ip address 10.0.23.1 255.255.255.252
 no shutdown
```

Once corrected, direct IP connectivity between R1-HQ and R2-WAN was restored.

---

## Build Issue 2 - Missing OSPF Network Statement on R1-HQ

A second issue was found on R1-HQ.

The initial OSPF configuration contained:

```text
router ospf 1
 router-id 1.1.1.1
 passive-interface GigabitEthernet0/0
 network 192.168.10.0 0.0.0.255 area 0
```

The network statement covering the R1-HQ to R2-WAN link had accidentally been omitted.

The missing command was:

```text
network 10.0.12.0 0.0.0.3 area 0
```

Without this statement, OSPF was not enabled on `GigabitEthernet0/1`.

The interface itself was operational and direct IP connectivity worked once the addressing problem was corrected, but the OSPF adjacency could not form.

Adding the missing network statement restored the expected neighbour relationship.

This reinforced the difference between:

```text
A working interface
```

```text
A working IP path
```

and:

```text
A working routing protocol
```

---

# Deliberately Introduced Faults

Once the known-good configuration had been successfully tested, three OSPF faults were deliberately introduced.

The faults were selected to create a logical troubleshooting progression rather than simply presenting three unrelated mistakes.

The intended learning path is:

```text
Interfaces are up
        |
        v
No OSPF neighbours
        |
        v
Investigate OSPF configuration
        |
        v
Fix R1-HQ / R2-WAN adjacency
        |
        v
R2-WAN / R3-Branch still down
        |
        v
Fix second adjacency
        |
        v
Both neighbours reach FULL
        |
        v
End-to-end connectivity still fails
        |
        v
Investigate the routing table
        |
        v
Discover missing LAN advertisement
        |
        v
Restore end-to-end connectivity
```

---

## Fault 1 - OSPF Area Mismatch

The first deliberate fault was introduced on R1-HQ.

The working statement:

```text
network 10.0.12.0 0.0.0.3 area 0
```

was replaced with:

```text
network 10.0.12.0 0.0.0.3 area 1
```

R2-WAN remained configured with:

```text
network 10.0.12.0 0.0.0.3 area 0
```

The two routers therefore disagreed about the OSPF area assigned to their shared link.

This prevents the OSPF adjacency from forming.

Importantly:

- Both interfaces remain `up/up`.
- Both interfaces retain correct IPv4 addressing.
- Both routers remain in the same `/30` subnet.
- Direct Layer 3 connectivity still works.
- OSPF neighbour formation fails.

During the correction process, IOS provided a particularly useful diagnostic message:

```text
%OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 10.0.12.2, GigabitEthernet0/1
```

This demonstrates how IOS logging can expose the cause of an OSPF adjacency failure directly.

### Intended Fix

```text
conf t
router ospf 1
 no network 10.0.12.0 0.0.0.3 area 1
 network 10.0.12.0 0.0.0.3 area 0
end
```

After the correction, IOS reported:

```text
%OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on GigabitEthernet0/1 from LOADING to FULL, Loading Done
```

---

## Fault 2 - R3-Branch WAN Interface Configured as Passive

The second deliberate fault was introduced on R3-Branch.

The following command was added:

```text
passive-interface GigabitEthernet0/2
```

`GigabitEthernet0/2` connects R3-Branch to R2-WAN.

A passive OSPF interface does not send OSPF Hello packets.

As a result:

- G0/2 remains `up/up`.
- Its IPv4 address remains correct.
- Direct IP communication with R2-WAN remains possible.
- No OSPF neighbour relationship forms across the link.

### Intended Fix

```text
conf t
router ospf 1
 no passive-interface GigabitEthernet0/2
end
```

When the passive-interface configuration was removed, IOS immediately reported:

```text
%OSPF-5-ADJCHG: Process 1, Nbr 2.2.2.2 on GigabitEthernet0/2 from LOADING to FULL, Loading Done
```

---

## Fault 3 - Branch LAN Missing from OSPF

The third fault was deliberately designed to remain after the learner restores both neighbour relationships.

The following statement was removed from R3-Branch:

```text
network 192.168.30.0 0.0.0.255 area 0
```

R3-Branch still knows about this network because it is directly connected.

However, without the OSPF network statement, the Branch LAN is not advertised to the rest of the OSPF domain.

This creates an important second stage in the exercise.

A learner may successfully restore:

```text
R1-HQ <-> R2-WAN       FULL
R2-WAN <-> R3-Branch   FULL
```

and assume the network has been fixed.

However, the HQ network still requires a route to:

```text
192.168.30.0/24
```

This reinforces an important lesson:

> A FULL OSPF neighbour state does not automatically mean every required network is being advertised correctly.

### Intended Fix

```text
conf t
router ospf 1
 network 192.168.30.0 0.0.0.255 area 0
end
```

---

# Broken Starting State

After all three deliberate faults were introduced, the lab was tested again.

R2-WAN showed:

```text
Interface                  IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0         unassigned      YES NVRAM  administratively down down
GigabitEthernet0/1         10.0.12.2       YES NVRAM  up                    up
GigabitEthernet0/2         10.0.23.1       YES NVRAM  up                    up
GigabitEthernet0/3         unassigned      YES NVRAM  administratively down down
```

The routed transit interfaces were therefore operational.

However:

```text
R2-WAN#show ip ospf neighbor
```

returned no neighbours.

Likewise:

```text
R2-WAN#show ip route ospf
```

showed no OSPF-learned routes.

The deliberate fault configurations were also confirmed.

### R1-HQ

```text
router ospf 1
 router-id 1.1.1.1
 passive-interface GigabitEthernet0/0
 network 10.0.12.0 0.0.0.3 area 1
 network 192.168.10.0 0.0.0.255 area 0
```

### R3-Branch

```text
router ospf 1
 router-id 3.3.3.3
 passive-interface GigabitEthernet0/0
 passive-interface GigabitEthernet0/2
 network 10.0.23.0 0.0.0.3 area 0
```

The Branch LAN network statement was absent.

The end-to-end ping between the two LANs failed as intended.

---

# Recommended Troubleshooting Approach

The learner is free to investigate the network in any order.

The intended approach is based on progressively verifying each layer of functionality rather than immediately changing configuration.

---

## Step 1 - Verify Interface State

```text
show ip interface brief
```

The relevant interfaces should report:

```text
up    up
```

This helps eliminate obvious interface failures.

---

## Step 2 - Verify Direct IP Connectivity

Test directly connected neighbours.

From R1-HQ:

```text
ping 10.0.12.2
```

From R2-WAN:

```text
ping 10.0.12.1
ping 10.0.23.2
```

From R3-Branch:

```text
ping 10.0.23.1
```

These tests should succeed.

This demonstrates that the underlying IPv4 connectivity is operational.

---

## Step 3 - Check OSPF Neighbours

```text
show ip ospf neighbor
```

In the deliberately broken state, R2-WAN has no OSPF neighbours.

This indicates that the problem exists within the routing protocol configuration.

---

## Step 4 - Inspect the OSPF Configuration

Useful commands include:

```text
show running-config | section router ospf
show ip ospf interface
show ip protocols
```

The learner should compare neighbouring routers rather than examining each router in isolation.

---

## Step 5 - Resolve the R1-HQ to R2-WAN Area Mismatch

R1-HQ incorrectly places the `10.0.12.0/30` link into Area 1.

R2-WAN places the same link into Area 0.

The R1-HQ configuration must therefore be restored to Area 0.

---

## Step 6 - Investigate the R2-WAN to R3-Branch Adjacency

The second neighbour relationship still fails because R3-Branch G0/2 has been configured as passive.

Removing:

```text
passive-interface GigabitEthernet0/2
```

allows OSPF Hellos to be exchanged again.

---

## Step 7 - Check the Routing Table

Once both adjacencies are restored:

```text
show ip route ospf
```

should be used to verify whether the expected remote LANs have actually been learned.

This prevents the troubleshooting process from stopping simply because the OSPF neighbours show `FULL`.

---

## Step 8 - Identify the Missing Branch LAN Advertisement

Inspection of R3-Branch reveals that:

```text
network 192.168.30.0 0.0.0.255 area 0
```

is missing.

Restoring this statement allows the Branch LAN to be advertised throughout the OSPF domain.

---

# Corrected Configuration

## R1-HQ

```text
router ospf 1
 router-id 1.1.1.1
 passive-interface GigabitEthernet0/0
 network 10.0.12.0 0.0.0.3 area 0
 network 192.168.10.0 0.0.0.255 area 0
```

## R2-WAN

```text
router ospf 1
 router-id 2.2.2.2
 network 10.0.12.0 0.0.0.3 area 0
 network 10.0.23.0 0.0.0.3 area 0
```

## R3-Branch

```text
router ospf 1
 router-id 3.3.3.3
 passive-interface GigabitEthernet0/0
 network 10.0.23.0 0.0.0.3 area 0
 network 192.168.30.0 0.0.0.255 area 0
```

---

# Final Verification

## OSPF Neighbours

After correcting all three faults, R2-WAN reported:

```text
R2-WAN#show ip ospf neighbor

Neighbor ID     Pri   State           Dead Time   Address         Interface
3.3.3.3           1   FULL/DR         00:00:31    10.0.23.2       GigabitEthernet0/2
1.1.1.1           1   FULL/BDR        00:00:31    10.0.12.1       GigabitEthernet0/1
```

Both required OSPF neighbour relationships had reached the `FULL` state.

---

## OSPF Routes

R2-WAN then showed:

```text
O     192.168.10.0/24 [110/2] via 10.0.12.1, GigabitEthernet0/1
O     192.168.30.0/24 [110/2] via 10.0.23.2, GigabitEthernet0/2
```

This confirmed that both user LANs were being successfully advertised through OSPF.

---

## End-to-End Connectivity

PC-HQ successfully reached the Branch PC:

```text
C:\>ping 192.168.30.10

Pinging 192.168.30.10 with 32 bytes of data:

Reply from 192.168.30.10: bytes=32 time=77ms TTL=125
Reply from 192.168.30.10: bytes=32 time=26ms TTL=125
Reply from 192.168.30.10: bytes=32 time=35ms TTL=125
Reply from 192.168.30.10: bytes=32 time=36ms TTL=125

Ping statistics for 192.168.30.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

The reverse test also succeeded:

```text
C:\>ping 192.168.10.10

Pinging 192.168.10.10 with 32 bytes of data:

Reply from 192.168.10.10: bytes=32 time=88ms TTL=125
Reply from 192.168.10.10: bytes=32 time=28ms TTL=125
Reply from 192.168.10.10: bytes=32 time=27ms TTL=125
Reply from 192.168.10.10: bytes=32 time=27ms TTL=125

Ping statistics for 192.168.10.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

This confirmed full bidirectional connectivity between the HQ and Branch LANs.

---

# Troubleshooting Lessons

## Build the Network Before Breaking It

One of the most important lessons from designing this exercise was the need to prove that the network works before introducing deliberate faults.

Genuine configuration mistakes were encountered during construction.

Without a known-good baseline, these accidental faults could easily have become mixed into the intended challenge.

---

## Start Below the Routing Protocol

The initial failed ping between R1-HQ and R2-WAN demonstrated that OSPF should not be the first thing investigated when directly connected devices cannot communicate.

The interface configuration and IP addressing needed to be corrected first.

---

## Interface State Is Only the Beginning

An interface reporting:

```text
up/up
```

does not prove that:

- OSPF is enabled
- OSPF neighbours have formed
- The correct area is configured
- Networks are being advertised
- Remote routes are being learned
- End-to-end connectivity exists

---

## Direct Connectivity Does Not Guarantee OSPF Adjacency

The area mismatch demonstrates that two routers can:

- Be directly connected
- Have correct IP addresses
- Successfully ping each other

while still failing to establish an OSPF neighbour relationship.

---

## IOS Messages Can Provide Valuable Clues

During correction of the area mismatch, IOS repeatedly reported:

```text
%OSPF-4-ERRRCV: Received invalid packet: mismatched area ID from backbone area from 10.0.12.2, GigabitEthernet0/1
```

This was an excellent example of the device itself providing a direct diagnostic clue.

Similarly, both corrected adjacencies generated `%OSPF-5-ADJCHG` messages when they reached `FULL`.

---

## Passive Interfaces Need to Be Understood Carefully

A passive OSPF interface can still advertise its connected network, but it does not send OSPF Hello packets.

This makes passive interfaces useful on LAN-facing interfaces but problematic when applied accidentally to router-to-router links.

---

## FULL Does Not Mean Everything Is Correct

Restoring both OSPF neighbour relationships does not necessarily complete the troubleshooting process.

The routing table must still be checked to confirm that the required networks are being advertised.

The missing Branch LAN network statement demonstrates that:

```text
OSPF adjacency formation
```

and:

```text
OSPF route advertisement
```

are related but separate troubleshooting stages.

---

## Verification Commands Work Best Together

Useful commands in this lab included:

```text
show ip interface brief
show ip ospf neighbor
show ip ospf interface
show ip route ospf
show ip protocols
show running-config | section router ospf
ping
```

Each answers a different troubleshooting question.

---

# Key Learnings

- Designing a troubleshooting lab requires a different thought process from solving one.
- A useful fault should produce realistic symptoms and meaningful diagnostic clues.
- Establishing a known-good configuration before introducing deliberate faults is essential.
- Directly connected devices should be tested before troubleshooting a routing protocol.
- An `up/up` interface does not guarantee successful dynamic routing.
- OSPF neighbours must agree on important parameters such as their area.
- Passive interfaces suppress OSPF Hello packets and therefore prevent neighbour formation.
- A router can have FULL OSPF neighbours while still missing required routes.
- Neighbour formation and route advertisement should be verified separately.
- IOS logging messages can be extremely useful during troubleshooting.
- Routing tables should always be checked rather than assuming adjacency automatically means successful routing.
- Designing the exercise helped reinforce the relationship between OSPF adjacency formation, route advertisement and end-to-end connectivity.

---

# What I Learnt From Designing the Lab

This exercise turned out to be useful in a different way from completing an existing lab.

When solving somebody else's troubleshooting exercise, the objective is to identify what is wrong.

When designing one, I had to think about:

- What should the learner initially see?
- What should still work?
- What should fail?
- Which commands should expose each problem?
- Should one fault hide another?
- At what point should the symptoms change?
- How difficult should the lab be without becoming artificial?
- What constitutes proof that the learner has genuinely fixed the network?

The three final faults were selected because they create a progression rather than simply being independent configuration mistakes.

The learner first deals with neighbour formation, then a second neighbour problem, and finally a route-advertisement problem after the adjacencies appear healthy.

Creating that progression helped reinforce my own understanding of OSPF.

It required thinking not only about which commands configure OSPF, but about how OSPF behaves when particular parts of the configuration are wrong.

---

# Improvements for Next Time

Future versions could increase the difficulty by:

- Removing the statement that exactly three faults exist
- Adding additional routers
- Using multiple OSPF areas
- Introducing Hello/dead timer mismatches
- Introducing incorrect wildcard masks
- Adding VLANs and inter-VLAN routing
- Adding DHCP relay
- Introducing an ACL after routing is restored
- Adding redundant network paths
- Providing optional progressive hints

For this version, the lab was intentionally kept at CCNA level.

The aim was to reinforce core OSPF troubleshooting rather than introduce unnecessary complexity.

---

# Final Result

The completed PingMyNetwork Sandbox exercise contains:

- Three Cisco routers
- Two end devices
- Two `/30` routed transit networks
- Two `/24` user LANs
- Single-area OSPF
- Manually configured router IDs
- Passive LAN-facing OSPF interfaces
- Three deliberately introduced OSPF faults
- Complete learner-facing addressing information
- Clear task instructions
- A defined success condition

The lab begins with:

- Operational physical interfaces
- Correct IPv4 addressing
- No useful OSPF neighbour relationships
- No end-to-end connectivity

The learner must progressively restore:

1. The R1-HQ to R2-WAN OSPF adjacency
2. The R2-WAN to R3-Branch OSPF adjacency
3. Advertisement of the Branch LAN

Successful completion produces two FULL OSPF neighbour relationships, correct OSPF routes and bidirectional connectivity between:

```text
PC-HQ
192.168.10.10
```

and:

```text
PC-Branch
192.168.30.10
```

---

# Raw CLI Evidence

Full captured CLI evidence for both the broken and corrected network states is available here:

[`evidence/raw-cli-output.md`](evidence/raw-cli-output.md)

---

# Project Context

This lab was created as part of my continued CCNA study and participation in the PingMyNetwork Sandbox Challenge.

One of the areas where PingMyNetwork has particularly helped my learning has been OSPF.

Working through practical labs and troubleshooting scenarios has helped turn concepts that I previously understood mainly in theory into something I am becoming increasingly comfortable investigating from the CLI.

Creating this lab represented another step in that process.

Instead of being given a broken OSPF network and trying to determine what somebody else had changed, I had to:

- Create the topology
- Build the working network
- Verify the intended behaviour
- Decide which failures would provide useful troubleshooting practice
- Introduce those faults deliberately
- Confirm that the resulting symptoms behaved as intended
- Solve the faults again
- Verify full recovery

That made designing the exercise a learning experience in its own right.

It also reinforced something I am increasingly finding throughout my networking studies: understanding the configuration commands is only part of the process.

The more useful skill is understanding what the network should be doing, knowing how to verify whether it is actually doing it, and then using the available evidence to work methodically towards the cause when it is not.