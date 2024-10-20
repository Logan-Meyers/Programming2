import turtle as trtl
import random
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()

def goto(x, y):
  painter.penup()
  painter.goto(x, y)
  painter.pendown()

# draw body
painter.pensize(40)
painter.circle(20)
painter.speed(0)

# leg variable set up
leg_number = 8
leg_length = 70
leg_angle = 20
print("leg angle:", leg_angle)
painter.pensize(5)
curr_leg = 0

# draw legs
painter.setheading(-50)
while (curr_leg < leg_number/2):
  painter.goto(0,20)
  painter.setheading(painter.heading()+leg_angle)
  print("leg #", curr_leg+1, " |  current heading:",(leg_angle*curr_leg))
  painter.forward(leg_length)
  painter.left(-15)
  painter.forward(leg_length/2)
  painter.forward(-leg_length/2)
  painter.left(15)
  painter.forward(-leg_length/2)
  curr_leg += 1

painter.setheading(130)
while (curr_leg < leg_number):
  painter.goto(0,20)
  painter.setheading(painter.heading()+leg_angle)
  print("leg #", curr_leg+1, " |  current heading:",(leg_angle*curr_leg))
  painter.forward(leg_length)
  painter.left(15)
  painter.forward(leg_length/2)
  painter.forward(-leg_length/2)
  painter.left(-15)
  painter.forward(-leg_length/2)
  curr_leg += 1

painter.setheading(0)
goto(0, -25)
painter.pensize(40)
painter.circle(10)

# draw eye 1
painter.pensize(5)
painter.pencolor("white")
goto(-12, -30)
painter.circle(5)

# daw eye 2
goto(13, -20)
painter.circle(5)

# draw smile
goto(0, -35)
painter.setheading(0)
painter.forward(7.5)
painter.left(45)
painter.forward(7.5)
painter.hideturtle()

# end
painter.hideturtle()
window = trtl.Screen()
window.mainloop()