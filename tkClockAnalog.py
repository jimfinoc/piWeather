import tkinter as tk
import datetime
import math

# def update_time():
#     current_time = time.strftime("%H:%M:%S")
#     label.config(text=current_time)
#     label.after(1000, update_time)

window = tk.Tk()
window.geometry("480x480")
window.title("Analog Clock")

canvas = tk.Canvas(window, width=480, height=480)
canvas.pack()
refresh = 1
def update_time():
    cx0 = 5 # x coordinate of the top-left corner of the bounding box
    cy0 = 5  # y coordinate of the top-left corner of the bounding box
    cx1 = 475  # x coordinate of the bottom-right corner of the bounding box
    cy1 = 475  # y coordinate of the bottom-right corner of the bounding box

    lx0 = (cx1 - cx0)/2  # Starting coordinates
    ly0 = (cy1 - cy0)/2  # Starting coordinates

    now = datetime.datetime.now()
    # print("now",now)
    hour = now.hour%12
    # print("hour",hour)
    minute = now.minute
    # print("minute", minute)
    second = now.second
    # print("second", second)
    minuteAngle = math.pi/2 - 2*math.pi*((minute+second/60)/60)
    mx1 = lx0 + 200 * math.cos(-minuteAngle)# Ending coordinates
    my1 = ly0 + 200 * math.sin(-minuteAngle) # Ending coordinates
    secondAngle = math.pi/2 - 2*math.pi*(second/60)
    sx1 = lx0 + 200 * math.cos(-secondAngle)# Ending coordinates
    sy1 = ly0 + 200 * math.sin(-secondAngle) # Ending coordinates
    hourAngle = math.pi/2 - 2*math.pi*((hour + (( minute + second/60 ) / 60))/12)
    # hourAngle = math.pi/2 - 2*math.pi*(hour /12)
    hx1 = lx0 + 150 * math.cos(-hourAngle)# Ending coordinates
    hy1 = ly0 + 150 * math.sin(-hourAngle) # Ending coordinates



    bigCircle = canvas.create_oval(cx0, cy0, cx1, cy1, outline="white", fill="black")
    radius = 7.5
    Start = canvas.create_oval(lx0-radius, ly0-radius, lx0+radius, ly0+radius, outline="white", fill="white")
    hourLine = canvas.create_line(lx0, ly0, hx1, hy1, width=radius*2, fill="white")
    minuteLine = canvas.create_line(lx0, ly0, mx1, my1, width=radius, fill="white")
    secondLine = canvas.create_line(lx0, ly0, sx1, sy1, width=radius/3, fill="red")
    # minuteEnd = canvas.create_oval(mx1-radius/3, my1-radius/3, mx1+radius/3, my1+radius/3, outline="white", fill="white")
    # hourEnd = canvas.create_oval(hx1-radius, hy1-radius, hx1+radius, hy1+radius, outline="white", fill="white")
    # hourLine.after(15,update_time)
    window.after(refresh,update_time)



# label = tk.Label(window, font=("Arial", 80), text="00:00:00")
# label.pack()

# update_time()
window.after(refresh,update_time)
window.mainloop()
