import random
import colorgram
import turtle as turtle_module

turtle_module.colormode(255)
cartman = turtle_module.Turtle()
cartman.pensize(20)
colors = colorgram.extract('./assets/img.webp', 27)

rgb_list = []
for c in colors:
    r = c.rgb[0]
    g = c.rgb[1]
    b = c.rgb[2]
    rgb_list.append((r, g, b))

cartman.speed(0)
cartman.penup()
cartman.hideturtle()

for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        cartman.goto(x, y)
        cartman.dot(20, random.choice(rgb_list))

screen = turtle_module.Screen()
screen.exitonclick()
