#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License: GPL v3
# Copyright: 2026- Mateusz Jamróz
# mj_hub/mjhub.py

import sys
from PyQt6.QtWidgets import QApplication
from mj_hub.bootstrap import start_app

def main():
    try:
        app = QApplication(sys.argv)
        _worker, _launcher = start_app()
        print(">>>DEBUG: MJHub application started.")

        sys.exit(app.exec())
    except Exception as e:
        print(f"Error starting MJHub: {e}")

if __name__ == "__main__":
    main()