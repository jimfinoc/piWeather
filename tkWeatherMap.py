# import tkinter as tk
# import datetime
# import math
# from PIL import Image, ImageTk
# import requests
# from io import BytesIO

# import urllib.request



# window = tk.Tk()
# my_geometry = 375
# x_geometry = 550
# y_geometry = 400
# pad = 10
# padx = pad
# pady = pad
# window.geometry(f"{x_geometry}x{y_geometry}")
# window.title("Weather Map")

# canvas = tk.Canvas(window, width=x_geometry, height=y_geometry)
# # canvas.grid(row=0,column=0,sticky="nsew")
# delay = 100

# def center_canvas(canvas, window):
#     window.update_idletasks()
#     width = window.winfo_width()
#     height = window.winfo_height()
#     canvas.place(x=width/2, y=height/2, anchor="center")

# weather_map = None


# def save_image_from_url(url, filename):
#   try:
#     response = requests.get(url, stream=True)
#     response.raise_for_status()

#     image = Image.open(BytesIO(response.content))
#     image.save(filename)
#     print(f"Image saved successfully to {filename}")
#   except requests.exceptions.RequestException as e:
#       print(f"Error downloading image: {e}")
#   except Exception as e:
#       print(f"Error processing image: {e}")

# # Example usage
# # image_url = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
# image_url = "https://graphical.weather.gov/GraphicalNDFD.php?width=515&timezone=PST&sector=CONUS&element=t&n=5"
# file_name = "downloaded_image.gif"
# save_image_from_url(image_url, file_name)

# def update_weatherMap(delay):
#     global weather_map
#     try:
#         url = "https://graphical.weather.gov/GraphicalNDFD.php?width=515&timezone=PST&sector=CONUS&element=t&n=5"
#         response = requests.get(url, stream=True)
#         response.raise_for_status()
#         # my_image = Image.open(BytesIO(response.content))
#         my_image = Image.open(file_name)


#         print('load successful')
#     except:
#         print('load NOT successful')
#         pass

#     try:
#         # image = tk.PhotoImage(file="image.png")
#         # url = "https://graphical.weather.gov/GraphicalNDFD.php?width=515&timezone=PST&sector=CONUS&element=t&n=5"
#         # my_image = Image.open(requests.get(url, stream=True).raw)
#         # print()
#         # print("url")
#         # print(url)
#         # print("my_image")
#         # print(my_image)
#         # my_image = Image.open("https://graphical.weather.gov/GraphicalNDFD.php?width=515&timezone=PST&sector=CONUS&element=t&n=5")
#         # gif_image = tk.PhotoImage(my_image)
#         my_img = Image.open(file_name)

#         photo_image = ImageTk.PhotoImage(my_img)
#         # print("my_photo")
#         # print(my_photo)

#         # if weather_map == None:
#         weather_map = canvas.create_image(0, 0, anchor=tk.CENTER,image=photo_image)
#         # weather_map = canvas.create_image(0, 0, anchor=tk.CENTER,image=photo_image)
#         print("weather_map-")
#         print(weather_map)
#             # weather_map = canvas.create_image(image_x, image_y, anchor=tk.CENTER, image=image)
#         # else:
#             # new_image = Image.open("https://graphical.weather.gov/GraphicalNDFD.php?width=515&timezone=PST&sector=CONUS&element=t&n=5")
#             # photo = ImageTk.PhotoImage(image)
#             # canvas.itemconfig(weather_map, image=my_photo)
#             # print("weather_map=")
#             # print(weather_map)
#     except FileNotFoundError:
#         print("Error: Image file not found. Please make sure 'image.png' is in the correct directory.")
#         # root.destroy()  # Close the window if the image is not found
#         # exit()
#     # window.after(delay,update_weatherMap,delay)


# # label = tk.Label(window, font=("Arial", 80), text="00:00:00")
# # label.pack()

# # window.grid_columnconfigure((0,1), weight=1)
# # window.grid_rowconfigure((0), weight=1)

# center_canvas(canvas, window)
# window.bind("<Configure>", lambda event: center_canvas(canvas, window))


# update_weatherMap(delay)
# # update_time(delay)
# window.mainloop()


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
