from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Snake Game by dani")

#creating snake and its body
snake = Snake()

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
    screen.listen()

















screen.exitonclick()