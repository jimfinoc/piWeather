import tkinter as tk

def animate(item, x, y, delay):
    canvas.move(item, x, y)
    canvas.after(delay, animate, item, x, y, delay)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

rect = canvas.create_rectangle(10, 10, 50, 50, fill="red")
animate(rect, 1, 1, 10)

root.mainloop()