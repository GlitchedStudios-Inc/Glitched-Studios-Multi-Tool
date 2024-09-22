import UnityPy, os, subprocess, argparse, shutil, json

def extract_strings(path):
    env = UnityPy.load(path)
    strings = []
    playfab_strings = []
    photon_strings = []
    other_strings = []

    for obj in env.objects:
        if obj.type.name == "GameObject":
            data = obj.read()
            tree = data.read_typetree()

            for key, value in tree.items():
                if isinstance(value, str):
                    strings.append(value)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, str):
                            strings.append(item)
                elif isinstance(value, dict):
                    for k, v in value.items():
                        if isinstance(v, str):
                            strings.append(v)

        elif obj.type.name == "MonoScript":
            data = obj.read()
            tree = data.read_typetree()

            for key, value in tree.items():
                if key.endswith("script"):
                    script_contents = value.read().decode("utf-8")

                    start_idx = 0
                    while True:
                        start_idx = script_contents.find('"', start_idx)
                        if start_idx == -1:
                            break
                        end_idx = script_contents.find('"', start_idx + 1)
                        if end_idx == -1:
                            break
                        string = script_contents[start_idx + 1:end_idx]
                        strings.append(string)
                        start_idx = end_idx + 1

    for string in strings:
        if "playfab" in string.lower():
            playfab_strings.append(string)
        elif "photon" in string.lower():
            photon_strings.append(string)
        else:
            other_strings.append(string)

    return playfab_strings, photon_strings, other_strings

def decompile(apk_path):
    print(f"\u001B[32mDecompiling\u001B[0m")
    script_dir = os.path.dirname(__file__)
    apktool_path = os.path.join(script_dir, 'resources', 'decompile', 'apktool.jar')
    apktool_path = os.path.abspath(apktool_path)
    sp = subprocess.Popen(["java", "-jar", apktool_path, "d", "-f", apk_path], stdin=subprocess.PIPE)
    sp.communicate(input=b'\n')

def main(apk_path):
    try:
        apk_folder_path = apk_path[:-4]
        decompile(apk_path)
        game_info_path = f"{apk_folder_path}/assets/bin/Data/data.unity3d"
        playfab_strings, photon_strings, other_strings = extract_strings(game_info_path)
        game_name = os.path.basename(apk_path)[:-4]

        output_dir = f"output/apkstuff/stringextrater/{game_name}"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(f"{output_dir}/playfab.txt", "w") as f:
            for string in playfab_strings:
                f.write(string + "\n")

        with open(f"{output_dir}/photon.txt", "w") as f:
            for string in photon_strings:
                f.write(string + "\n")

        with open(f"{output_dir}/other.txt", "w") as f:
            for string in other_strings:
                f.write(string + "\n")

        print("Strings extracted and logged to files")
    except Exception as e:
        with open("error_logs.txt", "a") as f:
            f.write(f"Error: {str(e)}\n")
    finally:
        shutil.rmtree(apk_folder_path, ignore_errors=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("apk_path", help="Path to APK file")
    args = parser.parse_args()
    main(args.apk_path)