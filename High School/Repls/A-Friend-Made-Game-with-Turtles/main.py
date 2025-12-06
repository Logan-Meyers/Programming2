"""
GAME OUTLINE:
Game to make: 
  - snek game <---- <---- <---- (best choice)
General outline of playthrough/game features:
  - Turtle player moves with wasd/arrow keys
  - Randomly generated apples or other fruit
    * once an apple is consumed, a new one spawns
      in a random spot
  - Changes asthetics from the normal snake game
    * different snake color
    * different fruits (as opposed to the normal apple)
    * different background + border colors
  - Stuck in box, if hits border game over
  - box (game space) changes size based on size of window
  - As turtle consumes froot it becomes bigger
    * Add to body length
    * If turtle hits itself game ends
"""
import turtle as trtl
import functions as fcs

alphabet = ["w", "a", "s", "d", "Up", "Down", "Left", "Right", "e"]  # List for keyboard functions

screen = trtl.Screen()  # Sets up screen

game_start = False

score = 0

# Turtle that counts score and its aesthetics
font_setup = ("Time", 20, "italic")
score_writer = trtl.Turtle()
score_writer.color('red')
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(-300,180)


# Code for a start play button and it's aesthetics
play_button = trtl.Turtle()
play_button.color('red')
play_button.shape('triangle')
play_button.turtlesize(2)

# code for collectible apple
apple = trtl.Turtle()  # Turtle for apple
apple.color("#00aa00")
apple.goto(50,60)
apple.penup() # Apple won't draw as it moves

# code for background drawing
background_turtle = trtl.Turtle()  # Turtle for background drawing

# code for player snake head
snake = trtl.Turtle()  # Turtle for snake that player guides & aesthetics
snake.shape('circle')
snake.color('lightblue')
snake.penup()
snake.hideturtle() # Hidden until game starts

# code for additional snake segments
segment = trtl.Turtle() # Turtle for body segment and aesthetics
segment.shape('circle')
segment.color('lightblue')
segment.penup()
segments = [] # List for all body segments of the snake

# code for snake movement stuff
next_heading = 0
segments_to_add = 0

# window and screen stuff
window_dimensions = [610, 310]  # initial dimensions to set the window to
grid_division_amount = 6  # amount to divide up the screen by
checker_grid_size = 0
game_loop_timer_delay = 20


#---Functions---#
# Logan- function to set window size
def set_window_size(w, h):
  # get the canvas from turutle and then get the tkinter root
  canvas = trtl.getcanvas()
  root = canvas.winfo_toplevel()
  # set window size in the "wxh" format (tkinter function)
  wh = str(w) + "x" + str(h)
  root.geometry(wh)

# Logan- window dimension information
class win_dims:
  # obvious
  width = window_dimensions[0]
  height = window_dimensions[1]
  # outer pixel value of the limits of the screen,
  # in the x-y plane with (0, 0) at the middle
  # of the screen (turtle default) as opposed to top-left with pygame
  left = (-width / 2)
  right = (width / 2) - 10
  top = (height / 2)
  bottom = (-height / 2) + 10
  # wid and hi of insides based on the arbituary pensize values when making the border.
  # used for apple position generating
  inside_width = width-40
  inside_height = height-40

# Logan- colors used for drawing background
class game_colors:
  light = "#00aa00"
  dark = "#006600"
  darker = "#005500"
  darkest = "#000000"

# Logan- function that draw the border and background
def draw_background(turtle):
  global checker_grid_size
  # move the turtle to the top-left corner of the screen,
  # does some more set-up
  trtl.tracer(False)
  # move turtle to top-left to start, set some other values
  fcs.setup_turtle(turtle, position=[win_dims.left, win_dims.top], pensize=30, fg_color=game_colors.darker)
  # some variables used to define where/how big to draw
  rect_width = int(-win_dims.left + win_dims.right)
  rect_height = int(win_dims.top + (-win_dims.bottom))
  # draw outer border rectangle
  fcs.draw_rect(turtle, rect_width, rect_height)

  # move turtle to new top-left position, set some other values
  fcs.setup_turtle(turtle, position=[win_dims.left + 15, win_dims.top - 15], pensize=5, fg_color=game_colors.darkest)
  # shrink drawing area
  rect_width -= 30
  rect_height -= 30
  # draw inner black border
  fcs.draw_rect(turtle, rect_width, rect_height)

  # calculate largest possible square size based off of drawable area
  gridSize = fcs.computeGCD(rect_width, rect_height)
  print(rect_width, rect_height, gridSize)  # debugging
  # calculate how many squares to draw in each direction
  grids_w = int(rect_width / gridSize)
  grids_h = int(rect_height / gridSize)
  # setup turtle values
  fcs.setup_turtle(turtle, heading=0, pensize=1)

  # variable to manage switching colors
  square_num = 1
  for h in range(grids_h):  #  for each row
    for w in range(grids_w):  # for each column
      if square_num % 2 == 0:  # even, light
          turtle.color(game_colors.light, game_colors.light)
      else:  # odd, dark
          turtle.color(game_colors.dark, game_colors.dark)
      # move turtle to top-left corner of new grid/checker square
      fcs.setup_turtle(turtle, position=[win_dims.left + 15 + (w * gridSize), win_dims.top - 15 - (h * gridSize)])
      # start fill, draw square, end fill, increment color-switching-variable
      turtle.begin_fill()
      fcs.draw_square(turtle, gridSize)
      turtle.end_fill()
      square_num += 1

  trtl.tracer(True)
  # set global variable for future reference in the program
  checker_grid_size = gridSize
  background_turtle.hideturtle()

