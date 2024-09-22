import aiohttp
import asyncio
import concurrent.futures
import json
import os
import uuid
import sys
from colorama import Fore, Style, init

init()  # Initialize colorama
def read_json_vars(filename, var1, var2):
    with open(filename, "r") as f:
        data = json.load(f)
        globals()[var1] = data[var1]
        globals()[var2] = data[var2]

read_json_vars("output/playfabstuff/etxnight-playfab-output/ids.json", "titleid", "devkey")

noa = 0  # Number of accounts created
failedacs = 0  # Number of failed accounts

async def loginPlayfabAccount(session, url, payload, accountType, deviceId):
    global noa, failedacs
    async with session.post(url, json=payload) as response:
        if response.status == 200:
            noa += 1
        else:
            failedacs += 1
        print(f"Sent {accountType}: {deviceId}")
        return response.status

async def verifyTitleId(titleId):
    async with aiohttp.ClientSession() as session:
        custom_id = str(uuid.uuid4())
        payload = {
            "TitleId": titleId,
            "CustomId": custom_id,
            "CreateAccount": True,
            "InfoRequestParameters": {
                "GetUserAccountInfo": True
            }
        }
        url = f"https://{titleId}.playfabapi.com/Client/LoginWithCustomID"
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                return True
            else:
                return False

def getAccountTypeInfo(titleId, deviceId):
    accountInfo = {
        "android": {
            "url": f"https://{titleId}.playfabapi.com/Client/LoginWithAndroidDeviceID",
            "payload": {
                "TitleId": titleId,
                "AndroidDeviceId": deviceId,
                "CreateAccount": True,
                "InfoRequestParameters": {
                    "GetUserAccountInfo": True
                }
            }
        },
        "nintendo": {
            "url": f"https://{titleId}.playfabapi.com/Client/LoginWithNintendoSwitchDeviceID",
            "payload": {
                "TitleId": titleId,
                "NintendoSwitchDeviceId": deviceId,
                "CreateAccount": True,
                "InfoRequestParameters": {
                    "GetUserAccountInfo": True
                }
            }
        },
        "ios": {
            "url": f"https://{titleId}.playfabapi.com/Client/LoginWithIOSDeviceID",
            "payload": {
                "TitleId": titleId,
                "DeviceId": deviceId,
                "CreateAccount": True,
                "InfoRequestParameters": {
                    "GetUserAccountInfo": True
                }
            }
        }
    }
    return [(accountType, info["url"], info["payload"]) for accountType, info in accountInfo.items()]

async def create_accounts(titleId, num_accounts, device_id):
    global noa, failedacs
    is_valid = await verifyTitleId(titleId)
    if is_valid:
        async with aiohttp.ClientSession() as session:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                loop = asyncio.get_event_loop()
                for _ in range(num_accounts):
                    tasks = [
                        loop.create_task(
                            loginPlayfabAccount(session, url, payload, accountType, device_id))
                        for accountType, url, payload in getAccountTypeInfo(titleId, device_id)
                    ]
                    await asyncio.gather(*tasks)
                    await asyncio.sleep(0)
                    if noa % 20 == 0:
                        print(f"{Fore.GREEN}account created: {noa}{Style.RESET_ALL} | {Fore.YELLOW}failed: {failedacs}{Style.RESET_ALL}")
    else:
        print("Invalid Title ID.")

def main():
    titleId = globals()['titleid']
    num_accounts = int(input("Enter number of accounts: "))
    device_id = str(uuid.uuid4())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(create_accounts(titleId, num_accounts, device_id))

main()
#F4AF3
#