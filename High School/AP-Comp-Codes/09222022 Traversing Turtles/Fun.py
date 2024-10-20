import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# make turtles with a unique shape and add them to the list
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  t.left(90)
  my_turtles.append(t)

# assign a color to each turtle
for i in range(len(turtle_colors)):
    my_turtles[i].color(turtle_colors[i], turtle_colors[i])

#  assign start x/y variables
startx = -100
starty = 0
turtlesDone = 0

# go through each turtle and set them up
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.right(45*turtlesDone)
  t.forward(50)

  # edit the start x/y variables
  startx = t.xcor()
  starty = t.ycor()
  turtlesDone += 1


wn = trtl.Screen()
wn.mainloop()