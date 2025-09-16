|cisco IOS|ExtremeOS|
|---------|---------|
|show int status|show ports|
|show vlan|show vlan|

# VLANs
```console
create vlan 2
configure vlan 2 name LAN
```
## VLAN attach to ports
```console
configure vlan LAN tag 2
configure vlan LAN add ports 12 untagged
```
## VLAN IP address
```console
configure vlan LAN ipaddress 10.4.4.1/24
enable ipforwarding vlan LAN
```
# PORTS
```console
configure ports 12 display-string PC4
enable ports 12
```
# BGP
```console
create vlan WAN
configure WAN tag 100
configure WAN add ports 1 untagged
configure WAN ipaddress 10.0.1.18/30
```

```console
configure bgp routerid 10.4.0.4
configure bgp AS-number 65400
create bgp neighbor 10.0.1.17 remote-AS-number 65100
enable bgp neighbor 10.0.1.17
enable bgp
```

```console
configure bgp add network 10.4.4.0/24
```
# References
- [Command Line Interface Cross-Reference Guide
ExtremeXOS, EOS, VOSS, BOSS, Cisco IOS](https://documentation.extremenetworks.com/CLI_X-Ref/1.0/CLI_X-Ref_Guide_1.0.pdf)