from tkinter import *
root = Tk()


def button_clicked():
    return


root.title("simple calculator")
e = Entry(root, width=35, borderwidth=3.5)

button_1 = Button(root, text=1, padx=40, pady=20, command= lambda : button_clicked(1))
button_2 = Button(root, text=2, padx=40, pady=20, command= lambda : button_clicked(2))
button_3 = Button(root, text=3, padx=40, pady=20, command= lambda : button_clicked(3))
button_4 = Button(root, text=4, padx=40, pady=20, command= lambda : button_clicked(4))
button_5 = Button(root, text=5, padx=40, pady=20, command= lambda : button_clicked(5))
button_6 = Button(root, text=6, padx=40, pady=20, command= lambda : button_clicked(6))
button_7 = Button(root, text=7, padx=40, pady=20, command= lambda : button_clicked(7))
button_8 = Button(root, text=8, padx=40, pady=20, command= lambda : button_clicked(8))
button_9 = Button(root, text=9, padx=40, pady=20, command= lambda : button_clicked(9))
button_0 = Button(root, text=0, padx=40, pady=20, command= lambda : button_clicked(0))
button_add = Button(root, text="+", padx=40, pady=20, command= lambda : button_clicked())
button_eq = Button(root, text="=", padx=91, pady=20, command= lambda : button_clicked())
button_clear = Button(root, text="c", padx=91, pady=20, command= lambda : button_clicked())



button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1,columnspan=2)
button_add.grid(row=5, column=0)
button_eq.grid(row=5, column=1,columnspan=3)


e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
root.mainloop()
