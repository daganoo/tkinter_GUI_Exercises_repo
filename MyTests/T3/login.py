from tkinter import *

root = Tk()

txt1 = Label(root, text='Premier champ :')
txt2 = Label(root, text='Second :')
txt3 = Label(root, text='Troisième :')
entr1 = Entry(root)
entr2 = Entry(root)
entr3 = Entry(root)

can1 = Canvas(root, width=160, height=160, bg='white')
photo = PhotoImage(file='xp.png')
item = can1.create_image(80, 80, image=photo)

txt1.grid(row=1, sticky=E)
txt2.grid(row=2, sticky=E)
txt3.grid(row=3, sticky=E)
entr1.grid(row=1, column=2)
entr2.grid(row=2, column=2)
entr3.grid(row=3, column=2)
can1.grid(row=1, column=3, rowspan=3, padx=10, pady=5)

root.mainloop()
