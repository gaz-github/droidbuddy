import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import time

window = tk.Tk()
window.title("Droidbuddy")
window.resizable(False, False)

info = tk.Frame()
buttons = tk.Frame()

# Commands
def installAPK():
    apk = filedialog.askopenfile(mode="r", initialdir="/home")
    subprocess.Popen(f"adb install -r {apk.name}", shell=True)
def viewScreen():
    subprocess.Popen("scrcpy")
def fileRecover():
    exec(open('recovery.py').read())
def fileUpload():
    files = filedialog.askopenfiles(mode="r", initialdir="/home")
    for i in range(len(files)):
        subprocess.run(f"adb push {files[i].name} /sdcard/DB-Transfer/{files[i].name}", shell=True)
    messagebox.showinfo("Information","Transfer successful, find files in DB-Transfer folder on device")

# Information
title = tk.Label(
    master=info,
    text="Droidbuddy",
    fg="white",bg="#08a300",
    height=2
)
warning = tk.Label(
    master=info,
    text="This program will only work if\nyou have USB Debugging enabled!",
    fg="white",bg="red",
    height=2
)

# Main menu
button = tk.Button(
    master=buttons,
    text="Install .APK",
    width=20,height=2,
    relief=tk.RAISED,
    command=installAPK
)
button2 = tk.Button(
    master=buttons,
    text="Recover files",
    width=20,height=2,
    relief=tk.RAISED,
    command=fileRecover
)
button3 = tk.Button(
    master=buttons,
    text="View screen",
    width=20,height=2,
    relief=tk.RAISED,
    command=viewScreen
)
button4 = tk.Button(
    master=buttons,
    text="Upload files",
    width=20,height=2,
    relief=tk.RAISED,
    command=fileUpload
)

# Grids
button.grid(row=0, column=0, padx=5, pady=5)
button2.grid(row=0, column=1, padx=5, pady=5)
button3.grid(row=1, column=0, padx=5, pady=5)
button4.grid(row=1, column=1, padx=5, pady=5)

# Packs
title.pack(fill=tk.X)
warning.pack(fill=tk.X)

info.pack(fill=tk.X)
buttons.pack()

window.mainloop()