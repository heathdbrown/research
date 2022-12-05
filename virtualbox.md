# Virtualbox

## Unattended Install for ubuntu does not put user in the sudo user group
- https://blogs.oracle.com/virtualization/post/guide-for-virtualbox-vm-unattended-installation
- https://askubuntu.com/questions/1440032/virtualbox-ubuntu-22-04-how-to-add-sudo-rights
- https://wiki.ubuntu.com/RecoveryMode
- https://www.techrepublic.com/article/virtualbox-unattended-installation-feature/
- Launch into recovery mode and then launch root console, use the password used for the user in the unattended install
- usermod -aG sudo USER
