import json
import os
import random
# https://replit.com/@dwoods15654/VSP-Playfab-Catalog-Puller?v=1#main.py
import requests
from playfab import PlayFabClientAPI, PlayFabSettings

proxies = {'http': 'http://167.235.205.228:8080'}

randomthing = random.randint(0, 69000)
Thing2 = randomthing
thing = {"CustomId": f"OCULUSMODD{randomthing}", "CreateAccount": True}
def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

PlayFabTitleID = globals()['titleid']
PlayFabSettings.TitleId = PlayFabTitleID


def callback(success, failure):
    if success:
        print("Congratulations You Pulled A Catalog!")
    else:
        print("Oh No! Your API Failed. Please Try Again:(")
        if failure:
            print("Here's some debug information:")
            print(failure.GenerateErrorReport())


PlayFabClientAPI.LoginWithCustomID(callback=callback, request=thing)

urls = [
    (f"https://{PlayFabTitleID}.playfabapi.com/Client/GetTitleData", f"titledata/{PlayFabTitleID}_titledata.json"),
    (f"https://{PlayFabTitleID}.playfabapi.com/Client/GetUserInventory", f"inventory/{PlayFabTitleID}_inventory.json"),
    (f"https://{PlayFabTitleID}.playfabapi.com/Client/GetCatalogItems", f"catalog/{PlayFabTitleID}_catalog.json"),
    (f"https://{PlayFabTitleID}.playfabapi.com/Client/GetUserReadOnlyData", f"stuff/{PlayFabTitleID}_stuff.json"),
    (f"https://{PlayFabTitleID}.playfabapi.com/Client/GetTitlePublicKey", f"pubkeys/{PlayFabTitleID}_titlepubkey.json")
]

headers = {
    "Content-Type": "application/json",
    "X-PlayFabSDK": "PlayFabSDK/2.94.210118",
    "X-Authorization": PlayFabSettings._internalSettings.ClientSessionTicket
}

for url, filename in urls:
    response = requests.post(url,
                             json=thing,
                             headers=headers,
                             proxies=proxies)
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        print(response.content)
    else:
        response_json = json.loads(response.text)
        catalog = response_json['data']
        print(catalog)

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w") as outfile:
            json.dump(catalog, outfile)