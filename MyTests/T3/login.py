from tkinter import *

# Create the main window
root = Tk()
root.title("tk")

sl = Label(root, text="Second:")
sl.pack(side=LEFT)  
e1 = Entry(root, width=35)
e1.pack(side=LEFT)  

pl = Label(root, text="Premier Champ:")
pl.pack(side=TOP)  
e = Entry(root, width=35)
e.pack(side=TOP)  
root.mainloop()
