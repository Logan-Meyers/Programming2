import turtle as trtl

bug = trtl.Turtle()
bug.speed(0)
bug.pensize(3)
bug.color("black", "#3C54BC")

bug.begin_fill()
bug.circle(150, 345)
bug.end_fill()

bug.left(90)
bug.color("white", "white")
bug.pensize(0)
bug.begin_fill()
bug.forward(150)
bug.left(180+(360-345))
bug.forward(160)
bug.end_fill()

bug.pensize(3)

num_spirals = 19
current_spiral = 0
spiral_angle_space = 345/num_spirals

bug.color("black", "#0492C2")

while current_spiral <= num_spirals:
    bug.penup()
    bug.goto(0, 150)
    bug.pendown()
    bug.setheading(-90 + (spiral_angle_space * current_spiral) + 10)
    if current_spiral != 0:
        bug.color("black", "#0492C2")
    else:
        bug.color("black", "white")
    bug.begin_fill()
    bug.forward(76)
    bug.left(-20)
    bug.forward(75)
    bug.end_fill()
    current_spiral += 1

bug.penup()
bug.left(180)
bug.forward(10)
bug.left(-135)
bug.pendown()
bug.forward(10)
bug.forward(-10)
bug.penup()
bug.left(135)
bug.forward(10)
bug.left(-45)
bug.pendown()
bug.forward(10)
bug.forward(-10)
bug.penup()

window = trtl.Screen()
window.mainloop()