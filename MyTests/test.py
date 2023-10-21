from tkinter import *
root=Tk()
canva=Canvas(root, width=500, height=500)
canva.pack()
canva.create_line((250,0,250,500))
canva.create_line((0,250,500,250))

canva.create_oval((200,200,300,300))
canva.create_oval((100,100,400,400))
canva.create_oval((150,150,180,180))
root.mainloop()