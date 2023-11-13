from tkinter import *

def nbpremiers(event):
    num1 = int(entry1.get())
    premiers = [x for x in range(2, num1) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
    premiers_str = ' '.join(map(str, premiers))
    entry2.delete(0, END)
    entry2.insert(0, premiers_str)

root = Tk()
label1 = Label(root, text="Entrez un nombre : ")
label1.grid(row=0,column=0)
entry1 = Entry(root)
entry1.grid(row=0,column=1)

label2 = Label(root, text="Nombres premier: ")
label2.grid(row=1,column=0)
entry2 = Entry(root)
entry2.grid(row=1,column=1)

entry1.bind("<KeyRelease>", nbpremiers)

root.mainloop()