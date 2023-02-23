from turtle import Screen, Turtle
from snake import Snake
import time

# Setup of screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

# Running codeS

snake = Snake()

# Keypresses
screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.1)

	snake.move()

# Needed for screen close out at end

screen.exitonclick()
