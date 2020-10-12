from cs1graphics import *
from time import sleep

canvas = None
silver = None

class _World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        
    def add(self, name, obj):
        self.objects[name] = obj

    def draw_scene(self):
        """ 
        backgourd drawing
        Don't forget _scene.add(name)
        """
        grass = Rectangle(600, 100)
        grass.setFillColor("brown")
        grass.moveTo(250,300)
        grass.setDepth(1)
        
        rock1 = Circle(30)
        rock1.setFillColor("black")
        rock1.moveTo(30,225)
        rock1.setDepth(5)
        
        rock2 = Square(70)
        rock2.setFillColor("black")
        rock2.moveTo(450,225)
        rock2.setDepth(10)
        
        silver.add(grass)
        silver.add(rock1)
        silver.add(rock2)


def create_world():
    global silver, canvas
    if silver:
        raise RuntimeError("A world already exists!")
    canvas = _World(500, 300)
    silver = Canvas(canvas.width, canvas.height)
    silver.setTitle("Snake!!")
    canvas.draw_scene()

COLOR = ["green", "yellow", "red"]
TYPE = ["dragon", "normal"]
    
class Snake(object):
    def __init__(self, color, type1):
        assert color in COLOR and type1 in TYPE
        layer = Layer()
        
        self.color = color
        self.type1 = type1
        
        head = Circle(10)
        head.setFillColor(self.color)
        
        eye = Circle(3)
        eye.setFillColor("blue")
        eye.setDepth(1)
        eye.moveTo(-3,-3)
        
        
        body1 = Rectangle(20, 15)
        body1.setFillColor(self.color)
        body1.moveTo(20,0)
        body1.setBorderColor("transparent")
        
        body2 = Rectangle(20, 15)
        body2.setFillColor(self.color)
        body2.moveTo(40,0)
        body2.setBorderColor("transparent")
        
        body3 = Rectangle(20, 15)
        body3.setFillColor(self.color)
        body3.moveTo(60,0)
        body3.setBorderColor("transparent")
        
        layer.moveTo(150,230)
        
        self.layer = layer
        self.head = head
        self.eye = eye
        self.body1 = body1
        self.body2 = body2
        self.body3 = body3
        
        layer.add(head)
        layer.add(body1)
        layer.add(body2)
        layer.add(body3)
        layer.add(eye)
    
        silver.add(self.layer)
        
    def shake1(self, theta):
        for i in range(theta):
            
            self.body1.rotate(i)
            self.body2.rotate(-i)
            self.body3.rotate(i)
            
        for i in range(theta):
            self.body1.rotate(-i)
            self.body2.rotate(i)
            self.body3.rotate(-i)
            
    def move(self, dx,dy):
        for i in range(dx):
            self.layer.move(i,0)
        for i in range(dy):
            self.layer.move(0,i)
    
    def moving(self, dx):
        for i in range(dx):
            self.layer.move(i,0)
            self.body1.rotate(i)
            self.body2.rotate(-i)
            self.body3.rotate(i)
    
    def moving2(self, dx):
        for i in range(dx):
            self.layer.move(-i,0)
            self.body1.rotate(i)
            self.body2.rotate(-i)   
            self.body3.rotate(i)
"""
Create your own animal object 
like 
class Mario(object):
    def __init__(self, ...
        self.layer = Layer()
        ...
        _scene.add(self.layer)
        
    ...

Don't forget '_scene.add(self.layer)' in constructor of object
"""

create_world()
#mario = Mario('Blue', 'normal')
#mushroom = Mushroom(200, 92)

# ......

snake = Snake("yellow", "dragon")
