from tkinter import *
from screeninfo import get_monitors
from PIL import ImageTk, Image
root = Tk()

photo = ImageTk.PhotoImage(Image.open("a.jpg"))
#photo = PhotoImage(file = "a.jpg")
label = Label(root, image=photo)
label.pack(side = "bottom", fill = "both", expand = "yes")
root.geometry("1536x864+0+0")
root.mainloop()