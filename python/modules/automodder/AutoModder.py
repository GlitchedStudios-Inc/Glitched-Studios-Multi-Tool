import UnityPy, os, subprocess, argparse, shutil, json

def modUnity3d(path, noWalls, noGrav, pvp):
    enable = []
    disable = []
    ignore = []
    reenable = []
    scale = []
    enable_is = []
    ends_in = []
    disable_is = [] # [ 'fly2' ] for cebus
    # enable_parent = [ 'enable', 'button', 'equip' ] doesn't work yet
    
    with open("settings/configs/AutoMod Configs.json", "r") as f:
        config = json.load(f)
        
    if config["enable"]:
        enable.extend(config["enable"])
    if config["disable"]:
        disable.extend(config["disable"])
    if config["ignore"]:
        ignore.extend(config["ignore"])
    if config["reenable"]:
        reenable.extend(config["reenable"])
    if config["scale"]:
        scale.extend(config["scale"])
    if config["enable_is"]:
        enable_is.extend(config["enable_is"])
    if config["ends_in"]:
        ends_in.extend(config["ends_in"])
    if config["disable_is"]:
        disable_is.extend(config["disable_is"])

    if noWalls:
        ignore.append('wall')
        ignore.append('roof')
    if noGrav:
        enable.append('grav')
        scale.append('grav')
        reenable.append('grav')
    if pvp:
        enable.append('pvp')
        scale.append('pvp')

    env = UnityPy.load(path)

    for obj in env.objects:
        if obj.type.name == "GameObject":
            data = obj.read()
            tree = data.read_typetree()

            was = data.m_IsActive
            will = "enable" if was else "disable"
            color = "\u001B[32m" if was else "\u001B[31m"
            changed = False

            for key in enable:
                if key in data.name.lower():
                    tree["m_IsActive"] = True
                    changed = True
                    will = "enable"
                    
            for key in ends_in:
                if data.name.lower().endswith(key):
                    tree["m_IsActive"] = True
                    changed = True
                    will = "enable"

            for key in disable:
                if key in data.name.lower():
                    tree["m_IsActive"] = False
                    changed = True
                    will = "disable"

            for key in ignore:
                if key in data.name.lower():
                    tree["m_IsActive"] = was
                    changed = True
                    will = "enable" if was else "disable"

            for key in reenable:
                if key in data.name.lower():
                    tree["m_IsActive"] = True
                    changed = True
                    will = "enable"
                    
            for key in enable_is:
                if key == data.name.lower():
                    tree["m_IsActive"] = True
                    changed = True
                    will = "enable"
                    
            for key in disable_is:
                if key == data.name.lower():
                    tree["m_IsActive"] = False
                    changed = True
                    will = "disable"

            # for key in enable_parent:
            #     if key in data.name.lower():
            #         tree["m_IsActive"] = True
            #         changed = True
            #         will = "enable"
            #         print(f"\u001B[34mTraversing{color}|\u001B[0m GameObject {data.name}")
            #         traverse_parents(data)
            #         print(f"\u001B[34mTraversed {color}|\u001B[0m GameObject {data.name}")

            for key in scale:
                if key in data.name.lower():
                    print(f"\u001B[34mScaling   {color}|\u001B[0m GameObject {data.name}")
                    transform = data.m_Transform.get_obj()
                    transform_data = transform.read()
                    transform_tree = transform.read_typetree()
                    transform_tree["m_LocalScale"]["x"] *= 100
                    transform_tree["m_LocalScale"]["y"] *= 100
                    transform_tree["m_LocalScale"]["z"] *= 100
                    print(f'\u001B[34mScaled    {color}|\u001B[0m {data.name} to {transform_tree["m_LocalScale"]}')
                    transform.save_typetree(transform_tree)

                    # target_path = tree['m_Component'][0]['component']['m_PathID']
                    # for obj2 in env.objects:
                    #     data2 = obj2.read()
                    #     tree2 = data2.read_typetree()
                    #     if hasattr(data2, 'path_id'):
                    #         if data2.path_id == target_path:
                    #             print(f"\u001B[34mFound Path{color}|\u001B[0m {data2.type.name} {data2.name}")
                    #             tree2["m_LocalScale"] *= 100
                    #             print(f"\u001B[34mScaled to {color}|\u001B[0m {data2.__getattribute__('m_LocalScale')}")
                    #             obj2.save_typetree(tree2)
                    #             break

            if changed:
                if will == "enable" and was == False:
                    print(f"\u001B[32mEnabled   {color}|\u001B[0m GameObject {data.name}")
                elif will == "disable" and was == True:
                    print(f"\u001B[31mDisabled  {color}|\u001B[0m GameObject {data.name}")
                else:
                    print(f"\u001B[33mIgnoring  {color}|\u001B[0m GameObject {data.name}")
            
            obj.save_typetree(tree)

    with open(path, "wb") as f:
        f.write(env.file.save())

def traverse_parents(data):
    parent = data.m_Transform.get_obj().read().m_Father.get_obj()
    if parent is not None:
        parent_data = parent.read()
        print(f"\u001B[34mParent    |\u001B[0m GameObject {parent_data.name}")
        parent_tree = parent_data.read_typetree()
        print(parent_tree)
        parent_tree["m_IsActive"] = True
        print(parent_tree)
        parent_data.save_typetree(parent_tree)
        traverse_parents(parent_data)

def decompile(apk_path):
    print(f"\u001B[32mDecompiling\u001B[0m")
    apktool_path = os.path.join(os.path.dirname(__file__), 'resources', 'decompile', 'apktool.jar')
    sp = subprocess.Popen(["java", "-jar", apktool_path, "d", "-f", apk_path], stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

def recompile(apk_path):
    print(f"\u001B[32mRecompiling\u001B[0m")
    apktool_path = os.path.join(os.path.dirname(__file__), 'resources', 'recompile', 'apktool.jar')
    sp = subprocess.Popen(["java", "-jar", apktool_path, "b", "-f", "--use-aapt2", "-d", apk_path[:-4], "-o", f"tmp-{apk_path}"], stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

    print(f"\u001B[32mAligning\u001B[0m")
    zipalign_path = os.path.join(os.path.dirname(__file__), 'resources', 'recompile', 'zipalign.exe')
    sp = subprocess.Popen([zipalign_path, "-p", "4", f"tmp-{apk_path}", f"tmp2-{apk_path}"], stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

    print(f"\u001B[32mSigning\u001B[0m")
    apksigner_path = os.path.join(os.path.dirname(__file__), 'resources', 'recompile', 'apksigner.jar')
    sp = subprocess.Popen(["java", "-jar", apksigner_path, "sign", "--key", 'index.pk8', "--cert", 'index.pem', "--v4-signing-enabled", 'false', "--out", f"modded-{apk_path}", f"tmp2-{apk_path}"], stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

def main(apk_path, noWalls, noGrav, pvp):
    try:
        apk_folder_path = apk_path[:-4]
        decompile(apk_path)
        modUnity3d(f"{apk_folder_path}/assets/bin/Data/data.unity3d", noWalls, noGrav, pvp)
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"Error: {str(e)}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("apk_path", help="Path to APK file")
    parser.add_argument("--noWalls", action="store_true", help="Disable walls")
    parser.add_argument("--noGrav", action="store_true", help="Disable gravity")
    parser.add_argument("--pvp", action="store_true", help="Enable PvP")
    args = parser.parse_args()


    main(args.apk_path, args.noWalls, args.noGrav, args.pvp)