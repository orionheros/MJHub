#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/bootstrap.py

from mj_hub.platform.os_platform import get_platform
from mj_hub.platform.platform_info import paltform_info
from mj_hub.launcher.launcher import LauncherWindow
from mj_hub.worker.worker_thread import WorkerThread
from mj_hub.ui.main_window import MainWindow

def start_app():
    platform = get_platform()
    paltform_info(platform)

    launcher = LauncherWindow() # folder launcher
    launcher.show()

    worker = WorkerThread()
    worker.progress_changed.connect(launcher.progress_bar.setValue)
    worker.status_changed.connect(launcher.status_label.setText)

    def main_app():
        launcher.close()
        print(">>>DEBUG: Closing launcher and starting main application.")

        main_window = MainWindow()
        main_window.show()
        launcher.main_window = main_window

    worker.success.connect(main_app)
    worker.start()

    return worker, launcher