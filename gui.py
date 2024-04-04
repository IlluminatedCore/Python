#Widgets = GUI elements, buttons, images, icons, textboxes, etc
#windows = serves as a containers to hold these widgets

from tkinter import *

windows = Tk() # instantiate an instance for windows
windows.geometry("420x420")
windows.title("Butta Biryani")

#icon = PhotoImage(file="backiee-98927.jpg")
#windows.iconphoto(True,icon)

windows.config(background="black")


windows.mainloop() #place window on computer screen and listen to events