# Pekay- function that is for play button
def start_button(x,y):
  global game_start
  play_button.hideturtle() # Hides play button on click
  game_start = True
  
# Pekay/Logan- Function for player controls. Nested inside is function for keypresses, made by Logan
def player():
  # Function for keypress
  def get_func(letter):
    def draw_letter():
      #print(letter)
      while True:
        # Moves player turtle with WASD
        if letter == 'w' or letter == "Up":  # Moves player forward
          if snake.heading() != 270:
            snake.setheading(90)
        elif letter == 's' or letter == "Down":  # Moves player backward
          if snake.heading() != 90:
            snake.setheading(270)
        elif letter == 'd' or letter == "Right":  # Moves player right
          if snake.heading() != 180:
            snake.setheading(0)
        elif letter == 'a' or letter == "Left":  # Moves player left
          if snake.heading() != 0:
            snake.setheading(180)
        elif letter == "e":  # debugging- spawn new segments
          global segments_to_add
          segments_to_add = 5
        
        if letter in alphabet:
          break
            
    return draw_letter

  # for each letter meant to be pressed, have turtle listen for them and its corrosponding method
  for letter in alphabet:
    screen.onkeypress(get_func(letter), letter)
  screen.listen()
  
# Pekay- Function that sets apple turtle as apple 
# image.
def draw_apple(apple, screen):
  red_apple = 'red_apple_.gif'  # Image used for apple
  # Adds to screen
  screen.addshape(red_apple)
  apple.shape(red_apple)  # Sets turtle to shape
  screen.update

# Pekay/Logan, function that creates/shifts segments of snake body
def shift_segments(new_segment=False):
  global segments, segment
  # set prior position to snake position
  prior_position = (snake.xcor(), snake.ycor())
  # for every segment currently in the segments list, shift it over
  for segment in segments:
    current_position = (segment.xcor(), segment.ycor())  # set current_position to where current segment position
    segment.goto(prior_position[0], prior_position[1])  # have current segment go to the position of the last segment
    prior_position = current_position  # set the last segment position to the position of the current segment

  # if we need to add a segment to our list:
  if new_segment:
    segments.append(segment.clone())  # make a clone of the segment turtle and append it to the list
    segments[-1].goto(prior_position)  # move that new segment to the last position

  # P.S.: There are DEFINITELY some flaws with this algorithm, and some improvements to be made

# Logan- crude way of checking border hitting
def snake_hit_border(snake):
  # x-position
  if (snake.xcor() < -win_dims.inside_width/2) or (snake.xcor() > win_dims.inside_width/2):
    return True
    print("Hit border!")
  # y-position
  if (snake.ycor() < -win_dims.inside_height/2) or (snake.ycor() > win_dims.inside_height/2):
    return True
    print("Hit border!")
  return False

def snake_hit_self(snake, segments):
  bubble = 1
  for segment in segments:
    # x-position
    if (snake.xcor() - bubble < segment.xcor() < snake.xcor() + bubble):
      # y-position
      if (snake.ycor() - bubble < segment.ycor() < snake.ycor() + bubble):
        return True  # return true if they're too close
        print("Hit self!")
  return False
  
# Pekay/Logan: main game loop
def game_loop():
  trtl.tracer(False)  # stop automatic updating
  global snake, segments_to_add, score

  # Checks to see if the play button has been pressed;
  # until then, continue to update the screen
  while True: 
    screen.update()
    play_button.onclick(start_button) # Starts game when clicked
    if game_start == True: # Shows the snake 
      snake.showturtle()  # show the main turtle
      apple.showturtle()
      break  # break the infinite loop

  # if the snake has hit the border, break out of the loop function
  if snake_hit_border(snake) or snake_hit_self(snake, segments):
    print("Exit")
    return -1
    
  # for every iteration of the main loop:
  # - shift over snake segments
  # - move the main snake forward
  # - draw apple and check for collecting, then move if necessary
  # - update screen and call game loop after a certain delay
  shift_segments(new_segment=segments_to_add)
  segments_to_add -= 1 if segments_to_add > 0 else 0  # subs 1 from to_add if it's more than 0
  draw_apple(apple,screen)
  snake.forward(3)

  # Checks functions that evaluate close xy coordinates, of the apple and snake, that return True if they match
  if fcs.x_check(apple,snake) == True and fcs.y_check(apple,snake) == True:
    fcs.move_apple(apple, win_dims.inside_width, win_dims.inside_height) # Moves apple
    # Code for the score counter
    score += 1
    score_writer.clear()
    score_writer.goto(-300,180)
    score_writer.write('Score: ' + str(score), font = font_setup)
    segments_to_add = 5  # adds segments
  screen.update()
  screen.ontimer(game_loop, game_loop_timer_delay)
  
#---Function Calls---#
trtl.tracer(False)
segment.goto(500, 500)

set_window_size(window_dimensions[0], window_dimensions[1])
draw_background(background_turtle)
player()

game_loop()
screen.mainloop()
