import colorama
import pyfiglet
import socket
import sys
import os
import subprocess

if "win" in sys.platform:
    subprocess.run(["pip", "install", "colorama", "pyfiglet"], shell=True)
else:
    subprocess.run(["pip3", "install", "colorama", "pyfiglet"], shell=True)

rd = colorama.Fore.RED
mag = colorama.Fore.MAGENTA
cv = colorama.Fore.WHITE
gn = colorama.Fore.GREEN
bl = colorama.Fore.LIGHTBLUE_EX
yl = colorama.Fore.LIGHTGREEN_EX

def banner():
    fg = pyfiglet.Figlet(font="small").renderText("RemaxBox Team")
    print(bl + fg)
    print(rd + "CloudFlare bypasser , Get Real IP of website")
    print(mag + "Created By Maximum Radikali (not by Glictched Studios)")

domains = {
    "www.",
    "ftp.",
    "mx.",
    "ns1.",
    "ns2.",
    "status.",
    "secure.",
    "stmp.",
    "news.",
    "blog.",
    "webmail.",
    "host.",
    "server.",
    "admin.",
    "test.",
    "remote.",
    "portal.",
    "beta.",
    "forum.",
    "pop.",
    "dev.",
    "vpn.",
    "cpanel.",
    "direct-connect.",
    "direct.",
    "m.",
    "mobile.",
    "mail.",
}

banner()
site = input(bl + "Please Enter a url ex : (google.com)-> ")
print(yl + "Waiting ...")
for domain in domains:
    try:
        hostname = domain + site
        ip_address = socket.gethostbyname(hostname)
        print(gn + ip_address + cv)
    except socket.gaierror:
        pass

wait = input(f"{gn}[FINISHED] Press anything to exit")