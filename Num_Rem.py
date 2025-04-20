#tells u what's on screen
#This script captures a specific region of the screen, processes the image to extract text using Tesseract OCR, and prints the detected numbers to the console.
import pytesseract
from PIL import Image
import pyautogui
import os
import time

#(x, y, width, height)
region = (900, 390, 1000, 100) 

custom_config = "--psm 6 -c tessedit_char_whitelist=0123456789"
print("Monitoring region for numbers")
try:
    while True:
        screenshot_path = "temp.png"
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(screenshot_path)
        
        image = Image.open(screenshot_path)
        text = pytesseract.image_to_string(image, config=custom_config).strip()
        os.remove(screenshot_path)

        if text:
            print("Detected number:", text)

        time.sleep(2)#timeGap between 2 monitors

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
