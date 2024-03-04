from turtle import Turtle

XPOISITION = -20
YPOSITION = 280
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')


# How to keep trace of the score
# How to display it in our program

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # call to the super class
        self.color("white")
        self.penup()
        self.score = 0
        self.read_high_score_store()
        self.speed("fastest")
        self.goto(XPOISITION, YPOSITION)
        self.hideturtle()

    def read_high_score_store(self):
        with open("data.txt", mode="r") as file:
            high_score = int(file.read())
            return high_score

    def write_to_high_score_store(self, score):
        print(f"write content!!")
        with open("data.txt", mode="w") as file:
            file.write(str(score))

    def score_display(self):
        self.clear()
        return self.write(f"Score: {self.score} " f" High_score: {self.read_high_score_store()}", move=False, align=ALIGNMENT, font=FONT)

    def score_clear(self):
        self.clear()

    def increase_score(self):
        self.score = self.score + 1

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        print("reset happened!!")
        print( f"read value: {self.read_high_score_store()}")
        print( f"score value: {self.score}")
        if self.score > (self.read_high_score_store()):
            # self.high_score = self.score
            self.write_to_high_score_store(self.score)
        self.score = 0
        self.score_display()
