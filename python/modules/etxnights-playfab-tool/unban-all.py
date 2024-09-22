import requests
import json
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

requests.packages.urllib3.util.ssl_.DEFAULT_SSL_CONTEXT = ssl_context
# Replace these with your actual PlayFab Title ID and API Key
def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

title_id = globals()['titleid']
secret_key = globals()['devkey']

# Set your PlayFab title ID and secret key

# Set the API endpoint and headers
endpoint = f"https://{title_id}.playfabapi.com/Admin"
headers = {
    "X-SecretKey": secret_key,
    "Content-Type": "application/json"
}

# Get all banned users
banned_users_response = requests.post(
    f"{endpoint}/GetUserBans",
    headers=headers,
    json={}
)

if banned_users_response.status_code == 200:
    banned_users = json.loads(banned_users_response.content)["data"]
    print(f"Found {len(banned_users)} banned users")

    # Extract ban IDs
    ban_ids = [ban["BanId"] for ban in banned_users]

    # Revoke bans
    revoke_bans_response = requests.post(
        f"{endpoint}/RevokeBans",
        headers=headers,
        json={"BanIds": ban_ids}
    )

    if revoke_bans_response.status_code == 200:
        print("Successfully revoked bans")
    else:
        print(f"Failed to revoke bans: {revoke_bans_response.text}")
else:
    print(f"Failed to get banned users: {banned_users_response.text}")