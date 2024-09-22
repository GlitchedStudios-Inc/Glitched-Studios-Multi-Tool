import json
import requests
from pystyle import Colors, Colorate, Center, Anime
import ctypes
from colorama import *
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
logo = Colorate.Horizontal (Colors.red_to_blue, f"""
     ▄▄ • ▄▄▌  ▪  ▄▄▄▄▄ ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄      .▄▄ · ▄▄▄▄▄▄• ▄▌·▄▄▄▄  ▪        .▄▄ · 
    ▐█ ▀ ▪██•  ██ •██  ▐█ ▌▪██▪▐█▀▄.▀·██▪ ██     ▐█ ▀. •██  █▪██▌██▪ ██ ██ ▪     ▐█ ▀. 
    ▄█ ▀█▄██▪  ▐█· ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄▐█· ▐█▌    ▄▀▀▀█▄ ▐█.▪█▌▐█▌▐█· ▐█▌▐█· ▄█▀▄ ▄▀▀▀█▄
    ▐█▄▪▐█▐█▌▐▌▐█▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌██. ██     ▐█▄▪▐█ ▐█▌·▐█▄█▌██. ██ ▐█▌▐█▌.▐▌▐█▄▪▐█
    ·▀▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•      ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀█▄▀▪ ▀▀▀▀ 
""")
script_dir = os.path.dirname(__file__)
config_path = os.path.join(script_dir, 'settings', 'configs', 'MenuSettings.json')

with open("settings/configs/MenuSettings.json") as f:
    config = json.load(f)

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
def title_changer(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
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
reset = Style.RESET_ALL

INPUT = f'{input_color}[{Fore.WHITE}>{input_color}] | {reset}'
INFO = f'{info_color}[{Fore.WHITE}!{info_color}] | {reset}'
ERROR = f'{error_color}[{Fore.WHITE}x{error_color}] | {reset}'
ADD = f'{add_color}[{Fore.WHITE}+{add_color}] | {reset}'
WAIT = f'{wait_color}[{Fore.WHITE}~{wait_color}] | {reset}'

GEN_VALID = f'{gen_valid_color}[{Fore.WHITE}+{gen_valid_color}] | {reset}'
GEN_INVALID = f'{gen_invalid_color}[{Fore.WHITE}x{gen_invalid_color}] | {reset}'
def get_all_segments(title_id, secret_key):
    url = f"https://{title_id}.playfabapi.com/Admin/GetAllSegments"
    headers = {"Content-Type": "application/json", "X-SecretKey": secret_key}
    response = requests.post(url, headers=headers)
    response_json = response.json()
    return response_json

def get_all_players_segment_id(title_id, secret_key):
    segments_response = get_all_segments(title_id, secret_key)
    if segments_response['code'] != 200:
        print(f"Failed to retrieve segments: {segments_response['errorMessage']}")
        return None
    all_players_segment = next(
        (segment for segment in segments_response['data']['Segments']
         if segment['Name'] == 'All Players'), None)
    if not all_players_segment:
        print("Failed to find the 'All Players' segment.")
        return None
    return all_players_segment['Id']

def get_players_in_segment(title_id, developer_secret_key, segment_id):
    url = f"https://{title_id}.playfabapi.com/Admin/GetPlayersInSegment"
    headers = {
        "Content-Type": "application/json",
        "X-SecretKey": developer_secret_key
    }
    request_body = {"SegmentId": segment_id}
    response = requests.post(url, headers=headers, json=request_body)
    return response

def process_response(response, title_id, segment_id):
    if response.status_code == 200:
        response_json = response.json()
        player_profiles = response_json.get("data", {}).get("PlayerProfiles", [])
        if player_profiles:
            print(f"{gen_valid_color}Playerbase:")
            for profile in player_profiles:
                print(f"{reset}Segments: {segment_id}")
                print(json.dumps(profile, indent=4))
            output_dir = "output/playfabstuff/PlayfabDataBaseINFO/"
            with open(os.path.join(output_dir, f'{title_id}_PlayerData.json'), 'w') as file:
                file.write(json.dumps(player_profiles, indent=4))
        else:
            print(f"No segments found.")
    else:
        print(f"Request failed. Error code: {response.status_code}")
        print(f"Error message: {response.text}")

def main():
    title_changer("Glitched Studios Multi Tool | Grab Playfab Database")
    print(logo)
    title_id = input(f"{INPUT}Enter Your Playfab Title Id: ")
    developer_secret_key = input(f"{INPUT}Enter Your Dev Key: ")
    segment_id = get_all_players_segment_id(title_id, developer_secret_key)
    if segment_id:
        print(f"Auto selected the 'All Players' segment with ID: {segment_id}")
        response = get_players_in_segment(title_id, developer_secret_key, segment_id)
        process_response(response, title_id, segment_id)
    else:
        print("Failed to retrieve the 'All Players' segment ID.")
        exit()

if __name__ == "__main__":
    main()