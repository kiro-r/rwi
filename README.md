<div align="center">
    <h2>• About •</h2>
    <h3></h3>
</div>

#### RWI — I really want it?

**RWI** is a lightweight background daemon for **[Hyprland](https://hyprland.org/)** that watches the active window and instantly closes it if it matches a blocklist. Useful if you want fewer distractions: block social media, games, or messengers — permanently, or only during "work mode".

<div align="center">
    <h2>• Quick start •</h2>
    <h3></h3>
</div>

## Requirements

- Hyprland
- Python 3

## Installing

```
curl -fSL https://raw.githubusercontent.com/kiro-r/rwi/master/install | bash
```

## Uninstalling

```
curl -fSL https://raw.githubusercontent.com/kiro-r/rwi/master/uninstall | bash
```

## Switching work mode

```
rwi on | off
```

## Config settings

| Option                | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `is_work_mode_active` | Whether work mode is enabled when the daemon starts    |
| `notify_on_start`     | Whether to send a notification when the service starts |
| `update_time`         | Interval between active-window checks (in seconds)     |
| `work_block`          | Windows names closed only when work mode is active     |
| `blocked`             | Windows names closed always                            |

<div align="center">
    <h2>• Additional •</h2>
    <h3></h3>
</div>

- Project structure

```
~/.config/
├── rwi.json
├── hypr/custom/scripts/
│   └── rwi.py
└── systemd/user/
    └── rwi.service

/usr/bin/
└── rwi
```

![License](https://img.shields.io/badge/license-AGPL--3.0-blue?style=for-the-badge)
