import turtle
import time
import keyboard
from Chess_Clock_Utilities import *

FONTSIZE = 50

def game_start(white_turtle, black_turtle, white_time_init, black_time_init, white_increment, black_increment):
    white_turn = True
    white_time = time_in_seconds(white_time_init)
    black_time = time_in_seconds(black_time_init)
    last_decrement = time.time()
    while 1:
        if time.time() - last_decrement >= 1:
            if white_turn:
                white_time -= 1
            else:
                black_time -= 1
            last_decrement = time.time()
        white_turtle.undo()
        white_turtle.write(time_string(white_time), align='center', font=('Arial', FONTSIZE, 'normal'))
        black_turtle.undo()
        black_turtle.write(time_string(black_time), align='center', font=('Arial', FONTSIZE, 'normal'))
        if (white_time <= 0) or (black_time <= 0):
            break
        time.sleep(0.075) # manually determined
        if keyboard.is_pressed('space'):
            if white_turn:
                white_time += white_increment
            else:
                black_time += black_increment
            white_turn = not white_turn
    return 0