from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Snake Game by dani")

#Creating snake and its body
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkeypress(snake.move_up, "w")
screen.onkeypress(snake.move_down, "s")
screen.onkeypress(snake.move_left, "a")
screen.onkeypress(snake.move_right, "d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collisions with food, moving food and changing scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Putting limits on the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    #In case the snake bites it self
    for part in snake.body:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()