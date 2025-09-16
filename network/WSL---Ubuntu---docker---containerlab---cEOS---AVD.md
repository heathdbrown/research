# prerequisites for ansible
I use pipx and uv on various hosts

source ~/.local/pipx/venvs/ansible/bin/activate
python -m pip install pyavd anta cvprac netaddr treelib jsonschema

it complained about ansible version

python -m pip install ansible --upgrade

# issues
## Debian Issues
* Debian and cEOS BGP peer group would stop BGP from listening on IPv4
```
netstat -pant | grep 179
```
* Debian and cEOS MLAG stays in inactive state

Fixed: by moving to Ubuntu

## Ubuntu Issues
```
TASK [arista.avd.eos_config_deploy_eapi : Replace configuration with intended configuration] *********************************************************************************************************************************************************************************
fatal: [DC1_LEAF1A]: FAILED! => changed=false
  module_stderr: 'Could not connect to https://172.100.100.4:443/command-api: [Errno 113] No route to host'
  module_stdout: ''
  msg: |-
    MODULE FAILURE
    See stdout/stderr for the exact error
```
### Removed a bad route
```
found by ip route | grep linkdown
sudo ip route del 172.100.100.0/24 dev br-2bd738ba2caf
```
### client issues with creating lacp interfaces
```
bash host_l3_config/l3_build.sh

[INFO] Configuring clab-avdirb-client1
client1
vconfig: ioctl error for add: No such device
ifconfig: SIOCSIFADDR: No such device
ip: ioctl 0x8913 failed: No such device
ip: can't find device 'team0.110'
ifconfig: team0.110: error fetching interface information: Device not found
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         172.100.100.1   0.0.0.0         UG    0      0        0 eth0
172.100.100.0   0.0.0.0         255.255.255.0   U     0      0        0 eth0
```
tried adding openrc for the rc-update command but this did not work

### Arista MLAG not coming up

```
DC1_LEAF1A#show mlag
MLAG Configuration:
domain-id                          :           DC1_LEAF1
local-interface                    :            Vlan4094
peer-address                       :        10.255.252.1
peer-link                          :       Port-Channel3
hb-peer-address                    :             0.0.0.0
peer-config                        :

MLAG Status:
state                              :            Inactive
negotiation status                 :          Connecting
peer-link status                   :                  Up
local-int status                   :                  Up
system-id                          :   00:00:00:00:00:00
dual-primary detection             :            Disabled
dual-primary interface errdisabled :               False

MLAG Ports:
Disabled                           :                   2
Configured                         :                   0
Inactive                           :                   0
Active-partial                     :                   0
Active-full                        :                   0
```

Peers see each other via netstat
```
[admin@DC1-LEAF1A ~]$ netstat -pantu | grep 10.255
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 10.255.252.0:52358      10.255.252.1:4432       ESTABLISHED -
tcp        0  19536 10.255.252.0:4432       10.255.252.1:52000      ESTABLISHED -
```

Fix or workaound configured MLAG L2 first then run automation.

# references
* https://arista-netdevops-community.github.io/avd-cEOS-Lab/install/
* https://blog.andreasm.io/2024/08/22/arista-cloudvision-and-avd-using-containerlab/