######################################################################
# Turtle                                                             #
# Austin U, Joseph T, Logan M, Dylan H, Cassius B                    #
#                                                                    #
# Arrow keys to move, F to f, and Z, P, X, C, V, B, and N to do secrets #
######################################################################
# imports
import turtle as t
import random
# painter/window setup    Courtesy of Austin U
painter = t.Turtle()
painter.home()
painter.pendown()
painter.speed(100)
wn = t.Screen()
# rainbow color data   Courtesy of Joseph T
colors = [(255, 0, 0),(255, 6, 0),(255, 12, 0),(255, 18, 0),(255, 25, 0),(255, 31, 0),(255, 37, 0),(255, 43, 0),(255, 50, 0),(255, 56, 0),(255, 62, 0),(255, 68, 0),(255, 75, 0),(255, 81, 0),(255, 87, 0),(255, 93, 0),(255, 100, 0),(255, 106, 0),(255, 112, 0),(255, 118, 0),(255, 125, 0),(255, 131, 0),(255, 137, 0),(255, 143, 0),(255, 150, 0),(255, 156, 0),(255, 162, 0),(255, 168, 0),(255, 175, 0),(255, 181, 0),(255, 187, 0),(255, 193, 0),(255, 200, 0),(255, 206, 0),(255, 212, 0),(255, 218, 0),(255, 225, 0),(255, 231, 0),(255, 237, 0),(255, 243, 0),(255, 255, 0),(237, 255, 0),(225, 255, 0),(212, 255, 0),(200, 255, 0),(187, 255, 0),(175, 255, 0),(162, 255, 0),(150, 255, 0),(137, 255, 0),(125, 255, 0),(112, 255, 0),(100, 255, 0),(87, 255, 0),(75, 255, 0),(62, 255, 0),(50, 255, 0),(37, 255, 0),(25, 255, 0),(12, 255, 0),(0, 255, 0),(0, 237, 12),(0, 225, 25),(0, 212, 37),(0, 200, 50),(0, 187, 62),(0, 175, 75),(0, 162, 87),(0, 150, 100),(0, 137, 112),(0, 125, 125),(0, 112, 137),(0, 100, 150),(0, 87, 162),(0, 75, 175),(0, 62, 187),(0, 50, 200),(0, 37, 212),(0, 25, 225),(0, 12, 237),(0, 0, 255),(12, 0, 255),(25, 0, 255),(37, 0, 255),(50, 0, 255),(62, 0, 255),(75, 0, 255),(87, 0, 255),(100, 0, 255),(112, 0, 255),(125, 0, 255),(137, 0, 255),(150, 0, 255),(162, 0, 255),(175, 0, 255),(187, 0, 255),(200, 0, 255),(212, 0, 255),(225, 0, 255),(237, 0, 255)]
# motion controls - Courtesy of Austin U
def forward():
  painter.forward(50)
  print("went forward")
def right():
  painter.right(90)
  print("turned right")
def left():
  painter.left(90)
  print("turned left")
def turn_around():
  painter.right(180)
def smoothRight():   # Courtesy of Joseph T
  for _ in range(90):
    painter.forward(0.872663889)
    painter.right(1)
  print('turned right smoothly')
def smoothLeft():   # Courtesy of Joseph T
  for _ in range(90):
    painter.forward(0.872663889)
    painter.left(1)
  print('turned left smoothly')
# changing color functions - Courtesy of Joseph T
def color_blue():
	painter.color('blue')
	print('changed color to blue')
def color_red():
	painter.color('red')
	print('changed color to red')
def color_yellow():
  painter.color('gold')
  print('changed color to yellow')
def color_green():
  painter.color('green')
  print('changed color to green')
def color_black():
	painter.color('black')
	print('changed color to black')
def color_white():
  painter.color('white')
  print("changed color to white")
# draw circle function - Courtesy of Logan M
def draw_circle():# painter.circle() does this too
  for null in range(360):
    painter.forward(0.872663889)
    painter.right(1)
  print('drew a circle with a 100-pixel diameter')
# Equation: C = pi*diameter ... 3.14159*100, then / 360 for a full 360 degrees of... drawing-ness? =D It's rounded, but still super close
# pen up and down function - Courtesy of Logan M
def penToggle():
	if painter.isdown():# runs if the pen is down
		painter.up()
		print('set pen to up')
	else:
		painter.down()
		print('set pen to down')
#draws a star - Courtesy of Joseph T
def star():
	painter.up()
	painter.forward(100)
	painter.right(5)
	painter.down()
	for _ in range(0,36,1):
		painter.right(170)
		painter.forward(99)
	painter.left(5)
