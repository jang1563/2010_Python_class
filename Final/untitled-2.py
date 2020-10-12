import math
class Point:
    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y
    def diff(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __str__(self):
        return "%d %d" %(self.x,self.y)

class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius
    def get_center_distance(self, other):
        diff = math.sqrt( (self.center.x-other.center.x)**2 + (self.center.y - other.center.y)**2)
        return diff
    def intersects(self, other):
        dist = self.get_center_distance(other)
        rad = self.radius + other.radius
        return dist <= rad
   
p1 = Point(2,2)
p2 = Point()
p3 = p1
print p2
print p3

"""
1 1
2 2
"""

see_you = Circle(10,10,10)
next_semester = Circle(15,15,10)
print see_you.intersects(next_semester)
print see_you.get_center_distance(next_semester)