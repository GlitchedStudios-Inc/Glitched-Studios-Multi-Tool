import aiohttp
import asyncio
import concurrent.futures
import json
import os
import tkinter as tk
import uuid
from colorama import Fore, Style, init

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + '''    
    =======
    |
    ====
    |
    |
    |   R O G G Y
    ''')

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

def create_multiple_accounts(titleId, num_accounts, device_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(create_accounts(titleId, num_accounts, device_id))

def create_accounts_on_click():
    titleId = titleIdEntry.get()
    num_accounts = int(numAccountsEntry.get())
    device_id = str(uuid.uuid4())
    create_multiple_accounts(titleId, num_accounts, device_id)

# Create Tkinter window
root = tk.Tk()
root.title("Bsu's SpammerThing")

# Title ID input
titleIdLabel = tk.Label(root, text="Title ID:")
titleIdLabel.grid(row=0, column=0)
titleIdEntry = tk.Entry(root)
titleIdEntry.grid(row=0, column=1)

# Number of accounts input
numAccountsLabel = tk.Label(root, text="Number of Accounts:")
numAccountsLabel.grid(row=1, column=0)
numAccountsEntry = tk.Entry(root)
numAccountsEntry.grid(row=1, column=1)

# Button to create accounts
createButton = tk.Button(root, text="Create Accounts", command=create_accounts_on_click)
createButton.grid(row=2, columnspan=2)

# Start Tkinter event loop
root.mainloop()