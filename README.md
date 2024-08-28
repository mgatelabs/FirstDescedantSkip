# First Descendant Notice Skipper

## Purpose

This will update a config file, so the app won't show the notice popup when you open the app.

## Why

When you try to stream TFD via steam link, the popup windows don't react very well.

## Workaround?

There is one, switch to touch controls only, disable keyboard / mouse, open TFD, use touch controls to skip the dialogs.  Then exit the game and re-start with K&M.

## Usage

You need to do three things

### Compile the app

From the main directory do the following

1. pip install pyinstaller
2. pyinstaller --onefile update_date.py

### Create the config

Now enter the /dist folder and create a new file "config.json"

The content of the JSON file should resemble this:

{"ini": "C:\\Users\\%YOUR_USER_NAME%\\AppData\\Local\\M1\\Saved\\Config\\Windows\\ToyPreferences.ini"}

### Add it to Steam

From inside steam choose "Games" > "Add a non-steamm game to my library..."

Choose the update_date.exe that was created in the dist folder.

Right click on the main in your steam list and rename it to something you would remember like "The First Descendant Skip"

## Other Utilities

Because TFD is sort of buggy over Steam Link I have added two extra programs that will
allow you to change your window configuration, since TFD likes to popup in a window that isn't visible.

### To build them

pyinstaller --onefile extend_display.py

pyinstaller --onefile internal_display.py

### Add them to steam

Then add both exes to steam as show earlier.

extend_display.exe will enable multi-monitor.
internal_display.exe will force one screen.