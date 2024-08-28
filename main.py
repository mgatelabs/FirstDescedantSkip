import json
import re
from datetime import datetime

# Make a exe
# pip install pyinstaller
# pyinstaller --onefile main.py

# config file config.json {"ini":"c:\\path\\to\\ini.file"}

# Function to update the date in the key's value
def update_conditional_banner_date(value, new_date):
    # Find all the date patterns and replace them with the new date
    updated_value = re.sub(r'"\d{8}"', f'"{new_date}"', value)
    return updated_value

def udate_skip_date():

    # Read the config.json file to get the path to the INI file
    with open('config.json', 'r') as json_file:
        config_data = json.load(json_file)

    # Extract the INI file path from the JSON data
    ini_file_path = config_data.get('ini')

    # Set the date to today's date in YYYYMMDD format
    today_date = datetime.now().strftime('%Y%m%d')

    # Read the INI file
    with open(ini_file_path, 'r') as file:
        content = file.read()

    # Find the key and update its value
    pattern = r'(ConditionalBannerDoNotShowToday=\(\(.*?\)\))'
    match = re.search(pattern, content)
    if match:
        current_value = match.group(1)
        updated_value = update_conditional_banner_date(current_value, today_date)

        # Replace the old value with the updated one
        updated_content = content.replace(current_value, updated_value)

        # Write the changes back to the file
        with open(ini_file_path, 'w') as file:
            file.write(updated_content)

        print(f"Updated ConditionalBannerDoNotShowToday to: {updated_value}")
    else:
        print("Key 'ConditionalBannerDoNotShowToday' not found in the INI file.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    udate_skip_date()