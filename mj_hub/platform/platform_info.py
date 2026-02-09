#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/platform/platform_info.py

from mj_hub.platform.os_platform import Platform
from PyQt6.QtWidgets import QMessageBox

def paltform_info(platform: Platform):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle("Platform Information")
    msg.setText(f"Your system is not supported.\nYour platform: {platform}")
    if platform in (Platform.UNKNOWN, 
                    Platform.MACOS,
                    Platform.SUSE, 
                    Platform.ARCH, 
                    Platform.RHEL):
        msg.exec()
    else:
        print(f">>>DEBUG: Supported platform {platform} detected.")
        pass