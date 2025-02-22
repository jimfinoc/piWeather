# import tkinter as tk
# from PIL import Image, ImageTk

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Static GIF Example")

#     canvas_width = 518
#     canvas_height = 400
#     root.geometry(f"{canvas_width}x{canvas_height}")

#     canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
#     width = root.winfo_width()
#     height = root.winfo_height()

#     # canvas.place(x=width/2, y=height/2, anchor="center")
#     canvas.pack()

#     # gif_file_path = "downloaded_image.gif"  # Replace with the actual path to your GIF file
#     gif_file_path = "downloaded_image.gif"  # Replace with the actual path to your GIF file
#     try:
#         img = Image.open(gif_file_path)
#         photo_img = ImageTk.PhotoImage(img)
#         canvas.create_image(width, height,  image=photo_img)
#         # canvas.create_image(width, height, anchor=tk.CENTER,  image=photo_img)
#         # canvas.create_image(0, 0, anchor=tk.CENTER, image=photo_img)
#         canvas.image = photo_img  # Keep a reference to prevent garbage collection
#     except FileNotFoundError:
#         print(f"Error: GIF file not found at {gif_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

#     root.mainloop()


import requests
from io import BytesIO
import urllib.request
import tkinter as tk
from PIL import Image, ImageTk

def load_and_center_gif(canvas, gif_path):
    """Loads a GIF image onto the canvas and centers it."""
    try:
        response = requests.get(gif_path, stream=True)
        img = Image.open(BytesIO(response.content))
        # img = Image.open(gif_path)
        # Use the first frame if it's an animated GIF
        if hasattr(img, "n_frames") and img.n_frames > 1:
            img.seek(0)
        
        photo_img = ImageTk.PhotoImage(img)
        canvas.image = photo_img  # Keep a reference to prevent garbage collection

        img_width = photo_img.width()
        img_height = photo_img.height()
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        x = (canvas_width - img_width) // 2
        y = (canvas_height - img_height) // 2

        canvas.create_image(x, y, anchor=tk.NW, image=photo_img)

    except FileNotFoundError:
        print(f"Error: Image file not found at {gif_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def on_resize(event, canvas, gif_path):
    """Handles canvas resize events and re-centers the image."""
    canvas.delete("all")  # Clear the canvas
    load_and_center_gif(canvas, gif_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Centered GIF Example")

    canvas_width = 600
    canvas_height = 400
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(fill=tk.BOTH, expand=tk.YES)

    gif_path = "https://graphical.weather.gov/GraphicalNDFD.php?width=515&timezone=PST&sector=CONUS&element=t&n=5"
    # gif_path = "downloaded_image.gif"  # Replace with the actual path to your GIF file
    load_and_center_gif(canvas, gif_path)

   # Bind the resize event to the window
    root.bind("<Configure>", lambda event: on_resize(event, canvas, gif_path))
    root.mainloop()
