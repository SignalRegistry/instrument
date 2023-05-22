#!/bin/bash
pyinstaller --onefile main.py --name instrument
rm -rf *.spec