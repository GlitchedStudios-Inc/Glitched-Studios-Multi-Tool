import os, sys
import time
import base64
from colorama import Fore

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
reset = Fore.RESET

def cls():
    os.system("cls")

Warning = f"{red}    [WARNING] The encrypted string is easily decodable and anyone with this tool can decode it!"

def crypt(text):
    cr1 = base64.encodebytes(text)
    cr2 = base64.b16encode(cr1)
    cr3 = base64.a85encode(cr2)
    return cr3
def decrypt(string):
    de1 = (base64.a85decode(string))
    de2 = (base64.b16decode(de1))
    de3 = (base64.decodebytes(de2))
    return de3

def main():
    cls()
    print(Warning)
    print("")
    option = input(f"""
    {green}[01]{blue} Encrypt text 
    {green}[02]{blue} Decrypt text
    {green}[{reset}BACK{green}]{blue} Go to the menu""")
    if option == "1":
        cls()
        cryptstring = input(f"{green}[{reset}CONFIG{green}]{blue} Enter text to encrypt {red}: ")
        cls()
        crypt(cryptstring)
        time.sleep(5)
        sys.exit(0)
    elif option == "2":
        cls()
        decryptstring = input(f"{green}[{reset}CONFIG{green}]{blue} Enter text to decrypt {red}: ")
        cls()
        decrypt(decryptstring)
        time.sleep(5)
        sys.exit(0)
    else:
        cls()
        print(f"{red}[{reset}ERROR{red}]{blue} Invalid input! ({option})")
        time.sleep(5)
        return
    
main()