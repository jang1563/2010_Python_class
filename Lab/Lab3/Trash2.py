from cs1robots import*
create_world(avenues = 11, streets = 11)
edit_world()

hubo = Robot()
hubo.set_trace("blue")

def turn_right():
    for i in range(3):
        hubo.turn_left()
def turn_around():
    for i in range(2):
        hubo.turn_left()

def go_ahead():
    while hubo.front_is_clear():
        while hubo.on_beeper():
            hubo.pick_beeper()
        hubo.move()
 

def up():
    go_ahead()
    turn_right()
    if hubo.front_is_clear():
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()
        turn_right()

def down():
    go_ahead()
    hubo.turn_left()
    if hubo.front_is_clear():
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()
        hubo.turn_left()
   

      
hubo.turn_left()
while hubo.front_is_clear():
    up()
    if hubo.front_is_clear():
        down()
if hubo.left_is_clear():
    turn_around()
    go_ahead()
elif hubo.right_is_clear():
    turn_around()
    go_ahead()
    hubo.turn_left()
    go_ahead()
while hubo.carries_beepers():
    hubo.drop_beeper()