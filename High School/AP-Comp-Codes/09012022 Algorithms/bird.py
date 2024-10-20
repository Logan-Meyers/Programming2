import turtle as trtl

painter = trtl.Turtle()

painter.turtlesize(2)
painter.pensize(3)

# rectangle 150x100
painter.forward(150)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(25)
# leg 1
painter.left(110)
painter.forward(75)
painter.back(75)
painter.right(110)
# yup
painter.forward(100)
# leg 2
painter.left(80)
painter.forward(75)
painter.back(75)
painter.right(80)
# yeeeeep
painter.forward(25)
painter.right(90)
painter.forward(100)
# tail
for _ in range(3):
    painter.forward(50)
    painter.back(50)
    painter.left(45)
# head
painter.penup()
painter.left(135)
painter.forward(150)
painter.pendown()
painter.circle(50)
# eye
painter.penup()
painter.left(90)
painter.forward(50)
painter.pendown()
painter.pensize(5)
painter.circle(1)
painter.pensize(2)
# beak
painter.penup()
painter.right(90)
painter.forward(40)
painter.right(45)
painter.forward(15)
painter.pendown()
painter.right(10)
painter.forward(50)
painter.right(140)
painter.forward(50)

wn = trtl.Screen()
wn.mainloop()