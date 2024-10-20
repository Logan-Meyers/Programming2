import turtle as trtl;
painter = trtl.Turtle()
painter.pensize(5)

painter.penup()
painter.goto(-150, -150)
painter.pendown()

# circle code
painter.circle(100)

# move
painter.penup()
painter.goto(-150, 150)
painter.pendown()

# arc code
painter.circle(100, 135)

# move
painter.penup()
painter.goto(150, 150)
painter.pendown()

# arc >90deg 5 steps
painter.circle(100, 91, 5)

# move
painter.penup()
painter.goto(150, -150)
painter.pendown()

# polygon
painter.circle(100, 360, 12)

wn = trtl.Screen()
wn.mainloop()