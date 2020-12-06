# droidbuddy
A GUI built in Tkinter, using ADB and scrcpy, for device recovery and maintenance.

# Dependencies
`scrcpy`, `tkinter`, `PIL` (debian - `sudo apt install python3-pil python3-pil.imagetk`) and `adb` are required for this program to function.

# Running on Linux
```
git clone https://github.com/gaz-github/droidbuddy
cd droidbuddy
python3 main.py
```
# Running on Windows
- Install the Chocolatey package manager for windows
```
choco install python pip git adb scrcpy
git clone https://github.com/gaz-github/droidbuddy
cd droidbuddy
pip install pillow
python main.py
```

# Features
- **APK Installation**: Install an Android application package with ease.
- **Screen viewing and interaction**: Control your device through an scrcpy window.
- **Recover files**: Allows you to back up music, downloads, photos or all of your device's files
- **Upload files**: Upload files from your computer to your device with ease
