import requests
import concurrent.futures
import json
from datetime import datetime, timedelta
def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

titleid = globals()['titleid']
devkey = globals()['devkey']
title_id = titleid
secret_key = devkey



def get_all_segments(title_id, secret_key):
  url = f"https://{title_id}.playfabapi.com/Admin/GetAllSegments"
  headers = {"Content-Type": "application/json", "X-SecretKey": secret_key}
  response = requests.post(url, headers=headers)
  response_json = response.json()
  return response_json


def get_segment_users(title_id, secret_key, segment_id):
  url = f"https://{title_id}.playfabapi.com/Admin/GetPlayersInSegment"
  headers = {"Content-Type": "application/json", "X-SecretKey": secret_key}
  data = {"SegmentId": segment_id}
  response = requests.post(url, json=data, headers=headers)
  response_json = response.json()
  return response_json


def ban_user(title_id, secret_key, playfab_id, reason, duration_hours):
  url = f"https://{title_id}.playfabapi.com/Admin/BanUsers"
  headers = {"Content-Type": "application/json", "X-SecretKey": secret_key}
  ban_duration = timedelta(hours=duration_hours)
  unban_time = datetime.utcnow() + ban_duration
  unban_time_iso = unban_time.isoformat() + "Z"
  data = {
    "Bans": [{
      "PlayFabId": playfab_id,
      "Reason": reason,
      "DurationInHours": duration_hours,
      "Expires": unban_time_iso
    }]
  }
  response = requests.post(url, json=data, headers=headers)
  response_json = response.json()
  return response_json


segments_response = get_all_segments(title_id, secret_key)
if segments_response['code'] != 200:
  print(f"Failed to retrieve segments: {segments_response['errorMessage']}")
  exit()

all_players_segment = next(
  (segment for segment in segments_response['data']['Segments']
   if segment['Name'] == 'All Players'), None)
if not all_players_segment:
  print("Failed to find the 'All Players' segment.")
  exit()

print(
  f"Auto selected the 'All Players' segment with ID: {all_players_segment['Id']}"
)

segment_id = all_players_segment['Id']
reason = input("Enter the ban reason: ")
duration_hours = int(input("Enter the ban duration in hours: "))

users_response = get_segment_users(title_id, secret_key, segment_id)
if users_response['code'] != 200:
  print(f"Failed to retrieve segment users: {users_response['errorMessage']}")
  exit()

playfab_ids = [
  user['PlayerId'] for user in users_response['data']['PlayerProfiles']
]


def ban_single_user(playfab_id):
  ban_response = ban_user(title_id, secret_key, playfab_id, reason,
                          duration_hours)
  if ban_response['code'] == 200:
    ban_duration = timedelta(hours=duration_hours)
    unban_time = datetime.utcnow() + ban_duration
    print(f"User with PlayFab ID '{playfab_id}' banned successfully")
    return {
      "PlayFabId": playfab_id,
      "Status": "Banned",
      "BanTime": datetime.utcnow().isoformat() + "Z",
      "UnbanTime": unban_time.isoformat() + "Z"
    }
  else:
    print(
      f"Failed to ban user with PlayFab ID '{playfab_id}': {ban_response['errorMessage']}"
    )
    return {"PlayFabId": playfab_id, "Status": "Failed"}


session = requests.Session()

max_workers = 30

banned_players = []

with concurrent.futures.ThreadPoolExecutor(
    max_workers=max_workers) as executor:

  ban_futures = [
    executor.submit(ban_single_user, playfab_id) for playfab_id in playfab_ids
  ]

  for future in concurrent.futures.as_completed(ban_futures):
    banned_player = future.result()
    banned_players.append(banned_player)

filename = "output/playfabstuff/etxnight-playfab-output/banned_players.json"
with open(filename, 'w') as file:
  json.dump(banned_players, file, indent=4)

print(f"\nBanned players logged in '{filename}'\n")

input("Press enter to exit")