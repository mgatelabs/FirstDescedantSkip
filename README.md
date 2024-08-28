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
2. pyinstaller --onefile main.py

### Create the config

Now enter the /dist folder and create a new file "config.json"

The content of the JSON file should resemble this:

{"ini": "C:\\Users\\%YOUR_USER_NAME%\\AppData\\Local\\M1\\Saved\\Config\\Windows\\ToyPreferences.ini"}

### Add it to Steam

From inside steam choose "Games" > "Add a non-steamm game to my library..."

Choose the main.exe that was created in the dist folder.

Right click on the main in your steam list and rename it to something you would remember like "The First Descendant Skip"
