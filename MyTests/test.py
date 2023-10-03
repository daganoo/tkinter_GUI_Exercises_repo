from tkinter import *
root=Tk()

def myC():
    mybb=Label(root ,text="Daganoooo")
    mybb.pack()

#crating a label widget
myB = Button(root,text="Marouane ", command=myC)

#shoving it into the window or screen ma3lina
myB.pack()
root.mainloop()