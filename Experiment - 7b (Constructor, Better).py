class Length :
    def __init__(self , length) : 
        self.length = length

class Breadth :
    def __init__(self , breadth) : 
        self.breadth = breadth

class Area(Length, Breadth):
    def __init__(self, shape, length, breadth = 0):
        Length.__init__(self, length);
        Breadth.__init__(self, breadth)
        self.shape = shape
        self.area = 0
        if shape == "triangle":
            self.area = self.length * self.breadth / 2
        elif shape == "rectangle":
            self.area = self.length * self.breadth
        elif shape == "square":
            self.area = self.length * self.length
    def showArea(self):
        print(f"Area of {self.shape}: {self.area}")

t = Area("triangle", 10, 20)
t.showArea()
r = Area("rectangle", 10, 20)
r.showArea()
s = Area("square", 10)
s.showArea()
