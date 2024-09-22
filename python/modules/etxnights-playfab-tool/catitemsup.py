import requests
import json
import playfab
from playfab import PlayFabSettings, PlayFabClientAPI
import random
import os
from colorama import init, Fore, Style
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

titleid = globals()['titleid']

class LoginRequestData:

  def __init__(self, custom_id, create_account=True):
    self.CustomId = custom_id
    self.CreateAccount = create_account


init(autoreset=True)


def custom_id_login():
  randomthing = random.randint(0, 69000)
  custom_id = f"OCULUS{randomthing}"
  request_data = LoginRequestData(custom_id)
  PlayFabSettings.TitleId = titleid
  PlayFabClientAPI.LoginWithCustomID(request=request_data.__dict__,
                                     callback=login_callback)


def login_callback(success, failure):
  if success:
    print("successful")
    playfab_settings = PlayFabSettings._internalSettings
    headers = {
        "Content-Type": "application/json",
        "X-PlayFabSDK": "PlayFabSDK/2.0",
        "X-Authorization": playfab_settings.ClientSessionTicket
    }
    get_catalog_items_endpoint = f"https://{PlayFabSettings.TitleId}.playfabapi.com/Client/GetCatalogItems"
    response = session.post(get_catalog_items_endpoint, headers=headers)
    if response.status_code != 200:
      print(f"Request failed with status code {response.status_code}")
      print(response.content)
    else:
      response_json = json.loads(response.text)
      catalog = response_json['data']
      print(catalog)
      with open(f"output/playfabstuff/etxnight-playfab-output/{PlayFabSettings.TitleId}.json", "w") as outfile:
        json.dump(catalog, outfile)
  else:
    print("Something went wrong with your first API call.  :(")
    if failure and 'code' in failure and 'errorCode' in failure:
      error_code = failure['errorCode']
      error_message = failure['errorMessage']
      print(f"Error Code: {error_code}")
      print(f"Error Message: {error_message}")


session = requests.Session()
retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount('http://', adapter)
session.mount('https://', adapter)

custom_id_login()
input("Press Enter to exit...")