from playfab import PlayFabClientAPI, PlayFabSettings
from colorama import Fore, Style


color = Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE

INPUT = f'{red}[{white}>{red}] | {reset}'
INFO = f'{red}[{white}!{red}] | {reset}'
ERROR = f'{red}[{white}x{red}] | {reset}'
ADD = f'{red}[{white}+{red}] | {reset}'
WAIT = f'{red}[{white}~{red}] | {reset}'

GEN_VALID = f'{green}[{white}+{green}] | {reset}'
GEN_INVALID = f'{red}[{white}x{red}] | {reset}'
rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

logo = f"""
	 {rainbow_colors[0]}  ▄▄ • ▄▄▌  ▪  ▄▄▄▄▄ ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄      .▄▄ · ▄▄▄▄▄▄• ▄▌·▄▄▄▄  ▪        .▄▄ · 
	{rainbow_colors[1]}  ▐█ ▀ ▪██•  ██ •██  ▐█ ▌▪██▪▐█▀▄.▀·██▪ ██     ▐█ ▀. •██  █▪██▌██▪ ██ ██ ▪     ▐█ ▀. 
	 {rainbow_colors[2]} ▄█ ▀█▄██▪  ▐█· ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄▐█· ▐█▌    ▄▀▀▀█▄ ▐█.▪█▌▐█▌▐█· ▐█▌▐█· ▄█▀▄ ▄▀▀▀█▄
	 {rainbow_colors[3]} ▐█▄▪▐█▐█▌▐▌▐█▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌██. ██     ▐█▄▪▐█ ▐█▌·▐█▄█▌██. ██ ▐█▌▐█▌.▐▌▐█▄▪▐█
	{rainbow_colors[4]}  ·▀▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•      ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀█▄▀▪ ▀▀▀▀ 
"""
def check_title_id(title_id):
    PlayFabSettings.TitleId = title_id
    request = {
        "CustomId": "GettingStartedGuide",
        "CreateAccount": True
    }

    def callback(success, failure):
        if success:
            print(f"{GEN_VALID} {title_id} is Valid")
        else:
            print(f"{GEN_INVALID} {title_id} is Invalid")
            if failure:
                print("Here's some debug information:")
                print(failure.GenerateErrorReport())

    PlayFabClientAPI.LoginWithCustomID(request, callback)
print(logo)
title_id = input(f"{INPUT}Title Id: ")
check_title_id(title_id)