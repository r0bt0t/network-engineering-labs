# Lab 001 - Basic Switch Configuration

<table>
<tr>
<td colspan="2" valign="top">

## Objective

**Learn and apply basic Cisco switch configuration using IOS CLI.**

</td>
</tr>

<tr>
<td valign="top">
<img src="Images/Topology2.png">
</td>
<td valign="top">
<img src="Images/networking_image_01.png">
</td>
</tr>
</table>

---

## Devices Used

- Switch (Cisco 2960)
- PC (for management access)

---

## Configuration Steps

### Enter privileged mode
```bash
enable
```

### Enter global configuration mode
```bash
configure terminal
```

### Set hostname
```bash
hostname S1
```

### Disable DNS lookup (prevents delays on typos)
```bash
no ip domain-lookup
```

### Set enable password
```bash
enable secret class
```

### Configure management VLAN interface
```bash
interface vlan 1
ip address 192.168.1.2 255.255.255.0
no shutdown
```

### Save configuration
```bash
write memory
```

---

## Verification Commands

```bash
show ip interface brief
show running-config
```

---

## What This Lab Demonstrates

- Basic IOS navigation
- Switch configuration fundamentals
- Management interface setup
- Saving running configuration

---

## Troubleshooting Notes

- Forgot to enable interface VLAN 1 → interface stayed down
- Typo in IP address caused connectivity failure
- Resolved using `show ip interface brief`

---

## Key Takeaways

- Switch management requires VLAN interface configuration
- **`no shutdown`** is essential for activation of an interface
- Verification commands are critical before troubleshooting
