import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background for better visibility of stars

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed
t.hideturtle()  # Hide the turtle cursor

# List of green shades that resemble Buttercup's theme, with brighter, vivid colors
green_shades = [
    "#66FF00",  # Bright neon green
    "#33FF00",  # Vivid lime green
    "#00FF00",  # Electric green
    "#00FF33",  # Bright lime green
    "#33CC33",  # Bright medium green
]

# Function to draw a filled star at a given size and position with a random green shade
def draw_star(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Choose a random green shade from the list
    color = random.choice(green_shades)

    t.begin_fill()
    t.fillcolor(color)  # Set the fill color to a random green shade

    # Draw a 5-pointed star
    for _ in range(5):
        t.forward(size)
        t.right(144)  # Turn 144 degrees to form the star's points

    t.end_fill()

# Draw multiple big stars with random sizes, positions, and shades of green
for _ in range(10):  # Draw 10 stars
    x = random.randint(-300, 300)  # Random x position
    y = random.randint(-200, 200)  # Random y position
    size = random.randint(50, 100)  # Random size between 50 and 100 (larger stars)
    draw_star(x, y, size)

# Keep the window open until clicked
screen.exitonclick()
