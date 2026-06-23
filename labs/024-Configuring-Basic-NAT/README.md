# Lab 024 - Configuring Basic NAT

<table>
<tr>
<td colspan="2" valign="top">

# Objective

#### Rebuild the ISP edge connection and confirm upstream reachability from the cafe router.
#### Configure and verify static NAT, dynamic NAT, and NAT overload.
#### Demonstrate how private cafe hosts can reach simulated internet addresses through public translations.
#### Finish with multiple inside hosts sharing one public interface address using PAT/overload.

</td>
</tr>

<tr>
<td valign="top">
<img src="Images/example-topology.png">
</td>

<td valign="bottom">
<img src="Images/example-supporting-image.png">
</td>
</tr>
</table>

---

## Scenario

District Theta's cafe bunker had working LAN connectivity, but not every endpoint could reliably reach the simulated internet. The task was to rebuild the NAT configuration from the ground up, starting with a live ISP emulator and then moving through three NAT approaches:

```text
ISP edge build -> Static NAT -> Dynamic NAT pool -> NAT overload -> Verification
```

In plain English:

> The cafe uses private inside addresses, but it needs to communicate with public test addresses beyond the WAN edge. NAT allows those private hosts to be translated into public-facing addresses, either one-to-one, from a shared pool, or by overloading a single public interface address using port numbers.

---

## Lab Topology

| Device | Role | Key Interfaces |
|---|---|---|
| ISP-Rtr | Simulated ISP router | Ethernet0/0, Loopback1, Loopback8 |
| Cafe-Rtr | Cafe edge router performing NAT | Ethernet0/0, Ethernet0/1 |
| PC1 | Inside cafe host | 192.168.1.50 |
| PC2 | Inside cafe host | 192.168.1.51 |

---

## Addressing

| Device | Interface | IP Address | Purpose |
|---|---:|---:|---|
| ISP-Rtr | Ethernet0/0 | 216.0.5.1/30 | WAN link to Cafe-Rtr |
| Cafe-Rtr | Ethernet0/1 | 216.0.5.2/30 | Outside NAT interface |
| Cafe-Rtr | Ethernet0/0 | 192.168.1.1/24 | Inside cafe LAN gateway |
| ISP-Rtr | Loopback1 | 1.1.1.1/32 | Public DNS test target |
| ISP-Rtr | Loopback8 | 8.8.8.8/32 | Public DNS test target |
| PC1 | NIC | 192.168.1.50/24 | Inside NAT host |
| PC2 | NIC | 192.168.1.51/24 | Inside NAT host |

---

## Task 1 - Rebuild the ISP Edge

ISP-Rtr was configured with the standard identity and access controls:

```text
hostname ISP-Rtr
enable secret Cisco
line console 0
 password Cisco
 login
line vty 0 4
 password Cisco
 login
service password-encryption
```

The WAN interface was configured as `216.0.5.1/30`, with Cafe-Rtr already using `216.0.5.2/30` on its WAN-facing interface.

Two loopbacks were then added to ISP-Rtr to act as public internet targets:

| Loopback | IP Address |
|---|---:|
| Loopback1 | 1.1.1.1/32 |
| Loopback8 | 8.8.8.8/32 |

Cafe-Rtr was configured with a default route towards ISP-Rtr:

```text
ip route 0.0.0.0 0.0.0.0 216.0.5.1
```

Reachability was confirmed from Cafe-Rtr to:

```text
216.0.5.1
1.1.1.1
8.8.8.8
```

All three tests returned `!!!!!`, confirming the WAN path and simulated internet loopbacks were reachable.

---

## Task 2 - Publish PC1 with Static NAT

Cafe-Rtr Ethernet0/0 was configured as the NAT inside interface, and Ethernet0/1 was configured as the NAT outside interface:

```text
interface Ethernet0/0
 ip nat inside

interface Ethernet0/1
 ip nat outside
```

PC1 was then mapped to a fixed public address:

```text
ip nat inside source static 192.168.1.50 216.0.5.20
```

