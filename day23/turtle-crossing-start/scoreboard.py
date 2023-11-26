from turtle import Turtle

XPOISITION = -200
YPOSITION = 260
ALIGNMENT = "center"
FONT = ('Courier',24, 'normal')
# How to keep trace of the score
# How to display it in our program

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()# call to the super class
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.goto(XPOISITION,YPOSITION)
        self.hideturtle()

    def score_display(self, score):
        return self.write(f"Score: {score}", move=False, align=ALIGNMENT, font=FONT)

    def score_clear(self):
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
