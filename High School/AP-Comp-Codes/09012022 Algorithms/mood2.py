import turtle as trtl

painter = trtl.Turtle()
painter.pensize(10)

def draw(mood, xoffset=0):
    painter.pencolor("green" if mood == "happy" else "orange" if mood == "meh" else "red" if mood == "sad" else "blue")

    painter.penup()
    painter.goto(-50+xoffset, 100)
    painter.pendown()
    painter.right(90)
    painter.forward(150)

    painter.penup()
    painter.goto(50+xoffset, 100)
    painter.pendown()
    painter.forward(150)

    painter.penup()
    if mood in ["happy", "meh", "unstable"]:
        painter.goto(-125+xoffset, -100)
    else:
        painter.goto(125+xoffset, -136.61)
    painter.pendown()

    if mood == "happy":
        painter.left(45)
        painter.circle(176.8, 90)
    elif mood == "meh":
        painter.left(90)
        painter.forward(250)
    elif mood == "sad":
        painter.right(135)
        painter.circle(176.8, 90)
    elif mood == "unstable":
        painter.left(45)
        for _ in range(8):
            painter.forward(22.097)
            painter.left(90)
            painter.forward(22.097)
            painter.right(90)

draw("happy")
painter.setheading(0)
draw("meh", 10)
painter.setheading(0)
draw("sad", 20)
painter.setheading(0)
draw("unstable", 30)

wn = trtl.Screen()
wn.mainloop()