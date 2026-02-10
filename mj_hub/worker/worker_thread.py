#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/worker/worker_thread.py

import time
from PyQt6.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    progress_changed = pyqtSignal(int)
    status_changed = pyqtSignal(str)
    success = pyqtSignal()

    def run(self):
        self.status_changed.emit("Worker thread started.")
        time.sleep(1)  # Simulate some startup delay
        self.progress_changed.emit(10)

        self.status_changed.emit("Performing task 1...")
        time.sleep(2)  # Simulate creating configure tasks
        self.progress_changed.emit(30)

        self.status_changed.emit("Performing task 2...")
        time.sleep(2)  # Simulate creating database
        self.progress_changed.emit(50)

        self.status_changed.emit("Finalizing...")
        time.sleep(2)  # Simulate finalizing tasks  
        self.progress_changed.emit(100)

        self.status_changed.emit("All tasks completed.")
        self.success.emit()