# Lab 007 - Tracking Devices with the CAM Table

<table>
<tr>
<td colspan="2" valign="top">


# Objective
- Translate an IP-only report into a MAC address using switch-side tools.
- Walk a MAC address from CoreSwitch down to Switch6 to identify the access port.
- Confirm the endpoint location for both a user PC and a suspicious server so responders can act.

</td>
</tr>

<tr>
<td valign="top">
<img src="images/Packet-Tracer-Img2.png">
</td>

<td valign="bottom">
<img src="images/networking_image_25.png">
</td>

</tr>
</table>

---

## Devices Used
- Switch SW1 / SW2 / SW3 / SW4 / SW5 / SW6
- PC1 / PC2 / PC3 / PC4 / PC5 / PC6 / PC7 / PC8
- Server SV1 / SV2
---

## Configuration Steps

### Step 1 - Basic setup
```bash
enable
configure terminal
```

### Explanation
Log in to global configuration mode

---

### Step 2 - Main configuration
```bash
CoreSwitch>
CoreSwitch>en
CoreSwitch#ping 192.168.1.118
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.118, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
CoreSwitch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.002c.5005    DYNAMIC     Et0/0
  10    5254.0030.1887    DYNAMIC     Et0/1
  10    5254.00d3.fdbb    DYNAMIC     Et0/0
  10    aabb.cc00.0100    DYNAMIC     Et0/0
Total Mac Addresses for this criterion: 4
CoreSwitch#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.1.1             -   aabb.cc80.0200  ARPA   Vlan10
Internet  192.168.1.118           0   5254.00d3.fdbb  ARPA   Vlan10
CoreSwitch#
CoreSwitch#show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Switch6          Eth 0/0           176             R S I  Linux Uni Eth 0/0

Total cdp entries displayed : 1
CoreSwitch#ping 192.168.1.111
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.111, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
CoreSwitch#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.1.1             -   aabb.cc80.0200  ARPA   Vlan10
Internet  192.168.1.111           0   5254.0030.1887  ARPA   Vlan10
Internet  192.168.1.118           5   5254.00d3.fdbb  ARPA   Vlan10
CoreSwitch#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.002c.5005    DYNAMIC     Et0/0
  10    5254.0030.1887    DYNAMIC     Et0/1
  10    5254.00d3.fdbb    DYNAMIC     Et0/0
  10    aabb.cc00.0100    DYNAMIC     Et0/0
Total Mac Addresses for this criterion: 4
CoreSwitch#show cdp neighbors    
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone, 
                  D - Remote, C - CVTA, M - Two-port Mac Relay 

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
Switch6          Eth 0/0           169             R S I  Linux Uni Eth 0/0

Total cdp entries displayed : 1
CoreSwitch#

Switch6>
Switch6>en
Switch6#show arp
Switch6#ping 192.168.1.118
% Unrecognized host or address, or protocol not running.

Switch6#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  10    5254.002c.5005    DYNAMIC     Et0/2
  10    5254.0030.1887    DYNAMIC     Et0/0
  10    5254.00d3.fdbb    DYNAMIC     Et0/1
  10    aabb.cc80.0200    DYNAMIC     Et0/0
Total Mac Addresses for this criterion: 4
Switch6#

```

### Explanation
To identify the physical location and burned in address of poorly performing devices

---

## Verification

- User complaint: IP 192.168.1.118 (PC7 on VLAN 10) reports sluggish service.
    - **Confirmed as having MAC 5254.00d3.fdbb and connected directly to Switch 6 on ET0/1**
- Security alert: IP 192.168.1.111 (Server2 on VLAN 10) needs containment.
    - **Confirmed as having MAC 5254.0030.1887 and is connected directly to the CoreSwitch on ET0/1**


---

## Key Learnings
- What you learned
    - Confirmation of correct use of ARP and CAM tables
- What improved
    -   Use of correct query commands
- What to remember next time
    - Work methodically

---
