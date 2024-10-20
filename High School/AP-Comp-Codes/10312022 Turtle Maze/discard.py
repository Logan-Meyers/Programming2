"""
# Pekay's lovely code
segments.append(segment)  # Adds segment to snake body
# this for loop is really smart- yet for some reason I can't get it to work as a whole
# see, I understand that it is supporsed to shift everything over and it SHOULD work (in theory, of course),
# but for some reason somewhere along the process it just
for index in range(len(segments)-1, 0, -1):  # From 0 to total body length
x = segments[index-1].xcor()  # Sets x and y coordinate of snake head/player
y = segments[index-1].ycor()
segments[index].goto(x, y)
if len(segments) > 0:  # Head segment
x = snake.xcor()
y = snake.ycor()
segments[0].goto(x, y)  # Sets the first segment to head
"""

"""
Colors:
Light: #00aa00
Dark:  #005500
"""