# draws a 3D square - Courtesy of Logan M
def square3d():
	# moveList structure: (forward_amount, turn_amount (degrees left))
	moveList = [(50, 90), (50, 90), (50, 90), (50, 135), (35.355339, -45), 
	  			    (50, 90), (50, 90), (50, 90), (50, 135), (70.7106781, -135), 
		  		    (50, -45), (35.355339, 180), (35.355339, 45), (50, 90), 
              (50, 45), (35.355339, 0)]
	beginning_coords = painter.pos()
	beginning_heading = painter.heading()
	for smallList in moveList:
		painter.forward(smallList[0])
		painter.left(smallList[1])
	painter.goto(beginning_coords)
	painter.setheading(beginning_heading)
# draws a swirl - Courtesy of Joseph T
def swirly():
  for i in range(60):
    painter.right(6)
    painter.forward(i/6)
# draws a randomized spirograph - Courtesy of Joseph T
def triSwirl():
	painter.speed(1000)
	angle = random.randint(90, 270)
	curve = random.randint(-45,45)
	intensity = random.randint(1,10)
	decay = random.randint(-5,5)
	for i in range(0,1000):
		index = int(i/10)
		color = colors[index]
		painter.color(color)
		painter.right(angle)
		decayCurve = decay
		for n in range(intensity):
			painter.forward(i/intensity)
			painter.right(decayCurve)
			decayCurve = decayCurve - decay
# draws a basic spirograph - Courtesy of Joseph T
def spirograph():
	painter.speed(500)
	for i in range(36):
		index = int(i*2.77777778)
		color = colors[index]
		painter.color(color)
		painter.circle(50)
		painter.right(10)
	painter.speed(100)
# draws an f
def F():#painter.setheading(90) will point the painter north
  painter.setheading(90)
  painter.speed(250)
  painter.forward(75)
  painter.right(90)
  painter.forward(50)
  painter.right(180)
  painter.forward(50)
  painter.right(90)
  painter.forward(50)
  painter.right(90)
  painter.forward(70)
# does something
def Poop():  # someone was working on this...
  painter.setheading(90)
  painter.forward(100)
  painter.right(90)
  painter.circle(-28,180)
  painter.left(90)
  painter.forward(44)
  painter.left(90)
  painter.up()
  painter.forward(80)
  painter.down()
  painter.circle(40)
  painter.up()
  painter.forward(90)
  painter.down()
  painter.circle(40)
  painter.up()
  painter.forward(80)
  painter.down()
  painter.left(90)
  painter.forward(100)
  painter.right(90)
  painter.circle(-28,180)
  painter.left(90)
  painter.forward(44)
  painter.up()
  painter.left(90)
  painter.forward(30)
  painter.down()
  painter.forward(5)
  painter.left(90)
  painter.forward(5)
  painter.left(90)
  painter.forward(5)
  painter.left(90)
  painter.forward(5)
  painter.left(90)
  painter.forward(5)
  print('POOP')
  
def w():#This is for anybody to work on#
	pass
# clears the screen and centers the cursor   Courtesy of Joseph T
def reset():
	painter.reset()
	painter.speed(100)
  

def leftish():
  painter.left(45)

def rightish():
  painter.right(45)

def moreforward():
  painter.forward(70)
# motion controls
wn.onkey(forward, 'Up')
wn.onkey(right, 'Right')
wn.onkey(left, 'Left')
wn.onkey(turn_around, 'Down')
wn.onkey(smoothRight, 'e')
wn.onkey(smoothLeft, 'q')
wn.onkey(leftish, 'u')
wn.onkey(rightish, 'i')
wn.onkey(moreforward, 'l')
# when num keys are pressed, pen color is changed
wn.onkey(color_blue, "1")
wn.onkey(color_red, "2")
wn.onkey(color_yellow, "3")
wn.onkey(color_green, "4")
wn.onkey(color_black, "5")
wn.onkey(color_white, "6")
# pressing space sets the pen up/down to the opposite.
wn.onkey(penToggle, 'space')
# other
wn.onkey(draw_circle, 'z')
wn.onkey(star, 'x')
wn.onkey(swirly, 'c')
wn.onkey(square3d, 'v')
wn.onkey(triSwirl, 'b')
wn.onkey(spirograph, 'n')
wn.onkey(F, 'f')
wn.onkey(Poop, 'p')
wn.onkey(reset, 'r')

wn.listen()
wn.mainloop()