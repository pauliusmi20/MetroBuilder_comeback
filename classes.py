
#utilities
def invert_width(x):
    return window_width-x
def invert_height(y):
    return window_height-y

class Circle():
    """ Super class: coordinates are complex"""
    
    Circles = list()
    def __init__(self, diam, real, imag ):
        self.diam = diam
        self.complex = complex(real,imag) 
        self.Circles.append(self)

    def inscrireCercle(self,n):
        return 

class City(Circle):

    def __init__(self, diam, real, imag):
        super().__init__(diam, real, imag)







