from cs1robots import *
load_world("worlds/harvest3.wld") 
hubo = Robot(beepers=7)
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
hubo.move()
hubo.turn_left()
    
def hubo_go():
    if not hubo.on_beeper():
        hubo.drop_beeper()
        hubo.move()
    else:
        hubo.move()
def unit():
    for i in range(5):
        hubo_go()
    if not hubo.on_beeper():
        hubo.drop_beeper()
        turn_right()
        hubo.move()
        turn_right()
    else:
        turn_right()
        hubo.move()
        turn_right()
    for i in range(5):
        hubo_go()
    if not hubo.on_beeper():
        hubo.drop_beeper()
    hubo.turn_left()
    if hubo.front_is_clear():
        hubo.move()
        hubo.turn_left()
for i in range(3):
    unit()