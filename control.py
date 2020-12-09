import tkinter as tk
import subprocess
from functools import partial

window = tk.Toplevel()
window.title("Control panel")
window.resizable(False, False)

global inputs
inputs = [["Back","4"],["Home","3"],["Copy","278"],["Paste","279"],["Cut","277"],["Brightness up","221"],["Brightness down","220"],["Toggle on/off","26"]]

def runBtn(btn):
    subprocess.Popen(f"adb shell input keyevent {inputs[btn][1]}",shell=True)

for x in range(len(inputs)):
    print(x)
    tk.Button(
        master=window,
        padx=5,pady=2,
        text=inputs[x][0],
        relief=tk.FLAT,
        command=partial(runBtn, x)
    ).pack(side=tk.LEFT)

window.mainloop()