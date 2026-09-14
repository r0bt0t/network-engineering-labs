#!/usr/bin/env python3
"""
Generate the Lab Index from the folders under /labs.

Design goals
------------
* No per-lab metadata is required.
* Every directory directly under /labs is included.
* Lab number, display title, subject area and skills are inferred from the folder name.
* Evidence links are added only when the matching evidence path exists.
* The first run can migrate the existing "Completed Labs" and
  "Skills Progression Map" sections automatically.
* Later runs only replace the generated blocks, leaving hand-written content intact.

Run from anywhere inside the repository:
    python scripts/generate_lab_index.py

Optional:
    python scripts/generate_lab_index.py --check
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parents[1]
LABS_DIR = REPO_ROOT / "labs"
INDEX_FILE = REPO_ROOT / "Lab-index.md"

CATALOGUE_START = "<!-- AUTO-LAB-CATALOGUE:START -->"
CATALOGUE_END = "<!-- AUTO-LAB-CATALOGUE:END -->"
SKILLS_START = "<!-- AUTO-SKILLS:START -->"
SKILLS_END = "<!-- AUTO-SKILLS:END -->"


# Words that should keep their conventional networking capitalisation.
TOKEN_CASE = {
    "aaa": "AAA",
    "acl": "ACL",
    "acls": "ACLs",
    "arp": "ARP",
    "asbr": "ASBR",
    "cam": "CAM",
    "cdp": "CDP",
    "cli": "CLI",
    "dai": "DAI",
    "dhcp": "DHCP",
    "dns": "DNS",
    "dscp": "DSCP",
    "dtp": "DTP",
    "eigrp": "EIGRP",
    "eui64": "EUI-64",
    "eui-64": "EUI-64",
    "ftp": "FTP",
    "glbp": "GLBP",
    "gre": "GRE",
    "hsrp": "HSRP",
    "icmp": "ICMP",
    "ios": "IOS",
    "ip": "IP",
    "ipv4": "IPv4",
    "ipv6": "IPv6",
    "isp": "ISP",
    "lacp": "LACP",
    "lan": "LAN",
    "lans": "LANs",
    "lldp": "LLDP",
    "mac": "MAC",
    "mib": "MIB",
    "nat": "NAT",
    "ntp": "NTP",
    "ospf": "OSPF",
    "pagp": "PAgP",
    "pat": "PAT",
    "pvst": "PVST",
    "qos": "QoS",
    "roas": "ROAS",
    "rstp": "RSTP",
    "slaac": "SLAAC",
    "snmp": "SNMP",
    "soho": "SOHO",
    "ssh": "SSH",
    "stp": "STP",
    "svi": "SVI",
    "svis": "SVIs",
    "tcp": "TCP",
    "tftp": "TFTP",
    "udp": "UDP",
    "vlan": "VLAN",
    "vlans": "VLANs",
    "vlsm": "VLSM",
    "vpn": "VPN",
    "vrrp": "VRRP",
    "vtp": "VTP",
    "wan": "WAN",
    "wans": "WANs",
    "wlc": "WLC",
    "wlan": "WLAN",
    "wlans": "WLANs",
}

LOWERCASE_WORDS = {
    "a", "an", "and", "as", "at", "between", "by", "for", "from",
    "in", "into", "of", "on", "or", "the", "to", "via", "with",
}


@dataclass(frozen=True)
class SkillRule:
    pattern: str
    skill: str
    group: str


# Rules intentionally overlap. For example, a title containing "OSPF ACL"
# should surface both OSPF and ACL skills.
SKILL_RULES = [
    # Network fundamentals / operations
    SkillRule(r"\b(base|basic).*config|\bcisco\b.*config", "Cisco IOS baseline configuration", "Network Fundamentals"),
    SkillRule(r"\binterface(s)?\b", "Interface configuration and verification", "Network Fundamentals"),
    SkillRule(r"interface counter|counter(s)?\b", "Interface counters and diagnostics", "Network Fundamentals"),
    SkillRule(r"\bipv4\b|ip address|addressing", "IPv4 addressing", "Network Fundamentals"),
    SkillRule(r"\bsubnet|vlsm\b", "Subnetting and VLSM", "Network Fundamentals"),
    SkillRule(r"\bmac\b|\bcam\b", "MAC/CAM table analysis", "Network Fundamentals"),
    SkillRule(r"\barp\b", "ARP operation and analysis", "Network Fundamentals"),
    SkillRule(r"cdp|lldp|discovery", "Network discovery with CDP/LLDP", "Network Operations & Services"),
    SkillRule(r"finding|tracking|recon|troubleshoot|diagnos|fault", "Network troubleshooting", "Network Fundamentals"),

    # Network access
    SkillRule(r"\bswitch(ing|es)?\b", "Layer 2 switching", "Network Access"),
    SkillRule(r"\bvlan(s)?\b", "VLAN configuration and segmentation", "Network Access"),
    SkillRule(r"trunk|802[.\- ]?1q", "802.1Q trunking", "Network Access"),
    SkillRule(r"native vlan", "Native VLAN design and control", "Network Access"),
    SkillRule(r"router[- ]?on[- ]?a[- ]?stick|\broas\b|inter[- ]?vlan|routing between vlan", "Inter-VLAN routing / ROAS", "Network Access"),
    SkillRule(r"\bsvi(s)?\b|multilayer", "Layer 3 switching and SVIs", "Network Access"),
    SkillRule(r"\bdtp\b|legacy trunk", "DTP hardening", "Network Security"),
    SkillRule(r"\bvtp\b", "VTP and VLAN management", "Network Access"),
    SkillRule(r"\bstp\b|spanning tree", "Spanning Tree Protocol", "Network Access"),
    SkillRule(r"\brstp\b|rapid[- ]?pvst|rapid spanning", "Rapid STP / Rapid PVST+", "Network Access"),
    SkillRule(r"etherchannel|\blacp\b|\bpagp\b", "EtherChannel, LACP and PAgP", "Network Access"),
    SkillRule(r"voice vlan|voip", "Voice VLANs", "Network Access"),

    # IP connectivity
    SkillRule(r"routing table|route selection|administrative distance", "Routing-table analysis and route selection", "IP Connectivity"),
    SkillRule(r"static rout", "Static routing", "IP Connectivity"),
    SkillRule(r"default rout", "Default routing", "IP Connectivity"),
    SkillRule(r"floating static|backup route|failover", "Floating static routes and failover", "IP Connectivity"),
    SkillRule(r"\beigrp\b", "EIGRP", "IP Connectivity"),
    SkillRule(r"\bospf\b", "OSPF", "IP Connectivity"),
    SkillRule(r"passive interface", "Passive-interface design", "IP Connectivity"),
    SkillRule(r"reference bandwidth", "OSPF reference-bandwidth tuning", "IP Connectivity"),
    SkillRule(r"hello|dead timer|neighbor|neighbour|adjacency", "Routing adjacency and timer troubleshooting", "IP Connectivity"),
    SkillRule(r"\bwan\b|serial link", "WAN connectivity", "IP Connectivity"),
    SkillRule(r"\bgre\b|tunnel", "GRE tunnelling", "IP Connectivity"),

    # IPv6
    SkillRule(r"\bipv6\b", "IPv6 addressing and routing", "IPv6"),
    SkillRule(r"\bslaac\b", "SLAAC", "IPv6"),
    SkillRule(r"eui[- ]?64", "EUI-64 addressing", "IPv6"),
    SkillRule(r"link[- ]?local", "IPv6 link-local addressing", "IPv6"),
    SkillRule(r"dual[- ]?stack", "IPv4/IPv6 dual stack", "IPv6"),

    # IP services / management
    SkillRule(r"static nat", "Static NAT", "IP Services"),
    SkillRule(r"dynamic nat", "Dynamic NAT", "IP Services"),
    SkillRule(r"nat overload|\bpat\b", "PAT / NAT overload", "IP Services"),
    SkillRule(r"\bnat\b", "Network Address Translation", "IP Services"),
    SkillRule(r"internet|\bisp\b", "Internet edge connectivity", "IP Services"),
    SkillRule(r"\bdhcp\b", "DHCP", "IP Services"),
    SkillRule(r"dhcp relay|helper", "DHCP relay", "IP Services"),
    SkillRule(r"\bdns\b|name resolution", "DNS and name resolution", "IP Services"),
    SkillRule(r"\bntp\b|time synchron", "NTP time synchronisation", "Network Operations & Services"),
    SkillRule(r"\bsnmp\b|\bmib\b", "SNMP monitoring and MIB queries", "Network Operations & Services"),
    SkillRule(r"syslog|logging", "Syslog and centralised logging", "Network Operations & Services"),
    SkillRule(r"\bssh\b", "SSH secure remote management", "Network Operations & Services"),
    SkillRule(r"\bftp\b|\btftp\b|file transfer|ios upgrade", "Cisco IOS file transfer and upgrade", "Network Operations & Services"),

    # Security
    SkillRule(r"standard acl", "Standard IPv4 ACLs", "Network Security"),
    SkillRule(r"extended acl", "Extended IPv4 ACLs", "Network Security"),
    SkillRule(r"\bacl(s)?\b|access control list", "Access control lists", "Network Security"),
    SkillRule(r"port security", "Switch port security", "Network Security"),
    SkillRule(r"dhcp snooping", "DHCP Snooping", "Network Security"),
    SkillRule(r"dynamic arp inspection|\bdai\b", "Dynamic ARP Inspection", "Network Security"),
    SkillRule(r"\baaa\b", "AAA", "Network Security"),
    SkillRule(r"\bvpn\b", "VPN fundamentals", "Network Security"),
    SkillRule(r"harden|lock(ing)? down|secure|security", "Network hardening", "Network Security"),

    # Availability / QoS / wireless
    SkillRule(r"\bhsrp\b|first[- ]?hop redundancy", "HSRP gateway redundancy", "High Availability"),
    SkillRule(r"\bvrrp\b", "VRRP", "High Availability"),
    SkillRule(r"\bglbp\b", "GLBP", "High Availability"),
    SkillRule(r"\bqos\b|\bdscp\b|traffic classification", "QoS, DSCP and traffic classification", "Quality of Service"),
    SkillRule(r"wireless|\bwlan(s)?\b|\bwlc\b", "Wireless LAN and WLC configuration", "Wireless"),
]


# Primary subject areas used to organise the catalogue.
CATEGORY_RULES = [
    ("Wireless", r"wireless|\bwlan(s)?\b|\bwlc\b"),
    ("Quality of Service", r"\bqos\b|\bdscp\b|traffic classification"),
    ("High Availability", r"\bhsrp\b|\bvrrp\b|\bglbp\b|first[- ]?hop redundancy"),
    ("IPv6", r"\bipv6\b|\bslaac\b|eui[- ]?64|link[- ]?local|dual[- ]?stack"),
    ("Network Security", r"\bacl(s)?\b|access control|port security|dhcp snooping|dynamic arp inspection|\bdai\b|\baaa\b|\bvpn\b|harden|lock(ing)? down|security"),
    ("Network Operations & Services", r"\bntp\b|\bdns\b|\bdhcp\b|\bsnmp\b|\bmib\b|syslog|logging|\bssh\b|\bftp\b|\btftp\b|cdp|lldp|discovery"),
    ("Tunnels & WAN", r"\bgre\b|tunnel|\bwan\b|serial link"),
    ("NAT & Internet Connectivity", r"\bnat\b|\bpat\b|internet|\bisp\b"),
    ("Dynamic Routing", r"\bospf\b|\beigrp\b|\brip\b"),
    ("Routing Fundamentals", r"routing|route selection|routing table|static route|default route|local routing"),
    ("VLANs & Inter-VLAN Routing", r"\bvlan(s)?\b|trunk|802[.\- ]?1q|\bdtp\b|\bvtp\b|\bsvi(s)?\b|router[- ]?on[- ]?a[- ]?stick|\broas\b|inter[- ]?vlan"),
    ("Spanning Tree & EtherChannel", r"\bstp\b|spanning tree|\brstp\b|rapid[- ]?pvst|etherchannel|\blacp\b|\bpagp\b"),
    ("Switching Fundamentals", r"\bswitch(ing|es)?\b|\bcam\b|\bmac\b|ethernet"),
    ("Troubleshooting & Discovery", r"finding|tracking|recon|troubleshoot|diagnos|counter|discovery"),
    ("Integrated Network Projects", r"\bsoho\b|castle|cafe|shelter|enterprise|campus|project|mega[- ]?lab"),
]

CATEGORY_DESCRIPTIONS = {
    "Switching Fundamentals": "Layer 2 switching, device interfaces, MAC/CAM behaviour and foundational switch operation.",
    "VLANs & Inter-VLAN Routing": "VLAN segmentation, trunking and Layer 3 connectivity between VLANs.",
    "Spanning Tree & EtherChannel": "Loop prevention, resilient Layer 2 design and bundled links.",
    "Routing Fundamentals": "Connected, static and default routing together with routing-table interpretation.",
    "Dynamic Routing": "Dynamic route exchange, neighbour relationships and routing-protocol behaviour.",
    "NAT & Internet Connectivity": "Address translation, PAT and edge connectivity towards an ISP.",
    "IPv6": "IPv6 addressing, autoconfiguration, dual stack and IPv6 routing.",
    "Network Operations & Services": "Core network services, monitoring, logging, discovery and secure device management.",
    "Network Security": "Traffic filtering, Layer 2 protections and infrastructure hardening.",
    "High Availability": "Gateway resilience, failover behaviour and first-hop redundancy.",
    "Tunnels & WAN": "Point-to-point, WAN and tunnel technologies.",
    "Quality of Service": "Traffic classification, marking and quality-of-service policy concepts.",
    "Wireless": "Wireless LAN and controller configuration.",
    "Troubleshooting & Discovery": "Finding devices, validating state and isolating faults with operational data.",
    "Integrated Network Projects": "Broader labs that combine multiple technologies in a realistic topology.",
    "Other Labs": "Additional networking labs that do not yet match a defined subject rule.",
}

CATEGORY_ORDER = [
    "Switching Fundamentals",
    "VLANs & Inter-VLAN Routing",
    "Spanning Tree & EtherChannel",
    "Routing Fundamentals",
    "Dynamic Routing",
    "NAT & Internet Connectivity",
    "IPv6",
    "Network Operations & Services",
    "Network Security",
    "High Availability",
    "Tunnels & WAN",
    "Quality of Service",
    "Wireless",
    "Troubleshooting & Discovery",
    "Integrated Network Projects",
    "Other Labs",
]

SKILL_GROUP_ORDER = [
    "Network Fundamentals",
    "Network Access",
    "IP Connectivity",
    "IPv6",
    "IP Services",
    "Network Operations & Services",
    "Network Security",
    "High Availability",
    "Quality of Service",
    "Wireless",
]


@dataclass
class Lab:
    folder: Path
    folder_name: str
    lab_id: str | None
    number: int | None
    title: str
    title_search: str
    category: str
    skills: list[str]
    skill_groups: dict[str, str]
    readme_exists: bool
    evidence_link: str | None


def markdown_url(path: str) -> str:
    """URL-encode spaces/special characters while retaining path separators."""
    return quote(path.replace("\\", "/"), safe="/-._~")


def smart_title(raw: str) -> str:
    raw = re.sub(r"[_\-]+", " ", raw).strip()
    raw = re.sub(r"\s+", " ", raw)
    if not raw:
        return "Untitled Lab"

    words = raw.split(" ")
    output: list[str] = []

    for i, word in enumerate(words):
        # Keep slash-separated terms readable (e.g. IPv4/IPv6).
        pieces = word.split("/")
        formatted_pieces = []
        for piece in pieces:
            key = piece.lower().strip("()[]{}.,:")
            if key in TOKEN_CASE:
                replacement = TOKEN_CASE[key]
                prefix = piece[: len(piece) - len(piece.lstrip("([{\"'"))]
                suffix = piece[len(piece.rstrip(")]}.,:;\"'")) :]
                formatted = f"{prefix}{replacement}{suffix}"
            elif i > 0 and piece.lower() in LOWERCASE_WORDS:
                formatted = piece.lower()
            else:
                formatted = piece[:1].upper() + piece[1:] if piece else piece
            formatted_pieces.append(formatted)
        output.append("/".join(formatted_pieces))

    title = " ".join(output)
    # Common phrases look better with these conventional forms.
    replacements = {
        r"\bRouter On A Stick\b": "Router-on-a-Stick",
        r"\bRouter on a Stick\b": "Router-on-a-Stick",
        r"\bInter Vlan\b": "Inter-VLAN",
        r"\bInter VLAN\b": "Inter-VLAN",
        r"\bLayer 2\b": "Layer 2",
        r"\bLayer 3\b": "Layer 3",
    }
    for pattern, replacement in replacements.items():
        title = re.sub(pattern, replacement, title, flags=re.IGNORECASE)
    return title


def parse_folder_name(folder_name: str) -> tuple[str | None, int | None, str]:
    # Examples accepted:
    # 001-Basic-Switch-Configuration
    # 031_Configuring_OSPF
    # 73 Something Else
    match = re.match(r"^\s*(\d{1,5})(?:[\s._-]+)?(.*)$", folder_name)
    if match:
        number = int(match.group(1))
        lab_id = str(number).zfill(max(3, len(match.group(1))))
        raw_title = match.group(2).strip(" -_.") or f"Lab {lab_id}"
        return lab_id, number, smart_title(raw_title)

    return None, None, smart_title(folder_name)


def infer_skills(title: str) -> tuple[list[str], dict[str, str]]:
    search = title.lower()
    skills: list[str] = []
    groups: dict[str, str] = {}

    for rule in SKILL_RULES:
        if re.search(rule.pattern, search, flags=re.IGNORECASE):
            if rule.skill not in skills:
                skills.append(rule.skill)
                groups[rule.skill] = rule.group

    # Useful fallbacks when a title describes a practical task but contains
    # none of the explicit protocol/technology keywords above.
    if not skills:
        if re.search(r"configur|implement|creat|deploy|build|setup|set up", search):
            skills.append("Cisco IOS configuration")
            groups["Cisco IOS configuration"] = "Network Fundamentals"
        elif re.search(r"understand|concept|purpose|explor|read|analyse|analyz", search):
            skills.append("Network concepts and verification")
            groups["Network concepts and verification"] = "Network Fundamentals"
        else:
            skills.append("Network design and implementation")
            groups["Network design and implementation"] = "Network Fundamentals"

    # Generic configuration skill is useful as a second skill only when the
    # title explicitly says this is a configuration/implementation exercise.
    if (
        re.search(r"configur|implement|creat|deploy", search)
        and "Cisco IOS configuration" not in skills
        and len(skills) < 5
    ):
        skills.append("Cisco IOS configuration")
        groups["Cisco IOS configuration"] = "Network Fundamentals"

    return skills, groups


def infer_category(title: str) -> str:
    search = title.lower()
    for category, pattern in CATEGORY_RULES:
        if re.search(pattern, search, flags=re.IGNORECASE):
            return category
    return "Other Labs"


def discover_evidence(folder: Path) -> str | None:
    candidates = [
        folder / "evidence" / "raw-cli-output.md",
        folder / "evidence" / "README.md",
        folder / "evidence",
    ]
    for candidate in candidates:
        if candidate.is_file() or candidate.is_dir():
            rel = candidate.relative_to(REPO_ROOT).as_posix()
            return markdown_url(rel + ("/" if candidate.is_dir() else ""))
    return None


def discover_labs() -> list[Lab]:
    if not LABS_DIR.exists():
        raise FileNotFoundError(f"Lab directory not found: {LABS_DIR}")

    folders = sorted(
        (p for p in LABS_DIR.iterdir() if p.is_dir() and not p.name.startswith(".")),
        key=lambda p: p.name.lower(),
    )

    labs: list[Lab] = []
    for folder in folders:
        lab_id, number, title = parse_folder_name(folder.name)
        skills, skill_groups = infer_skills(title)
        labs.append(
            Lab(
                folder=folder,
                folder_name=folder.name,
                lab_id=lab_id,
                number=number,
                title=title,
                title_search=title.lower(),
                category=infer_category(title),
                skills=skills,
                skill_groups=skill_groups,
                readme_exists=(folder / "README.md").exists(),
                evidence_link=discover_evidence(folder),
            )
        )

    labs.sort(
        key=lambda lab: (
            lab.number is None,
            lab.number if lab.number is not None else 10**9,
            lab.title.lower(),
        )
    )
    return labs


def lab_link(lab: Lab) -> str:
    rel = lab.folder.relative_to(REPO_ROOT).as_posix().rstrip("/") + "/"
    return markdown_url(rel)


def lab_label(lab: Lab) -> str:
    if lab.lab_id:
        return f"LAB {lab.lab_id} · {lab.title}"
    return lab.title


def render_summary_table(labs: list[Lab]) -> str:
    categories = len({lab.category for lab in labs})
    skills = len({skill for lab in labs for skill in lab.skills})
    documented = sum(lab.readme_exists for lab in labs)
    return "\n".join(
        [
            '<table>',
            '  <tr>',
            f'    <td align="center" width="25%"><strong>{len(labs)}</strong><br><sub>Lab folders</sub></td>',
            f'    <td align="center" width="25%"><strong>{categories}</strong><br><sub>Subject areas</sub></td>',
            f'    <td align="center" width="25%"><strong>{skills}</strong><br><sub>Inferred skills</sub></td>',
            f'    <td align="center" width="25%"><strong>{documented}</strong><br><sub>README files found</sub></td>',
            '  </tr>',
            '</table>',
        ]
    )


def render_lab_card(lab: Lab) -> str:
    title_url = lab_link(lab)
    skills_text = html.escape(" · ".join(lab.skills))
    status = "Documented" if lab.readme_exists else "Folder present"
    visible_label = html.escape(lab_label(lab))

    links = [f'<a href="{title_url}">View lab →</a>']
    if lab.evidence_link:
        links.append(f'<a href="{lab.evidence_link}">CLI evidence</a>')

    return "\n".join(
        [
            '<td width="50%" valign="top">',
            f'  <strong><a href="{title_url}">{visible_label}</a></strong><br>',
            f'  <sub><strong>Skills:</strong> {skills_text}</sub><br>',
            f'  <sub><strong>Status:</strong> {status}</sub><br><br>',
            f'  <sub>{" &nbsp;·&nbsp; ".join(links)}</sub>',
            '</td>',
        ]
    )


def render_category_cards(category_labs: list[Lab]) -> str:
    lines = ["<table>"]
    for i in range(0, len(category_labs), 2):
        lines.append("  <tr>")
        lines.append(render_lab_card(category_labs[i]))
        if i + 1 < len(category_labs):
            lines.append(render_lab_card(category_labs[i + 1]))
        else:
            lines.append('<td width="50%"></td>')
        lines.append("  </tr>")
    lines.append("</table>")
    return "\n".join(lines)


def render_catalogue(labs: list[Lab]) -> str:
    by_category: dict[str, list[Lab]] = defaultdict(list)
    for lab in labs:
        by_category[lab.category].append(lab)

    lines = [
        CATALOGUE_START,
        "## Lab Catalogue",
        "",
        "> This catalogue is generated automatically from the folder names in `labs/`. "
        "Subject areas and skills are inferred from each lab title, so no per-lab metadata is required.",
        "",
        render_summary_table(labs),
        "",
    ]

    for category in CATEGORY_ORDER:
        category_labs = by_category.get(category)
        if not category_labs:
            continue
        lines.extend(
            [
                f"### {category}",
                "",
                CATEGORY_DESCRIPTIONS.get(category, ""),
                "",
                render_category_cards(category_labs),
                "",
            ]
        )

    lines.extend([CATALOGUE_END])
    return "\n".join(lines)


def render_skills(labs: list[Lab]) -> str:
    # skill -> group, lab list
    skill_labs: dict[str, list[Lab]] = defaultdict(list)
    skill_group: dict[str, str] = {}

    for lab in labs:
        for skill in lab.skills:
            skill_labs[skill].append(lab)
            skill_group[skill] = lab.skill_groups.get(skill, "Network Fundamentals")

    by_group: dict[str, list[str]] = defaultdict(list)
    for skill in skill_labs:
        by_group[skill_group[skill]].append(skill)

    lines = [
        SKILLS_START,
        "## Skills Progression & Coverage",
        "",
        "> Generated from the current lab titles. The linked lab numbers show where each skill is practised "
        "or demonstrated; they are not manually maintained.",
        "",
    ]

    ordered_groups = SKILL_GROUP_ORDER + sorted(
        group for group in by_group if group not in SKILL_GROUP_ORDER
    )

    for group in ordered_groups:
        skills = by_group.get(group)
        if not skills:
            continue

        lines.extend(
            [
                f"### {group}",
                "",
                "| Skill | Labs |",
                "| --- | --- |",
            ]
        )

        for skill in sorted(skills, key=str.lower):
            linked_labs = []
            for lab in skill_labs[skill]:
                label = lab.lab_id or lab.title
                linked_labs.append(f"[{label}]({lab_link(lab)})")
            lines.append(f"| **{skill}** | {' · '.join(linked_labs)} |")
        lines.append("")

    lines.append(SKILLS_END)
    return "\n".join(lines)


def replace_marker_block(content: str, start: str, end: str, new_block: str) -> tuple[str, bool]:
    if start not in content or end not in content:
        return content, False

    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end),
        flags=re.DOTALL,
    )
    return pattern.sub(new_block, content, count=1), True


def heading_match(content: str, names: list[str]) -> re.Match[str] | None:
    escaped_names = "|".join(re.escape(name) for name in names)
    # Supports both standard "## Heading" and the older "**## Heading**" form.
    pattern = re.compile(
        rf"(?mi)^[ \t]*(?:\*\*)?##[ \t]+(?:{escaped_names})(?:\*\*)?[ \t]*$"
    )
    return pattern.search(content)


def find_next_h2(content: str, start_pos: int) -> int:
    pattern = re.compile(r"(?mi)^[ \t]*(?:\*\*)?##[ \t]+.+?(?:\*\*)?[ \t]*$")
    match = pattern.search(content, start_pos)
    return match.start() if match else len(content)


def migrate_or_insert_catalogue(content: str, block: str) -> str:
    updated, replaced = replace_marker_block(
        content, CATALOGUE_START, CATALOGUE_END, block
    )
    if replaced:
        return updated

    old = heading_match(content, ["Completed Labs", "Lab Catalogue"])
    skills = heading_match(
        content,
        ["Skills Progression Map", "Skills Progression & Coverage", "Skills Coverage"],
    )

    if old:
        end = skills.start() if skills and skills.start() > old.start() else find_next_h2(content, old.end())
        return content[: old.start()].rstrip() + "\n\n" + block + "\n\n" + content[end:].lstrip()

    if skills:
        return content[: skills.start()].rstrip() + "\n\n" + block + "\n\n" + content[skills.start():].lstrip()

    return content.rstrip() + "\n\n---\n\n" + block + "\n"


def migrate_or_insert_skills(content: str, block: str) -> str:
    updated, replaced = replace_marker_block(
        content, SKILLS_START, SKILLS_END, block
    )
    if replaced:
        return updated

    old = heading_match(
        content,
        ["Skills Progression Map", "Skills Progression & Coverage", "Skills Coverage"],
    )
    if old:
        end = find_next_h2(content, old.end())
        return content[: old.start()].rstrip() + "\n\n" + block + "\n\n" + content[end:].lstrip()

    return content.rstrip() + "\n\n---\n\n" + block + "\n"


def default_index_header() -> str:
    return """---
