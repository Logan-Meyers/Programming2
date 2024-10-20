import turtle as trtl

# modify with your two favorite colors
color1 = "red"
color1_5 = "darkred"
color2 = "black"

wn = trtl.Screen()
height = 350 # the radius of the shape

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)
painter.pensize(2)
wn.screensize(800, 800)

space = 1
angle = 50 # experiment with the shape
seg = int(360/angle)

while (painter.ycor() < height):
  if (space % 6 == 0):
    painter.fillcolor(color1)
    painter.color(color1)
  else: # elif (space % 5 != 1):
    painter.fillcolor(color2)
    painter.color(color2)

  painter.right(angle)
  painter.forward(2*space) # experiment
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()
  space += 1

wn.mainloop()