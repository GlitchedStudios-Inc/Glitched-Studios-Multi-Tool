import requests
import json
import os

def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

titleid = globals()['titleid']
devkey = globals()['devkey']

def get_account_data(playfab_id):
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
        return data
    else:
        print(f"Failed to get account info. Error: {response.text}")
        return None

def save_account_data(playfab_id, data):
    folder_name = "output/playfabstuff/etxnight-playfab-output/accdata"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    file_name = f"account_data{playfab_id}.json"
    file_path = os.path.join(folder_name, file_name)
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def main():
    playfab_id = input("Enter the PlayFab ID: ")
    data = get_account_data(playfab_id)
    if data:
        save_account_data(playfab_id, data)
        print(f"Account data saved to accdata/account_data{playfab_id}.json")
    else:
        print("Failed to get account data.")


main()