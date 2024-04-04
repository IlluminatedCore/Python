#function using parents class

class Rectangle:
    
    def __init__(self, width, length):
        self.width = width
        self.length = length

class Square(Rectangle):

    def __init__(self, width, length):
        super().__init__(width, length)
    
    def Area(self):
        return self.width * self.length


square = Square(6,7)

print(square.Area())