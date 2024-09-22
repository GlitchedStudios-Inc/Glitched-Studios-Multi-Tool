import subprocess
import os
import sys
import fade

logo = fade.purplepink(f"""
	   ▄▄ • ▄▄▌  ▪  ▄▄▄▄▄ ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄      .▄▄ · ▄▄▄▄▄▄• ▄▌·▄▄▄▄  ▪        .▄▄ · 
	  ▐█ ▀ ▪██•  ██ •██  ▐█ ▌▪██▪▐█▀▄.▀·██▪ ██     ▐█ ▀. •██  █▪██▌██▪ ██ ██ ▪     ▐█ ▀. 
	  ▄█ ▀█▄██▪  ▐█· ▐█.▪██ ▄▄██▀▐█▐▀▀▪▄▐█· ▐█▌    ▄▀▀▀█▄ ▐█.▪█▌▐█▌▐█· ▐█▌▐█· ▄█▀▄ ▄▀▀▀█▄
	  ▐█▄▪▐█▐█▌▐▌▐█▌ ▐█▌·▐███▌██▌▐▀▐█▄▄▌██. ██     ▐█▄▪▐█ ▐█▌·▐█▄█▌██. ██ ▐█▌▐█▌.▐▌▐█▄▪▐█
	  ·▀▀▀▀ .▀▀▀ ▀▀▀ ▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•      ▀▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀█▄▀▪ ▀▀▀▀         
""")
patcher_dir = os.path.dirname(os.path.abspath(__file__))

tools_dir = os.path.join(patcher_dir, 'apk_entitlement_checker_patcher_stuff')

output_dir = "output/apkstuff/apk_entitlement_checker_patcher_output/"

def decompile_apk(apk_path, apk_name):
    """Decompile the APK using apktool."""
    print("[+] DECOMPILING APK")
    
    subprocess.run(['java', '-jar', os.path.join(tools_dir, 'tools', 'apktool_2.9.3.jar'), 'd', '-f', '--force-manifest', '-o', apk_name, apk_path])

def patch_apk(name):
    """Patch the decompiled APK."""
    print("Patching is about to start...")
    print("***PLEASE NOTE***")
    print("After patching is completed it will say:")
    print("Press any key to exit...")
    print("Go ahead and press any key but the script is NOT done yet!")
    print("ONLY the patching has been finished.")
    print("The recompiling and signing of the APK will happen next.")
    input("Press Enter to continue...")
    print(f"\n[+]Patching {name} has started")
    if os.path.exists(f"{name}/lib/arm64-v8a/libovrplatformloader.so"):
        print("APK is 64 bit.")
        subprocess.run([os.path.join(tools_dir, 'Patcher.exe'), f"{name}/lib/arm64-v8a/libovrplatformloader.so", 'ovr_Message_IsError', '0'])
    elif os.path.exists(f"{name}lib/armeabi-v7a/libovrplatformloader.so"):
        print("APK is 32 bit.")
        subprocess.run([os.path.join(tools_dir, 'Patcher.exe'), f"{name}/lib/armeabi-v7a/libovrplatformloader.so", 'ovr_Message_IsError', '0'])
    elif os.path.exists(f"{name}lib/arm64-v8a/libOVRPlatform64_1.so"):
        print("APK is 64 bit VIRTUAL DESKTOP.")
        subprocess.run([os.path.join(tools_dir, 'Patcher.exe'), f"{name}/lib/arm64-v8a/libOVRPlatform64_1.so", 'ovr_Message_IsError', '0'])
def main():

    apk_path = sys.argv[1]
    apk_name = os.path.splitext(os.path.basename(apk_path))[0]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    decompile_apk(apk_path, apk_name)
    patch_apk(apk_name)
    print("Use Apk Toolkit To Complie The Game")

if __name__ == "__main__":
    print(logo)
    main()