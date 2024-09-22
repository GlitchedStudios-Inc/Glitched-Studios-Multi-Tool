import aiohttp
import asyncio
import concurrent.futures
import json
import os
import uuid
from colorama import Fore, Style, init


init(autoreset=True)

async def loginPlayfabAccount(session, url, payload, accountType, deviceId):
    async with session.post(url, json=payload) as response:
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
    else:
        print(Fore.YELLOW + "Invalid Title ID.")

def main():
    titleId = input("Enter Title ID: ")
    num_accounts = int(input("Enter number of accounts: "))
    device_id = str(uuid.uuid4())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(create_accounts(titleId, num_accounts, device_id))

if __name__ == "__main__":
    main()