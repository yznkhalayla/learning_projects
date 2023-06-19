import turtle
from turtle import Turtle, Screen
import random
import colorgram
import time


def draw_shape(polygon, timmy):
    angle = 360 / polygon
    for i in range(polygon):
        timmy.forward(100)
        timmy.right(angle)


def multiple_draw_shape(polygon, timmy):
    for i in range(3, polygon + 1):
        draw_shape(i)
        timmy.pencolor(random.random(), random.random(), random.random())


def draw_spirograph(gap, timmy):
    for i in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def extractor(image, colors_number):
    """turtle needs to be in RGB prior to using this function"""
    turtle.colormode(255)
    rgb_colors = []
    colors = colorgram.extract(image, colors_number)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)


def wall_checker(self):
    # print(self.xcor(), self.ycor())
    if self.xcor() > 300:
        self.goto(290, self.ycor())
    elif self.xcor() < -300:
        self.goto(-290, self.ycor())

    if self.ycor() > 300:
        self.goto(self.xcor(), 290)
    elif self.ycor() < -300:
        self.goto(self.xcor(), -290)


def random_walk(walks, timmy):
    l_boolean = True
    while l_boolean:
        timmy.color(random_color())
        timmy.setheading(random.randint(1, 4) * 90)

        wall_checker(timmy)
        timmy.forward(30)

        walks -= 1
        if walks == 0:
            l_boolean = False


def damien_hirst(height, width, timmy):
    turtle.colormode(255)
    rgb_colors = [(248, 244, 246), (232, 228, 221), (206, 145, 102), (20, 17, 18), (158, 167, 14), (45, 29, 17),
                  (219, 234, 227), (158, 56, 11), (112, 147, 184), (213, 228, 234), (41, 112, 164), (120, 184, 148),
                  (224, 212, 125), (201, 129, 136), (4, 57, 101), (78, 155, 82), (139, 5, 0), (246, 197, 0),
                  (230, 104, 36),
                  (98, 94, 96), (7, 67, 123), (124, 16, 20), (78, 140, 81), (208, 182, 185), (230, 173, 163),
                  (151, 118, 124), (165, 209, 178), (90, 132, 170), (97, 59, 26), (21, 23, 22), (175, 190, 214),
                  (87, 139, 164), (172, 201, 206)]
    l = 0
    timmy.hideturtle()
    timmy.penup()
    timmy.setheading(270)
    timmy.forward(200)
    timmy.setheading(180)
    timmy.forward(150)
    timmy.setheading(0)
    position = timmy.position()

    for i in range(0, height * width):
        timmy.color(random.choice(rgb_colors))
        timmy.dot(20)
        timmy.forward(50)
        l += 1
        if l == width:
            timmy.goto(position)
            timmy.left(90)
            timmy.forward(50)
            timmy.right(90)
            position = timmy.position()
            l = 0


def move_forward():
    timmy = Turtle('turtle')
    timmy.forward(10)


def move_backward():
    timmy = Turtle('turtle')
    timmy.backward(20)


def tilt_left():
    timmy = Turtle('turtle')
    timmy.left(10)


def tilt_right():
    timmy = Turtle('turtle')
    timmy.right(10)


def clear():
    timmy = Turtle('turtle')
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def play():
    screen = Screen()
    screen.listen()
    screen.onkey(key='w', fun=move_forward)
    screen.onkey(key='s', fun=move_backward)
    screen.onkey(key='a', fun=tilt_left)
    screen.onkey(key='d', fun=tilt_right)
    screen.onkey(key='c', fun=clear)


def turtles_race(turtle):
    screen = Screen()
    screen.setup(width=600, height=600)
    turtle.speed(10)

    is_race_on = False
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    y = [70, 40, 10, -10, -40, -70]
    turtles = []

    for index in range(0, 6):
        new = Turtle(shape='turtle')
        new.color(colors[index])
        new.penup()
        new.goto(-280, y[index])
        turtles.append(new)

    bet = screen.textinput(title='Make your bet', prompt='Which Turtle will win the race? Enter a color: ')
    winning_color = ''
    if bet:
        is_race_on = True

    while is_race_on:

        for turtle in turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)

            if turtle.xcor() > 270:
                is_race_on = False
                winning_color = turtle.pencolor()

    if winning_color == bet:
        print(f'You won! The {winning_color} turtle is the winner.')
    else:
        print(f'You won! The {winning_color} turtle is the winner.')

    screen.exitonclick()


