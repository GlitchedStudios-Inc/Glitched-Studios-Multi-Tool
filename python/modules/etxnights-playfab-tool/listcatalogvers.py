import json
import requests

def read_json_vars(filename, var1):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid")

title_id = globals()['titleid']

def get_catalog_items():
    url = f"https://{title_id}.playfabapi.com/Client/GetCatalogItems"
    
    response = requests.post(url)
    
    if response.status_code == 200:
        catalog_items = response.json()["Catalog"]
        print("Available Catalog Items:")
        for item in catalog_items:
            print(item["ItemId"])
    else:
        print(f"Failed to get catalog items. Error: {response.text}")

get_catalog_items()