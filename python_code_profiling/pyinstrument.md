# Pyinstrument Overview

# Typical Usage

```bash
pyinstrument -m <module> --show-all -t
```
- ouptput to stdout by default
- previous runs are stored `~/.local/share/pyinstrument/reports/` and can be rerun with `pyinstrument --load-prev <date:time> [options]`
