#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.speed(0)
    ht.goto(-350, tloc)
    ht.setheading(0)
    ht.speed(0.5)

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.speed(0)
    vt.goto( -tloc, 350)
    vt.setheading(270)
    vt.speed(0.5)

    tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
for step in range(100):
    for turtle_index in range(len(horiz_turtles)):
        horiz_turtles[turtle_index].forward(5)
        vert_turtles[turtle_index].forward(5)
    
    for hori_turt in horiz_turtles:
        for verti_turt in vert_turtles:
            x_diff = abs(hori_turt.xcor() - verti_turt.xcor())
            y_diff = abs(hori_turt.ycor() - verti_turt.ycor())
            if x_diff <= 20 and y_diff <= 20:
                horiz_turtles.remove(hori_turt)
                vert_turtles.remove(verti_turt)
    

wn = trtl.Screen()
wn.mainloop()