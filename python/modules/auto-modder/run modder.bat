@echo off
set /p "path=Enter path: "
set "path=%path:"=%"

start /B AutoModder.py --noWalls --noGrav --pvp "%path%"

pause