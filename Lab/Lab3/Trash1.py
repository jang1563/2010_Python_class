from cs1robots import*
load_world("worlds/trash1.wld")
hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for i in range(3):
        hubo.turn_left()
def turn_around():
    for i in range(2):
        hubo.turn_left()

def carry():
    while hubo.front_is_clear():
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()
    turn_around()
    while hubo.front_is_clear():
        hubo.move()
    turn_right()
    hubo.move()
    while hubo.carries_beepers():
        hubo.drop_beeper()
    turn_around()           
    hubo.move()
    hubo.turn_left()
    
carry()