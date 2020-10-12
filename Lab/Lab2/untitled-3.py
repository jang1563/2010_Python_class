from cs1robots import *
load_world("worlds/hurdles3.wld") 
hubo = Robot()
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
def jump():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
    else :
        jump()
