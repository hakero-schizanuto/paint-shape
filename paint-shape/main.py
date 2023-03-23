from tkinter import *
from PIL import Image, ImageTk
from shape import shapes


class PaintShape(Tk):
    def __init__(self, width=400, height=300, bg='#fff', lg='#000'):
        super().__init__()
        self.title('Paint Shape')
        self['bg'] = bg
        Label(self, text='Используй эти цвета', font=('Monospace', 15), height=2, bg=bg, fg=lg).pack()
        colors = Frame(self, width=width, height=100)
        self.color = '#000'
        for c in ['#000', '#f00', '#ff0', '#0f0', '#0ff', '#00f', '#f0f', '#fff']:
            b = Button(
                colors, bg=c, command=lambda c=c: self.select(c), width=5)
            b.pack(side='left', fill='x')
        colors.pack()
        self.canvas = Canvas(self, bg=bg, width=width, height=height)
        self.shapes = [(shape.draw(self.canvas), shape.color)
                       for shape in shapes]
        self.canvas.pack()
        self.after(1500, lambda: [(self.canvas.itemconfig(shape, fill=bg, outline=lg), self.canvas.tag_bind(
            shape, '<Button-1>', lambda _, i=shape: self.check(i))) for shape, _ in self.shapes])

    def select(self, c):
        self.color = c

    def check(self, shape):
        if (shape, self.color) in self.shapes:
            self.canvas.itemconfig(shape, fill=self.color, outline=self.color)
            del self.shapes[self.shapes.index((shape, self.color))]
        if self.shapes == []:
            self.after(1000, self.win)

    def win(self):
        global img
        win = Frame(self, bg='#fff')
        img = ImageTk.PhotoImage(Image.open('paint-shape/img.jpg'))
        Label(win, image=img).pack(fill="both")
        Button(win, text='OK', font=('Monospace', 10), command=exit, width=6, fg='#f00', bg='#fff').pack(expand=1)
        win.place(x=50, y=50)


if __name__ == "__main__":
    PaintShape().mainloop()
