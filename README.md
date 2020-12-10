# droidbuddy
A GUI built in Tkinter, using ADB and scrcpy, for device recovery and maintenance.

# Dependencies
`scrcpy`, `tkinter`, `pillow` and `adb` are required for this program to function.

# Running on Linux (Debian/Ubuntu)
```
git clone https://github.com/gaz-github/droidbuddy
cd droidbuddy
sudo apt install pip
pip install pillow
python3 main.py
```
# Running on Windows
- Install the Chocolatey package manager for windows
```
choco install python pip git adb scrcpy
git clone https://github.com/gaz-github/droidbuddy
cd droidbuddy
sudo pip3 install pillow
python main.py
```

# Features
- **APK Installation**: Install an Android application package with ease.
- **Screen viewing and interaction**: Control your device through an scrcpy window. ***For Xiaomi devices, you will need to enable "USB Debugging (Security settings) for touch input to function.***
- **Recover files**: Allows you to back up music, downloads, photos or all of your device's files
- **Upload files**: Upload files from your computer to your device easily.
- **Advanced device control**: This allows you to mimick home and back actions, change brightness and more to come.