import subprocess
import getpass

name = getpass.getuser()

subprocess.Popen(f"adb pull /sdcard/Music /home/{name}/Music/DB-Backup", shell=True)