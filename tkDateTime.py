import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S %Z \n %a %d %b %Y")
    label.config(text=current_time)
    label.after(1000, update_time)

window = tk.Tk()
window.geometry("375x300")
window.title("Date Time")

label = tk.Label(window, font=("Arial", 30), text="00:00:00")
label.grid(column=0,row=0)
window.grid_columnconfigure((0), weight=1)
window.grid_rowconfigure((0), weight=1)

update_time()

window.mainloop()
