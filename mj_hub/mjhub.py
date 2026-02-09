#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# MJHub/mj_hub.py

import sys
from PyQt5.QtWidgets import QApplication
from MJHub.bootstrap import start_app

def main():
    try:
        app = QApplication(sys.argv)
        _launcher, _worker = start_app()
        print(">>>DEBUG: MJHub application started.")
    except Exception as e:
        print(f"Error starting MJHub: {e}")

if __name__ == "__main__":
    main()