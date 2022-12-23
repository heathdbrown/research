# IP Commands
- [RedHat IP Command Cheat Sheet](https://access.redhat.com/sites/default/files/attachments/rh_ip_command_cheatsheet_1214_jcs_print.pdf)

# IP Queries
## ip addr 
```bash
┌──(kali㉿kali)-[~]
└─$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:f2:48:4e brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic noprefixroute eth0
       valid_lft 86382sec preferred_lft 86382sec
    inet6 fe80::dd54:acdb:d36c:66b7/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:81:83:81 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::543a:70d2:26da:d9f3/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```
## ip addr show dev eth1
```bash
┌──(kali㉿kali)-[~]
└─$ ip addr show dev eth1
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:81:83:81 brd ff:ff:ff:ff:ff:ff
```

## ip link
```bash
┌──(kali㉿kali)-[~]
└─$ ip link              
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:f2:48:4e brd ff:ff:ff:ff:ff:ff
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:81:83:81 brd ff:ff:ff:ff:ff:ff
```

## ip link show dev eth1
```bash
┌──(kali㉿kali)-[~]
└─$ ip link show dev eth1
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:81:83:81 brd ff:ff:ff:ff:ff:ff
```

## ip -s link
```bash
┌──(kali㉿kali)-[~]
└─$ ip -s link           
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    RX:  bytes packets errors dropped  missed   mcast           
           480       8      0       0       0       0 
    TX:  bytes packets errors dropped carrier collsns           
           480       8      0       0       0       0 
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:f2:48:4e brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed   mcast           
           590       1      0       0       0       0 
    TX:  bytes packets errors dropped carrier collsns           
          3220      25      0       0       0       0 
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:81:83:81 brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed   mcast           
             0       0      0       0       0       0 
    TX:  bytes packets errors dropped carrier collsns           
         19451     116      0       0       0       0 
```                                                                                                                             

## ip -s link show dev eth1
```bash           
┌──(kali㉿kali)-[~]
└─$ ip -s link show dev eth1
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:81:83:81 brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed   mcast           
             0       0      0       0       0       0 
    TX:  bytes packets errors dropped carrier collsns           
         19451     116      0       0       0       0
```

## ip route
```bash
┌──(kali㉿kali)-[~]
└─$ ip route                
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 metric 100 
```

## ip maddr
```bash
┌──(kali㉿kali)-[~]
└─$ ip maddr
1:      lo
        inet  224.0.0.1
        inet6 ff02::1
        inet6 ff01::1
2:      eth0
        link  01:00:5e:00:00:01
        link  33:33:00:00:00:01
        link  33:33:ff:6c:66:b7
        inet  224.0.0.1
        inet6 ff02::1:ff6c:66b7
        inet6 ff02::1
        inet6 ff01::1
3:      eth1
        link  01:00:5e:00:00:01
        link  33:33:00:00:00:01
        link  33:33:ff:da:d9:f3
        inet  224.0.0.1
        inet6 ff02::1:ffda:d9f3
        inet6 ff02::1
        inet6 ff01::1
```

## ip maddr show dev eth1

```bash
┌──(kali㉿kali)-[~]
└─$ ip maddr show dev eth1
3:      eth1
        link  01:00:5e:00:00:01
        link  33:33:00:00:00:01
        link  33:33:ff:da:d9:f3
        inet  224.0.0.1
        inet6 ff02::1:ffda:d9f3
        inet6 ff02::1
        inet6 ff01::1
```

## ip neigh
```bash

```

## ip neigh show dev eth1
```bash
```

## ip help

## ip addr help

## ip link help

## ip neigh help

# Modifying Address and Link Properties

## ip addr add 192.168.1.1/24 dev eth1

## ip addr del 192.168.1.1/24 dev eth1

## ip link set eth1 up

## ip link set eth1 down

## ip link set eth1 mtu 9000

## ip link set eth1 promisc on

# Adjusting and viewing routes

## ip route add default via 192.168.1.1 dev eth1

## ip route add 192.168.1.0/24 via 192.168.1.1

## ip route add 192.168.1.0/24 dev eth1

## ip route delete 192.168.1.0/24 via 192.168.1.1

## ip route replace 192.168.1.0/24 dev eth1

## ip route get 192.168.1.5
```bash
┌──(kali㉿kali)-[~]
└─$ ip route get 192.168.1.5
192.168.1.5 via 10.0.2.2 dev eth0 src 10.0.2.15 uid 1000 
    cache 
```

# Managing the arp table

## ip neigh add 192.168.1.1 lladdr 1:2:3:4:5:6 dev eth1

## ip neigh del 192.168.1.1 dev eth1

## ip neigh replace 192.168.1.1 lladdr 1:2:3:4:5:6 dev eth1

# Useful Networking commands not from ip route

## arpping -I eth0 192.168.1.1

## arping -D -I eth0 192.168.1.1

## ethtool -g eth0

## ethtool -i eth0

## ethtool -p eth0

## ethtool -S eth0

## ss -a

## ss -e

## ss -o

## ss -n

## ss -p