# Logan- a file with a bunch of useful functions
# to make the main file simpler and cleaner,
# hide away some functions into here
import random
# function for easy drawing perfect square (1 same side len)
def draw_square(turtle, width):
  # (repeat 4 times): forward, right
  for _ in range(4):
    turtle.forward(width)
    turtle.right(90)

# function for easy drawing rectangle
def draw_rect(turtle, width, height):
  # (repeat 2 times): forward, right, forward, right (2 diff side len's)
  for _ in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

# function for computing GCD
def computeGCD(x, y):
  # set small value
  if x > y:
    small = y
  else:
    small = x
  # repeat for every number we can logically divide both by
  for i in range(1, small + 1):
    # if both x and y can be divided by i, set the gcd to i
    if((x % i == 0) and (y % i == 0)):
      gcd = i
      
  # Now, to note: by default, all numbers are divisible by one, so
  # the gcd will be set to 1 every time, on the first iteration.
  # Then, if there are any other possible factors, the 1 will be
  # overridden and replaced with the new factor. This will never
  # not return a number, and gcd will always be 1 by default.
    
  return gcd

# function to easily setup turtle in one line with common things to be set
def setup_turtle(turtle, position=None, heading=None, pensize=None, fg_color=None, bg_color=None):
  # pull pen up if it was before
  if turtle.isdown():
    turtle.penup()
    was_down = True
  # if position is given, set it
  if position:
    turtle.goto(position)
  # if heading is given, set it
  if heading:
    turtle.setheading(heading)
  # if pensize is given, set it
  if pensize:
    turtle.pensize(pensize)
  # set fg and bg colors based on which are given
  if fg_color and bg_color:
    turtle.color(fg_color, bg_color)
  elif fg_color:
    turtle.color(fg_color, turtle.color()[1])
  elif bg_color:
    turtle.color(turtle.color()[0], bg_color)
  # put pen back down if it was up before
  if was_down:
    turtle.pendown()


# Pekay - Function to move apple to a random square
def move_apple(apple, width, height):
  # 19 x 9 is squares in the screen
  x = [] # Lists of x y coordinates
  y = []
  
  hor_squares = width / 19 # All the horizontal squares
  ver_squares = height / 9 # All the vertical squares
  
  # Horizontal locations
  for hor_steps in range(int(hor_squares - 5), int(width - 5)):
    x.append(hor_steps)
  # Vertical locations
  for ver_steps in range(int(ver_squares - 5), int(height- 5)):
    y.append(ver_steps)

  # Random coordinates with the subtraction moving the apple to negative coordinates
  rand_x = random.choice(x) - width/2
  rand_y = random.choice(y) - height/2

  # Sends apple to random location
  apple.goto(rand_x, rand_y)

# Pekay- Checks the x coordinate of the snake and apple to see if their locations matches, returns true or false for main file
def x_check(apple, snake):
  # if apple.xcor() - 25 == snake.xcor() - 25: # Checks coordinates
  if (snake.xcor() < apple.xcor() < snake.xcor()):
    return True
  else:
    return False
# Pekay- Checks the y coordinate of the snake and apple to see if their locations matches, returns true or false for main file
def y_check(apple, snake):
  # if apple.ycor() - 25 == snake.ycor() -25 : # Checks coordinates
  if (snake.ycor() < apple.ycor() < snake.ycor()):
    return True
  else:
    return False