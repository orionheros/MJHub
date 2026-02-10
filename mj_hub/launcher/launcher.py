#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/launcher/launcher.py

from PyQt6.QtWidgets import (
                            QWidget,
                            QVBoxLayout,
                            QLabel,
                            QProgressBar
                            )   
from PyQt6.QtCore import Qt

from mj_hub.ui.center_on_scr import CenterOnScreenWidget

class LauncherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setFixedSize(400, 200)

        CenterOnScreenWidget.center_on_screen(self)
        self.init_ui()

    def init_ui(self):

        layout = QVBoxLayout()

        self.logo = QLabel("MJHub Launcher")
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo.setStyleSheet("font-size: 24px; " \
                                "font-weight: bold; " \
                                "margin-bottom: 20px;"
                                )
        
        self.status_label = QLabel("Starting...")

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)

        layout.addWidget(self.logo)
        layout.addStretch()
        layout.addWidget(self.status_label)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)