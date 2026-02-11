#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/ui/widget/hub_info_label.py

from PyQt6.QtWidgets import QHBoxLayout, QLabel, QFrame
from mj_hub import __version__ as MJHUB_VERSION

class HubInfoLabel(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("HubInfoLabel {background-color: #757575; border-top: 1px solid black;}")

        self.build_ui()
        self.retranslate_ui()

    def build_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(10, 5, 10, 5)

        self.hub_version = QLabel()
        self.hub_version.setStyleSheet("color: white;")

        self.actualize_available = QLabel()
        self.actualize_available.setStyleSheet("color: green; font-weight: bold;")
        self.actualize_available.setVisible(True)  # Set to True for testing, 
                                                   # full implementation will check for updates 
                                                   # and set visibility accordingly

        layout.addWidget(self.hub_version)
        layout.addStretch()
        layout.addWidget(self.actualize_available)

        self.setLayout(layout)

    def retranslate_ui(self):
        self.hub_version.setText(self.tr(f"MJHub Version: {MJHUB_VERSION}"))
        self.actualize_available.setText(self.tr("Update Available!"))