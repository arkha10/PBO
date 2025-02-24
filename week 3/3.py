class shape:
    width=0
    def __init__(self,width):
        self.width=width

class square(shape):
    name="square"
    def get_area(self):
        return self.width**2
    
class triangle(shape):
    name="triangle"
    height=0
    def __init__(self, width,height):
        self.width=width
        self.height=height
    
    def get_area(self):
        return 0.5*self.width*self.height
squarex=square(5)
print("Luas persegi: ",squarex.get_area())
triangley=triangle(5,3)
print("Luas segitiga: ",triangley.get_area())