class Rectangle:

    def __init__(self) -> None:#Intialising the length and width of the rectangles
       
       length=int(input("Enter the length of Rectangle: "))
       width=int(input("Enter the width of Rectangle: "))
       self.length=length
       self.width=width

    def area(self):#Method to calculating the area
        print("The area of the rectange:",self.length*self.width)

newrectangle=Rectangle()

newrectangle.area()        
       