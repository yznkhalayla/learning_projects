from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_turtle_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_turtle_backward(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)