https://kali.org/tools

# dirb 
wordlist: https://github.com/v0re/dirb/blob/master/wordlists/common.txt

```bash
# install dirb
sudo apt install dirb -yq
# download a wordlist SecList has more words
curl https://raw.githubusercontent.com/v0re/dirb/master/wordlists/common.txt --output common.txt


dirb <Target URL/PATH> common.txt -c '<cookie id>=<cookie value>'
dirb <Target URL> common.txt,dirlist.txt -c '<cookie id>=<cookie value>'#dirlist has PATHs 
```

# SecLists 
- https://github.com/danielmiessler/SecLists

# dirsearch 
- https://github.com/maurosoria/dirsearch

```bash
sudo apt install python3.8-venv
git clone https://github.com/maurosoria/dirsearch.git --depth 1
python3 -m venv .venv
pip install -r requirement.txt

Another way is to do:
sudo apt install python3-pip
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install git+https://github.com/maurosoria/dirsearch.git
```

# Damn Small XSS Scanner
- https://github.com/stamparm/DSXS
```bash
git clone https://github.com/stamparm/DSXS.git
cd DSXS
chmod 700 dsxs.py

./dsxs.py -u "http://localhost/url?param=1" --data 'param2=1' --cookie 'SessionId=123123123123' 
```

# XSStrike
- https://github.com/s0md3v/XSStrike.git

```bash
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 ./xsstrike.py -u http://target/url --crawl --blind
```

# xsser 
- https://www.kali.org/tools/xsser/

```bash
pipx install git+https://gitlab.com/kalilinux/packages/xsser.git

# tricky part find the pipx venvs
pipx list

# typically here
cd ~/.local/pipx/venvs/xsser/bin
source activate # get into the veenv

sudo apt install python3-pycurl python3-bs4 python3-geoip python3-gi python3-cairocffi python3-selenium firefoxdriver -yq # selenium driver for firewfox
sudo apt install libcurl4-gnutls-dev -yq #  needed for pycurl curl-config
sudo apt-get install libgnutls28-dev # https://stackoverflow.com/questions/46290556/installing-pycurl-with-fatal-error-gnutls-gnutls-h-no-such-file-or-directory

python3 -m pip install pycurl bs4 pygeoip gobject cairocffi selenium

```
