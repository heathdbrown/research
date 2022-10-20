https://kali.org/tools

# dirb 
- SecLists
wordlist: https://github.com/v0re/dirb/blob/master/wordlists/common.txt

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
# examples
pipx install git+https://github.com/psf/black.git
pipx install git+https://github.com/psf/black.git@branch  # branch of your choice
pipx install git+https://github.com/psf/black.git@ce14fa8b497bae2b50ec48b3bd7022573a59cdb1  # git hash
pipx install https://github.com/psf/black/archive/18.9b0.zip  # install a release
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

python3 -m pip install pycurl bs4 pygeoip gobject cairocffi selenium

```