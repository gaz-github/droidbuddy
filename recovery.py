import tkinter as tk
import subprocess
import getpass

window = tk.Tk()
window.title("Recovery")
window.resizable(False, False)

name = getpass.getuser()

def recoverCam():
    exec(open('recover/camera.py').read())
def recoverDown():
    exec(open('recover/downloads.py').read())
def recoverMus():
    exec(open('recover/music.py').read())
def recoverAll():
    exec(open('recover/all.py').read())

cameraCheck = tk.Button (
    master=window,
    text="Camera",
    height=2,
    relief=tk.FLAT,
    width=10,
    command=recoverCam
)
downloadsCheck = tk.Button (
    master=window,
    text="Downloads",
    height=2,
    width=10,
    relief=tk.FLAT,
    command=recoverDown
)
musicCheck = tk.Button (
    master=window,
    text="Music",
    height=2,
    width=10,
    relief=tk.FLAT,
    command=recoverMus
)
all = tk.Button(
    master=window,
    text="All",
    height=2,
    width=10,
    command=recoverAll,
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