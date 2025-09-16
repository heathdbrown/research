# MikroTik CHR

## Interface
```shell
/ip address
add address=10.0.1.2/30 interface=ether1 network=10.0.1.0
add address=10.2.2.1/24 interface=ether2 network=10.2.2.0
```

## BGP
- Setup BGP filtering rules to allow for everything inbound, but block the address you are advertising
- Outbound allow the address you need to advertise
- Create a Firewall address-list for the bgp-networks
- Add a blackhole route
- Create the BGP connection
```shell
/routing filter rule
add chain=bgp-in comment="IN Filter" disabled=no rule="if (dst in 0.0.0.0/0) {accept}"
add chain=bgp-in comment="Block mine" disabled=no rule="if (dst in 10.2.2.0/24) {reject}"
add chain=bgp-out comment="out filter" disabled=no rule="if (dst == 10.2.2.0/24) {accept}"
/ip firewall address-list
add address=10.2.2.0/24 list=bgp-networks
/ip route
add blackhole disabled=no dst-address=10.2.2.0/24
/routing bgp connection
add as=65200 connect=yes disabled=no input.filter=bgp-in listen=yes local.address=10.0.1.2 .role=ebgp name=default \
    output.filter-chain=bgp-out .network=bgp-networks remote.address=10.0.1.1 .as=65100
```
# Resources
- https://help.mikrotik.com/docs/display/ROS/BGP
- https://guy-evans.com/posts/2022-11-13_bgp-ipv4-config-on-mikrotik-routerosv7/