# Study Notes & Cheatsheets

<table>
<tr>
<td valign="top">

### This section contains quick reference material used during lab work.

</td>
</tr>
<tr>

<td valign="top">
<img src="Images/networking_image_28.png" style="margin-top:2%">
</td>

</tr>
</table>

---

## Key Topics Covered

- VLAN configuration commands
- Routing basics
- Interface setup
- Verification commands (`show` commands)
- Subnetting practice

---

## Example Quick Commands

```bash
show ip interface brief
show running-config
show vlan brief
show ip route
```

---

## Purpose

These notes act as a quick reference during lab work to reinforce command familiarity.

## Glossary of useful commands 

- `Service password-encryption` Hashes all plain text passwords 
- `Reload` Restarts the device 
- `write memory` Saves running config to startup config 
- `Write erase` Factory reset the memory 
- `erase startup-config` Factory reset the startup configuration 
- `Write memory` Saves running config to startup config 
- `Copy running-config startup-config` Long way of achieving the above 
- `Ip default-gateway xxx.xxx.xxx.xxx` Set default gateway 
- `Line console 0` Select console port 
- `Line vty 0 4` Access all remote ports (first digit is start of range, second is end of range) 
- `Show ip interface brief` Outline of physical and VLAN port status  

**Once a VLAN is created it is not up until a physical port on that VLAN is up ie:**

```
Switch(config)# interface gigabitEthernet0/1 
Switch(config-if)# description Uplink-to-Router 
Switch(config-if)# no shutdown  

```

- `Description` Adds a description to ports etc to help future troubleshooting 
- `Password [password]` Adds an unhashed plain text password 
- `Secret` Creates an encrypted password that is unreadable in show commands 
- `Interface` Selects a virtual or physical interface on the equipment 
- `Show cdp neighbors` Displays Cisco Discovery Path data used to identify existing links 
- `Line` Access line configuration mode allowing you to manage and secure the physical and virtual access points 
- `username [username] secret [password]` Creates a username and encrypted local password 
- `login local` Utilises the locally stored password as login credentials 
- `transport input ssh` Ensures SSH is used for remote management traffic 
- `Show interface status` Displays interface status 
- `ip domain name [something].local` Assigns the default DNS domain name to the device which is required in order to generate cryptographic SSH keys 
- `crypto key generate rsa` Enable the SSH server on the switch and generate an RSA key pair 
- `ip ssh version 2` Upgrades the device to a newer more secure SSH standard 
- `exec-timeout 10 0` Sets a specific time to disconnect idle EXEC sessions. The default value for the EXEC timeout is 10 minutes 
- `Show mac address-table` Details MAC addresses 
- `clear mac address-table dynamic` Clear learned MAC addresses  
- `Show interfaces description` Descriptive detail of each interface 

---

## Additional Reference

**Glossary of useful command line commands**

- `arp –a` Displays Arp cache (known MAC addresses) 
- `ping xxx.xxx.xxx.xxx` Verifies IP-level connectivity to another TCP/IP computer by sending Internet Control Message Protocol (ICMP) echo Request messages. 
- `tracert` Tracks the path data packets traverse over an IP network from a source device to a destination device. 
- `ipconfig` Users can access important information such as their network interface's IP address (Internet Protocol address), subnet mask, default gateway, and DNS server configurations by running the ipconfig command. 
- `getmac` Retrieve the MAC address of their network devices 
- `nslookup` Used to query the Domain Name System (DNS) to retrieve domain name and IP address information. 
- `netstat` Provides information on active TCP connections, listening ports, Ethernet statistics, IP routing tables, and IPv4/IPv6 statistics. 
- `tasklist` Command displays a list of currently running processes on the system. 
- `taskkill` Command terminates tasks by process id (PID) or image name. 

<img src="Images/networking_image_24.png" style="margin-top:2%">
