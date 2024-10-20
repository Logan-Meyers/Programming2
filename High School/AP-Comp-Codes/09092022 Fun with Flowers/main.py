import turtle as trtl

painter = trtl.Turtle()

painter.speed(-1)

for line in range(4):
    painter.forward(100)
    painter.right(90)

wn = trtl.Screen()
wn.mainloop()