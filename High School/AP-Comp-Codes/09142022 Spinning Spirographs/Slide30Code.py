import turtle as trtl
painter = trtl.Turtle()

"""
###############################################################################
# Slide 30

import turtle as trtl
color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
width = 400
height = 300

painter.speed(0)
painter.color(color1)
painter.shape("circle")
painter.turtlesize(0.33)

answer = "y"
while (answer == "y"):
  wn.clearscreen()  
  painter.goto(0,0)
  space = 1

  angle = int(input("angle:"))
  seg = int(360/angle)

  totalSpaces = 0
  
  while painter.ycor() < height:
    if painter.pencolor() == color2:
        painter.fillcolor(color1)
        painter.color(color1)
    else:
        painter.fillcolor(color2)
        painter.color(color2)
    painter.right(angle)
    painter.forward(2 * space + 10) # experiment
    totalSpaces += (2 * space + 10)
    print(totalSpaces, totalSpaces % 100)
    painter.stamp()
    space = space + 1

  answer = input("again?")

wn.bye()"""


#######################################################################
## Slide 32
painter.penup()
painter.goto(-200, 0)
painter.pendown()
painter.speed(0)
x = -200
y = 0
move_x = 1
move_y = 1
while (x < 200):
    while (y < 100):
        x = x + move_x
        y = y + move_y
        painter.goto(x,y)
        print(move_y, move_x)
    move_y = -1
    while (y > 0):
        x = x + move_x
        y = y + move_y
        painter.goto(x,y)
        print(move_y, move_x)
    move_y = 1

move_y = -1
move_x = -1

while (x > -200):
    while (y > -100):
        x = x + move_x
        y = y + move_y
        painter.goto(x,y)
        print(move_y, move_x)
    move_y = 1
    while (y < 0):
        x = x + move_x
        y = y + move_y
        painter.goto(x,y)
        print(move_y, move_x)
    move_y = -1

def doDiamond(move_x, move_y, size=100):
    currPos = painter.pos()
    


wn = trtl.Screen()
wn.mainloop()