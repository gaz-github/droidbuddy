import subprocess
import getpass

name = getpass.getuser()

subprocess.Popen(f"adb pull /sdcard/ /home/{name}/Documents/DB-Backup", shell=True)