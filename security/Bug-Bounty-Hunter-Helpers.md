- Use ntfy.sh to send notifications to yourself on your phone NTFY and create a bash function that does a curl and posts a message.

```shell
function ntfy(){
	curl -d "$1" https://ntfy.sh/<key>
}
```

- Grab subdomains, check them, crawl them, curl them, create wordlist
```shell
function hakwordlist(){
    subfinder -silent -d $1 | anew subdomains.txt | httpx -nf -silent | anew urls.txt | hakrawler | anew endpoints.txt | while read url; do curl $url --insecure | haklistgen | anew wordlist.txt && ntfy "subdomain complete" || ntfy "subdomain error"; done
}
```
- gau to pull urls
```shell
function fuffygau(){
  echo $1 | gau --blacklist --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt,js | grep '=' | qsreplace -a | anew gau-$1-urls.txt | httpx -nf -silent | anew gau-$1-probed-urls.txt && ntfy "gau complete" || ntfy "gau error"
}
```
- Use ffuf to check for urls
```shell
ffuf -u 'FUZZ' -w gau-urls.txt -rate 100 && ntfy "ffuf complete" || ntfy "ffuf error"
```
- nmap  scans
```shell
mkdir -p scans                                                                         
sudo nmap -A -sC -p- -iL subdomains.txt -oA scans/nmap-initial && ntfy "nmap complete" || ntfy "nmap error" 
```

# Resources
- https://github.com/nahamsec/Resources-for-Beginner-Bug-Bounty-Hunters
- https://github.com/KingOfBugbounty/KingOfBugBountyTips
- https://github.com/tomnomnom
- https://github.com/projectdiscovery