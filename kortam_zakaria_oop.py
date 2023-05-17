# Zakaria Kortam - Professor Estrada - 3/30/2023
# Object Oriented Program
# 1. Create a Geometric Obejct class that has the colour, filled, and time fields.
# 2. Equip it with accessors and mutators.
# 3. Create a Circle and Rectangle class that extend the GeometricObjectClass
# 4. For Circle, add the radius field and the new accessors.
# 5. For Rectangle, add length and width and the new accessors
# 6. Have the user customize the cirlce and use the pre-formed rectangle.

from datetime import datetime

class GeometricObject:
    def __init__(self, colour, filled):
        self.__colour = colour
        self.__filled = filled
        self.__date = datetime.now()
    
    # Accessors
    def getColour(self):
        return self.__colour
    
    def isFilled(self):
        return self.__filled
    
    def getDate(self):
        return self.__date
    
    #Mutators
    def setColour(self, colour):
        self.__colour = colour

    def setFilled(self, filled):
        self.__filled = filled
    
    # String Formatter
    def __str__(self):
        return f"Date of Creation: {self.getDate()}\
            \nColour: {self.getColour()}\
            \nFilled: {self.isFilled()}"
    
class Circle(GeometricObject):
    def __init__(self, radius, colour, filled):
        super().__init__(colour, filled)
        self.__radius = radius
    
    #Accessors
    def getRadius(self):
        return self.__radius
    def getArea(self):
        return 3.14159 * (self.__radius ** 2)
    def getCircumference(self):
        return 2 * 3.14159 * self.__radius 

    #Mutators
    def setRadius(self, radius):
        self.__radius = radius

    #String Formatter
    def __str__(self):
        return f"=== Circle === \
            \nRadius: {self.getRadius()}\
            \n{super().__str__()}\
            \nArea: {self.getArea()}\
            \nCircumference: {self.getCircumference()}"
        
class Rectangle(GeometricObject):
    def __init__(self, width, height, colour, filled):
        super().__init__(colour, filled)
        self.__width = width
        self.__height = height
    
    #Accessors
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height
    def getArea(self):
        return self.__width * self.__height
    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    #Mutators
    def setWidth(self, width):
        self.__width = width
    def setHeight(self, height):
        self.__height = height
    
    def __str__(self):
        return f"=== Rectangle === \
            \nWidth: {self.getWidth()} \
            Height: {self.getHeight()}\
            \n{super().__str__()}\
            \nArea: {self.getArea()}\
            \nPerimeter: {self.getPerimeter()}"

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(">>>>>>> Zakaria Kortam - COMSC 78 >>>>>>>>")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

def main():
    circle_radius = float(input("Enter the radius of a circle: "))
    colour = str(input("Enter the colour of the circle/rectangle: "))
    filled = (str(input("Are they filled (Y/N) "))).upper()
    isFilled = False 
    if(filled == "Y"):
        isFilled = True
        
    circle = Circle(circle_radius, colour, isFilled)
    rectangle = Rectangle(5, 10, colour, isFilled)
    print(circle)
    print(rectangle)
main()