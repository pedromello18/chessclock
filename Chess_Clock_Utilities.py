import turtle
import time

def make_rectangle(turtle, height, width, startx, starty, color):
    x, y = turtle.xcor(), turtle.ycor()

    turtle.pu()
    turtle.goto(startx, starty)
    turtle.pd()

    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(height)
    turtle.right(90)
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(height)
    turtle.right(90)
    turtle.end_fill()

    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()

def time_in_seconds(time_string):
    l = time_string.split(":")
    time_in_seconds = 0
    for i in range(len(l)):
        try:
            time_in_seconds += int(l[i])*(60**(len(l)-1-i))
        except SyntaxError:
            time_in_seconds += int(l[i][1])*(60**(len(l)-1-i))
    return time_in_seconds

def time_string(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds - hours*3600) // 60
    seconds = time_in_seconds - hours*3600 - minutes*60
    if seconds < 10:
        time_string = '0' + str(seconds)
    else:
        time_string = str(seconds)
    if hours == 0:
        time_string = str(minutes) + ':' + time_string
    else:
        if minutes < 10:
            time_string = str(hours) + ':0' + str(minutes) + ':' + time_string
        else:
            time_string = str(hours) + ':' + str(minutes) + ':' + time_string
    return time_string
