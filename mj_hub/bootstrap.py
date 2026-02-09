#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/bootstrap.py

from mj_hub.platform.os_platform import get_platform
from mj_hub.platform.platform_info import paltform_info
from mj_hub.launcher.launcher import LauncherWindow

def start_app():
    platform = get_platform()
    paltform_info(platform)

    launcher = LauncherWindow() # folder launcher
    launcher.show()

    def main_app():
        launcher.close()
        print(">>>DEBUG: Closing launcher and starting main application.")

        # main_window = MainWindow()
        # main_window.show()

    return launcher # main_window