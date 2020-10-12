from cs1robots import*
create_world(14,14)
edit_world()
save_world("worlds/rain3.wld")
#load_world("worlds/rain2.wld")
hubo = Robot(beepers = 100, orientation = "E", avenue = 2, street = 6)
hubo.set_trace("blue")

def turn_right():
    for i in range(3):
        hubo.turn_left()
def turn_around():
    for i in range(2):
        hubo.turn_left()
        
def close_window():
    if hubo.right_is_clear():
        hubo.drop_beeper()
        hubo.move()
        if hubo.right_is_clear():
            turn_around()
            hubo.move()
            hubo.pick_beeper()
            hubo.turn_left()
            hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()

hubo.move()
hubo.drop_beeper()
turn_right()
hubo.move()
while not hubo.on_beeper():
    close_window()
hubo.pick_beeper()
