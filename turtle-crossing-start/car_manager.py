from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car = Turtle()
        self.car.penup()
        self.car.shape("square")
        self.car.shapesize(stretch_len=2, stretch_wid=1)
        self.car.color(random.choice(COLORS))
        self.car.goto(280, random.randint(-250, 250))
        self.car.setheading(180)
        self.x_move = 5
        self.cars = list()
        self.cars.append(self.car)

    def generate_car(self):
        self.car = Turtle()
        self.car.penup()
        self.car.shape("square")
        self.car.shapesize(stretch_len=2, stretch_wid=1)
        self.car.color(random.choice(COLORS))
        self.car.goto(280, random.randint(-250, 250))
        self.car.setheading(180)
        self.cars.append(self.car)

    def move(self):
        for i in range(len(self.cars)):
            new_x = self.cars[i].xcor() - self.x_move
            self.cars[i].goto(new_x, self.cars[i].ycor())

    def increase_speed(self):
        self.x_move += 10

    # def clear_cars(self):
    #     for car in self.cars:
    #         if car.xcor() < -280:
    #             car.reset()
    #             car.color("white")
    #             self.cars.remove(car)


