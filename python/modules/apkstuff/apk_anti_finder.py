import UnityPy, os, subprocess, argparse, shutil, json
import random
import string
from pystyle import Colors, Colorate, Center, Anime
from colorama import *
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
import json
import fade
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
logo = fade.purplepink(f"""
	   ▄▄ • ▄▄▌  ▪  ▄▄▄▄▄ ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄      .▄▄ · ▄▄▄▄▄▄• ▄▌·▄▄▄▄  ▪        .▄▄ · 
	  ▐█ ▀ ▪██•  ██ •██  ▐█ ▌▪██▪▐█▀▄.▀·██▪ ██     ▐█ ▀. •██  █▪██▌██▪ ██ ██ ▪     ▐█ ▀. 
	  ▄█ ▀█▄██▪  ▐█· ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄▐█· ▐█▌    ▄▀▀▀█▄ ▐█.▪█▌▐█▌▐█· ▐█▌▐█· ▄█▀▄ ▄▀▀▀█▄
	  ▐█▄▪▐█▐█▌▐▌▐█▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌██. ██     ▐█▄▪▐█ ▐█▌·▐█▄█▌██. ██ ▐█▌▐█▌.▐▌▐█▄▪▐█
	  ·▀▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•      ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀█▄▀▪ ▀▀▀▀         
{reset}                                                              
""")
class AntiCheatDetector:
    def __init__(self, output_path):
        self.output_path = output_path
        self.anticheats = [
            "AntiCheatTool",
            "Anti Joystick",
            "HydrasAntiCheat",
            "DllSigmaThing",
            "WallHackDetector",
            "SpeedHackDetector",
            "ModTool",
            "GOOBEREER",
            "IgottaremanethisitwasmadebyK_S_H_R",
            "ApkChecker",
            "Antimodders",
            "Code.Stages.Anticheats",
            "HydrasPrivAntiCheat",
            "Entitlementcheck",
            "KSHRAnti",
            "VersionChecker",
            "AppEntitlementCheck",
            "SignatureCheck",
            "QuestLink",
            "AntiDll",
            "DllChecker",
            "LemonFolderChecker",
            "Melonloaderchecker",
            "ModsFolderChecker",
            "UnitysAntiCheat",
            
        ]

    def detect_anticheats(self, file_path):
        if not os.path.isfile(file_path):
            print("Please select a valid file.")
            return

        env = UnityPy.load(file_path)
        found_anticheats = set()

        for obj in env.objects:
            if obj.type.name == "GameObject":
                data = obj.read()
                self.extract_anticheats_from_data(data, found_anticheats)

            elif obj.type.name == "MonoScript":
                data = obj.read()
                self.extract_anticheats_from_data(data, found_anticheats)

        with open(self.output_path, 'w') as txt_file:
            if found_anticheats:
                txt_file.write("ANTI-CHEATS FOUND:\n")
                for anticheat in found_anticheats:
                    txt_file.write(anticheat + "\n")
                    print(f"{GEN_VALID}Anti Found: {anticheat}")
                print(f"{INFO}Anti-cheats found and saved to {self.output_path}")
            else:
                txt_file.write("No anti-cheats found.")
                print(f"{GEN_INVALID}No anti-cheats found. Result saved to {self.output_path}")

    def extract_anticheats_from_data(self, data, found_anticheats):
        import re
        tree = data.read_typetree()
        strings = []
        for key, value in tree.items():
            if isinstance(value, str):
                strings.append(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        strings.append(item)
            elif isinstance(value, dict):
                for k, v in value.items():
                    if isinstance(v, str):
                        strings.append(v)

        for string in strings:
            for anticheat in self.anticheats:
                pattern = re.compile(r'\b' + re.escape(anticheat.lower()) + r'\b')
                if pattern.search(string.lower()):
                    found_anticheats.add(anticheat)
def decompile(apk_path):
    print(f"\u001B[32mDecompiling\u001B[0m")
    script_dir = os.path.dirname(__file__)
    apktool_path = os.path.join(script_dir, 'resources', 'decompile', 'apktool.jar')
    apktool_path = os.path.abspath(apktool_path)
    sp = subprocess.Popen(["java", "-jar", apktool_path, "d", "-f", apk_path], stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

def main():
    parser = argparse.ArgumentParser(description='Anti-Cheat Detector')
    parser.add_argument('file_path', help='Path to the APK file')
    args = parser.parse_args()
    game_name = os.path.basename(args.file_path)[:-4]
    output_dir = f"output/apkstuff/antifinder/{game_name}"
    if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    decompile(args.file_path)
    output_path = os.path.join(output_dir, f"{game_name}_anticheats.txt")
    detector = AntiCheatDetector(output_path)
    detector.detect_anticheats(args.file_path)
    shutil.rmtree(args.file_path, ignore_errors=True)
if __name__ == "__main__":
    set_console_background_color()
    print(logo)
    main()