# Lab 033 - Raw CLI Output

```bash
Connecting to console for Fallout-SW1

Fallout-SW1>en
Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#vlan 10
Fallout-SW1(config-vlan)#name Shelter-Operations
Fallout-SW1(config-vlan)#vlan 20
Fallout-SW1(config-vlan)#name Shelter-logistics
Fallout-SW1(config-vlan)#vlan 30
Fallout-SW1(config-vlan)#name Shelter-Medical
Fallout-SW1(config-vlan)#vlan 40
Fallout-SW1(config-vlan)#name Shelter-Comms
Fallout-SW1(config-vlan)#end
Fallout-SW1#show vlan brief | include 10  |20  |30  |40
10   Shelter-Operations               active    
20   Shelter-logistics                active    
30   Shelter-Medical                  active    
40   Shelter-Comms                    active    
Fallout-SW1#



Connecting to console for Fallout-SW2

Fallout-SW2>en
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#valn 10
                     ^
% Invalid input detected at '^' marker.

Fallout-SW2(config)#name Shelter-Operations
                         ^
% Invalid input detected at '^' marker.

Fallout-SW2(config)#vlan 20
Fallout-SW2(config-vlan)#name Shelter-Logistics
Fallout-SW2(config-vlan)#vlan 30
Fallout-SW2(config-vlan)#name Shelter-Medical
Fallout-SW2(config-vlan)#vlan 40
Fallout-SW2(config-vlan)#name Shelter-Comms
Fallout-SW2(config-vlan)#end
Fallout-SW2#show vlan brief | include 10  |20  |30  |40
20   Shelter-Logistics                active    
30   Shelter-Medical                  active    
40   Shelter-Comms                    active    
Fallout-SW2#vlan 10
% Bad IP address or host name% Unknown command or computer name, or unable to find computer address
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#vlan 10
Fallout-SW2(config-vlan)#name Shelter-Operations
Fallout-SW2(config-vlan)#end
Fallout-SW2#show vlan brief | include 10  |20  |30  |40
10   Shelter-Operations               active    
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
Fallout-SW6(config-vlan)#name Shelter-Medical
Fallout-SW6(config-vlan)#vlan 40
Fallout-SW6(config-vlan)#name Shelter-Comms
Fallout-SW6(config-vlan)#end
Fallout-SW6#show vlan brief | include 10  |20  |30  |40
10   Shelter-Operations               active    
20   Shelter-Logistics                active    
30   Shelter-Medical                  active    
40   Shelter-Comms                    active    
Fallout-SW6#


Fallout-SW2#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    28682
             Address     aabb.cc00.0300
             Cost        100
             Port        3 (Ethernet0/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Altn BLK 100       128.2    P2p 
Et0/2               Root FWD 100       128.3    P2p 


Fallout-SW2#show spanning-tree vlan 20

VLAN0020
  Spanning tree enabled protocol rstp
  Root ID    Priority    28692
             Address     aabb.cc00.0300
             Cost        100
             Port        3 (Ethernet0/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32788  (priority 32768 sys-id-ext 20)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Altn BLK 100       128.2    P2p 
Et0/2               Root FWD 100       128.3    P2p 


Fallout-SW2#show spanning-tree vlan 30

VLAN0030
  Spanning tree enabled protocol rstp
  Root ID    Priority    28702
             Address     aabb.cc00.0300
             Cost        100
             Port        3 (Ethernet0/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32798  (priority 32768 sys-id-ext 30)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Altn BLK 100       128.2    P2p 
Et0/2               Root FWD 100       128.3    P2p 


Fallout-SW2#show spanning-tree vlan 40

VLAN0040
  Spanning tree enabled protocol rstp
  Root ID    Priority    28712
             Address     aabb.cc00.0300
             Cost        100
             Port        3 (Ethernet0/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32808  (priority 32768 sys-id-ext 40)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Altn BLK 100       128.2    P2p 
Et0/2               Root FWD 100       128.3    P2p 


Fallout-SW2#show spanning-tree interface ethernet0/1 detail
 Port 2 (Ethernet0/1) of VLAN0010 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 28682, address aabb.cc00.0300
   Designated bridge has priority 32778, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 100
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 9, received 96

 Port 2 (Ethernet0/1) of VLAN0020 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 28692, address aabb.cc00.0300
   Designated bridge has priority 32788, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 9, received 145

 Port 2 (Ethernet0/1) of VLAN0030 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
          
Fallout-SW2#show spanning-tree interface ethernet0/2 detail
 Port 3 (Ethernet0/2) of VLAN0010 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 28682, address aabb.cc00.0300
   Designated bridge has priority 28682, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 30, received 78

 Port 3 (Ethernet0/2) of VLAN0020 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 28692, address aabb.cc00.0300
   Designated bridge has priority 28692, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 0
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 89, received 69

 Port 3 (Ethernet0/2) of VLAN0030 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 28702, address aabb.cc00.0300
   Designated bridge has priority 28702, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 0
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 87, received 63

 Port 3 (Ethernet0/2) of VLAN0040 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 28712, address aabb.cc00.0300
   Designated bridge has priority 28712, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 89, received 57
Fallout-SW2#


Fallout-SW1#enable
Fallout-SW1#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    28682
             Address     aabb.cc00.0300
             Cost        100
             Port        3 (Ethernet0/2)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)
             Address     aabb.cc00.0100
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Root FWD 100       128.3    P2p 


Fallout-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW1(config)#spanning-tree vlan 10,20,30,40 priority 24576
Fallout-SW1(config)#end
Fallout-SW1#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    24586
             Address     aabb.cc00.0100
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    24586  (priority 24576 sys-id-ext 10)
             Address     aabb.cc00.0100
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 


Fallout-SW1#show spanning-tree vlan 20

VLAN0020
  Spanning tree enabled protocol rstp
  Root ID    Priority    24596
             Address     aabb.cc00.0100
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    24596  (priority 24576 sys-id-ext 20)
             Address     aabb.cc00.0100
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Desg FWD 100       128.2    P2p 
Et0/2               Desg FWD 100       128.3    P2p 


Fallout-SW1#


Fallout-SW2#enable
Fallout-SW2#show spanning-tree vlan 10

VLAN0010
  Spanning tree enabled protocol rstp
  Root ID    Priority    24586
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32778  (priority 32768 sys-id-ext 10)
             Address     aabb.cc00.0200
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/1               Root FWD 100       128.2    P2p 
Et0/2               Altn BLK 100       128.3    P2p 


Fallout-SW2#show spanning-tree interface ethernet0/1 detail
 Port 2 (Ethernet0/1) of VLAN0010 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 24586, address aabb.cc00.0100
   Designated bridge has priority 24586, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 12, received 194

 Port 2 (Ethernet0/1) of VLAN0020 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 24596, address aabb.cc00.0100
   Designated bridge has priority 24596, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 0
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 12, received 243

 Port 2 (Ethernet0/1) of VLAN0030 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 24606, address aabb.cc00.0100
   Designated bridge has priority 24606, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 12, received 236

 Port 2 (Ethernet0/1) of VLAN0040 is root forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.2.
   Designated root has priority 24616, address aabb.cc00.0100
   Designated bridge has priority 24616, address aabb.cc00.0100
   Designated port id is 128.2, designated path cost 0
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 2
   Link type is point-to-point by default
   BPDU: sent 12, received 231
Fallout-SW2#show spanning-tree interface ethernet0/2 detail
 Port 3 (Ethernet0/2) of VLAN0010 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24586, address aabb.cc00.0100
   Designated bridge has priority 28682, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 31, received 173

 Port 3 (Ethernet0/2) of VLAN0020 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24596, address aabb.cc00.0100
   Designated bridge has priority 28692, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 90, received 164

 Port 3 (Ethernet0/2) of VLAN0030 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24606, address aabb.cc00.0100
   Designated bridge has priority 28702, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 88, received 158

 Port 3 (Ethernet0/2) of VLAN0040 is alternate blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24616, address aabb.cc00.0100
   Designated bridge has priority 28712, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 90, received 152
Fallout-SW2#


Fallout-SW2#
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#int
Fallout-SW2(config)#interface  eth
Fallout-SW2(config)#interface  ethernet0/2
Fallout-SW2(config-if)#spanning-tree vlan 10 cost 300
Fallout-SW2(config-if)#spanning-tree vlan 20 cost 300
Fallout-SW2(config-if)#spanning-tree vlan 30 cost 300
Fallout-SW2(config-if)#spanning-tree vlan 40 cost 300
Fallout-SW2(config-if)#end
Fallout-SW2#show spanning-tree int
Fallout-SW2#show spanning-tree interface eth
Fallout-SW2#show spanning-tree interface ethernet 0/2 detail
 Port 3 (Ethernet0/2) of VLAN0010 is alternate blocking 
   Port path cost 300, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24586, address aabb.cc00.0100
   Designated bridge has priority 28682, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 31, received 239

 Port 3 (Ethernet0/2) of VLAN0020 is alternate blocking 
   Port path cost 300, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24596, address aabb.cc00.0100
   Designated bridge has priority 28692, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 90, received 230

 Port 3 (Ethernet0/2) of VLAN0030 is alternate blocking 
   Port path cost 300, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24606, address aabb.cc00.0100
   Designated bridge has priority 28702, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 88, received 224

 Port 3 (Ethernet0/2) of VLAN0040 is alternate blocking 
   Port path cost 300, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24616, address aabb.cc00.0100
   Designated bridge has priority 28712, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 90, received 218
Fallout-SW2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Fallout-SW2(config)#int eth
Fallout-SW2(config)#int ethernet0/2
Fallout-SW2(config-if)#shut
Fallout-SW2(config-if)#no shut
Fallout-SW2(config-if)#end 
Fallout-SW2#show spanning-tree interface ethernet 0/2 detail
 Port 3 (Ethernet0/2) of VLAN0010 is alternate blocking 
   Port path cost 300, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24586, address aabb.cc00.0100
   Designated bridge has priority 28682, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 15, forward delay 0, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   BPDU: sent 1, received 4

 Port 3 (Ethernet0/2) of VLAN0020 is alternate blocking 
   Port path cost 300, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24596, address aabb.cc00.0100
   Designated bridge has priority 28692, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   BPDU: sent 1, received 3

 Port 3 (Ethernet0/2) of VLAN0030 is alternate blocking 
   Port path cost 300, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24606, address aabb.cc00.0100
   Designated bridge has priority 28702, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   BPDU: sent 1, received 3

 Port 3 (Ethernet0/2) of VLAN0040 is alternate blocking 
   Port path cost 300, Port priority 128, Port Identifier 128.3.
   Designated root has priority 24616, address aabb.cc00.0100
   Designated bridge has priority 28712, address aabb.cc00.0300
   Designated port id is 128.3, designated path cost 100
   Timers: message age 16, forward delay 0, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   BPDU: sent 1, received 3
Fallout-SW2#
```
