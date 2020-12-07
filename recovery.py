import tkinter as tk
import subprocess
import getpass
from pathlib import Path
from functools import partial

window = tk.Tk()
window.title("Recovery")
window.resizable(False, False)

home_dir = str(Path.home())

def recovery_fn(args):
    subprocess.Popen(f"adb pull /sdcard/{args[0]} {args[1]}", shell=True).wait()

cameraCheck = tk.Button (
    master=window,
    text="Camera",
    height=2,
    relief=tk.FLAT,
    width=10,
    command=partial(recovery_fn, ['DCIM', f'{home_dir}/DB-Backup-Pictures'])
)
downloadsCheck = tk.Button (
    master=window,
    text="Downloads",
    height=2,
    width=10,
    relief=tk.FLAT,
    command=partial(recovery_fn, ['Download', f'{home_dir}/DB-Backup-Downloads'])
)
musicCheck = tk.Button (
    master=window,
    text="Music",
    height=2,
    width=10,
    relief=tk.FLAT,
    command=partial(recovery_fn, ['Music', f'{home_dir}/DB-Backup-Music'])
)
all = tk.Button(
    master=window,
    text="All",
    height=2,
    width=10,
    command=partial(recovery_fn, ['', f'{home_dir}/DB-Backup-Device']),
    relief=tk.FLAT,
    fg="white",
    bg="red"
)
warning = tk.Label(
    master=window,
    text="WARNING!!!\nFILE SIZE WILL BE LARGE\nAND TRANSFER WILL BE LENGTHY.",
    width=30,
    relief=tk.FLAT,
    fg="white",
    bg="red"
)

cameraCheck.pack(side=tk.LEFT, fill=tk.Y)
downloadsCheck.pack(side=tk.LEFT, fill=tk.Y)
musicCheck.pack(side=tk.LEFT, fill=tk.Y)
all.pack(side=tk.LEFT, fill=tk.Y)
warning.pack(side=tk.LEFT, fill=tk.Y)

window.mainloop()