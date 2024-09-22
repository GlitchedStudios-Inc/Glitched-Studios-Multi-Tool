import json
import os
import requests
from playfab import PlayFabClientAPI, PlayFabSettings
import sys

def get_title_data(title_id):
    url = f"https://{title_id}.playfabapi.com/Client/GetTitleData"
    headers = {
        "Content-Type": "application/json",
        "X-PlayFabSDK": "PlayFabSDK/2.94.210118",
        "X-Authorization": PlayFabSettings._internalSettings.ClientSessionTicket
    }
    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        print(response.content)
    else:
        response_json = json.loads(response.text)
        catalog = response_json['data']
        print(catalog)
        filename = f"output/playfabstuff/etxnight-playfab-output/titledata/{title_id}_titledata.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as outfile:
            json.dump(catalog, outfile)

def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")
title_id = globals()['titleid']
get_title_data(title_id)
