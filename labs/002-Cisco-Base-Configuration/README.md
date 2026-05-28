# Lab 002 - CISCO BASE CONFIGURATION

<table>
<tr>
<td colspan="2" valign="top">

## Objective
### Configure a base level configuration on a Cisco switch

</td>
</tr>

<tr>
<td valign="top">
<img src="images/Topology2.png">
</td>

<td valign="top">
<img src="images/networking_image_04.png">
</td>
</tr>
</table>

---

## Devices Used
- Switch 1
- PC

---

## Configuration Steps

### Step 1 - Basic setup
```bash
enable
configure terminal
```

### Explanation
Move to global configuration mode

---

### Step 2 - Main configuration
```bash
Switch(config)#hostname Cafe-01-SW1
Cafe-01-SW1(config)#banner motd ^Unauthorized access ends badly. Authorized Castle Rysen engineers only.^
Cafe-01-SW1(config)#enable secret C4stleRysen!
Cafe-01-SW1(config)#line con 0
Cafe-01-SW1(config-line)#password VaultAccessCafe-01-SW1(config-line)# ^C
Cafe-01-SW1(config-line)#password VaultAccess
Cafe-01-SW1(config-line)#login
Cafe-01-SW1(config)#service password-encryption
Cafe-01-SW1(config)#line vty 0 4
Cafe-01-SW1(config-line)#password ShelterAccess
Cafe-01-SW1(config-line)#login
Cafe-01-SW1(config-line)#transport input ssh
Cafe-01-SW1(config-line)#exit
Cafe-01-SW1(config)#interface vlan1
Cafe-01-SW1(config-if)#ip address 192.168.10.10 255.255.255.0
Cafe-01-SW1(config-if)#no shutdown
Cafe-01-SW1(config-if)#interface ethernet0/0
Cafe-01-SW1(config-if)#description Uplink-to-Core-Distribution
Cafe-01-SW1(config-if)#
Cafe-01-SW1#copy running-config startup-config
Destination filename [startup-config]? 
```

### Explanation
- On Switch1, rename the switch from Switch to Cafe-01-SW1 so the prompt reflects the Castle Rysen device call sign.
- On Cafe-01-SW1, configure the MOTD banner with this exact text: Unauthorized access ends badly. Authorized Castle Rysen engineers only.
- On Cafe-01-SW1, protect privileged EXEC mode with the exact enable secret C4stleRysen!.
- On Cafe-01-SW1, set console line 0 to require login with the exact password VaultAccess.
- On Cafe-01-SW1, enable password encryption, set VTY lines 0 through 4 to require login with password ShelterAccess, and restrict remote transport to SSH only
- On Cafe-01-SW1, configure interface Vlan1 with IP address 192.168.10.10 and mask 255.255.255.0, then enable the SVI so it is usable for management.
- On Cafe-01-SW1, label interface Ethernet0/0 with the exact description Uplink-to-Core-Distribution.
- On Cafe-01-SW1, save the current running configuration to startup-config so the hostname, warning banner, access controls, management SVI, and uplink label survive a reload.

---

## Verification

```bash
show ip interface brief
show running-config
```

---

## Troubleshooting

### Issue 1
Did not understand the phrase "enable the SVI so it is usable for management"

### Diagnosis
Was unable to fulfill assessment criteria

### Fix
Simply brought the uplink up with the `no shutdown` command

---

## Key Learnings
- Learned the need and method for creating banner MOTD to protect liability rights
- Learned to enforce SSH secure remote access
- Learned about line level control
- Improved range of CLI commands and security understanding
- To bring up both virtual and physical ports

---

## Improvements for Next Time
- Seek to fully understand criteria of assessment prior to approaching assessment