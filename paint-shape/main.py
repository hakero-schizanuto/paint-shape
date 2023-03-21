from tkinter import *
from shape import shapes


class PaintShape(Frame):
    def __init__(self, master: None, width=400, height=300, bg='#fff', lg='#000'):
        super().__init__(master, bg=bg, width=width, height=height+100)
        self.canvas = Canvas(self, bg=bg, width=width, height=height)
        self.shapes = [shape.draw(self.canvas) for shape in shapes]
        self.canvas.pack()
        self.after(3000, lambda: [(self.canvas.itemconfig(shape, fill=bg, outline=lg), self.canvas.tag_bind(shape, '<Button1>')) for shape in self.shapes])


if __name__ == "__main__":
    win = Tk()
    win.title('Paint Shape')
    PaintShape(win).pack()
    win.mainloop()