The NAT table confirmed the one-to-one translation:

```text
Pro Inside global      Inside local       Outside local      Outside global
--- 216.0.5.20         192.168.1.50       ---                ---
```

ISP-Rtr successfully pinged `216.0.5.20`, proving the static translation was working. A ping to PC2's private address failed, which confirmed PC2 had not been exposed by a static public mapping.

---

## Task 3 - Shift to Dynamic NAT Pooling

The static NAT rule was removed, then a standard access list was used to match the whole cafe LAN:

```text
access-list 1 permit 192.168.1.0 0.0.0.255
```

A public NAT pool was configured and associated with access list 1:

```text
ip nat pool Cafe-Public 216.0.5.50 216.0.5.100 netmask 255.255.255.0
ip nat inside source list 1 pool Cafe-Public
```

PC1 and PC2 then generated traffic towards the public loopback addresses. The NAT translation table showed each inside host receiving a different public address from the pool:

```text
icmp 216.0.5.50:738    192.168.1.50:738   1.1.1.1:738        1.1.1.1:738
--- 216.0.5.50         192.168.1.50       ---                ---
icmp 216.0.5.51:739    192.168.1.51:739   8.8.8.8:739        8.8.8.8:739
--- 216.0.5.51         192.168.1.51       ---                ---
```

This confirmed dynamic NAT was assigning separate public addresses from the configured pool.

---

## Task 4 - Consolidate with NAT Overload

The dynamic NAT pool mapping could not be removed while translations were active:

```text
%Dynamic mapping in use, cannot remove
```

The active translations were cleared, then the dynamic mapping was removed. Cafe-Rtr's inside and outside interfaces were briefly shut down to halt new translations while the final overload rule was applied:

```text
ip nat inside source list 1 interface Ethernet0/1 overload
```

After restoring both interfaces, PC1 and PC2 resumed traffic to the simulated internet. The final NAT table showed both inside hosts sharing Cafe-Rtr's WAN address, `216.0.5.2`, with unique identifiers:

```text
icmp 216.0.5.2:1024    192.168.1.50:753   1.1.1.1:753        1.1.1.1:1024
icmp 216.0.5.2:1025    192.168.1.51:753   8.8.8.8:753        8.8.8.8:1025
```

This proved NAT overload/PAT was active.

---

## Verification

| Verification Command | Result |
|---|---|
| `show ip interface brief` on ISP-Rtr | WAN and loopbacks were up/up |
| `show ip interface brief` on Cafe-Rtr | Inside and outside interfaces were up/up |
| `show ip route` on Cafe-Rtr | Default route pointed to `216.0.5.1` |
| `show running-config \| include ip nat` | Final overload rule was present |
| `show ip nat translations` | PC1 and PC2 shared `216.0.5.2` using different identifiers |
| `show ip nat statistics` | Dynamic overload mapping was active |

Final NAT statistics confirmed:

```text
Total active translations: 2 (0 static, 2 dynamic; 2 extended)
Dynamic overload mapping configured: 1
[Id: 2] access-list 1 interface Ethernet0/1 refcount 2
```

---

## Final Outcome

The lab was completed successfully.

ISP-Rtr provided the upstream WAN link and public loopback targets. Cafe-Rtr was configured with inside and outside NAT boundaries, then tested through static NAT, dynamic pool NAT, and final interface-based NAT overload.

The final working state allowed both PC1 and PC2 to reach the simulated internet while sharing the single public WAN address `216.0.5.2`.

---

## Key Takeaways

- Static NAT creates a fixed one-to-one mapping between an inside local address and an inside global address.
- Dynamic NAT allows inside hosts to borrow addresses from a configured public pool.
- NAT overload/PAT allows many inside hosts to share one public address by tracking sessions with unique identifiers.
- Existing dynamic translations may need to be cleared before a NAT rule can be removed.
- Correctly defining `ip nat inside` and `ip nat outside` is essential before NAT rules can operate properly.

