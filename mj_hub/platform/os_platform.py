#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/platform/os_platform.py

import platform as pfm
from enum import Enum, auto

class Platform(Enum):
    WINDOWS = auto()
    DEBIAN = auto()     # Ubuntu, Debian, Mint
    RHEL = auto()       # Fedora, CentOS, RHEL
    ARCH = auto()       # Arch Linux, Manjaro
    SUSE = auto()       # openSUSE, SUSE Linux Enterprise
    MACOS = auto()
    UNKNOWN = auto()

def get_platform() -> Platform:
    system = pfm.system().lower()
    if system == "windows":
        return Platform.WINDOWS
    elif system == "darwin":
        return Platform.MACOS
    elif system == "linux":
        try:
            info = pfm.freedesktop_os_release()
            ids = info.get("ID", "").lower()
            if ids in ("ubuntu", "debian", "linuxmint"):
                return Platform.DEBIAN
            elif ids in ("fedora", "centos", "rhel"):
                return Platform.RHEL
            elif ids in ("arch", "manjaro"):
                return Platform.ARCH
            elif ids in ("opensuse", "suse"):
                return Platform.SUSE
        except Exception as e:
            print(f"Error detecting Linux distribution: {e}")
    else:
        return Platform.UNKNOWN