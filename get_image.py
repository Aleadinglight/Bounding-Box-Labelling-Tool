from tkinter import *
from screeninfo import get_monitors
from PIL import ImageTk, Image

root = Tk()

photo = ImageTk.PhotoImage(Image.open("a.jpg"))
#photo = PhotoImage(file = "a.jpg")
label = Label(root, image=photo)
label.pack(side = "bottom", fill = "both", expand = "yes")

# Set the app screen resolution
# We need the screen resolution so that we scale the input pictures
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
app_resolution = ""+str(screen_width)+"x"+str(screen_height)+"+0+0"

root.geometry(app_resolution)
root.mainloop()