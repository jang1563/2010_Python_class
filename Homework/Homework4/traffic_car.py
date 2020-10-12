'''
Do not modify import part.
'''
from cs1graphics import *
import random

class Car ():
    '''
    Car class
    
    Do not modify here.
    '''
    layer = None              # layer
    sign = None               # sign which means the direction that this car want to go
    sign_layer = None     # layer containg sign shape (You can ignore this.)
    road = None              # the road number of this car: 0 or 1 or 2 or 3
    road_w = None         # road width
    unit_length = None   # the length of car moving one step
    is_ready = False        # check this car ready
    

    
    
def make_car (canvas_size, road_num=0, sign='random'):
    '''
    (Input)
    canvas_size = (canvas_width, road_width)
    (Output)
    Car object
    
    Create a Car object on the 'road_num'th road with sign 'sign' 
    Do not modify this function.
    '''
    temp_car = Layer()
    temp_car.setDepth(80)
    # body
    body = Rectangle(50, 60)
    body.setFillColor("white")
    body.setDepth(80)
    temp_car.add(body)
    
    # sign
    arrow = Polygon( Point(0, -8), Point(8, 6), Point(-8, 6) )
    arrow.setDepth(79)
    arrow.adjustReference(0, 8)
    arrow.setFillColor("black")
    temp_car.add(arrow)

    
    if  sign == 'random':
        random_sign = random.randint(1, 3)
        if random_sign == 1:
            sign = 'left'
        elif random_sign == 2:
            sign = 'right'
        elif random_sign == 3:
            sign = 'straight'
    
    if sign == 'left':
        arrow.rotate(-90)
    elif sign == 'right':
        arrow.rotate(90)
    elif sign != 'straight':
        return None
    
    
    # road
    canvas_w, road_w = canvas_size
    if road_num == 0:
        temp_car.move( canvas_w//2 + road_w//4, canvas_w)
    elif road_num == 1:
        temp_car.rotate(-90)
        temp_car.move( canvas_w, canvas_w//2 - road_w//4 )
    elif road_num == 2:
        temp_car.rotate(180)
        temp_car.move( canvas_w//2 - road_w//4, 0)
    elif road_num == 3:
        temp_car.rotate(90)
        temp_car.move( 0, canvas_w//2 + road_w//4 )
    else:
        return None
    
    car = Car( )
    car.layer = temp_car
    car.sign = sign
    car.sign_layer = arrow
    car.road = road_num
    car.road_w = road_w
    car.unit_length = (canvas_w - road_w)//12
    return car


def make_cars (canvas, canvas_size, road_num=0, sign_list=[]):
    '''    
    (Input)
    canvas: Canvas object, Car objects should be added on this canvas.
    canvas_size = (canvas_width, road_width)
    road_num: Integer in (0,1,2,3), road number
    sign_list: string list, the directions that cars want to go. strings must be one of ('left', 'right', 'straight', 'random')
    (Output)
    cars: Car object list 
    
    Create Car objects on the 'road_num'th road  with the signs 'sign_list'.
    After creating Car objects, Add these Car objects on the 'canvas'.
    Do not modify this function.
    '''
    cars = []
    for i in range(len(sign_list)):
        cars.append( make_car(canvas_size, road_num, sign_list[i]) )
        canvas.add(cars[i].layer)
    return cars


def move_car (car, times = 1):
    '''
    (Input)
    car: Car object
    times: Integer
    (No Output)
    
    'car' moves car.unit_length*times steps forward.
    Each movement of length car.unit_length should be shown on the graphic animation.
    The meaning 'forward' depends on the road number.
    
           |  2  |               'forward' means on the road
           |      |               0: up
    -----+     +-----        1: left
    3  ->       <-  1        2: down
    -----+     +-----        3: right
           |      |
           |  0  |
    '''
    # You should implement this function (1/2)
    #################################
    #################################


# Car Action Function 1 
def go_straight_car (car):
    '''
    (Input)
    car: Car object
    (No Output)
    
    Car goes straight further and disappers. 'car' should be on the right position.
    'car' is on the starting position after using 'get_ready' function.
    You can check whether 'car' is ready or not by car.is_ready value.
    
    Do not modify this function.
    '''
    move_car(car, 13)

def make_straight_sign (car):
    '''
    For turn_left_car and turn_right_car functions.
    You can ignore this function.
    Do not modify this function.
    '''
    if car.sign == 'left':
        car.sign_layer.rotate(90)
    elif car.sign == 'right':
        car.sign_layer.rotate(-90)
    car.sign = 'straight'

    
# Car Action Function 2
def turn_left_car (car):
    '''
    (Input)
    car: Car object
    (No Output)
    
    Car is turning left. 'car' should be on the right position.
    'car' is on the starting position after using 'get_ready' function.
    You can check whether 'car' is ready or not by car.is_ready value.
    
    Do not modify this function.
    '''
    move_car(car)
    if car.road == 0:
        car.layer.adjustReference( -car.road_w*3//4, 0 )
    elif car.road == 1:
        car.layer.adjustReference( 0, car.road_w*3//4 )
    elif car.road == 2:
        car.layer.adjustReference( car.road_w*3//4, 0 )
    elif car.road == 3:
        car.layer.adjustReference( 0, -car.road_w*3//4 )
    for i in range(6):
        car.layer.rotate(-15)
            
    car.road = (car.road + 1) % 4
    make_straight_sign(car)
    move_car(car, 10)

    
# Car Action Function 3
def turn_right_car (car):
    '''
    (Input)
    car: Car object
    (No Output)
    
    Car is turning right. 'car' should be on the right position.
    'car' is on the starting position after using 'get_ready' function.
    You can check whether 'car' is ready or not by car.is_ready value.
    
    Do not modify this function.
    '''
    move_car(car)
    if car.road == 0:
        car.layer.adjustReference( car.road_w//4, 0 )
    elif car.road == 1:
        car.layer.adjustReference( 0, -car.road_w//4 )
    elif car.road == 2:
        car.layer.adjustReference( -car.road_w//4, 0 )
    elif car.road == 3:
        car.layer.adjustReference( 0, car.road_w//4 )
    for i in range(6):
        car.layer.rotate(15)
            
    car.road = (car.road + 3) % 4
    make_straight_sign(car)
    move_car(car, 10)



def find_action_function (car, traffic_sign='all'):
    '''
    (Input) 
    car : Car object
    traffic_sign: Current signal of traffic light. one of ('red', 'yellow', 'left', 'green')
    (Output)
    function: Proper action function depending on car sign and traffic sign. 
                   If they didn't match, return None
    
    This function is used for car_action function below.
    Check the sign of 'car' and 'traffic_sign'. 
    If they are met, return appropriate action function.
    Otherwise None object will be returned.
    
    '''
    
    # You should complete this function (2/2)
    if car.sign == 'left' and traffic_sign in ('left', 'all'):
        #  Do something on here. (2-1)
        #########################
        return
        #########################
    elif car.sign == 'right' and traffic_sign in ('green', 'all'):
        #  Do something on here. (2-2)
        #########################
        return
        #########################
    elif car.sign == 'straight' and traffic_sign in ('green', 'all'):
        #  Do something on here. (2-3)
        #########################
        return
        #########################
    else:
        #  Do something on here. (2-4)
        #########################
        return
        #########################
    

def car_action (canvas, car, traffic_sign='all'):
    '''
    (Input) 
    car : Car object
    traffic_sign: Current signal of traffic light. one of ('red', 'yellow', 'left', 'green')
    (Output)
    Boolean value : True if 'car' moved, False otherwise.
    
    Car should obey the traffic light signal.
    Do not modify this function.
    '''
    if car.is_ready:
        action_function = find_action_function (car, traffic_sign)
        if action_function != None:
            action_function(car)
            canvas.remove(car.layer)
            return True
        else:
            return False
        

