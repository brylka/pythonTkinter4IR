import tkinter as tk

class SimplePaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prosty Paint")

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.old_x = None
        self.old_y = None

        self.canvas.bind('<B1-Motion>', self.paint)
        #self.canvas.bind('<ButtonRelease-1>', self.reset)

    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, x, y, width=2, fill='red')
        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None


root = tk.Tk()
app = SimplePaintApp(root)
root.mainloop()
