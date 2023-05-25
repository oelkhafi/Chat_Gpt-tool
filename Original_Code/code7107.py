from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy    
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y   
    
    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)




 