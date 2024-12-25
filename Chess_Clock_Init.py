import turtle
import time
import keyboard
from Chess_Clock_Utilities import *
from Chess_Clock_Game import *

CLOCK_ON_RIGHT_OF_BLACK = True

white_time_init = '0:15'
black_time_init = '0:15'
white_increment = 0
black_increment = 0

screen = turtle.Screen()
screen.setup(width=0.8, height=0.8)

white = turtle.Turtle()
black = turtle.Turtle()
white.speed(0)
black.speed(0)
white.hideturtle()
black.hideturtle()
black.color('white')

if CLOCK_ON_RIGHT_OF_BLACK:
    make_rectangle(black, screen.window_height(), screen.window_width()/2, 0, screen.window_height()/2, 'black')
    white.pu()
    white.goto(-screen.window_width()/4, -FONTSIZE/2)
    white.pd()
    black.pu()
    black.goto(screen.window_width()/4, -FONTSIZE/2)
else:
    make_rectangle(black, screen.window_height(), screen.window_width()/2, -screen.window_width()/2, screen.window_height()/2, 'black')
    white.pu()
    white.goto(screen.window_width()/4, -FONTSIZE/2)
    white.pd()
    black.pu()
    black.goto(-screen.window_width()/4, -FONTSIZE/2)

white_time = time_in_seconds(white_time_init)
black_time = time_in_seconds(black_time_init)

white.write(time_string(white_time), align='center', font=('Arial', FONTSIZE, 'normal'))
black.write(time_string(black_time), align='center', font=('Arial', FONTSIZE, 'normal'))

while 1:
    if keyboard.is_pressed('space'):
        game_start(white, black, white_time, black_time, white_increment, black_increment)
        break

turtle.done()