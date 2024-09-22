import json
import requests
import warnings
warnings.simplefilter('ignore')

def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

title_id = globals()['titleid']
developer_secret_key = globals()['devkey']

def get_catalog_versions():
    url = f"https://{title_id}.playfabapi.com/Admin/GetCatalogVersions"
    headers = {
        "X-SecretKey": developer_secret_key
    }
    
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        catalog_versions = response.json()["CatalogVersions"]
        print("Available Catalog Versions:")
        for version in catalog_versions:
            print(version)
        return catalog_versions
    else:
        print(f"Failed to get catalog versions. Error: {response.text}")
        return []

def clear_playfab_catalog():
    catalog_versions = get_catalog_versions()
    if not catalog_versions:
        print("No catalog versions available.")
        return
    
    catalog_version = input("Enter the Catalog Version to clear: ")
    
    url = f"https://{title_id}.playfabapi.com/Admin/UpdateCatalog"
    headers = {
        "X-SecretKey": developer_secret_key
    }
    payload = {
        "Catalog": [],
        "CatalogVersion": catalog_version
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(f"Catalog version '{catalog_version}' cleared successfully.")
    else:
        print(f"Failed to clear catalog version. Error: {response.text}")


clear_playfab_catalog()