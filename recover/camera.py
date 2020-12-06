import subprocess
import getpass
from pathlib import Path

name = getpass.getuser()
home = str(Path.home())

subprocess.Popen(f"adb pull /sdcard/DCIM {home}/DB-Backup-Pictures", shell=True)