import requests
import json

# Set your PlayFab title ID and developer secret key
title_id = "YOUR_TITLE_ID"
dev_secret_key = "YOUR_DEV_SECRET_KEY"

# Set the API endpoint and headers
endpoint = f"https://{title_id}.playfabapi.com/Admin/GetPublisherData"
headers = {
    "Content-Type": "application/json",
    "X-SecretKey": dev_secret_key
}

# Set the request body (empty in this case, as we're not sending any data)
body = {}

# Send the request and get the response
response = requests.post(endpoint, headers=headers, json=body)

# Check if the response was successful
if response.status_code == 200:
    # Get the publisher data from the response
    publisher_data = response.json()["data"]

    # Store the publisher data to a file
    with open("output/playfabstuff/etxnight-playfab-output/publisher_data.json", "w") as f:
        json.dump(publisher_data, f, indent=4)

    print("Publisher data stored to publisher_data.json")
else:
    print("Error:", response.status_code, response.reason)