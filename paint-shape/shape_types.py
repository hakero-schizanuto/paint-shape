class rectangle():
    def __init__(self, x: int, y: int, w: int, h: int, color: str):
        self.x0 = x
        self.y0 = y
        self.x1 = x+w
        self.y1 = y+h
        self.color = color

    def draw(self, canvas):
        return canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.color, outline=self.color)


class circle():
    def __init__(self, x: int, y: int, r: int, color: str):
        self.x0 = x-r
        self.y0 = y-r
        self.x1 = x+r
        self.y1 = y+r
        self.color = color

    def draw(self, canvas):
        return canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill=self.color, outline=self.color)


class triangle():
    def __init__(self, x: int, y: int, w: int, h: int, color: str):
        self.x0 = int(x+w/2)
        self.y0 = y
        self.x1 = x
        self.y1 = y+h
        self.x2 = x+w
        self.y2 = y+h
        self.color = color

    def draw(self, canvas):
        return canvas.create_polygon(self.x0, self.y0, self.x1, self.y1, self.x2, self.y2, fill=self.color, outline=self.color)
