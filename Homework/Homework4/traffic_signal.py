'''
Do not modify import part.
'''
from cs1graphics import *

class Signal():
  '''
  Signal class 
  
  Do not modify this class.
  '''
  layer = None      # layer
  red = None        # red light
  green = None      # green light
  left_turn = None  # left turn green light
  yellow = None     # yellow light
  

def make_signal():
  '''
  (No Input)
  (Output)
  a Signal object
  
  Make a Signal object.
  Do not modify this function.
  '''
  traffic_light = Layer()
    
  light_box = Rectangle(80, 20)
  light_box.setFillColor("black")
  light_box.setDepth(30)
  traffic_light.add(light_box)
  
  red_light = Circle(8)
  red_light.setFillColor("black")
  red_light.move(-27, 0)
  red_light.setDepth(29)
  traffic_light.add(red_light)
  
  yellow_light = Circle(8)
  yellow_light.setFillColor("black")
  yellow_light.move(-9, 0)
  yellow_light.setDepth(29)
  traffic_light.add(yellow_light)
  
  # make triangle: reference point is at the first point.
  left_green_light = Polygon(Point(-8, 0), Point(6, 8), Point(6, -8))
  left_green_light.setFillColor("black")
  # move reference point of triangle to the center point
  left_green_light.adjustReference(8, 0)
  left_green_light.move(9, 0)
  left_green_light.setDepth(29)
  traffic_light.add(left_green_light)
  
  green_light = Circle(8)
  green_light.setFillColor("black")
  green_light.move(27, 0)
  green_light.setDepth(29)
  traffic_light.add(green_light)
  
  traffic_light.setDepth(30)
  
  signal = Signal()
  signal.layer = traffic_light
  signal.red = red_light
  signal.yellow = yellow_light
  signal.left_turn = left_green_light
  signal.green = green_light
    
  return signal


def make_signals(canvas_size):
  '''
  (Input)
  canvas_size = (canvas_width, road_width)
  (Output)
  signals: a list of 4 Signal objects
  
  Make 4 Signal objects on the intersection.
  Do not modify this function.
  '''
  signals = []
  canvas_w, road_w = canvas_size    
  for i in range(4):
    signals.append(make_signal())
    signals[i].layer.move(canvas_w//2, canvas_w//2+road_w//2)
    signals[i].layer.adjustReference(0, -road_w//2)
    signals[i].layer.rotate(-90*i)
  
  return signals


def set_signal(signal, light):
  '''
  (Input)
  signal: a Signal object
  light: one of the strings 'red', 'yellow', 'green', 'left'.
  (No Output)
    
  Changes the signal to display the requested light pattern.
  Set the right color for 'light' and black for others.
  '''
  # You should implement this function (1/1)
  #################################
  #################################
    
