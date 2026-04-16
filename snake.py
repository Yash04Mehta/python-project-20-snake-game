from turtle import Turtle

MOVE_FORWARD = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        x = 0
        for _ in range(3):
            body = Turtle(shape="square")
            body.color("white")
            body.penup()
            body.goto(x, 0)
            x -= 20
            self.snake.append(body)


    def move(self):
        for item in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[item - 1].xcor()
            new_y = self.snake[item - 1].ycor()
            self.snake[item].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)