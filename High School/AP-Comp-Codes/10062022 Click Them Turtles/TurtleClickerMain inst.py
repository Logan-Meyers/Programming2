#-----import statements-----
import turtle as trtl
import random, gradient

#-----game configuration----
spot_color = "pink"
spot_size = 3
spot_shape = "circle"
score = 0

score_writer = trtl.Turtle()
font_setup = ("Arial", 30, "normal")
score_writer.penup()
score_writer.speed(0)
score_writer.goto(-325, 262.5)

def draw_rect(painter, x, y, wid, hi):
    painter.speed(0)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()
    for _ in range(2):
        painter.forward(wid)
        painter.left(90)
        painter.forward(hi)
        painter.left(90)

border_painter = trtl.Turtle()
border_painter.pensize(5)
draw_rect(border_painter, -400, 300, 800, -600)
border_painter.ht()

box_painter = trtl.Turtle()
box_painter.pensize(2)
box_painter.color("#000000", "#eeeeee")
draw_rect(box_painter, -400, 300, 150, -75)
draw_rect(box_painter, 250, 300, 150, -75)
box_painter.ht()

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter = trtl.Turtle()
counter.penup()
counter.speed(0)
counter.goto(260, 250)

#-----initialize turtle-----
spot = trtl.Turtle()
spot.color(spot_color)
spot.turtlesize(spot_size)
spot.shape(spot_shape)

#-----game functions--------
def update_score():
    global score, score_writer, font_setup
    score += 1
    score_writer.clear()
    score_writer.goto(-390, 250)
    score_writer.write("Score: " + str(score), font=font_setup)

def change_position():
    new_x = random.randint(-400, 400)
    new_y = random.randint(-300, 300)
    spot.goto(new_x, new_y)

def spot_clicked(x, y):
    global timer_up, spot
    if not timer_up:
        change_position()
        update_score()
    else:
        spot.ht()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()

## spot.onclick