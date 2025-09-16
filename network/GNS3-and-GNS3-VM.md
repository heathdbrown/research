# GNS3 VM
- Error received when using VirtualBox
```console
KVM acceleration cannot be used (/dev/kvm doesn't exist). You can turn off KVM support in the gns3_server.conf by adding enable_kvm = false to the [Qemu] section
```
- Attempted fix by following the GNS3 troubleshooting guide and adding the following configuration, did not work.
```shell
nano ~/.config/GNS3/gns_server.conf
[Qemu]
enable_kvm = false
```
- Researching further found that if you have WSL installed you might not be able to utilize the 'nested' functions in Virtualbox due to Hyper-V. 
- Alternative is to use the Hyper-V for the GNS3 VM
- After switching now getting the following issue when trying to use Hyper-V
![image](https://github.com/heathdbrown/research/assets/618460/39ea6f1f-a1be-4c87-8528-59cfddd72354)
```console
Error while listing vms: GNS3VM: The Windows account running GNS3 does not have the required permissions for Hyper-V
```
- Fix run GNS3 as administrator: https://www.gns3.com/community/support/hyper-v-error-while-listing-vms-do-not-have-the-required-permissons-for-hyper-v
- Ran into disk space issue after fixing the administrator problem and had to move my machines and disks to my secondary partition (d:\)