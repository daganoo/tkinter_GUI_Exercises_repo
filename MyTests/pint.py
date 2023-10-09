import tkinter as tk

root = tk.Tk()
root.title("Bigger Point in tkinter")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw a bigger red point at coordinates (200, 200)
# Increase the size by specifying a larger bounding box
canvas.create_oval(195, 195, 50, 250, fill="red")

root.mainloop()
