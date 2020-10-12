'''
Do not modify import part.
'''
from cs1graphics import *
from time import sleep
from traffic_background import draw_background
from traffic_signal import make_signals, set_signal
from traffic_car import make_cars, move_car, car_action

'''
global variables
Do not modify here.
'''
# canvas ------------------------------------------------------------------------------------------------
canvas_w = 600       # canvas_width
road_w = 150           # road_width
canvas_size = (canvas_w, road_w)
canvas = draw_background(canvas_size)        # draw background
canvas.setAutoRefresh(False)                           # for fast actions

# road lists ----------------------------------------------------------------------------------------------
roads = []        # roads[i] : Car object list of ith road, i = 0, 1, 2, 3

'''
Roads look like the picture below.

       |  2  |               
       |      |               road[0]: the road on the bottom
-----+     +-----        road[1]: the road on the right
 3                1        road[2]: the road on the top
-----+     +-----        road[3]: the road on the left
       |      |
       |  0  |
'''

# traffic lights -----------------------------------------------------------------------------------------
lights = make_signals(canvas_size)        # light[i] : traffic light of road[i]
for i in range(4):
    canvas.add(lights[i].layer)
# set all lights to red at first.
for signal in lights:
    set_signal(signal, 'red')
# show the red lights
canvas.refresh()    


def get_ready ():
    '''
    (No Input)
    (No Output)
    
    The first car of roads moves to starting position before executing 'car_action' function.
    You should use this function before executing 'road_action' function.
    Do not modify this function.
    '''
    canvas.setAutoRefresh(True)
    for i in range(4):
        if len(roads[i]) > 0:
            car = roads[i][0]
            if not car.is_ready:
                move_car(car, 5)
                car.is_ready = True
    canvas.setAutoRefresh(False)


def is_empty():
    '''
    (No Input)
    (No Output)
    
    Return True if every road has no car, False otherwise.
    Do not modify this function.
    '''
    return len(roads[0]) == 0 and len(roads[1]) == 0 and len(roads[2]) == 0 and len(roads[3]) == 0


def road_action (road, traffic_sign='all'):
    '''
    (Input)
    road: Car object list, one of roads[i], i = 0, 1, 2, 3
    traffic_sign: String, one of ('red', 'yellow', 'left', 'green')
    (No Output)
    
    Send the first car ready if 'traffic_sign' and the sign of the car are met.
    If the car was moved, pop it from the road, otherwise just leave it.
    You should use 'get_ready' function before using this function.
    '''
    canvas.setAutoRefresh(True)
    if len(road) > 0:
        moved = car_action(canvas, road[0], traffic_sign)
        if moved:
            road.pop(0)
        else:
            sleep(1)
    else:
        sleep(1)
    canvas.setAutoRefresh(False)

    
def traffic_simulation1 ():
    '''
    (No Input)
    (No Output)

    This is an example where all lights change at the same time.
    '''
    sleep(1)
    for signal in lights:
        set_signal(signal, 'yellow')
    canvas.refresh()
    
    sleep(1)
    for signal in lights:
        set_signal(signal, 'left')
    canvas.refresh()
    
    sleep(1)
    for signal in lights:
        set_signal(signal, 'green')
    canvas.refresh()
    
    sleep(1)
    for signal in lights:
        set_signal(signal, 'red')
    canvas.refresh()


def traffic_simulation2 ():
    '''
    (No Input)
    (No Output)

    Here the signals go through the correct phases for each road.
    Your code must meet all the requirements in the description in 'HW4.pdf'
    '''
    # You should implement this function (1/2)
    ########################################
    ########################################

def traffic_simulation3 ():
    '''
    (No Input)
    (No Output)

    This is an example.
    Here all lights change at the same time.
    '''
    signal_list = ['right', 'left', 'straight', 'random']
    for i in range(4):
        roads.append( make_cars(canvas, canvas_size, i, signal_list) )
    
    while not is_empty():
        get_ready()
        canvas.refresh()
        sleep(1)
        
        for signal in lights:
            set_signal(signal, 'yellow')
        canvas.refresh()
        sleep(1)
        
        for signal in lights:
            set_signal(signal, 'left')
        canvas.refresh()
        
        for i in range(4):
            road_action(roads[i], 'left')
        
        for signal in lights:
            set_signal(signal, 'green')
        canvas.refresh()
        
        get_ready()
        for i in range(4):
            road_action(roads[i], 'green')
        
        for signal in lights:
            set_signal(signal, 'red')
        canvas.refresh()

def traffic_simulation4(how_many):
    '''
    (Input)
    how_many: Integer, the number of Car objects for each road
    (No Output)

    Here the lights go through the correct phases.
    Each road has 'how_many' cars of sign 'random'.
    Your code must meet all the requirements in the description in 'HW4.pdf'
    '''
    # You should implement this function. (2/2)
    ################################
    ################################
    


def canvas_refresh_example():
    '''
    This function works after completing move_car function.
    Example of using canvas.refresh() and canvas.setAutoRefresh()
    '''
    cars = make_cars(canvas, canvas_size, 0, ['straight', 'straight', 'straight'])
    
    # You can see every update
    canvas.setAutoRefresh(True)
    move_car(cars[0], 15)
    # Now you cannot see any undates until using canvas.refresh()
    canvas.setAutoRefresh(False)
    
    sleep(1)
    
    move_car(cars[1], 10)
    # Now you can see that cars[1] moved 10 step forward.
    canvas.refresh()
    
    sleep(1)
    # you never see that cars[2] moved.
    move_car(cars[2], 5)
    
'''
main part
'''
#canvas_refresh_example()
#traffic_simulation1()
#traffic_simulation2()
#traffic_simulation3()
#traffic_simulation4(3)
    
    
