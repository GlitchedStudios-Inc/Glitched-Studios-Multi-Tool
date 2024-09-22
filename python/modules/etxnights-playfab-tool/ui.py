import os
import time
from pystyle import Colors, Colorate, Center, Anime
import subprocess
import sys
import json
import datetime

os.system('mode con: cols=87 lines=33')
os.system('title made by etxnight - etxnight.glitch.me - creds to snake for 2 scripts')
DESCRIPTION_COLOR = "\033[90m"  # Gray
OPTION_COLOR = "\033[92m"  # Green

def starrt():
    print("Input title id")
    titleid = input("> ")
    print("Your developer secret key if you have one or click return")
    devkey = input("> ")

    data = {
        "titleid": titleid,
        "devkey": devkey
    }

    with open("output/playfabstuff/etxnight-playfab-output/ids.json", "w") as f:
        json.dump(data, f, indent=4)

def mainnn():
    os.system("clear" if os.name == "posix" else "cls")
    now = datetime.datetime.now()
    print(Colorate.Horizontal(Colors.green_to_red, '''
etxnight.glitch.me -- made by etxnight -- etxnight.glitch.me -- made by etxnight -- etx
            __                                 .__           .__   __           
     ____ _/  |_         ____  ___  _________  |  |    ____  |__|_/  |_  ______ 
   _/ __ \\   __\_______/ __ \ \  \/  /\____  \ |  |   /  _ \ |  |\   __\/  ___/ 
   \  ___/ |  | /_____/\  ___/  >    < |  |_> >|  |__(  <_> )|  | |  |  \___ \  
    \___  >|__|         \___  >/__/\_ \|   __/ |____/ \____/ |__| |__| /____  > 
        \/                  \/       \/|__|                                 \/  
                                                                             '''))
    print(f'''
    {DESCRIPTION_COLOR}
           requires dev key            |       requires only title id {OPTION_COLOR}
        a1 pull cloudscript            | b1 playfab spammer - visuals but slow
        a2 pull database               | b2 playfab spammer - not visuals but fast
        a3 ban all players             | b3 pull title data
        a4 unban all players banned    | b4 pull user inventory
        a5 pull publisher data         | b5 pull catelog items
        a6 delete playfab catalog      | b6 pull user read only data
        a7 delete title                | b7 pull title public key
        a8 give catalog item to user   | b8 pull all
        a9 get account data            | b9 list catalog versions
                                       | b10 get currencys

                                       
    note: some script require things u pull using scripts
          like to get playfab id - pull database
    Back = Back To Glitched Studios Multi Tool

    Date: {now.strftime("%m/%d/%Y")} Time: {now.strftime("%I:%M:%S %p")}
    ''')

    while True:
        choice = input("     > ")
        if choice in ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "a6", "a7", "a8", "a9", "Back", "back", "B", "b"]:
            break
        else:
            print("Invalid choice. Please try again.")

    if choice == "a1":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/cloudscript-puller.py"])
        os.system('pause')
        mainnn()
    elif choice == "a2":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/database-puller.py"])
        os.system('pause')
        mainnn()
    elif choice == "a3":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/ban-all.py"])
        os.system('pause')
        mainnn()
    elif choice == "a4":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/unban-all.py"])
        os.system('pause')
        mainnn()
    elif choice == "b1":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/pfsslow.py"])
        os.system('pause')
        mainnn()
    elif choice == "b2":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/pfsfast.py"])
        os.system('pause')
        mainnn()
    elif choice == "b3":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/titledata.py"])
        os.system('pause')
        mainnn()
    elif choice == "b4":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/usrinv.py"])
    elif choice == "b5":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/catitemsup.py"])
        os.system('pause')
        mainnn()
    elif choice == "b6":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/urod.py"])
        os.system('pause')
        mainnn()
    elif choice == "b7":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/tpk.py"])
        os.system('pause')
        mainnn()
    elif choice == "a5":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/pubdatapull.py"])
        os.system('pause')
        mainnn()
    elif choice == "b8":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/all.py"])
        os.system('pause')
        mainnn()
    elif choice == "b9":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/listcatalogvers.py"])
        os.system('pause')
        mainnn()
    elif choice == "b10":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/getcurr.py"])
        os.system('pause')
        mainnn()
    elif choice == "a6":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/delpc.py"])
        os.system('pause')
        mainnn()
    elif choice == "a7":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/deltitle.py"])
        os.system('pause')
        mainnn()
    elif choice == "a8":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/gpi.py"])
        os.system('pause')
        mainnn()
    elif choice == "a9":
        subprocess.run(["python", "python/modules/etxnights-playfab-tool/gad.py"])
        os.system('pause')
        mainnn()
    elif choice in ["Back", "back", "b", "B"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        subprocess.run(["python", "python/main.py"])

    time.sleep(3)

starrt()
mainnn()