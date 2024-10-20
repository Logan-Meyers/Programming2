#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import random

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
# [turtle, original color, original shape, collided?]
coords = []

print(trtl.screensize(400, 400))

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "classic", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.speed(0)
    ht.goto(-350, tloc)
    ht.setheading(0)
    # ht.speed(0.5)
    horiz_turtles.append([ht, new_color, s, False])

    vt = trtl.Turtle(shape=s)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.speed(0)
    vt.goto( -tloc, 350)
    vt.setheading(270)
    # vt.speed(0.5)
    vert_turtles.append([vt, new_color, s, False])

    tloc += 50

print(horiz_turtles)
print(vert_turtles)

# TODO: move turtles across and down screen, stopping for collisions
for step in range(50):
    # get each index in a turtle list
    for turtle_index in range(len(horiz_turtles)):
        # HORIZONTAL- if it is colliding, set color, spin, go
        if horiz_turtles[turtle_index][3]:
            horiz_turtles[turtle_index][0].color("#FF00FF")
            horiz_turtles[turtle_index][0].left(135)
        # else, just move forward
        else:
            horiz_turtles[turtle_index][0].forward(5)
        
        # VERTICAL- if it is colliding, set color, spin, go
        if vert_turtles[turtle_index][3]:
            vert_turtles[turtle_index][0].color("#FF00FF")
            vert_turtles[turtle_index][0].left(135)
        # else, must move forward
        else:
            vert_turtles[turtle_index][0].forward(5)
    
    # check for collisions through each horizontal and vertical
    for hori_turt in horiz_turtles:
        for verti_turt in vert_turtles:
            x_diff = abs(hori_turt[0].xcor() - verti_turt[0].xcor())
            y_diff = abs(hori_turt[0].ycor() - verti_turt[0].ycor())
            if x_diff <= 20 and y_diff <= 20:
                hori_turt[3] = True
                verti_turt[3] = True
            else:
                hori_turt[3] = False
                verti_turt[3] = False

wn = trtl.Screen()
wn.mainloop()