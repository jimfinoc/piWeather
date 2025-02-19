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
delay = 100

minuteAngle = 0
secondAngle = 0
hourAngle = 0


cx0 = padx # x coordinate of the top-left corner of the bounding box
cy0 = pady  # y coordinate of the top-left corner of the bounding box
cx1 = x_geometry - padx  # x coordinate of the bottom-right corner of the bounding box
cy1 = y_geometry - pady # y coordinate of the bottom-right corner of the bounding box
lx0 = (x_geometry)/2  # Starting coordinates
ly0 = (y_geometry)/2  # Starting coordinates

mx1 = cx0
my1 = cy0
sx1 = cx0
sy1 = cy0
hx1 = cx0
hy1 = cy0

radius = 7.5
bigCircle = canvas.create_oval(cx0, cy0, cx1, cy1, outline="white", fill="black")
Start = canvas.create_oval(lx0-radius, ly0-radius, lx0+radius, ly0+radius, outline="white", fill="white")
hourLine = canvas.create_line(lx0, ly0, hx1, hy1, width=radius*2, fill="white")
minuteLine = canvas.create_line(lx0, ly0, mx1, my1, width=radius, fill="white")
secondLine = canvas.create_line(lx0, ly0, sx1, sy1, width=radius/3, fill="red")


def update_time(delay):

    now = datetime.datetime.now()
    hour = now.hour%12
    minute = now.minute
    second = now.second
    minuteAngle = math.pi/2 - 2*math.pi*((minute+second/60)/60)
    mx1 = lx0 + (my_geometry/2-pad*5) * math.cos(-minuteAngle)# Ending coordinates
    my1 = ly0 + (my_geometry/2-pad*5) * math.sin(-minuteAngle) # Ending coordinates
    secondAngle = math.pi/2 - 2*math.pi*(second/60)
    sx1 = lx0 + (my_geometry/2-pad*5) * math.cos(-secondAngle)# Ending coordinates
    sy1 = ly0 + (my_geometry/2-pad*5) * math.sin(-secondAngle) # Ending coordinates
    hourAngle = math.pi/2 - 2*math.pi*((hour + (( minute + second/60 ) / 60))/12)
    hx1 = lx0 + 3/4*(my_geometry/2-pad*2) * math.cos(-hourAngle)# Ending coordinates
    hy1 = ly0 + 3/4*(my_geometry/2-pad*2) * math.sin(-hourAngle) # Ending coordinates

    canvas.coords(hourLine,lx0, ly0, hx1, hy1)
    canvas.coords(minuteLine,lx0, ly0, mx1, my1)
    canvas.coords(secondLine,lx0, ly0, sx1, sy1)
    window.after(delay,update_time,delay)



# label = tk.Label(window, font=("Arial", 80), text="00:00:00")
# label.pack()

# update_time()
update_time(delay)
window.mainloop()
