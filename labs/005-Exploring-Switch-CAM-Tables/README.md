# Lab 005 - Exploring Switch CAM Tables

## Objective
For this deployment to be successful, you must complete the following:
- Stage the endpoints so their Layer 2 identities are easy to spot from the switch.
- Trigger ARP-initiated traffic between PCs on the same VLAN to populate the CAM table.
- Inspect, clear, and repopulate the MAC address table to validate how the switch learns.

---

## Devices Used
- OpsServer
- CoreSwitch
- Switch 6
- PC1 / PC2

---

## Configuration Steps

### Step 1 - Basic setup
```bash
enable
configure terminal
```

### Explanation
Verify the PCs are addressed exactly as shown so any CAM table entries you see later are easy to recognize.
- Steps:
    - Log into PC1 with username cisco and password cisco, then verify its primary interface reports 192.168.1.50/24 with a default gateway of 192.168.1.1.
    - Repeat the verification on PC2 and confirm it shows 192.168.1.51/24 with the same default gateway.
    - Note which switch ports each PC uses (Et0/1 for PC1 and Et0/2 for PC2) so you can map MAC entries back to real cables.

---

### Step 2 - Main configuration
```bash
(put your CLI commands here)
```

### Explanation
Why these commands are used.

---

## Verification

```bash
show ip interface brief
show running-config
ping x.x.x.x
```

---

## Troubleshooting

### Issue 1
What went wrong?

### Diagnosis
How you found the problem.

### Fix
How you resolved it.

---

## Key Learnings
- What you learned
- What improved
- What to remember next time

---

## Improvements for Next Time
- What you would do differently