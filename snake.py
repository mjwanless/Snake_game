STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
	def __init__(self):
		self.segments = []
		self.create_snake()


	def create_snake(self):
		for position in starting_positions:
			new_segment = Turtle(shape="square")
			new_segment.color("white")
			new_segment.pu()
			new_segment.goto(position)
			segments.append(new_segment)