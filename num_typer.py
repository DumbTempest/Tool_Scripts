#types on a specified region of the screen
import pyautogui
import time
import random

def type_number_in_region(number, region):
    x, y, width, height = region
    rand_x = random.randint(x, x + width)
    rand_y = random.randint(y, y + height)
    
    pyautogui.click(rand_x, rand_y)
    time.sleep(0.2) 
    pyautogui.typewrite(str(number), interval=0.1)
    
    
def submit(regional):
    pyautogui.click(regional[0], regional[1])

def next(regiona):
    pyautogui.click(regiona[0], regiona[1])
    
    
if __name__ == "__main__":
    type_number_in_region(3, (1425, 450, 100, 100))
    
    time.sleep(0.5)  
    submit((949, 544))
    time.sleep(0.5)
    next((949, 544))



