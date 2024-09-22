@echo off
title Glitched Studios Multi Tool Module Installer
chcp 65001> nul

python -m pip install --upgrade pip
pip install --upgrade pip setuptools wheel
pip install --upgrade urllib3 chardet charset-normalizer
cls
python settings/setup.py
pause