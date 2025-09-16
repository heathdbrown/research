# Subnet Masks
- Dotted Decimal Format: 255.255.255.0
- Classless Inter-Domain routing (CIDR): /24

Usage:
- Typically on interfaces, static route statements, BGP network statements

Cisco IOS, Cisco IOS-XE
```shell
interface Gi0/0
  ip address 192.168.1.1 255.255.255.0

ip route 0.0.0.0 0.0.0.0 192.168.1.254
```

Cisco NXOS
```shell
interface Gi0/0
  ip address 192.168.1.1/24

ip route 0.0.0.0/0 192.168.1.254
```

Arista EOS
```shell
interface vlan 200
  ip address 10.0.0.1/24
```

# Wildcard Masks
- Derived by subtracting each octet by 255: 0.0.0.255
- Example: 255.255.255.0 (dotted decimal format) into the wildcard mask 0.0.0.255

# Discontigous Wildcard Masks
- Matches non-contiguous IPs, typically used for saving memory on switches and routers.
- 0.0.252.255
- To calculate gather the non-contiguous subnet addresses you want to utilize across and write them in AND format to get 'address'
- Now calculate the subnet mask by performing an XOR logic
- Example from routerjockey* and one I have used before to match every nth subnet in a larger /16
  - where 10.1.0.0/16 is the larger network block, and we want to match on every 4th network and the first 3 addresses: 10.1.0.0 0.0.252.3
  - In this case, the statement is matching:  10.1.0.[1-3]; 10.1.4.[1-3], 10.1.8.[1-3]
- WARNING: typically you will derive your discontigous wildcard mask and it will match MORE than you wanted by a few addresses. Make sure that you know what those extras are before implementing.
- NOTE: if you are  going to use discontigous wildcard masks in production, on a team, it is a good idea to build tooling for validating what is going to be matched and generally have some documentation on the process to derive and the common standard or common needs that they address.


# Resources
- https://en.wikipedia.org/wiki/Wildcard_mask
- https://routerjockey.com/using-discontiguous-wildcard-masks-in-acls/
- https://www.practicalnetworking.net/stand-alone/discontiguous-wildcard-masks/
- https://packetlife.net/blog/2008/sep/11/mask-comparison-subnet-versus-wildcard/
- [Cisco NX-OS Configuraiton Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/9-x/unicast/configuration/guide/l3_cli_nxos/l3_route.pdf)
- https://www.arista.com/en/um-eos/eos-ipv4#xx1097818
- [Boson Calculator](https://calculator.boson.com/wildcard)