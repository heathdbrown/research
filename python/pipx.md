# Pipx
> https://pypa.github.io/pipx/installation/?msclkid=1828077bb44611ec8cc75565fc24fd5e

Install packaged python applications into isolated virtualenvs.

# Installation

```console
python -m pip install --user pipx
```


## Things to remember NOT in the docs

### Cannot determine package name from '.'. Check package spec for errors.
You need to 'upgrade' the pipx internal pip to allow for installing from a local directory.

see: https://github.com/pypa/pipx/issues/365

So, if you are installing an application from the local directory using the ./ you may get the error.


```powershell
pipx install .
Cannot determine package name from spec '.'. Check package spec for errors.
```

The fix for this was the following in Windows powershell:

```powershell
$env:http_proxy='http://proxy.com:80'
$env:https_proxy='http://proxy.com:80'
python -m pipx upgrade-all
python -m pipx ensurepath
```

### Installing from local using proxy with verbose logging

```powershell
$env:http_proxy='http://proxy.com:80'
$env:https_proxy='http://proxy.com:80'
pipx install ./ --pip-args "--proxy http://proxy.com:80" --verbose
```

## Custom PIP_HOME and PIP_BIN_DIR

```bash
# RHEL7 with default python3
sudo /usr/bin/python3.6 -m pip install pipx
# login in as root
sudo su -
# Install ansible via pipx to custom location
# Set proxy vars ahead of time or pass --pip-args "--proxy http://proxy.com:80"
PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx install --include-deps ansible --pip-args "--proxy http://proxy.com:80" --verbose
# Add missing paramiko depedency
source /opt/pipx/venvs/ansible/bin/activate
(ansible) pip install paramiko --proxy http://proxy.com:80
# verify depedency installed
/opt/pipx/venvs/ansible/bin/python -m pip list
# get out of venv environment
exit
# Add $PIPX_BIN_DIR (/usr/local/bin) to $PATH
# vim ~/.bash_profile
PATH=$PATH:/usr/local/bin
# check to make sure pipx list ansible installation
PIPX_HOME=/opt/pipx PIPX_BIN_DIR=/usr/local/bin pipx list
```
