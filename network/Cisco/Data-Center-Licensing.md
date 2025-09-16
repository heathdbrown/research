# 2023-11-04
If you are in the networking field or just in information technology in general, and use any vendor's products, licensing is something we deal with all the time. These are my notes on the topic specifically regarding Cisco Data Center Licensing.

This is based solely on the [resources](#Resources) linked at the bottom.

First, we need to understand the tiered model that Cisco currently has for its Data Center Software subscriptions.

- DCN (Data Center Networking) Tiered Licenses
  - Data Center Networking Essentials Subscription
  - Data Center Networking Advantage Subscription
  - Data Center Networking Premier Subscription
- DCN Add-On Licenses

Great, now what do these subscriptions apply to, hardware wise.

- Cisco Nexus 9000 Series Switches

Subscription Terms come in 3,5,7 years for the initial hardware purchase, this is my understanding from the document in the [Purchasing](https://www.cisco.com/c/en/us/products/collateral/software/one-data-center-networking-subscription/nb-06-aci-dc-nw-sub-offer-faq-ctp-en.html#Purchasing) section.

After the 3,5,7 year subscription ends, you can do a renewal using the CCW-R tool and this supports 1Y, 3Y, 5Y renewals.

Let's breakdown the three tiers of licensing and the purpose of each.

|DCN Essentials (NX-OS)|DCN Essentials (ACI)|
|----------------------|--------------------|
|Enterprise LAN(2022) / Routing and switching features (2023)|MultiPOD|
|NDFC-LAN(2022) / Fabiric management features (2023)|ACI Base capabilities|
|Network Services (2022) / Fabric services features (2023)|PTP|

I am pretty sure that did not help when you look at the NX-OS side.

- Enterprise LAN / Routing and Switching features
   - OSPF
   - BGP
   - IS-IS
   - PIM
   - SSM
   - MSDP
   - PBR
   - GRE
   - EIGRP
   - VRF
   - VXLAN
   - BGP eVPN Control Plane
- NDFC-LAN (Network Dashboard Fabric Controller)
- Network Services
  - [Catena](https://blogs.cisco.com/datacenter/catena)
  - [iCAM](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/104x/configuration/icam/cisco-nexus-9000-series-nx-os-icam-configuration-guide-release-104x.html)
  - [Intelligent Traffic Director](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/7-x/itd/configuration/guide/b_Cisco_Nexus_9000_Series_NX-OS_Intelligent_Traffic_Director_Configuration_Guide_7x/b_Cisco_Nexus_9000_Series_NX-OS_Intelligent_Traffic_Director_Configuration_Guide_7x_chapter_010.html)
  - [Non-Blocking Multicast](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/102x/IP-Fabric-for-Media/cisco-nexus-9000-series-nx-os-ip-fabric-for-media-solution-guide-release-102x/m-non-blocking-multicast-service-reflection.html)
  - [Smart Channel](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/101x/configuration/smart-channel/cisco-nexus-9000-nx-os-smart-channel-configuration-guide-101x/m_overview.html)

|DCN Advantage NX-OS|DCN Advantage ACI|
|-------------------|-----------------|
|VPN Fabric| Multi-Site|
|Tenant Routed Multicast|Physical Remote Leaf|

- VPN Fabric
   - Inter-AS
   - MPLS Layer 3 VPN Pervasive Load Balancing (PLB)
- [Tenant Routed Multicast](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus3600/101x/configuration/vxlan/cisco-nexus-3600-nx-os-vxlan-configuration-guide-101x/m-configuring-trm.pdf)
- [VXLAN EVPN Multi-Site](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-739942.html)
- L3 EVPN over segment routing MPLS
- Fabric Services features (Enhanced PBR (EPBR))
- RTP Flow Monitoring (Media Flow Analytics)
- PTP Monitoring
- Multicast NAT

Product IDs for Subscription Tier Based Licenses for DCN (ACI+NX-OS) (Cisco Nexus 9000 Fixed Platforms)
- Essentials Package
  - 1G Fixed Platforms (GF)
     - C1E1TN9300GF-3Y
     - C1E1TN9300GF-5Y
     - C1E1TN9300GF-7Y
  - 10G/25G/40G/100G Fixed Platforms (XF)
     - C1E1TN9300XF-3Y
     - C1E1TN9300XF-5Y
     - C1E1TN9300XF-7Y
  - Cisco Nexus 9364C and 9300-GX Platforms (XF2)
     - C1E1TN9300XF2-3Y
     - C1E1TN9300XF2-5Y
     - C1E1TN9300XF2-7Y
- Advantage Package
  - 1G Fixed Platforms (GF)
     - C1A1TN9300GF-3Y
     - C1A1TN9300GF-5Y
     - C1A1TN9300GF-7Y
  - 10G/25G/40G/100G Fixed Platforms (XF)
     - C1A1TN9300XF-3Y
     - C1A1TN9300XF-5Y
     - C1A1TN9300XF-7Y
  - Cisco Nexus 9364C and 9300-GX Platforms (XF2)
     - C1A1TN9300XF2-3Y
     - C1A1TN9300XF2-5Y
     - C1A1TN9300XF2-7Y
- Premier package
  - 1G Fixed Platforms (GF)
     - C1P1TN9300GF-3Y
     - C1P1TN9300GF-5Y
     - C1P1TN9300GF-7Y
  - 10G/25G/40G/100G Fixed Platforms (XF)
     - C1P1TN9300XF-3Y
     - C1P1TN9300XF-5Y
     - C1P1TN9300XF-7Y
  - Cisco Nexus 9364C and 9300-GX Platforms (XF2)
     - C1P1TN9300XF2-3Y
     - C1P1TN9300XF2-5Y
     - C1P1TN9300XF2-7Y

PIDS for Perpetual Tier Based Licenses for DCN (ACI-NX-OS) (Cisco Nexus 9000)
- Advantage Package
  - 1G Fixed Platforms (GF)
    - ACI-AD-GF
  - 10G/25G/40G/100G Fixed Platforms (XF)
    - ACI-AD-XF
  - Cisco Nexus 9364C and 9300-GX Platforms (XF2)
    - ACI-AD-XF2

PIDS for Perpetual Tier Based Licenses for NX-OS (Cisco Nexus 9000)
- Advantage Package
  - 1G Fixed Platforms (GF)
    - NXOS-AD-GF
  - 10G/25G/40G/100G Fixed Platforms (XF)
    - NXOS-AD-XF
  - Cisco Nexus 9364C and 9300-GX Platforms (XF2)
    - NXOS-AD-XF2

# Resources:
- [Cisco NX-OS Licensing Options Guide](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/licensing-options/cisco-nexus-licensing-options-guide.html)
- [Cisco Data Center Networking Software Subscriptions Suites FAQ](https://www.cisco.com/c/en/us/products/collateral/software/one-data-center-networking-subscription/nb-06-aci-dc-nw-sub-offer-faq-ctp-en.html)
- [Cisco Nexus 9000 and 3000 Series NX-OS Switch License Navigator](https://www.cisco.com/c/dam/en/us/td/docs/Website/datacenter/license/index.html)
- [Cisco Live 2022: Introduction to NFDC - BRKDNC-1119](https://www.ciscolive.com/c/dam/r/ciscolive/global-event/docs/2022/pdf/BRKDCN-1119.pdf)
- [Catena](https://blogs.cisco.com/datacenter/catena)
- [About the Catena Solution](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/92x/catena/b-cisco-nexus-9000-series-nx-os-catena-configuration-guide-92x/b-cisco-nexus-9000-series-nx-os-catena-configuration-guide-92x_chapter_01.pdf)
- [Cisco Catena: An All-in-One Service chaining solution](https://video.cisco.com/detail/video/5739547296001)
- [Cisco iCAM](https://blogs.cisco.com/datacenter/icam)
- [Cisco iCAM Monitoring](https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference-release-9-3x/#!configuring-icam-monitoring)
- [Configuring iCAM - Cisco Nexus 3000 and 900 Series NXOS](https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference-release-9-3x/?ref=blog.networkers.fi#!configuring-icam)
- [Intelligent Traffic Director](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/7-x/itd/configuration/guide/b_Cisco_Nexus_9000_Series_NX-OS_Intelligent_Traffic_Director_Configuration_Guide_7x/b_Cisco_Nexus_9000_Series_NX-OS_Intelligent_Traffic_Director_Configuration_Guide_7x_chapter_010.html)
- [Non-Blocking Multicast](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/102x/IP-Fabric-for-Media/cisco-nexus-9000-series-nx-os-ip-fabric-for-media-solution-guide-release-102x/m-non-blocking-multicast-service-reflection.html)
- [Configuring Smart-Channel](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/92x/smart_channel/configuration/guide/b-cisco-nexus-9000-nx-os-smart-channel-configuration-guide-92x/b-cisco-nexus-9000-nx-os-smart-channel-configuration-guide-92x_chapter_011.pdf)
- [Cisco Nexus 9000 Series NX-OS Smart Channel](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/101x/configuration/smart-channel/cisco-nexus-9000-nx-os-smart-channel-configuration-guide-101x/m_overview.html)
- [Tenant Routed Multicast](https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus3600/101x/configuration/vxlan/cisco-nexus-3600-nx-os-vxlan-configuration-guide-101x/m-configuring-trm.pdf)
- [Cisco 9000 Tenant Routed Multicast](https://www.cisco.com/c/en/us/td/docs/switches/datacenter/nexus9000/sw/92x/vxlan-92x/configuration/guide/b-cisco-nexus-9000-series-nx-os-vxlan-configuration-guide-92x/b_Cisco_Nexus_9000_Series_NX-OS_VXLAN_Configuration_Guide_9x_chapter_01001.html)
- [VXLAN EVPN Multi-Site](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/white-paper-c11-739942.html)
 - [NextGen DCI with VXLAN EVPN Multi-Site Using VPC](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/whitepaper-c11-742114.html)