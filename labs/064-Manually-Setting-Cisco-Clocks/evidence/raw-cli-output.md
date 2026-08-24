# Lab 064 - Raw CLI Output

```bash
RTR-Training-01>en
RTR-Training-01#show clock
*11:18:49.947 UTC Thu Aug 20 2026
RTR-Training-01#
*Aug 20 11:18:53.897: %PKI-6-SUDI_INFO: PKI: platform doesn't support sudi certificate
*Aug 20 11:18:53.897: %PKI-6-SUDI_INFO: PKI: no sudi certificate is installed
*Aug 20 11:18:53.897: %PKI-2-NON_AUTHORITATIVE_CLOCK: PKI functions can not be initialized until an authoritative time source, like NTP, can be obtained.
RTR-Training-01#
*Aug 20 11:18:53.900: %SYS-5-CONFIG_P: Configured programmatically by process PnP Agent Discovery from console as vty0
RTR-Training-01#
*Aug 20 11:18:54.001: %PNP-6-PNP_TECH_SUMMARY_SAVED_OK: PnP tech summary (/pnp-tech/pnp-tech-discovery-summary) saved successfully (elapsed time: 19 seconds).
*Aug 20 11:18:54.001: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
RTR-Training-01#show clock detail
*11:19:26.333 UTC Thu Aug 20 2026
Time source is hardware calendar
RTR-Training-01#no logging console
                   ^
% Invalid input detected at '^' marker.

RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#no logging console
RTR-Training-01(config)#end
RTR-Training-01#


RTR-Training-01#
RTR-Training-01#clock set 11:22:30 12 September 2024
RTR-Training-01#show clock
11:22:35.210 UTC Thu Sep 12 2024
RTR-Training-01#show clock detail
11:22:42.625 UTC Thu Sep 12 2024
Time source is user configuration
RTR-Training-01#



RTR-Training-01#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
RTR-Training-01(config)#clock timezone CRST -7
RTR-Training-01(config)#end
RTR-Training-01#
RTR-Training-01#show running-config | include clock timezone
clock timezone CRST -7 0
RTR-Training-01#
RTR-Training-01#
RTR-Training-01#clock set 11:22:30 12 September 2024
RTR-Training-01#
RTR-Training-01#show clock
11:22:35.912 CRST Thu Sep 12 2024
RTR-Training-01#
RTR-Training-01#show clock detail
11:22:48.838 CRST Thu Sep 12 2024
Time source is user configuration
RTR-Training-01#
RTR-Training-01#
```
