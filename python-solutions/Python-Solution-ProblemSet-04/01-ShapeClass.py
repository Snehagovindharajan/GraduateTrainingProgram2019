# 1. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length
# as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by
# default.


class Shape:
    def area(self):
        self.area1 = 0
        print(self.area1)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        self.area1 = self.length * self.length
        print(self.area1)


square_area = Square(5)

square_area.area()
