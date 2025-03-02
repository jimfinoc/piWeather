import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S %Z \n %a %d %b %Y")
    label1.config(text=current_time)
    # future_time = future.strftime("%a %d %b %Y")

    future = time.strptime("1 Jun 25", "%d %b %y")
    difference = int((time.mktime(future)-time.time())/60/60/24)
    label2.config(text=f"{difference} Days Until\n Final Year.")

    future = time.strptime("1 Jun 26", "%d %b %y")
    difference = int((time.mktime(future)-time.time())/60/60/24)
    label3.config(text=f"{difference} Days Until \n Complete and\nK's Graduation.")

    future = time.strptime("1 Jun 27", "%d %b %y")
    difference = int((time.mktime(future)-time.time())/60/60/24)
    label4.config(text=f"{difference} Days Until\n Retirement and\nL's Graduation.")
    label1.after(1000, update_time)

window = tk.Tk()
window.geometry("375x720")
window.title("Days Until")

label1 = tk.Label(window, font=("Arial", 30), text="00:00:00")
label2 = tk.Label(window, font=("Arial", 30), text="00:00:00")
label3 = tk.Label(window, font=("Arial", 30), text="00:00:00")
label4 = tk.Label(window, font=("Arial", 30), text="00:00:00")
label1.grid(column=0,row=0)
label2.grid(column=0,row=1)
label3.grid(column=0,row=2)
label4.grid(column=0,row=3)
window.grid_columnconfigure((0), weight=1)
window.grid_rowconfigure((0,1,2,3), weight=1)

update_time()

window.mainloop()
