import requests
import json

def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

titleid = globals()['titleid']
devkey = globals()['devkey']

def get_account_master_id(playfab_id):
    url = f"https://{titleid}.playfabapi.com/Server/GetAccountInfo"
    payload = {
        "PlayFabId": playfab_id
    }
    headers = {
        "X-SecretKey": devkey
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        account_master_id = data.get("AccountInfo", {}).get("AccountMasterId")
        return account_master_id
    else:
        print(f"Failed to get account info. Error: {response.text}")
        return None

def grant_playfab_item():
    playfab_id = input("Enter the PlayFab ID: ")
    item_id = input("Enter the Item ID: ")
    catalog_version = input("Enter the Catalog Version: ")
    
    account_master_id = get_account_master_id(playfab_id)
    if account_master_id:
        url = f"https://{titleid}.playfabapi.com/Server/GrantItemsToUser"
        payload = {
            "PlayFabId": account_master_id,
            "ItemIds": [item_id],
            "CatalogVersion": catalog_version
        }
        headers = {
            "X-SecretKey": devkey
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            print(f"Item '{item_id}' granted successfully to Account Master ID '{account_master_id}'.")
        else:
            print(f"Failed to grant item. Error: {response.text}")
    else:
        print("Failed to get account master ID.")

grant_playfab_item()