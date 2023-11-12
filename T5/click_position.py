from tkinter import *

def f(event):
    print("click :", event.keysym)

def on_click(event):
    x, y = event.x, event.y
    canvas.create_text(x, y, text=f"position: ({x}, {y})")

wind = Tk()
wind.bind("<Key>", f)
canvas = Canvas(wind, width=400, height=400)
canvas.pack()

canvas.bind("<Button>", on_click)

wind.mainloop()
