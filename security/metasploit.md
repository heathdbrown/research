## Metasploit

# https://blog.eldernode.com/install-and-use-metasploit-on-ubuntu/

sudo apt install -y curl gpgv2 autoconf bison build-essential postgresql libaprutil1 libgmp3-dev libpcap-dev openssl libpq-dev libreadline6-dev libsqlite3-dev libssl-dev locate libsvn1 libtool libxml2 libxml2-dev libxslt-dev wget libyaml-dev ncurses-dev  postgresql-contrib xsel zlib1g zlib1g-dev ruby-dev

mkdir ~/apps

cd ~/apps

git clone https://github.com/rapid7/metasploit-framework.git

cd metasploit-framework/

sudo gem install bundler

bundle install

./msfconsole

git config --global user.name "jonny"

git config --global user.email "jonny@local"

./msfupdate

# Database setup
- https://fedoraproject.org/wiki/Metasploit_Postgres_Setup
- https://docs.rapid7.com/metasploit/no-database-connection/

```bash
sudo apt install postgresql-all postgresql-client -y
sudo su postgres
createuser msf_user -P # setup password and remember it
createdb --owner=msf_user msf_database
exit
```

Go back to metasplioit
```bash
msf>db_status
msf>db_connect msf_user:password@127.0.0.1:5432/msf_database

```

```bash
msf>help database
msf>hosts
msf>loot
msf>services
msf>vulns
```

# Metasploit Usage
- https://www.offensive-security.com/metasploit-unleashed/msfconsole/
```bash
msf>setg RHOSTS <target list>
msf>setg RPORT <target port>
msf>tips
```

- https://www.offensive-security.com/metasploit-unleashed/wmap-web-scanner/
```bash
msf>load wmap
msf>wmap_sites -h
msf>wmap_sites -a <target_site>
msf>wmap_sites -l
msf>wmap_targets -h
msf>wmap_targets -t <target_site_url>
msf>wmap_run -e
msf>wmap_vulns -l
msf>vulns
```

# Docs
* https://docs.metasploit.com/
* https://tryhackme.com/room/metasploitintro

## ERRORS

```
In Gemfile:
  metasploit-framework was resolved to 6.2.23, which depends on
    sqlite3
```
https://github.com/rapid7/metasploit-framework/issues/8765
sudo apt install -y libsqlite0-dev 
