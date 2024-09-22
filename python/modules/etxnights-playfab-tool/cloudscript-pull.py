import json
import random
import sys
import requests
from playfab import PlayFabClientAPI, PlayFabSettings
import os

def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

titleid = globals()['titleid']
devkey = globals()['devkey']

customidthing1 = "OCULUS" + str(random.randrange(0, 10000000))


PlayFabSettings.TitleId = titleid

sexysession = None

thing = {
    "CustomId": customidthing1,
    "CreateAccount": True,
}

def callback(success, failure):
  global sexysession
  if success:
    print("Acc Info Shi:", success)
    sexysession = success.get("SessionTicket", None)
  else:
    print("Login failed. Something went wrong.")
    if failure:
      print("Debug information:")
      print(failure.GenerateErrorReport())

PlayFabClientAPI.LoginWithCustomID(callback=callback, request=thing)

get_catalog_items_endpoint = f"https://{titleid}.playfabapi.com/Client/GetCloudScriptRevision"
headers = {
    "Content-Type": "application/json",
    "X-SecretKey": devkey
}

response = requests.post(get_catalog_items_endpoint, headers=headers)

thingggg = os.path.join("output/playfabstuff/etxnight-playfab-output/cloudscripts", f"{titleid}-cloudscript")

if not os.path.exists("output/playfabstuff/etxnight-playfab-output/cloudscripts"):
    os.makedirs("output/playfabstuff/etxnight-playfab-output/cloudscripts")

with open(thingggg, "w") as output_file:
    if response.status_code != 200:
        output_file.write(f"failed {response.status_code}\n")
        output_file.write(response.content.decode('utf-8') + "\n")

    response_json = json.loads(response.text)
    output_file.write(json.dumps(response_json, indent=2))
# ---
response = requests.post(get_catalog_items_endpoint, headers=headers)

if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}")
    print(response.content.decode('utf-8'))
    sys.exit(1)

print("Response text:", response.text)

if not response.text:
    print("Response text is empty")
    sys.exit(1)

try:
    response_json = json.loads(response.text)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
    print("Response text:", response.text)
    sys.exit(1)

thingggg = os.path.join("output/playfabstuff/etxnight-playfab-output/cloudscripts", f"{titleid}-cloudscript")

if not os.path.exists("output/playfabstuff/etxnight-playfab-output/cloudscripts"):
    os.makedirs("output/playfabstuff/etxnight-playfab-output/cloudscripts")

with open(thingggg, "w") as output_file:
    output_file.write(json.dumps(response_json, indent=2))