# Lab 034 - Raw CLI Output

```bash
Connecting to console for Fallout-SW1

Fallout-SW1>en
Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#vlan 10
Fallout-SW1(config-vlan)#name Shelter-Operations
Fallout-SW1(config-vlan)#vlan 20
Fallout-SW1(config-vlan)#name Shelter-Logistics
Fallout-SW1(config-vlan)#vlan 30
Fallout-SW1(config-vlan)#name Shelter-Medical
Fallout-SW1(config-vlan)#vlan 40
Fallout-SW1(config-vlan)#name Shelter-Comms
Fallout-SW1(config-vlan)#end
Fallout-SW1#show vlan brief | include 10  |20  |30  |40
10   Shelter-Operations               active    
20   Shelter-Logistics                active    
30   Shelter-Medical                  active    
40   Shelter-Comms                    active    
Fallout-SW1#

Fallout-SW2>en
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#vlan 10
Fallout-SW2(config-vlan)#name Shelter-Operations
Fallout-SW2(config-vlan)#vlan 20
Fallout-SW2(config-vlan)#Shelter-Logistics
                           ^
% Invalid input detected at '^' marker.

Fallout-SW2(config-vlan)#vlan 30
Fallout-SW2(config-vlan)#name Shelter-Medical
Fallout-SW2(config-vlan)#vlan 20 
Fallout-SW2(config-vlan)#name Shelter-Logistics
Fallout-SW2(config-vlan)#vlan 40
Fallout-SW2(config-vlan)#name Shelter-Comms
Fallout-SW2(config-vlan)#end
Fallout-SW2#show vlan brief | include vlan 10  |20  |30  |40
20   Shelter-Logistics                active    
30   Shelter-Medical                  active    
40   Shelter-Comms                    active    
Fallout-SW2#


Connecting to console for Fallout-SW6

Fallout-SW6>en
Fallout-SW6#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW6(config)#vlan 10
Fallout-SW6(config-vlan)#name Shelter-Operations
Fallout-SW6(config-vlan)#vlan 20
Fallout-SW6(config-vlan)#name Shelter-Logistics
Fallout-SW6(config-vlan)#vlan 30
Fallout-SW6(config-vlan)#Shelter-Medical
                           ^
% Invalid input detected at '^' marker.

Fallout-SW6(config-vlan)#name Shelter-Medical
Fallout-SW6(config-vlan)#vlan 40
Fallout-SW6(config-vlan)#name Shelter-Comms
Fallout-SW6(config-vlan)#end
Fallout-SW6#show vlan brief | include vlan 10  |20  |30  |40
20   Shelter-Logistics                active    
30   Shelter-Medical                  active    
40   Shelter-Comms                    active    
Fallout-SW6#

Fallout-SW2#
Fallout-SW2#show spanning-tree summary
Switch is in pvst mode
Root bridge for: VLAN0001
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     0         0        0          4          4
VLAN0010                     1         0        0          1          2
VLAN0020                     1         0        0          1          2
VLAN0030                     1         0        0          1          2
VLAN0040                     1         0        0          1          2
---------------------- -------- --------- -------- ---------- ----------
5 vlans                      4         0        0          8         12
Fallout-SW2#
Fallout-SW2#
Fallout-SW2#show spanning-tree vlan 10                      

VLAN0010
  Spanning tree enabled protocol ieee
  Root ID    Priority    4106
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    36874  (priority 36864 sys-id-ext 10)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 


Fallout-SW2#
Fallout-SW2#
Fallout-SW2#show spanning-tree vlan 20

VLAN0020
  Spanning tree enabled protocol ieee
  Root ID    Priority    4116
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    36884  (priority 36864 sys-id-ext 20)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 


Fallout-SW2#
Fallout-SW2#
Fallout-SW2#show spanning-tree vlan 30

VLAN0030
  Spanning tree enabled protocol ieee
  Root ID    Priority    4126
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    36894  (priority 36864 sys-id-ext 30)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 


Fallout-SW2#
Fallout-SW2#
Fallout-SW2#show spanning-tree vlan 40

VLAN0040
  Spanning tree enabled protocol ieee
  Root ID    Priority    4136
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    36904  (priority 36864 sys-id-ext 40)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 


Fallout-SW1(config)#spanning-tree mode rapid-pvst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW1(config)#end
Fallout-SW1#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: VLAN0001, VLAN0010, VLAN0020, VLAN0030, VLAN0040
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     4         0        0          0          4
VLAN0010                     2         0        0          0          2
VLAN0020                     2         0        0          0          2
VLAN0030                     2         0        0          0          2
VLAN0040                     2         0        0          0          2
---------------------- -------- --------- -------- ---------- ----------
5 vlans                     12         0        0          0         12
Fallout-SW1#
Fallout-SW1#show spanning-tree vlan 10 

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    4106
             Address     aabb.cc00.0100
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    4106   (priority 4096 sys-id-ext 10)
             Address     aabb.cc00.0100
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Desg FWD 100       128.2    P2p Peer(STP) 
Et0/2               Desg FWD 100       128.3    P2p Peer(STP) 


Fallout-SW1#

Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#spanning-tree mode rapid pvst
                                             ^
% Invalid input detected at '^' marker.

Fallout-SW2(config)#spanning-tree mode rapid-pvst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW2(config)#end
Fallout-SW2#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: VLAN0001
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     4         0        0          0          4
VLAN0010                     1         0        0          1          2
VLAN0020                     1         0        0          1          2
VLAN0030                     1         0        0          1          2
VLAN0040                     1         0        0          1          2
---------------------- -------- --------- -------- ---------- ----------
5 vlans                      8         0        0          4         12
Fallout-SW2#
Fallout-SW2#
Fallout-SW2#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    4106
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    36874  (priority 36864 sys-id-ext 10)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p Peer(STP) 


Fallout-SW2#


Fallout-SW6#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW6(config)#spanning-tree summary
                                   ^
% Invalid input detected at '^' marker.

Fallout-SW6(config)#show spanning-tree summary
                      ^
% Invalid input detected at '^' marker.

Fallout-SW6(config)#end
Fallout-SW6#show spanning-tree summary                      
Switch is in pvst mode
Root bridge for: VLAN0001
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     0         0        0          4          4
VLAN0010                     0         0        0          2          2
VLAN0020                     0         0        0          2          2
VLAN0030                     0         0        0          2          2
VLAN0040                     0         0        0          2          2
---------------------- -------- --------- -------- ---------- ----------
5 vlans                      0         0        0         12         12
Fallout-SW6##
Fallout-SW6#
Fallout-SW6#
Fallout-SW6#
Fallout-SW6#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW6(config)#spanning-tree mode rapid-pvst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW6(config)#end
Fallout-SW6#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: VLAN0001
EtherChannel misconfig guard            is enabled
Extended system ID                      is enabled
Portfast Default                        is disabled
PortFast BPDU Guard Default            is disabled
Portfast BPDU Filter Default           is disabled
Loopguard Default                      is disabled
UplinkFast                              is disabled
BackboneFast                            is disabled
Configured Pathcost method used is short

Name                   Blocking Listening Learning Forwarding STP Active
---------------------- -------- --------- -------- ---------- ----------
VLAN0001                     4         0        0          0          4
VLAN0010                     1         0        0          1          2
VLAN0020                     1         0        0          1          2
VLAN0030                     1         0        0          1          2
VLAN0040                     1         0        0          1          2
---------------------- -------- --------- -------- ---------- ----------
5 vlans                      8         0        0          4         12
Fallout-SW6#
Fallout-SW6#
Fallout-SW6#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    4106
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    28682  (priority 28672 sys-id-ext 10)
             Address     aabb.cc00.0300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Desg LRN 100       128.3    P2p 


Fallout-SW6#


Fallout-SW2#
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#interface ethernet0/1
Fallout-SW2(config-if)#shutdown
Fallout-SW2(config-if)#end
Fallout-SW2#show spanning-tree interface ethernet0/2 detail
 Port 3 (Ethernet0/2) of VLAN0010 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 4106, address aabb.cc00.0100
   Designated bridge has priority 28682, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 8, received 127

 Port 3 (Ethernet0/2) of VLAN0020 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 4116, address aabb.cc00.0100
   Designated bridge has priority 28692, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 8, received 127

 Port 3 (Ethernet0/2) of VLAN0030 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 4126, address aabb.cc00.0100
   Designated bridge has priority 28702, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 8, received 127

 Port 3 (Ethernet0/2) of VLAN0040 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 4136, address aabb.cc00.0100
   Designated bridge has priority 28712, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 8, received 127
Fallout-SW2#



Fallout-SW2#
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#int
Fallout-SW2(config)#interface eth
Fallout-SW2(config)#interface ethernet0/1
Fallout-SW2(config-if)#no shutdown
Fallout-SW2(config-if)#end
Fallout-SW2#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    4106
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    36874  (priority 36864 sys-id-ext 10)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 


Fallout-SW2#show spanning-tree interface eth
Fallout-SW2#show spanning-tree interface ethernet 0/1 detail
 Port 2 (Ethernet0/1) of VLAN0010 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 4106, address aabb.cc00.0100
   Designated bridge has priority 4106, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 5, received 24

 Port 2 (Ethernet0/1) of VLAN0020 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 4116, address aabb.cc00.0100
   Designated bridge has priority 4116, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 5, received 24

 Port 2 (Ethernet0/1) of VLAN0030 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 4126, address aabb.cc00.0100
   Designated bridge has priority 4126, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 5, received 24

 Port 2 (Ethernet0/1) of VLAN0040 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 4136, address aabb.cc00.0100
   Designated bridge has priority 4136, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 5, received 24
Fallout-SW2#
Fallout-SW2#show spanning-tree interface ethernet 0/2 detail
 Port 3 (Ethernet0/2) of VLAN0010 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 4106, address aabb.cc00.0100
   Designated bridge has priority 28682, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 8, received 189

 Port 3 (Ethernet0/2) of VLAN0020 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 4116, address aabb.cc00.0100
   Designated bridge has priority 28692, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 8, received 189

 Port 3 (Ethernet0/2) of VLAN0030 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 4126, address aabb.cc00.0100
   Designated bridge has priority 28702, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 8, received 189

 Port 3 (Ethernet0/2) of VLAN0040 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 4136, address aabb.cc00.0100
   Designated bridge has priority 28712, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 8, received 189
Fallout-SW2#


Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#spanning-tree mode mst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW1(config)#spanning-tree mst configuration
Fallout-SW1(config-mst)#name RYSEN-CORE
Fallout-SW1(config-mst)#revision 5
Fallout-SW1(config-mst)#instance 1 vlan 10,20
Fallout-SW1(config-mst)#instance 1 vlan 30,40
Fallout-SW1(config-mst)#exit
Fallout-SW1(config)#end
Fallout-SW1#show spanning-tree mst configuration 
Name      [RYSEN-CORE]
Revision  5     Instances configured 2

Instance  Vlans mapped
--------  ---------------------------------------------------------------------
0         1-9,11-19,21-29,31-39,41-4094
1         10,20,30,40
-------------------------------------------------------------------------------
Fallout-SW1#show spanning-tree mst

##### MST0    vlans mapped:   1-9,11-19,21-29,31-39,41-4094
Bridge        address aabb.cc00.0100  priority      32768 (32768 sysid 0)
Root          this switch for the CIST
Operational   hello time 2 , forward delay 15, max age 20, txholdcount 6 
Configured    hello time 2 , forward delay 15, max age 20, max hops    20

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Desg BKN*2000000   128.2    P2p Bound(PVST) *PVST_Inc 
Et0/2                            Desg BKN*2000000   128.3    P2p Bound(PVST) *PVST_Inc 
Et1/0                            Desg FWD 2000000   128.5    P2p 
Et1/1                            Desg FWD 2000000   128.6    P2p 
Et1/2                            Desg FWD 2000000   128.7    P2p 
Et1/3                            Desg FWD 2000000   128.8    P2p 

##### MST1    vlans mapped:   10,20,30,40
Bridge        address aabb.cc00.0100  priority      32769 (32768 sysid 1)
Root          this switch for MST1

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Desg BKN*2000000   128.2    P2p Bound(PVST) *PVST_Inc 
Et0/2                            Desg BKN*2000000   128.3    P2p Bound(PVST) *PVST_Inc 

Fallout-SW1#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          none
Et0/2          none
Fallout-SW1#


Fallout-SW2#
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#spanning-tree mode mst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW2(config)#spanning-tree mst configuration
Fallout-SW2(config-mst)#name RYSEN-CORE
Fallout-SW2(config-mst)#revision 5
Fallout-SW2(config-mst)#instance 1 vlan 10,20
Fallout-SW2(config-mst)#instance 1 vlan 30,40
Fallout-SW2(config-mst)#exit
Fallout-SW2(config)#end
Fallout-SW2#show spanning-tree mst configuration
Name      [RYSEN-CORE]
Revision  5     Instances configured 2

Instance  Vlans mapped
--------  ---------------------------------------------------------------------
0         1-9,11-19,21-29,31-39,41-4094
1         10,20,30,40
-------------------------------------------------------------------------------
Fallout-SW2#show spanning-tree mst

##### MST0    vlans mapped:   1-9,11-19,21-29,31-39,41-4094
Bridge        address aabb.cc00.0200  priority      32768 (32768 sysid 0)
Root          address aabb.cc00.0100  priority      32768 (32768 sysid 0)
              port    Et0/1           path cost     0        
Regional Root address aabb.cc00.0100  priority      32768 (32768 sysid 0)
                                      internal cost 2000000   rem hops 19
Operational   hello time 2 , forward delay 15, max age 20, txholdcount 6 
Configured    hello time 2 , forward delay 15, max age 20, max hops    20

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Root FWD 2000000   128.2    P2p 
Et0/2                            Desg BKN*2000000   128.3    P2p Bound(PVST) *PVST_Inc 
Et1/0                            Desg LRN 2000000   128.5    P2p 
Et1/1                            Desg LRN 2000000   128.6    P2p 
Et1/2                            Desg LRN 2000000   128.7    P2p 
Et1/3                            Desg LRN 2000000   128.8    P2p 

##### MST1    vlans mapped:   10,20,30,40
Bridge        address aabb.cc00.0200  priority      32769 (32768 sysid 1)
Root          address aabb.cc00.0100  priority      32769 (32768 sysid 1)
              port    Et0/1           cost          2000000   rem hops 19

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Root FWD 2000000   128.2    P2p 
Et0/2                            Desg BKN*2000000   128.3    P2p Bound(PVST) *PVST_Inc 

Fallout-SW2#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40
Et0/2          none
Fallout-SW2#


Fallout-SW6#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW6(config)#spanning-tree mode mst
Warning: Changing STP mode can disrupt the traffic and make system unstable
Recommend to change STP mode only during maintenance window
Fallout-SW6(config)#spanning-tree mst configuration
Fallout-SW6(config-mst)#name RYSEN-CORE
Fallout-SW6(config-mst)#revision 5
Fallout-SW6(config-mst)#instance 1 vlan 10,20
Fallout-SW6(config-mst)#instance 2 vlan 30,40
Fallout-SW6(config-mst)#exit
Fallout-SW6(config)#end
Fallout-SW6#show spanning-tree mst con
Fallout-SW6#show spanning-tree mst configuration 
Name      [RYSEN-CORE]
Revision  5     Instances configured 3

Instance  Vlans mapped
--------  ---------------------------------------------------------------------
0         1-9,11-19,21-29,31-39,41-4094
1         10,20
2         30,40
-------------------------------------------------------------------------------
Fallout-SW6#show spanning-tree mst

##### MST0    vlans mapped:   1-9,11-19,21-29,31-39,41-4094
Bridge        address aabb.cc00.0300  priority      32768 (32768 sysid 0)
Root          address aabb.cc00.0100  priority      32768 (32768 sysid 0)
              port    Et0/1           path cost     2000000  
Regional Root this switch
Operational   hello time 2 , forward delay 15, max age 20, txholdcount 6 
Configured    hello time 2 , forward delay 15, max age 20, max hops    20

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Root FWD 2000000   128.2    P2p Bound(RSTP) 
Et0/2                            Altn BLK 2000000   128.3    P2p Bound(RSTP) 
Et1/0                            Desg LRN 2000000   128.5    P2p 
Et1/1                            Desg LRN 2000000   128.6    P2p 
Et1/2                            Desg LRN 2000000   128.7    P2p 
Et1/3                            Desg LRN 2000000   128.8    P2p 

##### MST1    vlans mapped:   10,20
Bridge        address aabb.cc00.0300  priority      32769 (32768 sysid 1)
Root          this switch for MST1

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Mstr FWD 2000000   128.2    P2p Bound(RSTP) 
Et0/2                            Altn BLK 2000000   128.3    P2p Bound(RSTP) 

##### MST2    vlans mapped:   30,40
Bridge        address aabb.cc00.0300  priority      32770 (32768 sysid 2)
Root          this switch for MST2

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Mstr FWD 2000000   128.2    P2p Bound(RSTP) 
Et0/2                            Altn BLK 2000000   128.3    P2p Bound(RSTP) 

Fallout-SW6#show interface trunk | begin Port
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40
Et0/2          none
Fallout-SW6#


Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#spanning-tree mst con
Fallout-SW2(config)#spanning-tree mst configuration 
Fallout-SW2(config-mst)#instance 1 vlan 10,20 
Fallout-SW2(config-mst)#instance 2 vlan 30,40 
Fallout-SW2(config-mst)#end
Fallout-SW2#show spanning-tree mst configuration
Name      [RYSEN-CORE]
Revision  5     Instances configured 3

Instance  Vlans mapped
--------  ---------------------------------------------------------------------
0         1-9,11-19,21-29,31-39,41-4094
1         10,20
2         30,40
-------------------------------------------------------------------------------
Fallout-SW2#show spanning-tree mst              

##### MST0    vlans mapped:   1-9,11-19,21-29,31-39,41-4094
Bridge        address aabb.cc00.0200  priority      32768 (32768 sysid 0)
Root          address aabb.cc00.0100  priority      32768 (32768 sysid 0)
              port    Et0/1           path cost     2000000  
Regional Root this switch
Operational   hello time 2 , forward delay 15, max age 20, txholdcount 6 
Configured    hello time 2 , forward delay 15, max age 20, max hops    20

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Root FWD 2000000   128.2    P2p Bound(RSTP) 
Et0/2                            Desg FWD 2000000   128.3    P2p 
Et1/0                            Desg LRN 2000000   128.5    P2p 
Et1/1                            Desg LRN 2000000   128.6    P2p 
Et1/2                            Desg LRN 2000000   128.7    P2p 
Et1/3                            Desg LRN 2000000   128.8    P2p 

##### MST1    vlans mapped:   10,20
Bridge        address aabb.cc00.0200  priority      32769 (32768 sysid 1)
Root          this switch for MST1

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Mstr FWD 2000000   128.2    P2p Bound(RSTP) 
Et0/2                            Desg FWD 2000000   128.3    P2p 

##### MST2    vlans mapped:   30,40
Bridge        address aabb.cc00.0200  priority      32770 (32768 sysid 2)
Root          this switch for MST2

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Mstr FWD 2000000   128.2    P2p Bound(RSTP) 
Et0/2                            Desg FWD 2000000   128.3    P2p 

Fallout-SW2#show interface trunk | begin Port   
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40
Et0/2          10,20,30,40
Fallout-SW2#


Fallout-SW1#
Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)# spanning-tree mst conf
Fallout-SW1(config)# spanning-tree mst configuration 
Fallout-SW1(config-mst)#instance 1 vlan 10,20
Fallout-SW1(config-mst)#instance 2 vlan 30,40
Fallout-SW1(config-mst)#end
Fallout-SW1#show spanning-tree mst configuration
Name      [RYSEN-CORE]
Revision  5     Instances configured 3

Instance  Vlans mapped
--------  ---------------------------------------------------------------------
0         1-9,11-19,21-29,31-39,41-4094
1         10,20
2         30,40
-------------------------------------------------------------------------------
Fallout-SW1#show spanning-tree mst              

##### MST0    vlans mapped:   1-9,11-19,21-29,31-39,41-4094
Bridge        address aabb.cc00.0100  priority      32768 (32768 sysid 0)
Root          this switch for the CIST
Operational   hello time 2 , forward delay 15, max age 20, txholdcount 6 
Configured    hello time 2 , forward delay 15, max age 20, max hops    20

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Desg FWD 2000000   128.2    P2p 
Et0/2                            Desg FWD 2000000   128.3    P2p 
Et1/0                            Desg BLK 2000000   128.5    P2p 
Et1/1                            Desg BLK 2000000   128.6    P2p 
Et1/2                            Desg BLK 2000000   128.7    P2p 
Et1/3                            Desg BLK 2000000   128.8    P2p 

##### MST1    vlans mapped:   10,20
Bridge        address aabb.cc00.0100  priority      32769 (32768 sysid 1)
Root          this switch for MST1

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Desg FWD 2000000   128.2    P2p 
Et0/2                            Desg FWD 2000000   128.3    P2p 

##### MST2    vlans mapped:   30,40
Bridge        address aabb.cc00.0100  priority      32770 (32768 sysid 2)
Root          this switch for MST2

Interface                        Role Sts Cost      Prio.Nbr Type
----------------                 ---- --- --------- -------- --------------------------------
Et0/1                            Desg FWD 2000000   128.2    P2p 
Et0/2                            Desg FWD 2000000   128.3    P2p 

Fallout-SW1#show interface trunk | begin Port   
Port           Mode             Encapsulation  Status        Native vlan  
Et0/1          on               802.1q         trunking      1
Et0/2          on               802.1q         trunking      1

Port           Vlans allowed on trunk
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans allowed and active in management domain
Et0/1          10,20,30,40
Et0/2          10,20,30,40

Port           Vlans in spanning tree forwarding state and not pruned
Et0/1          10,20,30,40
Et0/2          10,20,30,40
Fallout-SW1#
```
