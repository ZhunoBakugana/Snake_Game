from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

score = Scoreboard()
snake = Snake()
food = Food()
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() >280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        snake.remove_parts()
        score.highest()

    for parts in snake.snake_body[2:]:
        if snake.head.distance(parts) < 10:

            snake.remove_parts()
            score.highest()

screen.exitonclick()
