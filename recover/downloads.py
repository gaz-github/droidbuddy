import subprocess
import getpass

name = getpass.getuser()

subprocess.Popen(f"adb pull /sdcard/Download /home/{name}/Downloads/DB-Backup", shell=True)