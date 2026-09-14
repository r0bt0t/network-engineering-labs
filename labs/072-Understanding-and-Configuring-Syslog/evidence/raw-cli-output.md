# Lab 072 - Raw CLI Output

```bash
RTR-Training-01>
RTR-Training-01>en
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#
*Aug 24 20:40:50.239: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
RTR-Training-01(config)#
*Aug 24 20:40:50.341: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 20:40:50.342: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 20:40:50.447: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
RTR-Training-01(config)#
*Aug 24 20:40:50.548: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 24 20:40:50.548: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
RTR-Training-01(config)#exit
RTR-Training-01#
*Aug 24 20:41:12.479: %SYS-5-CONFIG_I: Configured from console by console
RTR-Training-01#show ip int brief | include Ethernet0/0|Ethernet0/1
Ethernet0/0            10.23.0.10      YES TFTP   up                    up      
Ethernet0/1            unassigned      YES unset  administratively down down    
RTR-Training-01#
RTR-Training-01#show logging | begin Syslog logging
Syslog logging: enabled (0 messages dropped, 2 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)

No Active Message Discriminator.



No Inactive Message Discriminator.


    Console logging: level debugging, 43 messages logged, xml disabled,
                     filtering disabled
    Monitor logging: level debugging, 0 messages logged, xml disabled,
                     filtering disabled
    Buffer logging:  level debugging, 43 messages logged, xml disabled,
                    filtering disabled
    Exception Logging: size (4096 bytes)
    Count and timestamp logging messages: disabled
    Persistent logging: disabled
    Trap logging: level informational, 45 message lines logged
        Logging Source-Interface:       VRF Name:

Log Buffer (4096 bytes):
 the preferred publickey or hostkey algorithms by default. Users may choose to configure them explicitly if required
*Aug 24 20:40:00.048: TODCLK-STUB: REGISTERED
*Aug 24 20:40:00.049: ISIS-GRACEFUL-RELOAD: Init State GR_NONE
*Aug 24 20:40:00.050: PTP-ENGINE: REGISTERED
*Aug 24 20:40:00.100: %TLSCLIENT-5-TLSCLIENT_IOS: TLS Client is IOS based
*Aug 24 20:40:00.112: %CRYPTO_ENGINE-5-CSDL_COMPLIANCE_ENFORCED: Cisco PSB security compliance is being enforced
*Aug 24 20:40:00.203: %PNP-6-PNP_DISCOVERY_STARTED: PnP Discovery started
*Aug 24 20:40:00.203: %PNP-6-PNP_GOOD_UDI_UPDATE: Good UDI [PID:Unix,VID:,SN:131184641] identified via (platform-registry)
*Aug 24 20:40:00.203: %PNP-6-PNP_CDP_UPDATE: Device UDI [PID:Unix,VID:,SN:131184641] identified for CDP
*Aug 24 20:40:00.232: %SYS-7-NVRAM_INIT_WAIT_TIME: Waited 0 seconds for NVRAM to be available
*Aug 24 20:40:00.292: %SYS-5-CONFIG_I: Configured from unix:config by console
*Aug 24 20:40:00.292: : File bootup successful. Autoinstall will not start now.
*Aug 24 20:40:01.738: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Aug 24 20:40:01.750: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
*Aug 24 20:40:01.762: %LINK-3-UPDOWN: Interface Ethernet0/2, changed state to up
*Aug 24 20:40:01.773: %LINK-3-UPDOWN: Interface Ethernet0/3, changed state to up
*Aug 24 20:40:02.738: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
*Aug 24 20:40:02.750: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Aug 24 20:40:02.762: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
*Aug 24 20:40:02.773: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to up
*Aug 24 20:40:19.313: %SYS-5-RESTART: System restarted --
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.16.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.
Compiled Thu 19-Dec-24 17:54 by mcpre
*Aug 24 20:40:19.315: %CRYPTO-5-SELF_TEST_START: Crypto algorithms release (Rel5a), Entropy release (3.4.1)
       begin Crypto Module self-tests
*Aug 24 20:40:19.316: %CRYPTO-5-SELF_TEST_END: Crypto Algorithm self-test completed successfully
       All tests passed.
*Aug 24 20:40:19.316: %LINK-5-CHANGED: Interface Ethernet0/1, changed state to administratively down
*Aug 24 20:40:19.316: %LINK-5-CHANGED: Interface Ethernet0/2, changed state to administratively down
*Aug 24 20:40:19.316: %LINK-5-CHANGED: Interface Ethernet0/3, changed state to administratively down
*Aug 24 20:40:20.128: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Aug 24 20:40:20.128: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
*Aug 24 20:40:20.128: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
*Aug 24 20:40:20.316: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Aug 24 20:40:20.316: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
*Aug 24 20:40:20.316: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down
*Aug 24 20:40:50.239: %PNP-6-PNP_SAVING_TECH_SUMMARY: Saving PnP tech summary (/pnp-tech/pnp-tech-discovery-summary)... Please wait. Do not interrupt.
*Aug 24 20:40:50.341: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 20:40:50.342: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 20:40:50.447: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
*Aug 24 20:40:50.548: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 1 seconds).
*Aug 24 20:40:50.548: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
*Aug 24 20:41:12.479: %SYS-5-CONFIG_I: Configured from console by console
RTR-Training-01# 



RTR-Training-01# 
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#service timestamps log datetime msec
RTR-Training-01(config)#logging buffered 32000 informational
RTR-Training-01(config)#e
*Aug 24 20:43:21.265: %SYS-5-LOG_CONFIG_CHANGE: Buffer logging: level informational, xml disabled, filtering disabled, size (32000)
RTR-Training-01(config)#end
RTR-Training-01#
*Aug 24 20:43:23.068: %SYS-5-CONFIG_I: Configured from console by console
RTR-Training-01#
RTR-Training-01#show logging | include Buffer logging
    Buffer logging:  level informational, 2 messages logged, xml disabled,
*Aug 24 20:43:21.265: %SYS-5-LOG_CONFIG_CHANGE: Buffer logging: level informational, xml disabled, filtering disabled, size (32000)
RTR-Training-01#
RTR-Training-01#show logging | include LOG_CONFIG_CHANGE|CONFIG_I
*Aug 24 20:43:21.265: %SYS-5-LOG_CONFIG_CHANGE: Buffer logging: level informational, xml disabled, filtering disabled, size (32000)
*Aug 24 20:43:23.068: %SYS-5-CONFIG_I: Configured from console by console
RTR-Training-01#



Connecting to console for Log-Archive-01

Core Linux
Log-Archive-01 login: 
Core Linux
Log-Archive-01 login: cisco
Password: 
Login incorrect
login[639]: invalid password for 'cisco' on 'ttyS0'
Log-Archive-01 login: tc
   ( '>')
  /) TC (\   Core is distributed with ABSOLUTELY NO WARRANTY.
 (/-_--_-\)           www.tinycorelinux.net

tc@Log-Archive-01:~$ 
tc@Log-Archive-01:~$ sudo killall nc>/dev/null || true
killall: nc: no process killed
tc@Log-Archive-01:~$ sudo sh -c "rm -f /tmp/syslog-capture.log; nc -u -l -s 10.2
3.0.60 -p 514 > /tmp/syslog-capture.log &"
tc@Log-Archive-01:~$ netstat -anu | grep 514
udp        0      0 10.23.0.60:514          0.0.0.0:*                           
tc@Log-Archive-01:~$ 




RTR-Training-01#
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#logging host 10.23.0.60 transport udp port 514
RTR-Training-01(config)#loggi
*Aug 24 20:49:27.028: %SYS-6-LOGGINGHOST_STARTSTOP: Logging to host 10.23.0.60 port 514 started - CLI initiated
RTR-Training-01(config)#logging trap informational
RTR-Training-01(config)#logging source-interface Ethernet0/0
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#
*Aug 24 20:49:58.701: %SYS-5-CONFIG_I: Configured from console by console
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#
*Aug 24 20:50:04.701: %SYS-6-LOGGINGHOST_STARTSTOP: Logging to host 10.23.0.60 port 514 started - reconnection
RTR-Training-01(config)#interface Ethernet0/1
RTR-Training-01(config-if)#shutdown
RTR-Training-01(config-if)#end
RTR-Training-01#
*Aug 24 20:50:21.655: %SYS-5-CONFIG_I: Configured from console by console
RTR-Training-01#
RTR-Training-01#
RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#interface Ethernet0/1
RTR-Training-01(config-if)#no shutdown
RTR-Training-01(config-if)#end
RTR-Training-01#
*Aug 24 20:51:02.842: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
RTR-Training-01#
*Aug 24 20:51:02.946: %SYS-5-CONFIG_I: Configured from console by console
RTR-Training-01#
*Aug 24 20:51:03.842: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
RTR-Training-01#
RTR-Training-01#show logging | include 10.23.0.60
        Logging to 10.23.0.60  (udp port 514, audit disabled,
*Aug 24 20:49:26.028: %SYS-6-LOGGINGHOST_STARTSTOP: Logging to host 10.23.0.60 port 0 CLI Request Triggered
*Aug 24 20:49:27.028: %SYS-6-LOGGINGHOST_STARTSTOP: Logging to host 10.23.0.60 port 514 started - CLI initiated
*Aug 24 20:50:04.701: %SYS-6-LOGGINGHOST_STARTSTOP: Logging to host 10.23.0.60 port 514 started - reconnection
RTR-Training-01#
RTR-Training-01#show running-config | include logging
logging buffered 32000 informational
no logging btrace
logging source-interface Ethernet0/0
logging host 10.23.0.60
 logging synchronous
RTR-Training-01#



tc@Log-Archive-01:~$ 
tc@Log-Archive-01:~$ cat /tmp/syslog-capture.log
<189>50: *Aug 24 20:49:58.701: %SYS-5-CONFIG_I: Configured from console by console<190>51: *Aug 24 20:50:04.701: %SYS-6-LOGGINGHOST_STARTSTOP: Logging to host 10.23.0.60 port 514 started - reconnection<189>52: *Aug 24 20:50:21.655: %SYS-5-CONFIG_I: Configured from console by console<187>53: *Aug 24 20:51:02.842: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up<189>54: *Aug 24 20:51:02.946: %SYS-5-CONFIG_I: Configured from console by console<189>55: *Aug 24 20:51:03.842: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to uptc@Log-Archive-01:~$
```
