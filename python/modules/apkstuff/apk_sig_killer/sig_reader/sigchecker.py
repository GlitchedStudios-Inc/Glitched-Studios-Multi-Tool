import os
import subprocess

def find_java_home():
    java_home = os.environ.get('JAVA_HOME')
    if java_home:
        return java_home

    # Try to find Java home from the registry (Windows)
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\JavaSoft\Java Runtime Environment')
        value, _ = winreg.QueryValueEx(key, 'CurrentVersion')
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, f'SOFTWARE\\JavaSoft\\Java Runtime Environment\\{value}')
        java_home, _ = winreg.QueryValueEx(key, 'JavaHome')
        return java_home
    except (ImportError, OSError):
        pass

    # Try to find Java home from the PATH environment variable
    for path in os.environ['PATH'].split(os.pathsep):
        java_exe = os.path.join(path, 'java.exe')
        if os.path.exists(java_exe):
            java_home = os.path.dirname(os.path.dirname(java_exe))
            return java_home

    return None

def find_java_executable(java_home=None):
    if java_home:
        java_exe = os.path.join(java_home, 'bin', 'java.exe')
        if os.path.exists(java_exe):
            return java_exe
    else:
        java_exe = 'java.exe'
        if subprocess.call([java_exe, '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
            return java_exe
    return None

def execute_gradle(apk_path, java_home=None, gradle_opts=None, java_opts=None):
    gradle_wrapper_jar = os.path.join(os.path.dirname(__file__), 'gradle', 'wrapper', 'gradle-wrapper.jar')
    classpath = gradle_wrapper_jar

    java_exe = find_java_executable(java_home)
    if not java_exe:
        print("ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.")
        print("Please set the JAVA_HOME variable in your environment to match the location of your Java installation.")
        return

    command = [
        java_exe,
        '-Xmx64m', '-Xms64m',  # default JVM options
    ]

    if java_opts:
        command.extend(java_opts)

    if gradle_opts:
        command.extend(gradle_opts)

    command.extend([
        '-Dorg.gradle.appname=gradle',
        '-classpath', classpath,
        'org.gradle.wrapper.GradleWrapperMain',
        '--apk', apk_path
    ])

    subprocess.call(command)

def main():
    apk_path = input("Enter the path to the APK file: ")
    java_home = find_java_home()
    if not java_home:
        java_home = input("Enter the path to the Java home directory: ")
    gradle_opts = input("Enter any additional Gradle options (optional): ")
    java_opts = input("Enter any additional Java options (optional): ")

    if gradle_opts:
        gradle_opts = gradle_opts.strip().split()
    else:
        gradle_opts = None

    if java_opts:
        java_opts = java_opts.strip().split()
    else:
        java_opts = None

    execute_gradle(apk_path, java_home, gradle_opts, java_opts)

if __name__ == '__main__':
    main()