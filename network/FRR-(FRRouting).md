# FRR (FRRouting)

Topology used for lab with FRR.

![image](https://github.com/heathdbrown/research/assets/618460/7861db32-ee2a-4e79-942a-a9a7425e6037)

## Interfaces

```shell
interface eth0
 ip address 10.0.1.1/30
exit
!
interface eth2
 ip address 10.1.1.1/24
```

## BGP

- Initial setup with the ASN a neighbor and remote-as
- Configure the 'network' to advertise statically in this example.
- Set soft-reconfiguration inbound
- MUST use route-maps to advertise and received routes
- prefix-lists used with route-maps, FRR allows for 'any' == 0.0.0.0/0 le 32

```shell
ip prefix-list pfx.bgp-out seq 5 permit 0.0.0.0/0 le 32
ip prefix-list pfx.bgp-in seq 5 permit any

route-map BGP-OUT permit 1
 match ip address prefix-list pfx.bgp-out
route-map BGP-IN permit 1
 match ip address prefix-list pfx.bgp-in

router bgp 65100
  neighbor 10.0.1.2 remote-as 65200
  address-family ipv4 unicast
    network 10.1.1.0/24
    neighbor 10.0.1.2 soft-reconfiguration inbound
    neighbor 10.0.1.2 route-map BGP-IN in
    neighbor 10.0.1.2 route-map BGP-OUT out
```

- validation

```shell
frr# show bgp ipv4 unicast neighbors 10.0.1.2 received-routes
BGP table version is 4, local router ID is 10.1.1.1, vrf id 0
Default local pref 100, local AS 65100
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

   Network          Next Hop            Metric LocPrf Weight Path
*> 10.2.2.0/24      10.0.1.2                               0 65200 i

Total number of prefixes 1
```


# Resources
- https://frrouting.org/
- https://www.reddit.com/r/networking/comments/hfmnun/frr_bgp_not_advertising_routes/