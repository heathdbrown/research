# GNS3 on Windows 2022

## Using the GNS3 VM via VirtualBox and nested Virtualization

- https://forums.virtualbox.org/viewtopic.php?t=99390

- Disable Hyper-V: bcdedit /set hypervisorlaunchtype off
  - Alt: Search for Windows Features
    - Disable Hyper-V
    - Containers
    - Windows Virtualization Platform
    - Windows Subsystem for Linux
- Disable Windows Memory Integrity
