from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.level_up(1)

    def level_up(self, level):
        self.clear()
        self.goto(-280, 260)
        self.write(f'Level: {level}', align='left',font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

