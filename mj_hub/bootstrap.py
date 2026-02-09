#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# MJHub/bootstrap.py

from MJHub.platform.os_platform import get_platform
from MJHub.platform.platform_info import paltform_info
from MJHub.launcher.launcher import LauncherWindow

def start_app():
    platform = get_platform()
    paltform_info(platform)

    launcher = LauncherWindow() # folder launcher
    launcher.show()

    def main_app():
        launcher.close()

        # main_window = MainWindow()
        # main_window.show()

    return launcher # main_window