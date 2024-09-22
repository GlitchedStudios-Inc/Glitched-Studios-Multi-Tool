import requests
import time
import pystyle
import os
import json
from pystyle import Colors, Colorate
from colorama import *
import subprocess
import ctypes
import sys
import fade 
import threading
from bs4 import BeautifulSoup
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import ipapi
import random
import re
import threading
import multiprocessing
from sys import stdout
import os, threading, requests, sys, cloudscraper, datetime, time, socket, socks, ssl, random, httpx
import datetime
URL = "http://httpbin.org/ip"
PROXY_LIST_URLS = [
           "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=https&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/themiralay/Proxy-List-World/master/data.txt",
        "https://raw.githubusercontent.com/casals-ar/proxy-list/main/http",
        "https://raw.githubusercontent.com/casals-ar/proxy-list/main/https",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://github.com/monosans/proxy-list/blob/main/proxies/http.txt",
        "https://raw.githubusercontent.com/hookzof/HTTP-Proxy-List/master/proxy-list.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/master/proxies/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy-list.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-list/master/proxy-list.txt",
        "https://raw.githubusercontent.com/Volodichev/proxy-list/master/proxy-list.txt",
        "https://raw.githubusercontent.com/almroot/proxy-list/master/proxy-list.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/master/proxies/https.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https-proxy-list.txt",
    "https://spys.me/socks.txt"
]
# Functions

