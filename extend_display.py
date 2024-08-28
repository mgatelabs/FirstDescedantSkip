import subprocess

# make a EXE
# pip install pyinstaller
# pyinstaller --onefile extend_display.py

def switch_to_extend_display():
    # Execute displayswitch.exe with the /internal argument
    subprocess.run(["displayswitch.exe", "/extend"])

if __name__ == "__main__":
    switch_to_extend_display()