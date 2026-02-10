#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/ui/main_window.py

from PyQt6.QtWidgets import (
    QMainWindow, 
    QLabel, 
    QVBoxLayout, 
    QWidget,
    QPushButton
)
from PyQt6.QtCore import Qt, QEvent

from .widget.title_bar import TitleBar
from .center_on_scr import CenterOnScreenWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setGeometry(100, 100, 500, 300)

        CenterOnScreenWidget.center_on_screen(self)
        self.init_ui()
        self.retranslate_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.title_bar = TitleBar(self)
        layout.addWidget(self.title_bar)

        self.welcome_label = QLabel()
        self.welcome_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ok = QPushButton()
        self.ok.clicked.connect(self.close)

        layout.addWidget(self.welcome_label)
        layout.addWidget(self.ok)
        central_widget.setLayout(layout)

    def changeEvent(self, event):
        if event.type() == QEvent.Type.LanguageChange:
            self.retranslate_ui()
        super().changeEvent(event)

    def retranslate_ui(self):
        self.title_bar.title_label.setText(self.tr("MJHub"))
        self.welcome_label.setText(self.tr("Welcome to MJHub!"))
        self.ok.setText(self.tr("OK"))

