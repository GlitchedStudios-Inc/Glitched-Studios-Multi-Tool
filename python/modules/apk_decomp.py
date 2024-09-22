import os
from colorama import Fore
import shutil
import time

rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

color = Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
blue = color.BLUE

INPUT = f'{red}[{white}>{red}] | {reset}'
INFO = f'{red}[{white}!{red}] | {reset}'
ERROR = f'{red}[{white}x{red}] | {reset}'
ADD = f'{red}[{white}+{red}] | {reset}'
WAIT = f'{red}[{white}~{red}] | {reset}'

GEN_VALID = f'{green}[{white}+{green}] | {reset}'
GEN_INVALID = f'{red}[{white}x{red}] | {reset}'

path = input("Path: ")

os.system(f"python\\modules\\decomp\\Cpp2IL2.exe --game-path {path} --just-give-me-dlls-asap-dammit")

# Wait for the cpp2il_out folder to be created
cpp2il_out_folder = os.path.join("cpp2il_out")
while not os.path.exists(cpp2il_out_folder):
    time.sleep(1)  # wait for 1 second

# Get the APK name from the path
apk_name = os.path.basename(path)
apk_name = os.path.splitext(apk_name)[0]

# Create the output/decomp folder if it doesn't exist
output_folder = "output/apkstuff/decomp"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Move the cpp2il_out folder to output/decomp and rename it to the APK name
decomp_folder = os.path.join(output_folder, apk_name)
shutil.move(cpp2il_out_folder, decomp_folder)

print(f"{GEN_VALID} Successful")