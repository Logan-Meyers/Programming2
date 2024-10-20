import turtle as trtl
painter = trtl.Turtle()
painter.pensize(5)
x, y = -150, -150
for floor in range(63):
    if floor % 21 == 0:
        x += 60
        y = -150
    painter.penup()
    painter.goto(x, y)
    painter.color("blue" if floor % 6 > 3 else "green" if floor % 6 > 1 else "red")
    y += 5
    painter.pendown()
    painter.forward(50)
wn = trtl.Screen()
wn.mainloop()