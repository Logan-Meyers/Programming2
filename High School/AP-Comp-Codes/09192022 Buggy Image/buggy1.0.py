import turtle as trtl
import random
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()

# draw body
painter.pensize(40)
painter.circle(20)
painter.speed(0)

# leg variable set up
leg_number = 8
leg_length = 70
leg_angle = 360 / leg_number
print("leg angle:", leg_angle)
painter.pensize(5)
curr_leg = 0

# draw legs
while (curr_leg < leg_number):
  painter.goto(0,20)
  # painter.color(colors[curr_leg])
  painter.setheading(leg_angle*curr_leg)
  print("leg #", curr_leg+1, " |  current heading:",(leg_angle*curr_leg))
  painter.forward(leg_length)
  curr_leg = curr_leg + 1

# end
painter.hideturtle()
window = trtl.Screen()
window.mainloop()