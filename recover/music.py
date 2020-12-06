import subprocess
import getpass
from pathlib import Path

name = getpass.getuser()
home = str(Path.home())

subprocess.Popen(f"adb pull /sdcard/Music {home}/DB-Backup-Music", shell=True)