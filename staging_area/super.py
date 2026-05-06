class shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        # print(f"This is {self.color} color and {'filled' if self.is_filled else 'not filled'}")
        print(f"It is {'filled' if self.is_filled else 'not filled'} with {self.color if self.is_filled else 'any'} color")

    

class circle(shapes):
    def __init__(self, color, is_filled, radius):
        self.radius = radius
        super().__init__(color, is_filled)
        
    def describe(self):
        print(f"The area of the circle is {3.14 * self.radius ** 2 } Cm²")
        super().describe()        

        

class square(shapes):
    def __init__(self, color, is_filled, width):
        self.width = width
        super().__init__(color, is_filled)

    def describe(self):
        print(f"The area of the square is {self.width * self.width } Cm²")
        super().describe()

    

class triangle(shapes):
    def __init__(self, color, is_filled, base, height):
        self.base = base
        self.height = height
        super().__init__(color, is_filled)

    def describe(self):
        print(f"The area of the triangle is {0.5 * self.base * self.height} Cm²")
        super().describe()


circle = circle("black", True, 6)
square = square("blue", False, 8)
triangle = triangle("red", True, 4, 9)



# print(circle.color)
# print(circle.is_filled)
# print(circle.radius)
# print(square.color)
# print(square.is_filled)
# print(square.width)
print("_____________________________________")
square.describe()
print("_____________________________________")
triangle.describe()
print("_____________________________________")
circle.describe()
print("_____________________________________")







