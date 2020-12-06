import subprocess
import getpass

name = getpass.getuser()

subprocess.Popen(f"adb pull /sdcard/DCIM /home/{name}/Pictures/DB-Backup", shell=True)