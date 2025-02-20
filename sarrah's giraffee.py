import turtle
import random

screen = turtle.Screen()
screen.setup(800, 500)  
screen.bgcolor("#1a5276")

t = turtle.Turtle()
t.speed(100)

t.width(5)

t.color('black','#f8c471')
t.begin_fill()
t.pu()
t.goto(-30,-250)
t.pd()
t.goto(-10,0)
t.pu()
t.goto(30,-250)
t.pd()
t.goto(10,0)
t.pu()
t.goto(-35,13)
t.pd()

def draw(rad):
  for i in range(2):
    t.circle(rad,90)
    t.circle(rad//2,90)

t.seth(-45)
draw(50)
t.end_fill()

t.pu()
t.goto(-30,-250)
t.pd()

t.width(5)
t.color('black','#f8c471')
t.begin_fill()
t.goto(30,-250)
t.goto(10,0)
t.goto(-10,0)
t.end_fill()
t.goto(-30,-250)
t.end_fill()

t.pu()
t.goto(-22,85)
t.pd()

t.color('black','#f8c471')
t.begin_fill()
def draw(rad):
  for i in range(2):
    t.circle(rad,90)
    t.circle(rad/2,90)

t.seth(-130)
draw(50)
t.end_fill()

t.pu()
t.goto(-35,13)
t.pd()
t.color('black','#FFDEAD')
t.begin_fill()
def draw(rad):
  for i in range(2):
    t.circle(rad,90)
    t.circle(rad//2,90)

t.seth(-45)
draw(50)
t.end_fill()

t.pu()
t.goto(20,87)
t.pd()

t.color('#784212')
t.width(15)
t.lt(100)
t.fd(20)
t.rt(50)
t.fd(3)
t.circle(3)

t.pu()
t.goto(-20,87)
t.pd()

t.color('#784212')
t.width(15)
t.lt(100)
t.fd(20)
t.rt(50)
t.fd(3)
t.circle(3)

t.pu()
t.goto(-15,70)
t.pd()

t.width(2)
t.color('black','black')
t.begin_fill()
t.circle(3)
t.end_fill()

t.pu()
t.rt(55)
t.fd(27)
t.pd()

t.width(2)
t.color('black','black')
t.begin_fill()
t.circle(3)
t.end_fill()

t.pu()
t.goto(23,83)
t.pd()

t.lt(20)
t.fd(35)
t.color('black','#f8c471')
t.begin_fill()
for count in range(35):
    t.rt(5)
    t.fd(1)

t.goto(20,77)
t.rt(90)
t.fd(5)
t.end_fill()

t.pu()
t.goto(-20,80)
t.pd()

t.lt(20)
t.fd(35)
t.color('black','#f8c471')
t.begin_fill()
for count in range(35):
    t.lt(5)
    t.fd(1)

t.goto(-20,83)
t.rt(90)
t.fd(5)
t.end_fill()

t.pu()
t.goto(-20,35)
t.rt(90)
t.pd()
t.fd(5)

for count in range(10):
    t.lt(25)
    t.fd(2)

t.fd(3)

t.pu()
t.goto(20,35)
t.lt(45)
t.pd()
t.fd(5)

for count in range(10):
    t.rt(25)
    t.fd(2)

t.fd(5)

t.pu()
t.goto(10,-50)
t.pd()

t.color('#af601a','#af601a')
t.begin_fill()
for count in range(5):
    t.rt(25)
    t.fd(2)

t.lt(90)
t.fd(5)

for count in range(5):
    t.lt(25)
    t.fd(2)

t.fd(10)

for count in range(2):
    t.rt(25)
    t.fd(2)

t.lt(90)
t.fd(3)

for count in range(2):
    t.lt(25)
    t.fd(2)

t.fd(10)
t.lt(90)
t.fd(15)
t.lt(90)
t.fd(7)
t.end_fill()



t.pu()
t.goto(-18,-100)
t.pd()

t.rt(180)
t.fd(5)

t.color('#af601a','#af601a')
t.begin_fill()
for count in range(5):
    t.rt(25)
    t.fd(2)

t.lt(90)
t.fd(5)

for count in range(5):
    t.lt(25)
    t.fd(2)

t.fd(10)

for count in range(2):
    t.rt(25)
    t.fd(2)

t.lt(90)
t.fd(3)

for count in range(2):
    t.lt(25)
    t.fd(2)

t.fd(10)
t.lt(90)
t.fd(15)
t.lt(90)
t.fd(7)
t.end_fill()

t.pu()
t.goto(-25,-150)
t.pd()

t.fd(5)

t.color('#af601a','#af601a')
t.begin_fill()
for count in range(5):
    t.rt(25)
    t.fd(3)

t.lt(90)
t.fd(7)

for count in range(5):
    t.lt(25)
    t.fd(2)

t.fd(10)

for count in range(2):
    t.rt(25)
    t.fd(2)

t.lt(90)
t.fd(4)

for count in range(2):
    t.lt(25)
    t.fd(3)

t.fd(10)
t.lt(90)
t.fd(15)
t.lt(90)
t.fd(7)
t.end_fill()

t.fd(5)

t.color('white')
def draw_star(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(5):  
        t.forward(10)
        t.right(144)

def draw_random_stars(number_of_stars):
    for _ in range(number_of_stars):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        draw_star(x, y)


draw_random_stars(50)


t.hideturtle()

turtle.done()