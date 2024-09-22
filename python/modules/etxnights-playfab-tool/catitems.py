import json
import os
from playfab import PlayFabClientAPI, PlayFabSettings

def read_json_vars(filename, var1):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid")
title_id = globals()['titleid']

def get_catalog_items(title_id):
    # Initialize PlayFabSettings
    PlayFabSettings._internalSettings.TitleId = title_id
    PlayFabClientAPI.SetTitleId(title_id)

    try:
        catalog_items = PlayFabClientAPI.GetCatalogItems()
        print(json.dumps(catalog_items, indent=4))  # pretty-print the catalog items
        filename = f"output/playfabstuff/etxnight-playfab-output/{title_id}_catalog.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as outfile:
            json.dump(catalog_items, outfile)
    except Exception as e:
        print(f"Error: {e}")

get_catalog_items(title_id)