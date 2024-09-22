import os
import requests
import json
import sys

def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

titleid = globals()['titleid']
developer_secret_key = globals()['devkey']

url = f"https://{titleid}.playfabapi.com/Admin/GetSegments"

headers = {
  "Content-Type": "application/json",
  "X-SecretKey": developer_secret_key
}

request_body = {"SegmentIds": []}

response = requests.post(url, headers=headers, json=request_body)

output_file_path = os.path.join("databases", f"{titleid}-segments.json")

if not os.path.exists("output/playfabstuff/etxnight-playfab-output/databases"):
    os.makedirs("output/playfabstuff/etxnight-playfab-output/databases")

with open(output_file_path, "w") as output_file:
    if response.status_code == 200:
        output_file.write("GetSegments request successful.\n")

        response_json = response.json()

        segments = response_json.get("data", {}).get("Segments", [])

        if segments:
            output_file.write("Segments:\n")
            for segment in segments:
                segment_id = segment.get("Id")
                output_file.write(f"Segment ID: {segment_id}\n")
                json.dump(segment, output_file, indent=4)
                output_file.write("\n")
        else:
            output_file.write("No segments found.\n")
    else:
        output_file.write(f"GetSegments request failed. Error code: {response.status_code}\n")
        output_file.write(f"Error message: {response.text}\n")

print(f"Output written to {output_file_path}")
import json

import requests

print("""
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
   PlayerDataBase Puller!
  credits: MellowFishy                                                               
<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
""")

segment_id = input("enter segment id lol: ")

url = f"https://{titleid}.playfabapi.com/Admin/GetPlayersInSegment"

headers = {
  "Content-Type": "application/json",
  "X-SecretKey": developer_secret_key
}

request_body = {"SegmentId": segment_id}

response = requests.post(url, headers=headers, json=request_body)

os.makedirs('output/playfabstuff/etxnight-playfab-output/databases', exist_ok=True)

if response.status_code == 200:
    print("GetSegments request successful.")

    response_json = response.json()

    segments = response_json.get("data", {}).get("PlayerProfiles", [])

    if segments:
        print("Playerbase:")
        for segment in segments:
            print(f"Playerbase: {segment.get('id', 'Unknown ID')}")
            print(json.dumps(segment, indent=4))

        # Save to file in 'databases' folder
        file_path = os.path.join('output/playfabstuff/etxnight-playfab-output/databases', f'playerbase{titleid}.txt')
        with open(file_path, 'w') as file:
            file.write(json.dumps(segments, indent=4))
        print(f"Data saved to {file_path}")
    else:
        print("No segments found.")
else:
    print(f"GetSegments request failed. Error code: {response.status_code}")
    print(f"Error message: {response.text}")

input("Press Enter to exit...")