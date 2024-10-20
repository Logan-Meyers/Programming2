import turtle as trtl

painter = trtl.Turtle()

sides = 5
angle = 360/sides

currentSide = 0

while currentSide != sides:
    painter.forward(50)
    painter.right(angle)
    currentSide += 1

wn = trtl.Screen()
wn.mainloop()
