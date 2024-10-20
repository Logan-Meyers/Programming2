#-----import statements-----
import turtle as trtl
import random, gradient
import leaderboard as lb

#-----game classes----------
class Cookie:
    def __init__(self):
      self.OUTERSIZE = 6
      self.INNERSIZE = 5
      self.CHOCOSIZE = 1
      self.init_turtles()
      self.intendedPosition = (0, 0)
      self.sizeMod = 1
      self.move_shapes()
    
    def change_position(self):
      new_x = random.randint(-400, 400)
      new_y = random.randint(-300, 300)
      self.intendedPosition = (new_x, new_y)
      self.handle_size_mod(new_position=True)
      self.move_shapes()
    
    def handle_size_mod(self, new_position=False):
      if new_position:
        self.sizeMod = 1
      else:
        self.sizeMod -= 0.05 if self.sizeMod > 0.3 else 0

    def init_turtles(self):
      self.outerTrtl = trtl.Turtle()
      self.outerTrtl.shape("circle")
      self.outerTrtl.turtlesize(self.OUTERSIZE, self.OUTERSIZE)
      self.outerTrtl.color("#000000", "#d67d00")
      self.outerTrtl.speed(0)
      self.outerTrtl.penup()
      self.innerTrtl = self.outerTrtl.clone()
      self.innerTrtl.color("#bf7000", "#bf7000")
      self.innerTrtl.turtlesize(self.INNERSIZE, self.INNERSIZE)
      self.chocoTrtl1 = trtl.Turtle()
      self.chocoTrtl1.shape("circle")
      self.chocoTrtl1.turtlesize(self.CHOCOSIZE, self.CHOCOSIZE)
      self.chocoTrtl1.color("#4A2B00", "#4A2B00")
      self.chocoTrtl1.speed(0)
      self.chocoTrtl1.penup()
      self.chocoTrtl2 = self.chocoTrtl1.clone()
      self.chocoTrtl3 = self.chocoTrtl2.clone()

    def change_turtle_sizes(self):
      self.outerTrtl.turtlesize(self.OUTERSIZE*self.sizeMod, self.OUTERSIZE*self.sizeMod)
      self.innerTrtl.turtlesize(self.INNERSIZE*self.sizeMod, self.INNERSIZE*self.sizeMod)
      self.chocoTrtl1.turtlesize(self.CHOCOSIZE*self.sizeMod, self.CHOCOSIZE*self.sizeMod)
      self.chocoTrtl2.turtlesize(self.CHOCOSIZE*self.sizeMod, self.CHOCOSIZE*self.sizeMod)
      self.chocoTrtl3.turtlesize(self.CHOCOSIZE*self.sizeMod, self.CHOCOSIZE*self.sizeMod)
      self.move_shapes()

    def move_shapes(self):
      self.outerTrtl.goto(self.intendedPosition)
      self.innerTrtl.goto(self.intendedPosition)
      self.chocoTrtl1.goto(self.intendedPosition[0] + (27*self.sizeMod), self.intendedPosition[1] + (27*self.sizeMod))
      self.chocoTrtl2.goto(self.intendedPosition[0] + (15*self.sizeMod), self.intendedPosition[1] - (18*self.sizeMod))
      self.chocoTrtl3.goto(self.intendedPosition[0] - (27*self.sizeMod), self.intendedPosition[1] - (9*self.sizeMod))
    
    def hide_turtles(self):
      self.outerTrtl.ht()
      self.innerTrtl.ht()
      self.chocoTrtl1.ht()
      self.chocoTrtl2.ht()
      self.chocoTrtl3.ht()
    
    def set_clicked_funcs(self, func):
      self.outerTrtl.onclick(func)
      self.innerTrtl.onclick(func)
      self.chocoTrtl1.onclick(func)
      self.chocoTrtl2.onclick(func)
      self.chocoTrtl3.onclick(func)

#-----game configuration----
leaderboard_file_name = "LEADERBOARD.txt"
player_name = input("Please enter your name here:\n$ ")

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

def setup_field():
  trtl.tracer(15)

  bg_painter = trtl.Turtle()
  # 600px / 10 = 60 shades
  bg_painter.pensize(10)
  bg_painter.speed(0)
  bg_painter.penup()
  bg_painter.goto(-395, 295)
  bg_top_color = "#00beff"
  bg_bottom_color = "#DEF7FF"
  bg_gradient = gradient.makeHexGradient(bg_top_color, bg_bottom_color, 60)
  for color in bg_gradient:
      bg_painter.color(color)
      bg_painter.pendown()
      bg_painter.forward(795)
      bg_painter.penup()
      bg_painter.goto(-395, bg_painter.ycor()-10)
  bg_painter.ht()

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

  trtl.tracer(1)
  
setup_field()

score = 0

score_writer = trtl.Turtle()
font_setup = ("Arial", 30, "normal")
score_writer.penup()
score_writer.speed(0)
score_writer.goto(-325, 262.5)

timer = 15
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter = trtl.Turtle()
counter.penup()
counter.speed(0)
counter.goto(260, 250)

#-----initialize turtle-----
cookie = Cookie()

#-----game functions--------
def update_score():
    global score, score_writer, font_setup
    score += 1
    score_writer.clear()
    score_writer.goto(-390, 250)
    score_writer.write("Score: " + str(score), font=font_setup)

def spot_clicked(x, y):
    global timer_up, spot
    cookie.change_position()
    update_score()

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0 or cookie.sizeMod <= 0.3:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def shrink_handler():
  cookie.handle_size_mod()
  cookie.change_turtle_sizes()
  counter.getscreen().ontimer(shrink_handler, 250)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  global score
  global cookie

  cookie.hide_turtles()

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  leaderboard_turtle = trtl.Turtle()
  leaderboard_turtle.speed(0)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, leaderboard_turtle, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, leaderboard_turtle, score)

#-----events----------------
cookie.set_clicked_funcs(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.ontimer(shrink_handler, 250)
wn.mainloop()

# two files
# - all data
# - top 5 sorted
