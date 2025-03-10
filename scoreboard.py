from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        with open("high_scores.txt") as file:
            self.high_score = int(file.read())
        self.something = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)
        self.board()

    def board(self):
        self.clear()
        self.write(f"Score: {self.something} High Score: {self.high_score}", False, 'center', ('Courier',16, 'normal'))

    def increase_score(self):
        self.something += 1
        self.board()

    def highest(self):
        if self.something > self.high_score:
            self.high_score = self.something
            with open("high_scores.txt", mode="w") as file:
                 file.write(str(self.high_score))
        self.something = 0
        self.board()
