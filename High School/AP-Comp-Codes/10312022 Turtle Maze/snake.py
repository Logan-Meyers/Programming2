import turtle as trtl


snake = trtl.Turtle()

segment = trtl.Turtle()
segments = []

screen = trtl.Screen()
new_segment_next = False

alphabet = "wasde"

def player():
  #Function for keypress
  def get_func(letter):

    def draw_letter():
        print(letter)
        while True:
          #Moves player turtle with WASD
          if letter == 'w':  #Moves player forward
            if snake.heading() != 270:
              snake.setheading(90)
          elif letter == 's':  #Moves player backward
            if snake.heading() != 90:
              snake.setheading(270)
          elif letter == 'd':  #Moves player right
            if snake.heading() != 180:
              snake.setheading(0)
          elif letter == 'a':  #Moves player left
            if snake.heading() != 0:
              snake.setheading(180)
          elif letter == "e":
            global new_segment_next
            new_segment_next = True
          
          if letter in "wasde":
            break
            
    return draw_letter

  for letter in alphabet:
    screen.onkeypress(get_func(letter), letter)
  screen.listen()

def move_segments(new_segment=False):
  global segments
  if len(segments) > 0:
    last_x, last_y = (segments[-1].xcor(), segments[-1].ycor()) if new_segment else (None, None)
    print(last_x, last_y)
    for index in range(len(segments)-1, 0, -1):
      new_x = segments[index-1].xcor()
      new_y = segments[index-1].ycor()
      segments[index].goto(new_x, new_y)
    segments[0].goto(snake.xcor(), snake.ycor())
    if new_segment:
      segments.append(segment)
      segments[-1].goto(last_x, last_ys)
  else:
    if new_segment:
      segments.append(segment)
      segments[-1].goto(snake.xcor(), snake.ycor())
  

def add_segment():
  pass

def gameLoop():
    global snake, new_segment_next
    trtl.tracer(False)
    move_segments(new_segment=new_segment_next)
    new_segment_next = False
    snake.forward(2)
    print(len(segments))
    screen.update()
    screen.ontimer(gameLoop, 20)

player()
gameLoop()
screen.mainloop()
