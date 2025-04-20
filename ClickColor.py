#gives u color of where the pointer is.
import pyautogui
from PIL import ImageGrab
import time


def get_pixel_color():
    try:
        x, y = pyautogui.position() 
        screen = ImageGrab.grab(bbox=(x, y, x+1, y+1))
        color = screen.getpixel((0, 0)) 
        return color
    except Exception as e:
        print(f"Error: {e}")
        return None

def click_if_color(target_color):
    try:
        x, y = pyautogui.position()
        color = get_pixel_color()
        if color == target_color:
            pyautogui.click()
            print(f"Clicked at ({x}, {y}) due to color match: {color}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_color = (75, 219, 106) #decide target color
    print("Move your mouse to the desired pixel")
    try:
        while True:
            color = get_pixel_color()
            if color:
                click_if_color(target_color)
            time.sleep(0.0001) 
    except KeyboardInterrupt:
        print("\nExiting...")