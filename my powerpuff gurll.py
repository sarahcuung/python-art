
import turtle
import random

screen = turtle.Screen()
screen.setup(800, 500)  
screen.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.speed(0)

def draw_head(x, y, width, height):
    t.color("black","#FFDEB9")  
    t.penup()
    t.goto(x, y - height / 2) 
    t.pendown()
    t.setheading(0)  
    t.begin_fill()
    t.seth(45) 
    for _ in range(2): 
        t.circle(width, 90)  
        t.circle(height, 90)  
    t.end_fill()

def eyes(x, y, width, height):
    t.color('black','white')
    t.penup()
    t.goto(x, y - height / 2) 
    t.pendown()
    t.setheading(0) 
    t.begin_fill() 
    t.seth(45) 
    for _ in range(2): 
        t.circle(width, 90)  
        t.circle(height, 90)  
    t.end_fill()

def asung(x, y, width, height):
    t.color('black','#8DD070')
    t.penup()
    t.goto(x, y - height / 2) 
    t.pendown()
    t.setheading(0) 
    t.begin_fill() 
    t.seth(45) 
    for _ in range(2): 
        t.circle(width, 90)  
        t.circle(height, 90)  
    t.end_fill()

def asungta(x, y, width, height):
    t.color('black','black')
    t.penup()
    t.goto(x, y - height / 2) 
    t.pendown()
    t.setheading(0) 
    t.begin_fill() 
    t.seth(45) 
    for _ in range(2): 
        t.circle(width, 90)  
        t.circle(height, 90)  
    t.end_fill()

def asungtatleng(x, y, width, height):
    t.color('white','white')
    t.penup()
    t.goto(x, y - height / 2) 
    t.pendown()
    t.setheading(0) 
    t.begin_fill() 
    t.seth(45) 
    for _ in range(2): 
        t.circle(width, 90)  
        t.circle(height, 90)  
    t.end_fill()

draw_head(130, 35, 115, 155)
eyes(150, 35, 40, 70)
eyes(-5, 35, 40, 70)
asung(-5, 20, 40, 40)
asung(110, 20, 40, 40)
asungta(100, 20, 35, 35)
asungta(-5, 20, 35, 35)
asungtatleng(-15, 13, 25, 10)
asungtatleng(75, 15, 25, 10)

def draw_head(x, y, width, height):
    t.color("black")  
    t.penup()
    t.goto(x, y - height / 2) 
    t.pendown()
    t.setheading(0)  
    t.seth(45) 
    for _ in range(2): 
        t.circle(width, 90)  
        t.circle(height, 90)  

draw_head(130, 35, 115, 155)

t.color('black','black')
t.begin_fill()
t.fd(162)
t.lt(135)
t.fd(200)
t.rt(60)
t.fd(50)
t.lt(120)
t.fd(50)
t.rt(60)
t.fd(150)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(400)
t.rt(90)
t.fd(150)
t.end_fill()

t.pu()
t.goto(10,-60)
t.pd()

t.lt(100)
t.fd(40)

t.hideturtle()
screen.exitonclick()

turtle.done()



