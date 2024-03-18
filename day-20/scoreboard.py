from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write("Score: 0", align=ALIGNMENT, font=FONT)

    def increase_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)