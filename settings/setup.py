import sys
import os
import subprocess
import time
import threading
def change_colors():
    colors = ["1", "2", "3", "4", "5"]
    while True:
        for color in colors:
            os.system("color " + color)
            time.sleep(0.2)

color_thread = threading.Thread(target=change_colors)
color_thread.daemon = True
color_thread.start()
print("Installing the python modules required for the Glitched Studios Multi Tool")

if sys.platform.startswith("win"):
    print("WINDOWS")
    os.system("pip install deep-translator")
    os.system("pip install dnspython")
    os.system("pip install selenium")
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install json")
    os.system("pip install random")
    os.system("pip install string")
    os.system("pip install ctypes")
    os.system("pip install base64")
    os.system("pip install threading")
    os.system("pip install psutil")
    os.system("pip install bs4")
    os.system("pip install webbrowser")
    os.system("pip install itertools")
    os.system("pip install phonenumbers")
    os.system("pip install discord")
    os.system("pip install discord.py")
    os.system("pip install PyQt5")
    os.system("pip install PyQtWebEngine")
    os.system("pip install pytube")
    os.system("pip install cryptography")
    os.system("pip install pycryptodome")
    os.system("pip install pywin32")
    os.system("pip install scapy")
    os.system("pip install UnityPy")
    os.system("pip install playfab")
    os.system("pip install jsonlint")
    os.system("pip install pystyle")
    os.system("pip install gdown")
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("pip install httpx")
    os.system("pip install tls_client")
    os.system("pip install websocket")
    os.system("pip install aiohttp")
    os.system("pip install asyncio")
    os.system("pip install pytz")
    os.system("pip install undetected_chromedriver")
    os.system("pip install faker")
    os.system("pip install colorama")
    os.system("pip install pycryptodome")
    os.system("pip install pathlib")
    os.system("pip install pytube")
    os.system("pip install pywin32")
    os.system("pip install websocket-client")
    os.system("pip install fade")
    os.system("pip install ipapi")
    os.system("pip install ipapi")
    print("Finish.")

elif sys.platform.startswith("linux"):
    print("LINUX")
    os.system("python3 -m pip install --upgrade pip")
    os.system("python3 -m pip install --upgrade pip setuptools wheel")
    os.system("python3 -m pip install deep-translator")
    os.system("python3 -m pip install dnspython")
    os.system("python3 -m pip install selenium")
    os.system("python3 -m pip install colorama")
    os.system("python3 -m pip install requests")
    os.system("python3 -m pip install json")
    os.system("python3 -m pip install random")
    os.system("python3 -m pip install string")
    os.system("python3 -m pip install ctypes")
    os.system("python3 -m pip install base64")
    os.system("python3 -m pip install threading")
    os.system("python3 -m pip install psutil")
    os.system("python3 -m pip install bs4")
    os.system("python3 -m pip install webbrowser")
    os.system("python3 -m pip install itertools")
    os.system("python3 -m pip install phonenumbers")
    os.system("python3 -m pip install discord")
    os.system("python3 -m pip install discord.py")
    os.system("python3 -m pip install PyQt5")
    os.system("python3 -m pip install PyQtWebEngine")
    os.system("python3 -m pip install pytube")
    os.system("python3 -m pip install cryptography")
    os.system("python3 -m pip install pycryptodome")
    os.system("python3 -m pip install scapy")
    os.system("python3 -m pip install UnityPy")
    os.system("python3 -m pip install playfab")
    os.system("python3 -m pip install jsonlint")
    os.system("python3 -m pip install pystyle")
    os.system("python3 -m pip install gdown")
    os.system("python3 -m pip install pywin32")  # added
    print("Finish.")