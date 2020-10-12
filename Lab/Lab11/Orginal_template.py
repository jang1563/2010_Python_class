from cs1graphics import *
from time import sleep

_scene = None
_world = None

class _World(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = {}
        
    def add(self, name, obj):
        self.objects[name] = obj

    def draw_scene(self):
        """ 
        backgourd drawing
        Don't forget _scene.add(name)
        """
        


def create_world():
    global _scene, _world
    if _scene:
        raise RuntimeError("A world already exists!")
    _world = _World(500, 300)
    _scene = Canvas(_world.width, _world.height)
    _scene.setTitle("Mario World")
    _world.draw_scene()


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

