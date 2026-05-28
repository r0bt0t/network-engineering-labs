# Lab 003 - Small Network Config (Micro Campus)

<table>
<tr>
<td colspan="2" valign="top">

## Objective
- Re-establish device identity, banners, and secrets across both switches and the router.
- Lock down console and VTY access with the Castle credential set and enable password encryption.
- Stand up the management VLAN on each switch and tie it to the router’s inside interface.
- Save, verify, and (when asked) wipe configurations without losing control of the site.
</td>
</tr>

<tr>
<td valign="top">
<img src="images/Topology.png">
</td>

<td valign="bottom">
<img src="images/CaricatureMe.png">
</td>

</tr>
</table>

---

## Devices Used
- Router DS-07-RTR1
- Switch DS-07-SW1
- Switch DS-07-SW2

---

## Configuration Steps

### Step 1 - Basic setup
```bash
Switch1>en
Switch1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch1(config)#hostname DS-07-SW1                                                         
DS-07-SW1(config)#banner motd ^Castle Rysen Ops: Authorised engineers only.^
DS-07-SW1(config)#enable secret CrC0ffee!

Switch2>en
Switch2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Switch2(config)#hostname DS-07-SW2
DS-07-SW2(config)#banner motd ^Castle Rysen Ops: Authorised Engineers only.^
DS-07-SW2(config)#enable secret CrC0ffee!

Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname DS-07-RTR1
DS-07-RTR1(config)#banner motd ^Castle Rysen Ops: Authorised engineers only.^
DS-07-RTR1(config)#enable secret CrC0ffee!
```

### Explanation
- Update each device so its hostname reflects DS-07-SW1, DS-07-SW2, and DS-07-RTR1.
- Ensure all three systems display the Castle warning banner text Castle Rysen Ops: Authorized engineers only. whenever someone connects.
- Protect privileged access with the shared secret CrC0ffee! and confirm stored passwords are hidden by the standard encryption feature.

---

### Step 2 - Main configuration
```bash
DS-07-SW1(config)#line con 0
DS-07-SW1(config-line)#password VaultAccess
DS-07-SW1(config-line)#login
DS-07-SW1(config-line)#exit
DS-07-SW1(config)#service password encryption
                                   ^
% Invalid input detected at '^' marker.

DS-07-SW1(config)#service password-encryption
DS-07-SW1(config)#username admin secret ShelterAccess
DS-07-SW1(config)#line vty 0 4
DS-07-SW1(config-line)#login local
DS-07-SW1(config-line)#transport input ssh
DS-07-SW1(config-line)#exit
DS-07-SW1(config)#ip ssh version 2
DS-07-SW1(config)#exec-timeout 10 0
                    ^
% Invalid input detected at '^' marker.

DS-07-SW1(config)#line vty 0 4
DS-07-SW1(config-line)#exec-timeout 10 0
DS-07-SW1(config-line)#exit
DS-07-SW1(config)#interface vlan1
DS-07-SW1(config-if)#ip address 192.168.10.11 255.255.255.0
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#exit
DS-07-SW1(config)#ip default-gateway 192.168.10.1
DS-07-SW1(config)#ip domain name castle.local
DS-07-SW1(config)#crypto key generate rsa
The name for the keys will be: DS-07-SW1.castle.local
Choose the size of the key modulus in the range of 2048 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [2048]: 2048
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

DS-07-SW1(config)#interface en0/3
                             ^
% Invalid input detected at '^' marker.

DS-07-SW1(config)#interface et0/3
DS-07-SW1(config-if)#description Uplink-to-Router
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#interface e0/2
DS-07-SW1(config-if)#description WAP1-Feed
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#interface e0/1
DS-07-SW1(config-if)#description Link-to-DS-07-SW2
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#interface e0/0
DS-07-SW1(config-if)#description 2nd-Link-to-DS-07-SW2
DS-07-SW1(config-if)#no shutdown
DS-07-SW1(config-if)#^Z
DS-07-SW1#write memory
Building configuration...
[OK]
DS-07-SW1#

DS-07-SW2(config)#line con 0
DS-07-SW2(config-line)#password VaultAccess
DS-07-SW2(config-line)#login
DS-07-SW2(config-line)#exit
DS-07-SW2(config)#service password encryption
                                   ^
% Invalid input detected at '^' marker.

DS-07-SW2(config)#service password-encryption
DS-07-SW2(config)#username admin secret ShelterAccess
DS-07-SW2(config)#line vty 0 4
DS-07-SW2(config-line)#login local
DS-07-SW2(config-line)#transport input ssh
DS-07-SW2(config-line)#exec-timeout 10 0
DS-07-SW2(config-line)#exit
DS-07-SW2(config)#ip ssh version 2
DS-07-SW2(config)#ip domain name castle.local
DS-07-SW2(config)#crypto key generate rsa
The name for the keys will be: DS-07-SW2.castle.local
Choose the size of the key modulus in the range of 2048 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [2048]: 2048
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

DS-07-SW2(config)#interface vlan1
DS-07-SW2(config-if)#ip address 192.168.10.12 255.255.255.0
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#exit
DS-07-SW2(config)#ip default-gateway 192.168.10.1
DS-07-SW2(config)#interface e0/0
DS-07-SW2(config-if)#description Link-to-DS-07-SW1
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#interface e0/1
DS-07-SW2(config-if)#description 2nd-Link-to-DS-07-SW1
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#interface e0/2
DS-07-SW2(config-if)#description WAP2-link
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#interface e0/3
DS-07-SW2(config-if)#description Drop-to-Server
DS-07-SW2(config-if)#no shutdown
DS-07-SW2(config-if)#exit
DS-07-SW2(config)#exit
DS-07-SW2#write memory
Building configuration...
[OK]
DS-07-SW2#

Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname DS-07-RTR1
DS-07-RTR1(config)#banner motd ^Castle Rysen Ops: Authorised engineers only.^
DS-07-RTR1(config)#enable secret CrC0ffee!
DS-07-RTR1(config)#line con 0
DS-07-RTR1(config-line)#password VaultAccess
DS-07-RTR1(config-line)#login
DS-07-RTR1(config-line)#exit
DS-07-RTR1(config)#service password-encryption
DS-07-RTR1(config)#username admin secret ShelterAccess
DS-07-RTR1(config)#ip ssh version 2
DS-07-RTR1(config)#ip domain name castle.local
DS-07-RTR1(config)#crypto key generate rsa
The name for the keys will be: DS-07-RTR1.castle.local
Choose the size of the key modulus in the range of 2048 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [2048]: 2048
% Generating 2048 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

DS-07-RTR1(config)#line vty 0 4
DS-07-RTR1(config-line)#login local
DS-07-RTR1(config-line)#transport input ssh
DS-07-RTR1(config-line)#exec-timeout 10 0
DS-07-RTR1(config-line)#exit
DS-07-RTR1(config)#interface e0/0
DS-07-RTR1(config-if)#description Link-to-DS-07-SW1
DS-07-RTR1(config-if)#no shutdown
DS-07-RTR1(config-if)#inteface vlan1
                       ^
% Invalid input detected at '^' marker.

DS-07-RTR1(config-if)#interface vlan1
                                 ^
% Invalid input detected at '^' marker.

DS-07-RTR1(config)#interface vlan1
                              ^
% Invalid input detected at '^' marker.

DS-07-RTR1(config)#interface e0/0
DS-07-RTR1(config-if)#ip address 192.168.10.1
% Incomplete command.

DS-07-RTR1(config-if)#ip address 192.168.10.1 255.255.255.0
DS-07-RTR1(config-if)#^Z
DS-07-RTR1#write memory
Building configuration...
[OK]

DS-07-SW1#ping 192.168.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.1, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
DS-07-SW1#ping 192.168.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
DS-07-SW1#

DS-07-SW2#ping 192.168.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.1, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
DS-07-SW2#ping 192.168.10.1
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.10.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
DS-07-SW2#
```

