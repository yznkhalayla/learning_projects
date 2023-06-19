from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.cars_count = len(self.all_cars)
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.level = 1

    def create_car(self):
        random_chance = random.randint(1, 6)

        if random_chance == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(1, 2)
            color = random.choice(COLORS)
            car.color(color)
            car.penup()
            y_position = random.randint(-250, 250)
            car.goto(300, y_position)
            car.setheading(180)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.cars_speed)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT
        self.level += 1