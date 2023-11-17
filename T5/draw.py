from tkinter import*
class Application:
    def __init__(self, wnd):
        self.wnd = wnd
        self.wnd.title("draw ")

        self.canvas = Canvas(wnd, width=420, height=300, bg="white")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.dessiner_ligne)

    def dessiner_ligne(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(x, y, x+1, y+1, fill="blue", width=2)

wnd = Tk()
app = Application(wnd)
wnd.mainloop()

