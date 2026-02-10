#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/core/retranslate.py

from PyQt6.QtCore import QCoreApplication, QTranslator

def retranslate_ui(self, lang_code):
    self.translator = QTranslator()

    if self.translator.load(f"translations_{lang_code}.qm"):
        QCoreApplication.installTranslator(self.translator)
        self.retranslateUi(self)
    else:
        print(f"Translation file for '{lang_code}' not found.")