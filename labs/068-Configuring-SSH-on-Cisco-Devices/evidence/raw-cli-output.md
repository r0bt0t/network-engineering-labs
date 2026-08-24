# Lab 068 - Raw CLI Output

```bash
Connecting to console for RTR-Training-SSH

Router>
Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#no logginf
*Aug 20 13:37:59.732: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
Router(config)#no logging
*Aug 20 13:37:59.834: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 13:37:59.835: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 20 13:37:59.940: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
Router(config)#no logging 
*Aug 20 13:38:00.041: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 20 13:38:00.041: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Router(config)#no logging console
Router(config)#
Router(config)#end
Router#
Router#
Router#show ip interface brief | include Ethernet0/0
Ethernet0/0            10.22.45.1      YES TFTP   up                    up      
Router#
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname RTR-Training-SSH
RTR-Training-SSH(config)#ip domain name castlerysen.local
RTR-Training-SSH(config)#end
RTR-Training-SSH#wr
Building configuration...
[OK]
RTR-Training-SSH#
RTR-Training-SSH#
RTR-Training-SSH#show running-config | include hostname|ip domain name 
hostname RTR-Training-SSH
ip domain name castlerysen.local
RTR-Training-SSH#




RTR-Training-SSH#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-SSH(config)#username fieldtech privilege 15 secret BunkerSSH!
RTR-Training-SSH(config)#exit
RTR-Training-SSH#
RTR-Training-SSH#show runnning-config | include username
                          ^
% Invalid input detected at '^' marker.

RTR-Training-SSH#show running-config | include username 
username fieldtech privilege 15 secret 9 $9$8LKaOniOwlOU7.$MbzGH5tklYd8.eOZ4QFleZIVCyoMNr2Z4sS18pKPVVI
RTR-Training-SSH#
RTR-Training-SSH#crypto key generate rsa
The name for the keys will be: RTR-Training-SSH.castlerysen.local
Choose the size of the key modulus in the range of 2048 to 4096 for your
  General Purpose Keys. Choosing a key modulus greater than 512 may take
  a few minutes.

How many bits in the modulus [2048]: 2048
% Generating crypto RSA keys in background ...

RTR-Training-SSH#show ip ssh
SSH Enabled - version 2.0
Authentication methods:publickey,keyboard-interactive,password
Authentication Publickey Algorithms:ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-ed25519,x509v3-ecdsa-sha2-nistp256,x509v3-ecdsa-sha2-nistp384,x509v3-ecdsa-sha2-nistp521,rsa-sha2-256,rsa-sha2-512,x509v3-rsa2048-sha256
Hostkey Algorithms:ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,rsa-sha2-512,rsa-sha2-256
Encryption Algorithms:chacha20-poly1305@openssh.com,aes128-gcm@openssh.com,aes256-gcm@openssh.com,aes128-gcm,aes256-gcm,aes128-ctr,aes192-ctr,aes256-ctr
MAC Algorithms:hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com
KEX Algorithms:curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512
Authentication timeout: 120 secs; Authentication retries: 3
Minimum expected Diffie Hellman key size : 2048 bits
IOS Keys in SECSH format(ssh-rsa, base64 encoded): RTR-Training-SSH.castlerysen.local
Modulus Size : 2048 bits
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDTkNaJ8JFd790RjPyh8cN4BxtJOdfpyXMfDHTUDUQV
pmFAX6+65dfryxia/cdnwgDcdk2Iulcn+HZfze4OiDrFXwbV6i6FB5DiH4fF+amiYXYTq16IzMUpVP8Z
OfzTydZHgIpJl09zZFGXwRFK1jPmnp+Uk4uwu/tLxUS5UThDlA8F4tL6wPTn4EdI/3EIVvy/20fDq9WR
iamahyK/J4W0ZJKb+dcm4IW/gUNot967aczLOp0tJzpTkMG+e8iJU9OCK4wp7vvyP5IAsoVhzo9jfhJL
7GtM58Kc88BS5Wp6pEWRjaQFxrJ1HVzZNU+6Oykm0BbphMhDQJAOzcFlowZH                    
IOS Keys in SECSH format(ssh-ec, base64 encoded): NONE
RTR-Training-SSH#



RTR-Training-SSH#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-SSH(config)#line vty 0 4
RTR-Training-SSH(config-line)#login local
RTR-Training-SSH(config-line)#transport input ssh
RTR-Training-SSH(config-line)#exit
RTR-Training-SSH(config)#ip ssh version 2
RTR-Training-SSH(config)#end
RTR-Training-SSH#
RTR-Training-SSH#show running-config | section line vty
line vty 0 4
 password cisco
 login local
 transport input ssh
RTR-Training-SSH#



Connecting to console for Admin-Term

Core Linux
Admin-Term login: 
Core Linux
Admin-Term login: cisco
Password: 
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

cisco@Admin-Term:~$ 
cisco@Admin-Term:~$ 
cisco@Admin-Term:~$ telnet 10.22.45.1
telnet: can't connect to remote host (10.22.45.1): Connection refused
cisco@Admin-Term:~$ 
cisco@Admin-Term:~$ ssh -o StrictHostKeyChecking=no -l fieldtech 10.22.45.1
Warning: Permanently added '10.22.45.1' (RSA) to the list of known hosts.
(fieldtech@10.22.45.1) Password: 



RTR-Training-SSH#show users
    Line       User       Host(s)              Idle       Location
   0 con 0                idle                 00:02:45   
*  2 vty 0     fieldtech  idle                 00:00:00 10.22.45.10

  Interface    User               Mode         Idle     Peer Address

RTR-Training-SSH#show ip ssh
SSH Enabled - version 2.0
Authentication methods:publickey,keyboard-interactive,password
Authentication Publickey Algorithms:ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,ssh-ed25519,x509v3-ecdsa-sha2-nistp256,x509v3-ecdsa-sha2-nistp384,x509v3-ecdsa-sha2-nistp521,rsa-sha2-256,rsa-sha2-512,x509v3-rsa2048-sha256
Hostkey Algorithms:ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521,rsa-sha2-512,rsa-sha2-256
Encryption Algorithms:chacha20-poly1305@openssh.com,aes128-gcm@openssh.com,aes256-gcm@openssh.com,aes128-gcm,aes256-gcm,aes128-ctr,aes192-ctr,aes256-ctr
MAC Algorithms:hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com
KEX Algorithms:curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512
Authentication timeout: 120 secs; Authentication retries: 3
Minimum expected Diffie Hellman key size : 2048 bits
IOS Keys in SECSH format(ssh-rsa, base64 encoded): RTR-Training-SSH.castlerysen.local
Modulus Size : 2048 bits
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDTkNaJ8JFd790RjPyh8cN4BxtJOdfpyXMfDHTUDUQV
pmFAX6+65dfryxia/cdnwgDcdk2Iulcn+HZfze4OiDrFXwbV6i6FB5DiH4fF+amiYXYTq16IzMUpVP8Z
OfzTydZHgIpJl09zZFGXwRFK1jPmnp+Uk4uwu/tLxUS5UThDlA8F4tL6wPTn4EdI/3EIVvy/20fDq9WR
iamahyK/J4W0ZJKb+dcm4IW/gUNot967aczLOp0tJzpTkMG+e8iJU9OCK4wp7vvyP5IAsoVhzo9jfhJL
7GtM58Kc88BS5Wp6pEWRjaQFxrJ1HVzZNU+6Oykm0BbphMhDQJAOzcFlowZH                    
IOS Keys in SECSH format(ssh-ec, base64 encoded): NONE
RTR-Training-SSH#
RTR-Training-SSH#show logging | include SSH
*Aug 20 13:44:11.848: %CRYPTO_ENGINE-5-KEY_ADDITION: A key named RTR-Training-SSH.castlerysen.local has been generated or imported by crypto-engine
*Aug 20 13:44:11.848: %SSH-5-ENABLED: SSH 2.0 has been enabled
*Aug 20 13:44:12.117: %CRYPTO_ENGINE-5-KEY_ADDITION: A key named RTR-Training-SSH.castlerysen.local.server has been generated or imported by crypto-engine
*Aug 20 13:50:09.067: %SSH-5-SSH2_SESSION: SSH2 Session request from 10.22.45.10 (tty = 0) using crypto cipher 'chacha20-poly1305@openssh.com', hmac 'hmac-sha2-256-etm@openssh.com' Succeeded
*Aug 20 13:50:30.691: %SSH-5-SSH2_USERAUTH: User 'fieldtech' authentication for SSH2 Session from 10.22.45.10 (tty = 0) using crypto cipher 'chacha20-poly1305@openssh.com', hmac 'hmac-sha2-256-etm@openssh.com' Succeeded
RTR-Training-SSH#
```
