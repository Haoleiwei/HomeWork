from math import *
class rectangle(object):
    def __init__(self,border1,border2):
        self.border1=border1
        self.border2=border2
    def area(self):
        print(self.border1*self.border2)
    
class square(rectangle):
    def __init__(self,border):
        super().__init__(border,border)
    
class ellipse():
    def __init__(self,a,b):
       self.a=a
       self.b=b
    def area(self):
        print( self.a*self.b*pi)

class circle(ellipse):
    def __init__(self,r):
        self.a=r
        self.b=r
                
shapes=[ellipse(10,20),square(15),circle(5),rectangle(20,15),circle(5),square(15),ellipse(10,20)]
t=total_area=0
while(t<len(shapes)):
    total_area+=shapes[t].area()
    t+=1
print(total_area)


