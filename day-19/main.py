import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput(title="Which color you bet on?", prompt="Which turtle will win the race? Enter color: ").lower()
colors = ["red", "orange", "blue", "purple", "green", "yellow"]
y_post = [-70, -40, -10, 20, 50, 80]
turtles = []
race_on = False

y_init = -70
x_init = -200

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_post[index])
    new_turtle.color(colors[index])
    new_turtle.pendown()
    new_turtle.penup()
    turtles.append(new_turtle)

if bet in colors:
    race_on = True

while race_on:
    for turtle in turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            if turtle.color()[0] == bet:
                print("You won!")
            else:
                print("You lost!")
            race_on = False


screen.exitonclick()
