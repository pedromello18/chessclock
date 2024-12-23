import turtle
import time
import keyboard
from Chess_Clock_Utilities import *

FONTSIZE = 50
SENSITIVITY = 0.5 # manually adjusted

def white_special_rule(white_time, white_move_count):
    # if white_move_count == 3:
    #     return white_time + 5*60
    return white_time

def black_special_rule(black_time, black_move_count):
    # if black_move_count == 3:
    #     return black_time + 5*60
    return black_time

def game_start(white_turtle, black_turtle, white_time_init, black_time_init, white_increment, black_increment):
    white_move_counter = 0
    black_move_counter = 0
    white_turn = True
    white_time = time_in_seconds(white_time_init)
    black_time = time_in_seconds(black_time_init)
    last_stamp = time.time()
    time.sleep(SENSITIVITY)
    while 1:
        if white_turn:
            white_time -= time.time() - last_stamp
        else:
            black_time -= time.time() - last_stamp
        last_stamp = time.time()
        white_turtle.undo()
        white_turtle.write(time_string(white_time), align='center', font=('Arial', FONTSIZE, 'normal'))
        black_turtle.undo()
        black_turtle.write(time_string(black_time), align='center', font=('Arial', FONTSIZE, 'normal'))
        if (white_time <= 0) or (black_time <= 0):
            break
        if keyboard.is_pressed('space'):
            if white_turn:
                white_time += white_increment
                white_move_counter += 1
                white_time = white_special_rule(white_time, white_move_counter)
            else:
                black_time += black_increment
                black_move_counter += 1
                black_time = black_special_rule(black_time, black_move_counter)
            white_turn = not white_turn
            time.sleep(SENSITIVITY)
    return 0