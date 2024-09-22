import requests
import json
import os

def read_json_vars(filename, var1):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid")

titleid = globals()['titleid']

def get_currencies(playfab_id):
    url = f"https://{titleid}.playfabapi.com/Client/GetCurrencyBalances"
    payload = {
        "PlayFabId": playfab_id
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to get currencies. Error: {response.text}")
        return None

def main():
    playfab_id = input("Enter the PlayFab ID: ")
    currencies = get_currencies(playfab_id)
    if currencies:
        print("Currencies:")
        for currency in currencies["Balance"]:
            print(f"{currency['CurrencyCode']}: {currency['BalanceValue']}")
    else:
        print("Failed to get currencies.")

main()