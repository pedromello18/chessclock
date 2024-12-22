import turtle
import time
import keyboard
from Chess_Clock_Utilities import *
from Chess_Clock_Game import *

CLOCK_ON_RIGHT_OF_BLACK = True

white_time_init = '0:15'
black_time_init = '0:15'
white_increment = 2
black_increment = 2

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

white.write(white_time_init, align='center', font=('Arial', FONTSIZE, 'normal'))
black.write(black_time_init, align='center', font=('Arial', FONTSIZE, 'normal'))

while 1:
    if keyboard.is_pressed('space'):
        game_start(white, black, white_time_init, black_time_init, white_increment, black_increment)
        break

turtle.done()