from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
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
        self.head.setheading(0)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body = Turtle(shape="square")
        body.color("#1A472A")
        body.penup()
        body.goto(position)
        self.snake.append(body)

    def extend_snake(self):
        self.add_segment(self.snake[-1].position())

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