# Create VM
- Install tools `git clone $TOOLSREPO`
- `cd $TOOLSREPO`
- `./install.sh`
- Change DNS settings if using AZURE as DNS will be rate limited
  - Virtual Networks -> find vnet for VM
  - Click 'DNS Servers'
  - Add 1.1.1.1, grab from https://public-dns.info/
# Review target Information
- Review Acquisitions of main target
- Find the ASN for each, if this exists
- Search domains `https://bgp.he.net`
- `amass intel -org $TARGET`
- `amass intel -asn $TARGET_ASNs`
- `echo $TARGET | metabigor net --org -v`
# Enumerate target
- Slow Scan top 100 `nmap -A -F -T1 $TARGET -v -oA nmap-initial.txt`
- Ffuf 2  second delay generic wordlist `ffuf -w /usr/share/wordlists/dirb/common.txt -u $TARGET_URL/FUZZ -fc 403 -p 2 -o ffuf-dirb-common.log`
- dirb `dirb $TARGET_URL`

# Additional Resources
- https://gowthams.gitbook.io/bughunter-handbook/checklists
- https://book.hacktricks.xyz/linux-hardening/useful-linux-commands
- https://github.com/KingOfBugbounty/KingOfBugBountyTips
- https://book.hacktricks.xyz/generic-methodologies-and-resources/external-recon-methodology
