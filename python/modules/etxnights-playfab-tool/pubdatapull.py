import requests
import json
from playfab import PlayFabClientAPI, PlayFabSettings
import sys
import os

def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

title_id = globals()['titleid']
dev_secret_key = globals()['devkey']

endpoint = f"https://{title_id}.playfabapi.com/Admin/GetPublisherData"
headers = {
    "Content-Type": "application/json",
    "X-SecretKey": dev_secret_key
}

body = {}

response = requests.post(endpoint, headers=headers, json=body)

if response.status_code == 200:
    publisher_data = response.json()["data"]

    os.makedirs("output/playfabstuff/etxnight-playfab-output/pubdata", exist_ok=True)  # create the pubdata folder if it doesn't exist
    with open(f"output/playfabstuff/etxnight-playfab-output/pubdata/publisher_data{title_id}.json", "w") as f:
        json.dump(publisher_data, f, indent=4)

    print("Publisher data stored to output/playfabstuff/etxnight-playfab-output/pubdata/publisher_data.json")
else:
    print("Error:", response.status_code, response.reason)