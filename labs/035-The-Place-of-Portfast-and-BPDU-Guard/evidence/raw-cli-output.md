# Lab 035 - Raw CLI Output

```bash
Connecting to console for Bunker-SW1
Connected to CML terminalserver.

Bunker-SW1>en
Bunker-SW1#show spanning-tree summary
Switch is in rapid-pvst mode
Root bridge for: VLAN0001, VLAN0010
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
VLAN0001                     0         0        0          3          3
VLAN0010                     0         0        0          3          3
---------------------- -------- --------- -------- ---------- ----------
2 vlans                      0         0        0          6          6
Bunker-SW1#
Bunker-SW1#
Bunker-SW1#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0010 is designated forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 32778, address aabb.cc00.0400
   Designated bridge has priority 32778, address aabb.cc00.0400
   Designated port id is 128.4, designated path cost 0
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 32, received 0
Bunker-SW1#
Bunker-SW1#
Bunker-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Bunker-SW1(config)#interface ethernet0/3
Bunker-SW1(config-if)#shut
Bunker-SW1(config-if)#no shut
Bunker-SW1(config-if)#end
Bunker-SW1#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0010 is designated blocking 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 32778, address aabb.cc00.0400
   Designated bridge has priority 32778, address aabb.cc00.0400
   Designated port id is 128.4, designated path cost 0
   Timers: message age 0, forward delay 9, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   BPDU: sent 4, received 0
Bunker-SW1#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0010 is designated learning 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 32778, address aabb.cc00.0400
   Designated bridge has priority 32778, address aabb.cc00.0400
   Designated port id is 128.4, designated path cost 0
   Timers: message age 0, forward delay 12, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   BPDU: sent 10, received 0
Bunker-SW1#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0010 is designated learning 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 32778, address aabb.cc00.0400
   Designated bridge has priority 32778, address aabb.cc00.0400
   Designated port id is 128.4, designated path cost 0
   Timers: message age 0, forward delay 6, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   BPDU: sent 13, received 0
Bunker-SW1#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0010 is designated learning 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 32778, address aabb.cc00.0400
   Designated bridge has priority 32778, address aabb.cc00.0400
   Designated port id is 128.4, designated path cost 0
   Timers: message age 0, forward delay 2, hold 0
   Number of transitions to forwarding state: 0
   Link type is point-to-point by default
   BPDU: sent 15, received 0
Bunker-SW1#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0010 is designated forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 32778, address aabb.cc00.0400
   Designated bridge has priority 32778, address aabb.cc00.0400
   Designated port id is 128.4, designated path cost 0
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   Link type is point-to-point by default
   BPDU: sent 19, received 0
Bunker-SW1#


Bunker-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Bunker-SW1(config)#interface ethernet0/3
Bunker-SW1(config-if)#
[connection closed]

[reconnecting…]
Connecting to console for Bunker-SW1

Bunker-SW1(config-if)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet0/3 but will only
 have effect when the interface is in a non-trunking mode.
Bunker-SW1(config-if)#exit
Bunker-SW1(config)#interface ethernet1/0 
Bunker-SW1(config-if)#spanning-tree portfast
%Warning: portfast should only be enabled on ports connected to a single
 host. Connecting hubs, concentrators, switches, bridges, etc... to this
 interface  when portfast is enabled, can cause temporary bridging loops.
 Use with CAUTION

%Portfast has been configured on Ethernet1/0 but will only
 have effect when the interface is in a non-trunking mode.
Bunker-SW1(config-if)#exit                  
Bunker-SW1(config)#interface ethernet0/3 
Bunker-SW1(config-if)#shut 
Bunker-SW1(config-if)#no shut
Bunker-SW1(config-if)#end
Bunker-SW1#show spanning-tree interface ethernet0/3 detail
 Port 4 (Ethernet0/3) of VLAN0010 is designated forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.4.
   Designated root has priority 32778, address aabb.cc00.0400
   Designated bridge has priority 32778, address aabb.cc00.0400
   Designated port id is 128.4, designated path cost 0
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   The port is in the portfast mode
   Link type is point-to-point by default
   BPDU: sent 5, received 0
Bunker-SW1#show spanning-tree interface ethernet1/0 detail
 Port 5 (Ethernet1/0) of VLAN0010 is designated forwarding 
   Port path cost 100, Port priority 128, Port Identifier 128.5.
   Designated root has priority 32778, address aabb.cc00.0400
   Designated bridge has priority 32778, address aabb.cc00.0400
   Designated port id is 128.5, designated path cost 0
   Timers: message age 0, forward delay 0, hold 0
   Number of transitions to forwarding state: 1
   The port is in the portfast mode
   Link type is point-to-point by default
   BPDU: sent 230, received 5
Bunker-SW1#


Bunker-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Bunker-SW1(config)#spanning-tree portfast bpduguard default
Bunker-SW1(config)#end

Connecting to console for Rogue-SW
Connected to CML terminalserver.

Rogue-SW>en
Rogue-SW#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Rogue-SW(config)#int
Rogue-SW(config)#interface eth
Rogue-SW(config)#interface ethernet0/0
Rogue-SW(config-if)#shut
Rogue-SW(config-if)#no shut
Rogue-SW(config-if)#end
Rogue-SW#


Bunker-SW1#
Bunker-SW1#show interfaces status | include err-disabled|et1/0|Port
Port         Name               Status       Vlan       Duplex  Speed Type
Et1/0        Access to Rogue-SW err-disabled 10           full   auto 10/100/1000BaseTX
Bunker-SW1#show spanning-tree interface ethernet1/0 detail
no spanning tree info available for Ethernet1/0 

Bunker-SW1#show logging | include BPDU|BPDUGUARD|err
Syslog logging: enabled (0 messages dropped, 2 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)
*Jul  1 19:28:18.899: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Jul  1 19:37:33.456: %SPANTREE-2-BLOCK_BPDUGUARD: Received BPDU from bridge aabb.cc00.0600 on port Ethernet1/0 with BPDU Guard enabled. Disabling port.
*Jul  1 19:37:33.456: %PM-4-ERR_DISABLE: bpduguard error detected on Et1/0, putting Et1/0 in err-disable state
Bunker-SW1#


Rogue-SW#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Rogue-SW(config)#int
Rogue-SW(config)#interface eth
Rogue-SW(config)#interface ethernet0/0
Rogue-SW(config-if)#shutdown
Rogue-SW(config-if)#end
Rogue-SW#


Bunker-SW1#
Bunker-SW1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Bunker-SW1(config)#int
Bunker-SW1(config)#interface eth
Bunker-SW1(config)#interface ethernet1/0
Bunker-SW1(config-if)#shut
Bunker-SW1(config-if)#no shut
Bunker-SW1(config-if)#exit
Bunker-SW1(config)#end
Bunker-SW1#show interfaces status | include et1/0|Port
Port         Name               Status       Vlan       Duplex  Speed Type
Bunker-SW1#show interfaces status | include Et1/0|Port
Port         Name               Status       Vlan       Duplex  Speed Type
Et1/0        Access to Rogue-SW connected    10           full   auto 10/100/1000BaseTX
Bunker-SW1#
```
