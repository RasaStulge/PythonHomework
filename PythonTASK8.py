#TASK 8

# Create a Rectangle class whose attributes will be the height and width of

# the figure.Implement methods to measure the perimeter and areas of a rectangle.

# Then create a Square class remembering that every square is a rectangle,

# but not every rectangle is a square.


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def findarea(self):
        return self.height*self.width
    def findperimeter(self):
        return 2*(self.height+self.width)

print('To measure the the perimeter and areas of a rectangle...')
height=int(input('Enter height: '))
width=int(input('Enter width: '))

r1=Rectangle(height, width)
print('Area : ',r1.findarea())
print('Perimeter : ',r1.findperimeter())




