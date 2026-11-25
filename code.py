from tkinter import *
from tkinter import colorchooser
def choose_color():
   color_code = colorchooser.askcolor(title="Choose color")
   print(color_code)
root = Tk()

button = Button(root, text="Select color",

command=choose_color, fg="yellow", bg="blue")

button.place(x=100, y=60)

root.geometry("300x300")

root.configure(background="lightblue")

root.mainloop()
