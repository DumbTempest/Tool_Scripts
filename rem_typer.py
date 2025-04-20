#sees number and types it on a specified region in an area of the screen
import pytesseract
from PIL import Image
import pyautogui
import os
import time
import random


region = (900, 390, 1000, 100)  #  # (x, y, width, height)

def type_number_in_region(number, regio):
    x, y, width, height = regio
    rand_x = random.randint(x, x + width)
    rand_y = random.randint(y, y + height)
    
    pyautogui.click(rand_x, rand_y)
    time.sleep(0.2) 
    pyautogui.typewrite(str(number), interval=0.2)

def submit(coords):
    pyautogui.click(coords[0], coords[1])

def next_button(coords):
    pyautogui.click(coords[0], coords[1])

custom_config = "--psm 6 -c tessedit_char_whitelist=0123456789"

print("Monitoring region for numbers...")

retry_count = 0  # Track how many times it retries
delay = 1.5  # Initial delay

try:
    while True:
        screenshot_path = "temp.png"
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(screenshot_path)
        
        image = Image.open(screenshot_path)
        text = pytesseract.image_to_string(image, config=custom_config).strip()
        os.remove(screenshot_path)
        
        # Ensure valid number detection
        if text.isdigit():
            print(f"Detected number: {text} (after {retry_count} retries, delay: {delay:.1f}s)")
            time.sleep(delay)  # Increase sleep time gradually
            type_number_in_region(text, (1425, 450, 100, 100))
            time.sleep(0.5)  
            submit((1430, 544))
            time.sleep(0.5)
            next_button((1434, 602))
            retry_count = 0  # Reset retry count after success
            delay += 1  # Increase sleep time by 1 sec
            time.sleep(1)
        else:
            retry_count += 1
            print(f"No valid number detected. Retrying... ({retry_count})")
            time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
