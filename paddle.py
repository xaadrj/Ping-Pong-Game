from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(coordinate)
        self.shapesize(5, 1)
        self.shape("square")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move(self, key1, key2):
        screen.onkeypress(self.move_up, key1)
        screen.onkeypress(self.move_down, key2)
