from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Courier',18, 'normal')
# How to keep trace of the score
# How to display it in our program

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()# call to the super class
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()

    def score_display(self, l_score, r_score):
        self.goto(-100, 280)
        self.write(f"L_Score: {l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 280)
        self.write(f"R_Score: {r_score}", move=False, align=ALIGNMENT, font=FONT)

    def score_clear(self):
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
