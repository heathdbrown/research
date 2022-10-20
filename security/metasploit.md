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



## ERRORS

```
In Gemfile:
  metasploit-framework was resolved to 6.2.23, which depends on
    sqlite3
```
