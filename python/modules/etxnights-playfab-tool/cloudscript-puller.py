import json
import os
import requests
from playfab import PlayFabClientAPI, PlayFabSettings

# Set your title ID and developer secret key
def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

titleid = globals()['titleid']
devkey = globals()['devkey']

# Set the endpoint and headers
get_cloud_script_revision_endpoint = f"https://{titleid}.playfabapi.com/Admin/GetCloudScriptRevision"
headers = {
    "Content-Type": "application/json",
    "X-SecretKey": devkey
}

# Set the request body
request_body = {
    "Revision": -1,
    "Version": -1
}

# Make the request
response = requests.post(get_cloud_script_revision_endpoint, headers=headers, json=request_body)

# Check if the request was successful
if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}")
    print(response.content.decode('utf-8'))
    exit(1)

# Parse the response JSON
response_json = response.json()

# Get the cloud script revisions
revisions = response_json["Revisions"]

# Create the directory if it doesn't exist
if not os.path.exists("output/playfabstuff/etxnight-playfab-output/cloudscripts"):
    os.makedirs("output/playfabstuff/etxnight-playfab-output/cloudscripts")

# Save each revision to a file
for revision in revisions:
    filename = os.path.join("output/playfabstuff/etxnight-playfab-output/cloudscripts", f"{titleid}-cloudscript-{revision['Revision']}.json")
    with open(filename, "w") as output_file:
        json.dump(revision, output_file, indent=2)

print("Cloud script revisions saved to cloudscripts directory")