title: Lab Index
---

# Lab Index

<table>
  <tr>
    <td valign="top">
      <h3>This page provides an overview of all completed and planned CCNA labs in this repository.</h3>
      <h3>Each lab is designed to demonstrate practical networking skills, configuration knowledge, and troubleshooting ability.</h3>
      <p>
        The work here is entirely of my own making but has been completed whilst I follow the
        <strong>Summer of CCNA</strong> CCNA training course hosted by the
        <strong>Network Chuck Academy</strong>.
      </p>
    </td>
  </tr>
</table>

---
"""


def build_index(existing: str, labs: list[Lab]) -> str:
    catalogue = render_catalogue(labs)
    skills = render_skills(labs)

    content = existing if existing.strip() else default_index_header()
    content = migrate_or_insert_catalogue(content, catalogue)
    content = migrate_or_insert_skills(content, skills)

    # Keep the file stable across platforms/runs.
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    content = re.sub(r"\n{4,}", "\n\n\n", content)
    return content.rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Lab-index.md from /labs folder names.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit 1 if Lab-index.md would change.",
    )
    args = parser.parse_args()

    try:
        labs = discover_labs()
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    existing = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""
    generated = build_index(existing, labs)

    if args.check:
        if generated != existing:
            print("Lab-index.md is out of date.")
            return 1
        print(f"Lab-index.md is current ({len(labs)} lab folders).")
        return 0

    if generated == existing:
        print(f"No changes required: {len(labs)} lab folders already indexed.")
        return 0

    INDEX_FILE.write_text(generated, encoding="utf-8")
    category_count = len({lab.category for lab in labs})
    skill_count = len({skill for lab in labs for skill in lab.skills})
    print(
        f"Updated {INDEX_FILE.name}: "
        f"{len(labs)} lab folders, {category_count} subject areas, {skill_count} inferred skills."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
