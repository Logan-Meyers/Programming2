import turtle as trtl
import random as rand

maze_maker = trtl.Turtle()
maze_maker.pensize(5)
maze_maker.speed(0)

initial_distance = 20
door_width = 20
barrier_height = 40

def draw_door(turtle):
    turtle.penup()
    turtle.forward(door_width)
    turtle.pendown()

def draw_barrier(turtle):
    turtle.left(90)
    turtle.forward(barrier_height)
    turtle.forward(-barrier_height)
    turtle.right(90)

def draw_maze():
    global maze_maker
    maze_maker.clear()
    maze_maker.penup()
    maze_maker.goto(0, 0)
    maze_maker.pendown()
    distance_add = 0
    for _ in range(30):
        maze_maker.left(90)
        
        if distance_add < 6:
            maze_maker.penup()
            maze_maker.forward(initial_distance + (distance_add * 20))
        else:
            maze_maker.pendown()
            path_width = initial_distance
            wall_len = initial_distance + (distance_add * 20)
            dist_gone = 0

            while True:
                door = rand.randint(path_width*2, (wall_len - path_width*2))
                barrier = rand.randint(path_width*2, (wall_len - path_width*2))
                if abs(door-barrier) > door_width:
                    break

            if door < barrier:
                maze_maker.forward(door)
                draw_door(maze_maker)
                dist_gone += door + door_width
                maze_maker.forward(barrier-dist_gone)
                dist_gone += barrier-dist_gone
                draw_barrier(maze_maker)
                maze_maker.forward(wall_len-dist_gone)
            elif barrier < door:
                maze_maker.forward(barrier)
                draw_barrier(maze_maker)
                dist_gone += barrier
                maze_maker.forward(door-dist_gone)
                dist_gone += door-dist_gone
                draw_door(maze_maker)
                dist_gone += door_width
                maze_maker.forward(wall_len-dist_gone)

        distance_add += 1

print("maze finished")

runner_heading = -1
runner_progressing = False
running = True

def get_key_func(key):
    def on_key_press():
        global runner_heading, running, runner_progressing
        if key in "wasd":
            runner_progressing = True
        if key == "w":
            runner_heading = 90
        elif key == "a":
            runner_heading = 180
        elif key == "s":
            runner_heading = 270
        elif key == "d":
            runner_heading = 0
        elif key == "q":
            running = False
        elif key == "r":
            draw_maze()
        elif key == "space":
            runner_progressing = False if runner_progressing else True
    return on_key_press

print("get key funcs made")

runner = trtl.Turtle()

wn = trtl.Screen()

print("runner and wn made")

useable_keys = ["w", "a", "s", "d", "q", "r", "space"]
for key in useable_keys:
    wn.onkeypress(get_key_func(key), key)
wn.listen()

print("on key pressed assigned")
print(running)

def game_loop():
    if runner_progressing:
        runner.setheading(runner_heading)
        runner.forward(5)
    wn.ontimer(game_loop, 10)

draw_maze()
game_loop()

wn.mainloop()
# comment