import random

# Pekay - Function to move apple to a random square
def move_apple(apple, width, height):
  # 19 x 9 is squares in the screen
  x = [] # Lists of x y coordinates
  y = []
  
  hor_squares = width / 19 # All the horizontal squares
  ver_squares = height / 9 # All the Vertical squares
  
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