### Explanation
- Require the console password VaultAccess before anyone can move past the initial prompt on every device.
- Guard the remote-access lines with the password ShelterAccess, limiting them to SSH sessions, and confirm both passwords are stored in encrypted form.
- Assign DS-07-SW1 the management address 192.168.10.11/24, ensure the virtual interface is active, and document which physical ports face the router and the neighboring switch.
- Assign DS-07-SW2 the management address 192.168.10.12/24, confirm the interface is active, and label the uplink along with the ports that feed the existing WAP and server drops.
- Point both switches at 192.168.10.1 as their management gateway.
- Place the router’s inside interface on 192.168.10.1/24, describing the link back to DS-07-SW1.
- Confirm the interface is brought online so switch traffic reaches the router through that connection.
- Compare the live configuration to the saved startup copy on each device to check whether the new banner, hostnames, and secrets have been preserved.
- Commit the changes to non-volatile storage, repeat the comparison, and restart DS-07-SW1 to confirm the passwords still take effect (VaultAccess on the console, CrC0ffee! for privileged access).
- Every prompt reads DS-07-*, the banner flashes Castle Rysen Ops: Authorized engineers only., and the enable secret reports as type 5 under show running-config.
- Both switches report the management interface as operational with addresses 192.168.10.11 and 192.168.10.12, and their management gateway is set to 192.168.10.1.
- The router lists 192.168.10.1/24 on its inside connection with the Castle security controls active.
- Saved configurations match the running state on every device, and DS-07-SW2 powers up with the hardened settings instead of reverting to the factory prompt.
---

## Verification

```bash
show ip interface brief
show running-config
ping 192.168.10.1
ping 192.168.10.11
ping 192.168.10.12
```

---

## Troubleshooting

### Issue 1
- **Attempting to assign router ip address to vlan1 instead of ethernet0/0 (the connection to the internal network)**

### Diagnosis
- **Unable to complete task/unable to ping**

### Fix
- **Assigned ip direct to port as specified**

---

## Key Learnings
- Ensure I am in the correct mode at all times
- Learned to fully secure SSH and upgrade it to the newer more secure version
- Memorisation of CLI commands
- Check spellings, mode and especially hyphens where appropriate

---

## Improvements for Next Time
- Speed improvement in completing basic config is my aim for the next lab