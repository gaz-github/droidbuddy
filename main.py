import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import subprocess
import time

window = tk.Tk()
window.title("AndroidBuddy")
window.resizable(False, False)
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='images/icon.png'))

info = tk.Frame(bg="white")
buttons = tk.Frame(bg="white")

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
    if not files:
        return
    for i in range(len(files)):
        subprocess.run(f"adb push {files[i].name} /sdcard/DB-Transfer/{files[i].name}", shell=True)
    messagebox.showinfo("Information","Transfer successful, find files in DB-Transfer folder on device")

# Information
titleimg = ImageTk.PhotoImage(Image.open("images/logo2.png"))
title = tk.Label(
    image = titleimg,
    height = 100,
    width=30
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
    fg="white",bg="#08a300",
    relief=tk.FLAT,
    command=installAPK
)
button2 = tk.Button(
    master=buttons,
    text="Recover files",
    width=20,height=2,
    fg="white",bg="#4287f5",
    relief=tk.FLAT,
    command=fileRecover
)
button3 = tk.Button(
    master=buttons,
    text="View screen",
    width=20,height=2,
    fg="white",bg="orange",
    relief=tk.FLAT,
    command=viewScreen
)
button4 = tk.Button(
    master=buttons,
    text="Upload files",
    width=20,height=2,
    fg="white",bg="#4287f5",
    relief=tk.FLAT,
    command=fileUpload
)
    
# Grids
button.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)

# Packs
title.pack(fill=tk.X)
warning.pack(fill=tk.X)

info.pack(fill=tk.X)
buttons.pack()

window.mainloop()
