
#gives u cord of a pointer of screen

import tkinter as tk
import pyautogui

saver_cord = []
def update_saver_cord():
    saved_text = "\n".join([f"({x}, {y})" for x, y in saver_cord])
    saved_label.config(text=saved_text)

def save_cord(event=None):
    x, y = pyautogui.position()
    saver_cord.append((x, y))
    update_saver_cord()
def up_cord():
    x, y = pyautogui.position()
    position_label.config(text=f"Mouse Position: ({x}, {y})")
    root.after(100, up_cord)    



root = tk.Tk()
root.title("Mouse Coord Tracker")

root.geometry("500x300")

position_label = tk.Label(root, text="Mouse Coord: (0, 0)", font=("Arial", 14))
position_label.pack(pady=15)

save_button = tk.Button(root, text="Save Coords", command=save_cord)
save_button.pack(pady=2)

saved_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
saved_label.pack(pady=10)

root.bind("<s>", save_cord)

up_cord()
root.mainloop()
