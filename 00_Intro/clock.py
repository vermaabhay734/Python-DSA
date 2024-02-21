import time
from tkinter import *

def timer():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,timer)

root=Tk()
root.geometry('500x350')
root.title("Python Digital Clock")
root.config(bg='ivory')

clock = Label(root, font = ("times",50,"bold"), bg="white")
clock.grid(row=2, column=2, pady=25,padx=100)
timer()

digi = Label(root, text="Digital clock", font="times 24 bold")
digi.grid(row=0, column=2)

notation = Label(root, text="  Hours        Minutes      Seconds    ",font="times 15 bold")
notation.grid(row=3, column=2)

Blank = Label(root, text="              ", font="times 14 bold",bg='ivory')
Blank.grid(row=4, column=2)

madeBy = Label(root, text="Made by: Abhay Verma.", font="times 14 bold")
madeBy.grid(row=5, column=2)

root.mainloop()