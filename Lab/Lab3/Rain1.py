from cs1robots import*
load_world("worlds/rain1.wld")
hubo = Robot(beepers = 100, orientation = "E", avenue = 2, street = 6)
hubo.set_trace("blue")

def turn_right():
    for i in range(3):
        hubo.turn_left()

def close_window():
    if hubo.right_is_clear():
        hubo.drop_beeper()
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
