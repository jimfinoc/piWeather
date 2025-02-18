import tkinter as tk
import datetime
import math

window = tk.Tk()
my_geometry = 375
x_geometry = my_geometry
y_geometry = my_geometry
pad = 10
padx = pad
pady = pad
window.geometry(f"{x_geometry}x{y_geometry}")
window.title("Analog Clock")

canvas = tk.Canvas(window, width=x_geometry, height=y_geometry)
canvas.pack()
refresh = 500
def update_time():
    cx0 = padx # x coordinate of the top-left corner of the bounding box
    cy0 = pady  # y coordinate of the top-left corner of the bounding box
    cx1 = x_geometry - padx  # x coordinate of the bottom-right corner of the bounding box
    cy1 = y_geometry - pady # y coordinate of the bottom-right corner of the bounding box

    # lx0 = (cx1 - cx0)/2  # Starting coordinates
    lx0 = (x_geometry)/2  # Starting coordinates
    # ly0 = (cy1 - cy0)/2  # Starting coordinates
    ly0 = (y_geometry)/2  # Starting coordinates

    now = datetime.datetime.now()
    # print("now",now)
    hour = now.hour%12
    # print("hour",hour)
    minute = now.minute
    # print("minute", minute)
    second = now.second
    # print("second", second)
    minuteAngle = math.pi/2 - 2*math.pi*((minute+second/60)/60)
    mx1 = lx0 + (my_geometry/2-pad*5) * math.cos(-minuteAngle)# Ending coordinates
    my1 = ly0 + (my_geometry/2-pad*5) * math.sin(-minuteAngle) # Ending coordinates
    secondAngle = math.pi/2 - 2*math.pi*(second/60)
    sx1 = lx0 + (my_geometry/2-pad*5) * math.cos(-secondAngle)# Ending coordinates
    sy1 = ly0 + (my_geometry/2-pad*5) * math.sin(-secondAngle) # Ending coordinates
    hourAngle = math.pi/2 - 2*math.pi*((hour + (( minute + second/60 ) / 60))/12)
    # hourAngle = math.pi/2 - 2*math.pi*(hour /12)
    hx1 = lx0 + 3/4*(my_geometry/2-pad*2) * math.cos(-hourAngle)# Ending coordinates
    hy1 = ly0 + 3/4*(my_geometry/2-pad*2) * math.sin(-hourAngle) # Ending coordinates



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
