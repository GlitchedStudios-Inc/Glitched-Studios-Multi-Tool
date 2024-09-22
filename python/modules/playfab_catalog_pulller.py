import requests
import json
import playfab
from playfab import PlayFabSettings, PlayFabClientAPI
import random
import os
from colorama import init, Fore, Style
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import uuid
import subprocess
import jsonlint
init(autoreset=True)

rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
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

logo = f"""
	 {rainbow_colors[0]}  ▄▄ • ▄▄▌  ▪  ▄▄▄▄▄ ▄▄·  ▄.▄▄▄▄.·▄▄▄▄     .▄▄ · ▄▄▄▄▄▄• ▄▌·▄▄▄▄  ▪       .▄▄ · 
	{rainbow_colors[1]}  ▐█ ▀ ▪██•  ██ •██  ▐█ ▌▪██▪▐█▀▄.▀·██▪ ██     ▐█ ▀. •██  █▪██▌██▪ ██ ██ ▪     ▐█ ▀. 
	 {rainbow_colors[2]} ▄█ ▀█▄██▪  ▐█· ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄▐█· ▐█▌    ▄▀▀▀█▄ ▐█.▪█▌▐█▌▐█· ▐█▌▐█· ▄█▀▄ ▄▀▀▀█▄
	 {rainbow_colors[3]} ▐█▄▪▐█▐█▌▐▌▐█▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌██. ██     ▐█▄▪▐█ ▐█▌·▐█▄█▌██. ██ ▐█▌▐█▌.▐▌▐█▄▪▐█
	{rainbow_colors[4]}  ·▀▀▀▀.▀▀▀ ▀▀▀ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•      ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀█▄▀▪ ▀▀▀▀ 
"""

class LoginRequestData:
    def __init__(self, custom_id, create_account=True):
        self.CustomId = custom_id
        self.CreateAccount = create_account

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print("MADE BY PRVIPER")

def custom_id_login():
    randomthing = random.randint(0, 69000)
    custom_id = f"OCULUS{randomthing}"
    request_data = LoginRequestData(custom_id)
    PlayFabSettings.TitleId = input(f"{INPUT}Title ID: ")
    PlayFabClientAPI.LoginWithCustomID(request=request_data.__dict__, callback=login_callback)


def login_callback(success, failure):
    if success:
        print(f"{GEN_VALID}Login successful!")
        playfab_settings = PlayFabSettings._internalSettings
        headers = {
            "Content-Type": "application/json",
            "X-PlayFabSDK": "PlayFabSDK/2.0",
            "X-Authorization": playfab_settings.ClientSessionTicket
        }
        get_catalog_items_endpoint = f"https://{PlayFabSettings.TitleId}.playfabapi.com/Client/GetCatalogItems"
        response = session.post(get_catalog_items_endpoint, headers=headers)
        if response.status_code!= 200:
            print(f"{GEN_INVALID}Request failed with status code {response.status_code}")
            print(f"Error response: {response.content}")
        else:
            response_json = json.loads(response.text)
            print(f"Response JSON: {response_json}")
            catalog = response_json.get('data')
            if catalog is None:
                print(f"{GEN_INVALID}Catalog data is empty or missing")
            else:
                print(f"Catalog items:")
                for item in catalog:
                    if isinstance(item, dict):
                        print(f"{ADD}  Item ID: {item.get('ItemId')}")
                        print(f"{ADD}  Display Name: {item.get('DisplayName')}")
                        print(f"{ADD}  Catalog Version: {item.get('CatalogVersion')}")
                        print(f"{ADD}  Can Become Character: {item.get('CanBecomeCharacter')}")
                        print(f"{ADD}  Is Stackable: {item.get('IsStackable')}")
                        print(f"{ADD}  Is Tradable: {item.get('IsTradable')}")
                        print(f"{ADD}  Is Limited Edition: {item.get('IsLimitedEdition')}")
                        print(f"{ADD}  Initial Limited Edition Count: {item.get('InitialLimitedEditionCount')}")
                    else:
                        print(f"{ADD}  Item: {item}") 
                    print("") 
                with open(f"output/playfabstuff/catalog/{PlayFabSettings.TitleId}.json", "w") as outfile:
                    json.dump(catalog, outfile, indent=4) 
                print(f"Catalog saved to output/playfabstuff/catalog/{PlayFabSettings.TitleId}.json")
               

                
    else:
        print(f"{ERROR}Something went wrong with your first API call. :(")
        if failure and 'code' in failure and 'errorCode' in failure:
            error_code = failure['errorCode']
            error_message = failure['errorMessage']
            print(f"{ERROR}Error Code: {error_code}")
            print(f"{ERROR}Error Message: {error_message}")
session = requests.Session()
retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount('https://', adapter)

print_banner()
custom_id_login()