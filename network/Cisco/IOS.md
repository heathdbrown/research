> AI Generated using the following prompt:

> I want you to act as a Cisco Network Expert. I will ask you questions related to Cisco routing, switching, security, wireless, and network design. You should provide detailed explanations, configuration examples, troubleshooting steps, and best practices based on Cisco technologies and industry standards. My first request is: create a cheat sheet for IOSXE common commands for Campus networks

# Basic Device Operations

```bash
# Device Info
show version                     # Software, uptime, image, license
show inventory                   # Hardware inventory
show license summary             # License info
show running-config              # Current config
show startup-config              # Config on next reload
copy running-config startup-config   # Save config

# File Management
dir flash:                       # List files in flash
copy tftp: flash:                # Copy from TFTP
delete flash:<filename>          # Delete file

# Reload / Management
reload in 5                      # Reload in 5 minutes
write memory                     # Save config (legacy)
```

# Interface and VLANs

```bash
# Interface Config
interface GigabitEthernet1/0/1
 description Uplink-to-Core
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 no shut

# Access Port
interface GigabitEthernet1/0/2
 description User-Workstation
 switchport mode access
 switchport access vlan 20
 spanning-tree portfast

# VLAN Management
show vlan brief                  # List VLANs
vlan 10
 name DATA
```

# Spanning-tree

```bash
show spanning-tree               # View STP status
spanning-tree mode rapid-pvst    # Enable RPVST+
spanning-tree vlan 10 priority 4096   # Make switch root for VLAN 10
spanning-tree portfast default   # Enable portfast globally
spanning-tree bpduguard enable   # On access ports
```

# Routing (SVIs, Static, Dynamic)
```bash
# SVI
interface vlan 10
 ip address 10.10.10.1 255.255.255.0
 no shut

# Static Route
ip route 0.0.0.0 0.0.0.0 10.10.10.254

# OSPF
router ospf 10
 router-id 1.1.1.1
 network 10.10.10.0 0.0.0.255 area 0
show ip ospf neighbor

# EIGRP
router eigrp 100
 network 10.10.0.0 0.0.255.255
 passive-interface default
 no passive-interface vlan10
```

# Security

```bash
# Port Security
interface GigabitEthernet1/0/2
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 switchport port-security mac-address sticky

# ACL
ip access-list standard ACL-MGMT
 permit 10.10.10.0 0.0.0.255
 deny any log

interface vlan 10
 ip access-group ACL-MGMT in
```

# Monitoring and Troubleshooting

```bash
# Interfaces
show ip interface brief          # IPs & status
show interface gig1/0/1          # Errors, CRCs, utilization
show controllers gig1/0/1        # Physical layer info

# Neighbors
show cdp neighbors detail
show lldp neighbors

# Routing
ping 10.10.10.1
traceroute 8.8.8.8
show ip route

# Logs
show logging
terminal monitor                 # View logs in session
```

# QoS
```bash
mls qos                          # Enable QoS globally
interface gig1/0/1
 mls qos trust dscp              # Trust DSCP from upstream device
```

# StackWise and High Availability
```bash
show switch                      # Show stack members
show redundancy                  # SSO/HA status
redundancy force-switchover      # Manual failover
```

# Device Tracking
```bash
# Enable global device tracking
device-tracking

# Apply to interfaces (commonly on access)
interface GigabitEthernet1/0/10
 device-tracking attach-policy IPDT-POLICY

# Policy example
device-tracking policy IPDT-POLICY
 tracking enable

# Verification
show device-tracking database
show device-tracking all

```

# 802.1x

```bash
# Global Config
aaa new-model
aaa authentication dot1x default group radius
aaa authorization network default group radius
aaa accounting update periodic 5

# Define RADIUS servers
radius server ISE1
 address ipv4 10.10.10.10 auth-port 1812 acct-port 1813
 key Cisco123
!
aaa group server radius ISE-GRP
 server name ISE1

# Enable dot1x globally
dot1x system-auth-control

# Interface Config
interface GigabitEthernet1/0/20
 switchport mode access
 switchport access vlan 20
 authentication port-control auto        # 802.1X mode
 mab                                       # Enable MAC Authentication Bypass
 dot1x pae authenticator
 spanning-tree portfast

# Optional: Guest VLAN & Restricted VLAN
authentication event fail action next-method
authentication event server dead action authorize vlan 999
authentication event server alive action reinitialize
authentication host-mode multi-auth         # Multiple hosts allowed

```

# 802.1x Troubleshooting
```bash
# Global status
show dot1x
show dot1x all

# Per-interface status
show authentication sessions interface gig1/0/20
show authentication sessions interface gig1/0/20 details

# RADIUS connectivity
test aaa group radius ISE-GRP username testuser password testpass

# Logs
debug dot1x all
debug authentication all
debug radius authentication
debug radius accounting

# Device-tracking verification
show device-tracking database

```

# 📝 Cisco IOS-XE Regex Reference Sheet

---

## 1️⃣ Basic Regex Symbols

| Symbol    | Meaning                       |
|-----------|-------------------------------|
| `^`       | Start of line                 |
| `$`       | End of line                   |
| `.`       | Any single character          |
| `.*`      | Any string of characters      |
| `+`       | One or more of previous       |
| `?`       | Zero or one occurrence        |
| `[abc]`   | Match a, b, or c              |
| `[^abc]`  | Match anything except a, b, or c |
| `[0-9]`   | Any digit 0–9                 |
| `[a-z]`   | Any lowercase letter          |
| `[A-Z]`   | Any uppercase letter          |

---

## 2️⃣ Interface Filtering

```bash
# Only interface lines in config
show running-config | include ^interface

# Show all interfaces that are up
show ip interface brief | include up

# Show interfaces administratively down
show ip interface brief | include administratively down

# Look for errors or CRC drops
show interface | include (error|drop|CRC|lost)
```

## Vlans and macs

```bash
# Show VLANs by number pattern (2–3 digits)
show vlan brief | include ^[0-9]{2,3}

# Find MAC addresses in standard Cisco format
show mac address-table | include [0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}
```

## Routes
```bash
# Find any IPv4 address in config
show running-config | include [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+

# OSPF routes
show ip route | include ^O

# BGP routes
show ip route | include ^B

# Static routes
show ip route | include ^S
```

## Authentication / 802.1x
```bash
# Filter authentication sessions by state
show authentication sessions | include (Auth|Unauth|Failed)

```

## Logs / Syslog
```bash
# Interface link events
show logging | include %LINK

# Security / auth events
show logging | include %SEC|%AUTH

# Exclude noise
show logging | exclude ^!

```

## Older platforms ssh

```
Host <>
  HostName <>
  User <>
  StrictHostKeyChecking no
  UserKnownHostsFile /dev/null
  KexAlgorithms +diffie-hellman-group1-sha1,diffie-hellman-group14-sha1
  HostKeyAlgorithms +ssh-rsa
  PubkeyAcceptedKeyTypes +ssh-rsa
  MACs +hmac-sha1,hmac-sha2-256,hmac-sha2-512
```