class Snake:
    def __init__(self):
        self.STARTING_POSITION = [(-40, 0), (-20, 0), (0, 0)]
        self.RIGHT = 0
        self.UP = 90
        self.LEFT = 180
        self.DOWN = 270

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.score = 0

        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.title("Snake Game")
        self.screen.tracer(0)

        self.screen.listen()
        self.screen.onkey(key='a', fun=self.left)
        self.screen.onkey(key='d', fun=self.right)
        self.screen.onkey(key='w', fun=self.up)
        self.screen.onkey(key='s', fun=self.down)

    def create_snake(self):
        for position in self.STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle('square')
        segment.penup()
        segment.color('white')
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[segment_number - 1].xcor()
            y_pos = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(x_pos, y_pos)
        self.head.forward(20)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)

    def down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)

    def food_collision(self, food):
        if self.head.distance(food) < 15:
            food.refresh()
            self.score += 1
            self.extend()

    def wall_collision(self):
        if self.head.xcor() > 280:
            self.head.goto(-280, self.head.ycor())
        elif self.head.xcor() < -280:
            self.head.goto(280, self.head.ycor())
        elif self.head.ycor() > 280:
            self.head.goto(self.head.xcor(), -280)
        elif self.head.ycor() < -280:
            self.head.goto(self.head.xcor(), 280)

    def tail_collision(self):
        # idk why it doesn't work in the last iteration
        for i in range(1, len(self.segments) - 1):
            if self.head.distance(self.segments[i]) < 10:
                return True
        return False


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.ALIGNMENT = None
        self.FONT = None
        self.scoreboard = None
        self.hideturtle()
        self.penup()
        self.color('white')

    def write_score_snake(self, snake):
        self.ALIGNMENT = 'center'
        self.FONT = ("Courier", 24, "normal")

        self.clear()
        self.goto(0, 270)
        self.scoreboard = snake.score
        self.write(arg=f'Score: {self.scoreboard}', align=self.ALIGNMENT, font=self.FONT)

    def write_score_paddle(self, paddle_R, paddle_L):
        self.ALIGNMENT = 'center'
        self.FONT = ("Courier", 80, "normal")

        self.clear()
        self.goto(-100, 200)
        self.scoreboard = paddle_L.score
        self.write(arg=f'{self.scoreboard}', align=self.ALIGNMENT, font=self.FONT)
        self.goto(100, 200)
        self.scoreboard = paddle_R.score
        self.write(arg=f'{self.scoreboard}', align=self.ALIGNMENT, font=self.FONT)

    def write_gameover(self):
        self.goto(0, 0)
        self.write(arg=f'GAME OVER', align=self.ALIGNMENT, font=self.FONT)


class Paddle(Turtle):
    def __init__(self, position, keys):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.score =0

        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor('black')
        self.screen.title("Pong Game")
        # self.screen.tracer(0)

        self.goto(position)

        self.screen.listen()
        self.screen.onkey(key=keys[0], fun=self.go_up)
        self.screen.onkey(key=keys[1], fun=self.go_down)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 60)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 60)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.x_speed = 10
        self.y_speed = 10
        self.ball_speed = 0.02

    def ball_move(self):
        x_posiiton = self.xcor() + self.x_speed
        y_posiiton = self.ycor() + self.y_speed
        self.goto(x_posiiton, y_posiiton)

    def wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            ball.wall_bounce()

    def wall_bounce(self):
        self.y_speed *= -1

    def paddle_collision(self, paddle):
        if (self.xcor() > 350 or self.xcor() < -350) and self.distance(paddle) <50:
            self.paddle_bounce()

    def paddle_bounce(self):
        self.x_speed *= -1

        if self.ball_speed > 0.001:
            self.ball_speed *= 0.7

    def is_ball_out(self, paddle_R, paddle_L, scoreboard):
        if self.xcor() > 380 and self.distance(paddle_R) > 50:
            paddle_L.score += 1
            scoreboard.write_score_paddle(paddle_R, paddle_L)
            self.ball_speed = 0.02
            self.reset_position()
            return True
        if self.xcor() < -380 and self.distance(paddle_L, scoreboard) > 50:
            paddle_R.score += 1
            scoreboard.write_score_paddle(paddle_R, paddle_L)
            self.ball_speed = 0.02
            self.reset_position()
            return True
        return False

    def reset_position(self):
        self.goto(0, 0)
        self.x_speed *= -1


paddle_R = Paddle(position=(380, 0), keys=('u', 'j'))
paddle_L = Paddle(position=(-380, 0), keys=('r', 'f'))
ball = Ball()
scoreboard = Scoreboard()

scoreboard.write_score_paddle(paddle_L, paddle_R)

is_game_on = True

while is_game_on:
    time.sleep(ball.ball_speed)
    ball.ball_move()
    ball.wall_collision()
    ball.paddle_collision(paddle_R)
    ball.paddle_collision(paddle_L)

    ball.is_ball_out(paddle_R, paddle_L, scoreboard)

    if paddle_R.score == 5:
        is_game_on = False
        scoreboard.write_gameover()
    elif paddle_L.score == 5:
        is_game_on = False
        scoreboard.write_gameover()


paddle_R.screen.exitonclick()





