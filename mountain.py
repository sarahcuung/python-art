import turtle
import random

screen = turtle.Screen()
screen.setup(800, 500)  
screen.bgcolor("#87CEEB")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_wavy_hill(color, start_x, start_y, width, wave_height, wave_length):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    for x in range(start_x, start_x + width, wave_length):
        y_offset = random.randint(-wave_height, wave_height)
        t.goto(x, start_y + y_offset)

    t.goto(start_x + width, -200)
    t.goto(start_x, -200)
    t.goto(start_x, start_y)
    
    t.end_fill()

draw_wavy_hill("#90EE90", -400, -100, 900, 30, 50)
draw_wavy_hill("#66CDAA", -400, -150, 900, 20, 50)

t.penup()
t.goto(250, 150)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

turtle.done()