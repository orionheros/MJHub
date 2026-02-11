#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/ui/widget/menu_bar.py

from PyQt6.QtWidgets import (
    QMenuBar, 
    QHBoxLayout, 
    QPushButton,
    QMenu,
)
from PyQt6.QtCore import pyqtSignal as Signal

class MenuBar(QMenuBar):
    exit_requested = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(30)
        self.setStyleSheet("background-color: #404040; color: white; border-bottom: 1px solid black;")
        self.init_ui()
        self.retranslate_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 0, 5, 0)

        # File menu
        self.file_button = QPushButton()
        self.file_button.setStyleSheet("QPushButton { font-size: 14px; } QPushButton::menu-indicator { image: none; }")
        self.file_menu = QMenu(self)
        # options
        self.settings = self.file_menu.addAction("")
        self.exit = self.file_menu.addAction("")
        self.exit.triggered.connect(self.exit_requested.emit)
        self.file_button.setMenu(self.file_menu)

        # Modules menu
        self.modules_button = QPushButton()
        self.modules_button.setStyleSheet("QPushButton { font-size: 14px; } QPushButton::menu-indicator { image: none; }")
        self.modules_menu = QMenu(self)
        # options
        self.install = self.modules_menu.addAction("")
        self.update_modules = self.modules_menu.addAction("")
        self.manage = self.modules_menu.addAction("")
        self.refresh = self.modules_menu.addAction("")
        self.modules_button.setMenu(self.modules_menu)

        self.tools_button = QPushButton()
        self.tools_button.setStyleSheet("QPushButton { font-size: 14px; } QPushButton::menu-indicator { image: none; }")

        self.help_button = QPushButton()
        self.help_button.setStyleSheet("QPushButton { font-size: 14px; } QPushButton::menu-indicator { image: none; }")

        layout.addWidget(self.file_button)
        layout.addWidget(self.modules_button)
        layout.addWidget(self.tools_button)
        layout.addWidget(self.help_button)
        layout.addStretch()
        self.setLayout(layout)

    def retranslate_ui(self):
        self.file_button.setText(self.tr("File"))
        self.modules_button.setText(self.tr("Modules"))
        self.tools_button.setText(self.tr("Tools"))
        self.help_button.setText(self.tr("Help"))

        self.settings.setText(self.tr("Settings"))
        self.exit.setText(self.tr("Exit"))

        self.install.setText(self.tr("Install Modules"))
        self.update_modules.setText(self.tr("Update Modules"))
        self.manage.setText(self.tr("Manage Modules"))
        self.refresh.setText(self.tr("Refresh list"))