def get_proxies(url, timeout=5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def scrape_website(url, timeout=5):
    proxies = get_proxies(url, timeout=timeout)
    with threading.Lock():
        all_proxies.extend(proxies)
    print(f"Website scraped: {url}")

def main(timeout=5):
    global all_proxies
    all_proxies = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(scrape_website, PROXY_LIST_URLS)
    filename = "output/others/proxies/proxies.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(proxy + "\n" for proxy in all_proxies)
    print(f"Total proxies saved: {len(all_proxies)}")

def remove_invalid_proxies(filename):
    with open(filename, "r", encoding="utf-8") as file:
        proxies = file.read().splitlines()
    valid_proxies = [proxy for proxy in proxies if re.match(r"\d+\.\d+\.\d+\.\d+:\d+", proxy)]
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(proxy + "\n" for proxy in valid_proxies)
    print(f"Total valid proxies: {len(valid_proxies)}")

test_number = 1

def check_proxy(proxy):
    global test_number
    try:
        webhook_url = "https://ptb.discord.com/api/webhooks/1277155516086227076/eRkRljpBLni1ECaFKXptfNceOUpe-sfkflN-d76zR41K7PFyBBjPKGipLObXsyVh8msV"
        data = {"content": f"Test {test_number}"}
        response = requests.post(webhook_url, json=data, proxies={"http": proxy, "https": proxy}, timeout=10)
        response.raise_for_status()
        print(f"{GEN_VALID}Proxy {proxy} is working fine{reset}")
        with open("output/others/proxies/working_proxies.txt", "a", encoding="utf-8") as file:
            file.write(proxy + "\n")

        test_number += 1

    except requests.exceptions.RequestException:
        print(f"{GEN_INVALID}Proxy {proxy} failed to send webhook request{reset}")

def check_proxies_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        proxies = file.read().splitlines()
    print(f"Total proxies read from {filename}: {len(proxies)}")
    
    threads = []
    for i, proxy in enumerate(proxies):
        thread = threading.Thread(target=check_proxy, args=(proxy,))
        threads.append(thread)
        thread.start()
        # Add a cooldown if needed
        # if cooldown > 0:
        #     time.sleep(cooldown)
    for thread in threads:
        thread.join()
    print(f"Proxy checking complete")

def check_proxies_chunk(proxies):
    for proxy in proxies:
        check_proxy(proxy)
def proxygen():
    start_time = time.time()
    clear_file("output/others/proxies/proxies.txt")
    clear_file("output/others/proxies/working_proxies.txt")
    main(timeout=5)
    remove_invalid_proxies("output/others/proxies/proxies.txt")
    check_proxies_from_file("output/others/proxies/proxies.txt")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
    return_to_menu()

def clear_file(filename):
    with open(filename, "w"): pass
def title_changer(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
    set_console_background_color()
rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

color = Fore
red = color.RED
white = color.WHITE
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
try:
	username_pc = os.getlogin()
except:
	print("[ERROR] failed getting username")
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

GEN_VALID = f'{gen_valid_color}[{Fore.WHITE}+{gen_valid_color}] | {reset}'
GEN_INVALID = f'{gen_invalid_color}[{Fore.WHITE}x{gen_invalid_color}] | {reset}'
init()
def loaderoption(inputtext):
    input(f"""{red}┌───({white}{inputtext})─[{white}~{red}]
└──{white}$ {Fore.RESET}""")
logo = fade.purplepink(f"""
	   ▄▄ • ▄▄▌  ▪  ▄▄▄▄▄ ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄      .▄▄ · ▄▄▄▄▄▄• ▄▌·▄▄▄▄  ▪        .▄▄ · 
	  ▐█ ▀ ▪██•  ██ •██  ▐█ ▌▪██▪▐█▀▄.▀·██▪ ██     ▐█ ▀. •██  █▪██▌██▪ ██ ██ ▪     ▐█ ▀. 
	  ▄█ ▀█▄██▪  ▐█· ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄▐█· ▐█▌    ▄▀▀▀█▄ ▐█.▪█▌▐█▌▐█· ▐█▌▐█· ▄█▀▄ ▄▀▀▀█▄
	  ▐█▄▪▐█▐█▌▐▌▐█▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌██. ██     ▐█▄▪▐█ ▐█▌·▐█▄█▌██. ██ ▐█▌▐█▌.▐▌▐█▄▪▐█
	  ·▀▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•      ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀█▄▀▪ ▀▀▀▀         
{reset}                                                              
""")
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    total_messages = int(t)
    while True:
        remaining_messages = int((until - datetime.datetime.now()).total_seconds())
        if remaining_messages > 0:
            stdout.flush()
            stdout.write(f"\r{INFO}Messages left: {total_messages - (total_messages - remaining_messages)}")
        else:
            stdout.flush()
            stdout.write(f"\r{GEN_VALID}All messages sent!\n")
            return

import concurrent.futures

def send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url):
    if username == "":
        username = "GLITCHED STUDIOS MULTI TOOL WEBHOOK DESTROYER"
    if message == "":
        message = "@everyone@here GLITCHED STUDIOS IS TAKING OVER | discord.gg/glitched-studios"
    if avatar_url == "":
        avatar_url = "https://cdn.discordapp.com/icons/1192296192130953298/4ed647049bddcd97895339081f9e8ddf.png?size=1024"
    payload = {
        'username': username,
        'content': message,
        'avatar_url': avatar_url
    }
    print(f"{gen_valid_color} **WEBHOOK ANNIHILATION SEQUENCE INITIATED**\n{INFO}Username: {username}\n{INFO}Message: {message}\n{INFO}Message Amount: {num_messages}")

    def send_message(webhook_url, payload):
        try:
            response = requests.post(webhook_url, json=payload)
        except requests.exceptions.RequestException as e:
            pass

    def countdown(t):
        for i in range(t, 0, -1):
            sys.stdout.flush()
            sys.stdout.write(f"\r{INFO}Messages left: {i}")
            time.sleep(1)
        sys.stdout.flush()
        sys.stdout.write(f"\r{GEN_VALID}All messages sent!\n")

    threads = []
    for i in range(num_messages):
        thread = threading.Thread(target=send_message, args=(webhook_url, payload))
        threads.append(thread)
        thread.start()
        if cooldown > 0:
            time.sleep(cooldown)
    countdown_thread = threading.Thread(target=countdown, args=(num_messages,))
    countdown_thread.daemon = True
    countdown_thread.start()
    for thread in threads:
        thread.join()
    print(f"{gen_valid_color} **WEBHOOK ANNIHILATION COMPLETE**\n{INFO}Username: {username}\n{INFO}Message: {message}\n{INFO}Message Amount: {num_messages}\n{INFO}Webhook Url: {webhook_url}")
def send_multi_webhook_message(webhook_urls, username, message, num_messages, cooldown, avatar_url):
    if username == "":
        username = "Glitched Studios Multi Tool Webhook Killer"
    if message == "":
        message = "@everyone@here Glitched Studios On Top | discord.gg/glitched-studios"
    if avatar_url == "":
        avatar_url = "https://cdn.discordapp.com/icons/1192296192130953298/4ed647049bddcd97895339081f9e8ddf.png?size=1024"
    payload = {
        'username': username,
        'content': message,
        'avatar_url': avatar_url
    }
    print(f"**SPAMMING INITIATED**\n{INFO}Username: {username}\n{INFO}Message: {message}\n{INFO}Message Amount: {num_messages}")
    
    webhook_urls_list = [url.strip() for url in webhook_urls.split(',')]

    def send_message(webhook_url, payload):
        try:
            response = requests.post(webhook_url, json=payload)
            print(f"{GEN_VALID} Message sent to {webhook_url}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"{GEN_INVALID} **ERROR SENDING MESSAGE** to {webhook_url}. {e}")
            return False

    for _ in range(num_messages):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(send_message, webhook_url, payload) for webhook_url in webhook_urls_list]
            success_count = sum(future.result() for future in concurrent.futures.as_completed(futures))
        if cooldown > 0:
            time.sleep(cooldown)
    print(f"{reset}**SPAMMING COMPLETE**\n{INFO}Username: {username}\n{INFO}Message: {message}\n{INFO}Message Amount: {num_messages}\n")
def delete_webhook(webhook_url):
    requests.delete(webhook_url)
def Reset():
        if sys.platform.startswith("win"):
            "WINDOWS"
            file = f'python python/main.py'
            subprocess.run(file, shell=True)
        elif sys.platform.startswith("linux"):
            "LINUX"
            file = f'python3 python/main.py'
            subprocess.run(file, shell=True)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_webhook_info(webhook_url):
    try:
        response = requests.get(webhook_url)
        if response.status_code == 200:
            webhook_data = response.json()
            print("Webhook Information:")
            print(f"{INFO}Webhook Name: {webhook_data['name']}")

            
            if 'guild_id' in webhook_data and 'channel_id' in webhook_data:
                guild_id = webhook_data['guild_id']
                channel_id = webhook_data['channel_id']
                print(f"{INFO}Server ID > {guild_id}")
                print(f"{INFO}Channel ID> {channel_id}")
            else:
                print(f"{GEN_INVALID}Server and Channel information not available.")
        else:
            print(f"{ERROR}Unable to retrieve webhook information. Make sure the URL is correct.")
    except Exception as e:
        print(f"{ERROR}An error occurred: {str(e)}")

def return_to_menu():
    input("\nPress Enter to return to the menu.")
    clear_console()
    show_menu()

def show_menu():
    clear_console()
    print(logo)
    print(Colorate.Horizontal(Colors.red_to_white, f"""
                                            [1] Spam the webhook
                                            [2] Delete the webhook
                                            [3] Webhook information
                                            [4] Multi Spam Webhooks
                                            [5] Proxie Gen
                                            [6] Go Back
  """))
    menu_choice = input(f"""{red}┌───({white}Pick An Option)─[{white}~{red}]
└──{white}$ {Fore.RESET}""")

    if menu_choice == "1":
        webhook_url = input(f"{INPUT}Webhook URL> ")
        username = input( f"{INPUT}Webhook Name> ")
        message = input( f"{INPUT}Message> ")
        num_messages = int(input( f"{INPUT}How many messages> "))
        cooldown = int(input( f"{INPUT}Delay (0 = no delay)> "))
        avatar_url = input(f"{INPUT}Avatar link> ")

        send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url)
        return_to_menu()

    elif menu_choice == "2":
        webhook_url = input(f"{INPUT}Webhook URL> ")
        delete_webhook(webhook_url)
        print(f"{GEN_VALID}Webhook deleted.")
        return_to_menu()

    elif menu_choice == "3":
        webhook_url = input(f"{INPUT}Webhook URL> ")
        get_webhook_info(webhook_url)
        return_to_menu()
    elif menu_choice == "6":
         clear_console()
         Reset()
    elif menu_choice == "5":
        proxygen()
    elif menu_choice == "4":
        webhook_url = input(f"{INPUT}Webhook URL (Split by (,)'s )> ")
        username = input( f"{INPUT}Webhook Name> ")
        message = input( f"{INPUT}Message> ")
        num_messages = int(input( f"{INPUT}How many messages> "))
        cooldown = int(input( f"{INPUT}Delay (0 = no delay)> "))
        avatar_url = input(f"{INPUT}Avatar link> ")

        send_multi_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url)
        return_to_menu()

    else:
        print(f"{GEN_INVALID}Invalid choice.")
        return_to_menu()


show_menu()