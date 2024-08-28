import subprocess

# make a EXE
# pip install pyinstaller
# pyinstaller --onefile internal_display.py

def switch_to_internal_display():
    # Execute displayswitch.exe with the /internal argument
    subprocess.run(["displayswitch.exe", "/internal"])

if __name__ == "__main__":
    switch_to_internal_display()