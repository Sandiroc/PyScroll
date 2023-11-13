from time import sleep
import pyautogui as pg
import tkinter as tk
import threading
import keyboard

# Start scrolling
def start_scroll():
    global running
    running = True
    scroll_thread = threading.Thread(target=scrolling_thread)
    scroll_thread.daemon = True
    scroll_thread.start()

# Threading to avoid GUI update issues
def scrolling_thread():
    while running:
        pg.scroll(-1 * int(scroll_speed_field.get()))
        sleep(0.025)

# Function to toggle scrolling
def toggle_scroll():
    global running
    if running:
        stop_scroll()
    else:
        start_scroll()

# Stop scrolling
def stop_scroll():
    global running
    running = False
    

# Close the program
def quit_scroll():
    global running
    running = False
    window.quit()


# Initialize window
window = tk.Tk()
window.title("PyScroll")
window.iconbitmap('../scroll.ico')
window.geometry("350x200")

# Row of buttons
button_frame = tk.Frame(window)
button_frame.pack()

# Scroll speed field
scroll_speed_field = tk.Entry(window)
scroll_speed_field.pack(side="left", padx=10)

# Start button
start_butt = tk.Button(window, text="START", command=start_scroll)
start_butt.pack(side="left", padx=10)

# Toggle button
toggle_butt = tk.Button(window, text="TOGGLE", command=toggle_scroll)
toggle_butt.pack(side="left", padx=10)

# Quit button
quit_butt = tk.Button(window, text="KILL", command=window.quit)
quit_butt.pack(side="left", padx=10)

running = False

# Bind the space key to toggle scrolling
keyboard.on_press_key("shift", lambda e: toggle_scroll())

# Bind the escape key to quit script
keyboard.on_press_key("esc", lambda e: quit_scroll())

window.mainloop()
