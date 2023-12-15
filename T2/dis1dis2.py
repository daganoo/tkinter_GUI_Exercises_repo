import tkinter as tk


def cercle(x, y, r, coul='black'):
    can.create_oval(x-r, y-r, x+r, y+r, outline=coul)


def figure_1():
    can.delete(all)
    can.create_line(100, 0, 100, 200, fill='blue')
    can.create_line(0, 100, 200, 100, fill='blue')
    rayon = 2
    while rayon < 100:
        cercle(100, 100, rayon)
        rayon += 10


def figure_2():
    can.delete(all)
    diss2 = [[100, 100, 80, 'red'],
            [70, 70, 15, 'blue'],
            [130, 70, 15, 'blue'],
            [70, 70, 5, 'black'],
            [130, 70, 5, 'black'],
            [44, 115, 20, 'red'],
            [156, 115, 20, 'red'],
            [100, 95, 15, 'purple'],
            [100, 145, 30, 'purple']]
    for i in range(0, len(diss2)):
        x = diss2[i]
        cercle(x[0], x[1], x[2], x[3])


fen = tk.Tk()
can = tk.Canvas(fen, width=200, height=200, bg='ivory')
can.pack(side='top', padx=5, pady=5)
b1 = tk.Button(fen, text='dessin 1', command=figure_1)
b1.pack(side='left', padx=3, pady=3)
b2 = tk.Button(fen, text='dessin 2', command=figure_2)
b2.pack(side='right', padx=3, pady=3)
fen.mainloop()
