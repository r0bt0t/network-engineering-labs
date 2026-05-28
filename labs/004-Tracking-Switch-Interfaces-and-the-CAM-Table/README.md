# Lab 004 - Tracking Switch Interfaces and the CAM Table

<table>
<tr>
<td colspan="2" valign="top">

## Objective
- Distinguish interface naming conventions and roles using the switch’s summary views.
- Evaluate duplex and speed negotiation on active ports to flag connectivity issues early.
- Correlate interface descriptions and CAM table entries to pinpoint where devices live.

</td>
</tr>

<tr>
<td colspan="2" valign="top">
<img src="Images/Topology2.png">
</td>

<td valign="top">
<img src="Images/networking_image_02.png">
</td>

</tr>
</table>

---

## Devices Used
- CoreSwitch
- Switch 6
---

## Configuration Steps

### Main configuration

```bash
Switch6#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
Ethernet0/0            unassigned      YES unset  up                    up      
Ethernet0/1            unassigned      YES unset  up                    up      
Ethernet0/2            unassigned      YES unset  up                    up      
Ethernet0/3            unassigned      YES unset  administratively down down    
Switch6#show interfaces description
Interface                      Status         Protocol Description
Et0/0                          up             up       Uplink-to-CoreSwitch
Et0/1                          up             up       AccessPoint1
Et0/2                          up             up       SensorPod-A
Et0/3                          admin down     down     Reserved-StackLink
Switch6#show interface status

Port         Name               Status       Vlan       Duplex  Speed Type
Et0/0        Uplink-to-CoreSwit connected    trunk        full   auto 10/100/1000BaseTX
Et0/1        AccessPoint1       connected    10           full   auto 10/100/1000BaseTX
Et0/2        SensorPod-A        connected    20           full   auto 10/100/1000BaseTX
Et0/3        Reserved-StackLink disabled     1            full   auto 10/100/1000BaseTX
Switch6#show mac address table
                         ^
% Invalid input detected at '^' marker.

Switch6#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.0058.297b    DYNAMIC     Et0/1
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
  20    5254.0036.d8d6    DYNAMIC     Et0/2
  20    7c7c.b2b2.2020    STATIC      Et0/2 
  99    40a6.b77d.aa01    STATIC      Et0/0 
  99    40a6.b77d.bb02    STATIC      Et0/0 
Total Mac Addresses for this criterion: 6
Switch6#show mac address-table|5a5a.1c1c.0d0d
                              ^
% Invalid input detected at '^' marker.

Switch6#show mac address-table | 5a5a.1c1c.0d0d
                                 ^
% Invalid input detected at '^' marker.

Switch6#show mac address-table | 5a5a.1c1c.0d0d
                                 ^
% Invalid input detected at '^' marker.

Switch6#show mac address-table address 5a5a.1c1c.0d0d 
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5a5a.1c1c.0d0d    STATIC      Et0/1 
Total Mac Addresses for this criterion: 1
```

### Explanation
- From the Switch6 console, confirm you can reach the elevated prompt, then pull the quick status sheet that lists every interface so you can see which Ethernet ports are live versus dormant.
    - Climb from the user prompt to the privileged prompt on Switch6.
    - Display the concise interface roster that shows each port name, IP assignment, and operational state.
    - Note the interface numbering (Ethernet0/0 through Ethernet0/3) so you can match ports to the deployment diagram.

- Still at the privileged prompt, call up the status view that reveals duplex, speed, and VLAN information so you can verify everything is running full tilt and auto-negotiated correctly.
    - Stay on Switch6# and present the interface status snapshot that includes VLAN, duplex, and speed columns.
    - Focus on Et0/0 for the core uplink, Et0/1 for AccessPoint1, and Et0/2 for SensorPod-A; confirm each reports full duplex and auto-negotiated speed.
    - Record any port that drops to half duplex or unexpectedly locks to a low speed so you can escalate it for follow-up.

- Use the switch’s descriptions to tie interfaces back to their cable endpoints so you can avoid tracing wires in the dark.
    - While still on Switch6#, display the view that lists each interface alongside its description text.
    - Read the descriptions so you can map Et0/0 to the core uplink, Et0/1 to AccessPoint1, and Et0/2 to SensorPod-A without tracing cables.
    - Confirm every described interface is currently in the state you expect based on the topology.

- Interrogate the MAC address table to locate the coffee shop endpoints and recognize when a port is actually another switch in disguise.
    - From Switch6#, display the learned MAC addresses so you can see which ports are populated.
    - Spot the uplink port by finding the interface that lists multiple remote MAC addresses (the CoreSwitch itself plus OpsServer riding behind it).
    -Filter the table for the access point’s MAC address (5a5a.1c1c.0d0d)—it’s preloaded in the switch so you can immediately confirm the expected port.

---

## Verification

### Completion Check

- The interface summary on Switch6 confirms the state of Ethernet0/0 through Ethernet0/3.
- The status report shows full-duplex, healthy links for AccessPoint1, SensorPod-A, and the core uplink, or flags any negotiation issues you noted.
- The MAC address table review pinpoints where each device connects and highlights which ports backhaul to the core.

---

## Troubleshooting

### Issue 1
What went wrong?
- Attempted to filter table using incorrect syntax

### Diagnosis
How you found the problem.
- Filtering failed on request

### Fix
How you resolved it.
- Correctly filtered MAC address table using the "address" filter command

---

## Key Learnings
- What you learned
    - How to interrogate devices for connection status, device ID and connection type
- What improved
    - Navigation through tables and filtering ability
- What to remember next time
    - Check filtering terms

---

## Improvements for Next Time
- What you would do differently
    - Look up filtering glossary prior to undertaking a future task
