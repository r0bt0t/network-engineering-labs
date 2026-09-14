# Lab 071 - Raw CLI Output

```bash
RTR-Training-01#
RTR-Training-01#show ip interface brief | include Ethernet0/0
Ethernet0/0            10.23.0.1       YES TFTP   up                    up      
RTR-Training-01#
RTR-Training-01#ping 10.23.0.50
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.23.0.50, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 1/1/1 ms
RTR-Training-01#
RTR-Training-01#show running-config | include snmp
RTR-Training-01#
RTR-Training-01#show snmp
%SNMP agent not enabled
RTR-Training-01#
RTR-Training-01#show snmp engineID
%SNMP agent not enabled
RTR-Training-01#



RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#ip access-list standard SNMP-MGMT
RTR-Training-01(config-std-nacl)#permit 10.23.0.50
RTR-Training-01(config-std-nacl)#exit
RTR-Training-01(config)#
RTR-Training-01(config)#snmp-server community CSTL-RO ro SNMP-MGMT
RTR-Training-01(config)#snmp-server community CSTL-RW rw SNMP-MGMT
RTR-Training-01(config)#snmp-server contact bunker.noc@castlerysen.coffee
RTR-Training-01(config)#snmp-server location Castle Rysen Command Bunker 
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#show snmp community

Community name: CSTL-RO
Community Index: CSTL-RO
Community SecurityName: CSTL-RO
storage-type: nonvolatile        active access-list: SNMP-MGMT


Community name: CSTL-RW
Community Index: CSTL-RW
Community SecurityName: CSTL-RW
storage-type: nonvolatile        active access-list: SNMP-MGMT


RTR-Training-01#
RTR-Training-01#show running-config | section snmp
snmp-server community CSTL-RO RO SNMP-MGMT
snmp-server community CSTL-RW RW SNMP-MGMT
snmp-server location Castle Rysen Command Bunker
snmp-server contact bunker.noc@castlerysen.coffee
RTR-Training-01#
RTR-Training-01#show running-config | section ip access-list
ip access-list standard SNMP-MGMT
 10 permit 10.23.0.50
RTR-Training-01#
RTR-Training-01#show snmp engineID
Local SNMP engineID: 800000090300AABBCC000100
Remote Engine ID          IP-addr    Port
RTR-Training-01#



RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#snmp-server group castleSecure v3 priv
RTR-Training-01(config)#snmp-server user JeremyOps CastleSecure v3 auth sha P@$
RTR-Training-01(config)#
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#show snmp group | section CastleSecure
RTR-Training-01#conf t                                
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#snmp-server group castleSecure v3 priv         
RTR-Training-01(config)#no snmp-server group castleSecure v3 priv
RTR-Training-01(config)#snmp-server group CastleSecure v3 priv   
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#show snmp group | section CastleSecure
groupname: CastleSecure                     security model:v3 priv 
RTR-Training-01#
RTR-Training-01#show snmp user JeremyOps

User name: JeremyOps
Engine ID: 800000090300AABBCC000100
storage-type: nonvolatile        active
Authentication Protocol: SHA
Privacy Protocol: AES128
Group-name: CastleSecure

RTR-Training-01#
RTR-Training-01#$ackets|Bad|Unknown|Illegal|Encoding|global trap|logging     
0 SNMP packets input
    0 Bad SNMP version errors
    0 Unknown community name
    0 Illegal operation for community name supplied
    0 Encoding errors
0 SNMP packets output
    0 Bad values errors
SNMP global trap: disabled
SNMP logging: disabled
RTR-Training-01#
```
