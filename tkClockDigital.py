import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

window = tk.Tk()
window.geometry("375x150")
window.title("Digital Clock")

label = tk.Label(window, font=("Arial", 70), text="00:00:00")
label.pack()

update_time()

window.mainloop()
