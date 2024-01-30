from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DIST = 5
MOVE_INCREMENT = 10
LEFT = 180


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DIST
        self.car_list = []

    def create_car(self):
        random_no = random.randint(1, 5)
        random_y = random.randint(-230, 265)
        if random_no == 5:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.setheading(LEFT)
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(x=300, y=random_y)
            self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.forward(self.car_speed)
            # To stop off-screen cars from moving/being displayed
            if car.xcor() <= -320:
                car.hideturtle()
                self.car_list.remove(car)

    def speed_up_car(self):
        self.car_speed += MOVE_INCREMENT
