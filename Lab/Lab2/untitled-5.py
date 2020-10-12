from cs1robots import *
create_world(7,7) 
hubo = Robot()
hubo.turn_left()
def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
def go():
    while hubo.front_is_clear():
        hubo.move()
go()
turn_right()
def go_one():
    if hubo.front_is_clear():
        hubo.move()
        turn_right()
        go()
        hubo.turn_left()
def go_two():
    if hubo.front_is_clear():
        hubo.move()
        hubo.turn_left()
        go()
        turn_right()
while hubo.front_is_clear():
    go_one()
    go_two()
    