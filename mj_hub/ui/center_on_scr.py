#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/ui/center_on_scr.py

from PyQt6.QtWidgets import QWidget

class CenterOnScreenWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.center_on_screen()

    def center_on_screen(self):
        screen = self.screen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)