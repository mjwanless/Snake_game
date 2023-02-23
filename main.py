from turtle import Screen, Turtle
import time

# Setup of screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")

# segment list for building the snake out

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
	new_segment = Turtle(shape="square")
	new_segment.color("white")
	new_segment.pu()
	new_segment.goto(position)
	segments.append(new_segment)

# Running code

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.1)

	for seg_num in range((len(segments)-1), 0, -1):
		new_x = segments[(seg_num - 1)].xcor()
		new_y = segments[(seg_num - 1)].ycor()
		segments[seg_num].goto(new_x, new_y)

	segments[0].forward(20)

# Needed for screen close out at end

screen.exitonclick()
