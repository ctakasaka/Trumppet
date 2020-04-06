import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Trumpy")
window.geometry("400x300")
window.resizable(0, 0)

button = tkinter.Button(text=" Hello ")
button.place(x=200,y=150)
button.pack()

window.mainloop()