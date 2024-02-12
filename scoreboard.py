from turtle import Turtle
FONT = ("Courier", 17, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.level = 1
        self.goto(-270, 260)
        self.write(f"Level: {self.level}", False, "left", FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)




