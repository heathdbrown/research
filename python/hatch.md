# Hatch
> Another python package dependency tool

Found this one when reading through: https://packaging.python.org/en/latest/tutorials/managing-dependencies/

https://hatch.pypa.io/latest/

# Installation

```console
pipx install hatch
```

# Configuration

Configuration for Hatch itself is stored in a config.toml file located by default in one of the following platform-specific directories.

|Platform|Path|
|--------|----|
|macOS|~/Library/Preferences/hatch|
|Windows|%USERPROFILE%\AppData\Local\hatch|
|Unix|$XDG_CONFIG_HOME/hatch (the XDG_CONFIG_HOME environment variable default is ~/.config)|

Example:

```
#config.toml
mode = "local"
project = ""
shell = ""

[dirs]
project = []
python = "isolated"
data = "C:\\Users\\heath\\AppData\\Local\\hatch"
cache = "C:\\Users\\heath\\AppData\\Local\\hatch\\Cache"

[dirs.env]
virtual = "D:\\heath\\.virtualenvs"

[projects]

[publish.index]
repo = "main"

[template]
name = "Heath Brown"
email = "heathd.brown@gmail.com"

[template.licenses]
headers = true
default = [
    "MIT",
]

[template.plugins.default]
tests = true
ci = true
src-layout = true

[terminal.styles]
info = "bold"
success = "bold cyan"
error = "bold red"
warning = "bold yellow"
waiting = "bold magenta"
debug = "bold"
spinner = "simpleDotsScrolling"
```

# Project templates

https://hatch.pypa.io/latest/config/project-templates/#project-templates

```
[template.plugins.default]
tests = true
ci = true
src-layout = true
```

# Usage

## New Project
```console
hatch new "new project"
```

## Existing Project
```console
hatch new --init
```
