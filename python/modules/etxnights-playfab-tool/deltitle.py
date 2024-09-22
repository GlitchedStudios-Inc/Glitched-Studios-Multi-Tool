import requests
import json
def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

title_id = globals()['titleid']
dev_secret_key = globals()['devkey']

def delete_playfab_title():
    
    url = f"https://{title_id}.playfabapi.com/Admin/DeleteTitle"
    headers = {
        "X-SecretKey": dev_secret_key
    }
    
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        print("Title deleted successfully.")
    else:
        print(f"Failed to delete title. Error: {response.text}")
delete_playfab_title()