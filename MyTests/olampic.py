from tkinter import*
window=Tk()
window.title=("circles")

def create_circle(color,x,y):
    canva.create_oval(x, y, x+100, y+100, outline=color, width=5)


def red_circle():
    create_circle("red",10 ,10 )

def yellow_circle():
    create_circle("yellow",100 ,100 )

def green_circle():
    create_circle("green",1 ,100 )

canva=Canvas(window, width=600, height=600)
canva.pack()
red = Button(window, text="Red", command = red_circle)
red.pack()
yellow = Button(window, text="yellow", command = yellow_circle)
yellow.pack()
green = Button(window, text="green", command = green_circle)
green.pack()
window.mainloop()
