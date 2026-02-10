#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/ui/widget/title_bar.py

import sys

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import QStyleOption, QStyle

class TitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(30)

        self.setStyleSheet("background-color: #303030; color: white; border-bottom: 1px solid black;")

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 0, 5, 0)

        self.title_label = QLabel()
        self.title_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.title_label)
        layout.addStretch()

        x_button = QLabel("X")
        x_button.setStyleSheet("""\
        QLabel {
            font-size: 14px; 
            font-weight: bold; 
            color: red;
            border: none;
        }
        QLabel:hover {
            background-color: #505050;
            color: white;            
            }
        """)
        x_button.setAlignment(Qt.AlignmentFlag.AlignCenter)
        x_button.setFixedSize(20, 20)
        x_button.mousePressEvent = lambda event: sys.exit(0)
        layout.addWidget(x_button)

        self.setLayout(layout)

        self.start_pos = None

    def mousePressEvent(self, event):
            if event.button() == Qt.MouseButton.LeftButton:
                self.start_pos = event.globalPosition().toPoint()
                event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.start_pos:
            delta = event.globalPosition().toPoint() - self.start_pos
            self.start_pos = event.globalPosition().toPoint()
            self.window().move(self.window().pos() + delta)
            event.accept()

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, p, self)