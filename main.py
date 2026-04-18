from turtle import Screen , Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#0B1F14")
screen.title("The Basilisk's Path")
screen.tracer(0)

#   ADDED AN INTRO SCREEN
intro = Turtle()
intro.hideturtle()
intro.penup()
intro.color("#C0C0C0")

intro.write(
    "The Chamber opens...\nGuide the Basilisk\nPress SPACE to begin",
    align="center",
    font=("Georgia", 18, "bold italic")
)

game_started = False

def start_game():
    global game_started
    game_started = True
    intro.clear()

screen.listen()
screen.onkey(start_game, "space")

while not game_started:
    screen.update()

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #   COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        screen.title("The Basilisk Feeds...")
        food.refresh()
        snake.extend_snake()
        score.track_score()

    #   COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset_board()
        snake.reset()
        # game_on = False
        # score.game_over()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 5:
            score.reset_board()
            snake.reset()
            # game_on = False
            # score.game_over()


screen.exitonclick()