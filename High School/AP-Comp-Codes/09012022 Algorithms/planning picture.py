# import Turtle module
import turtle as trtl
import random as rnd

# colors = ["red", "orange", "yellow", "green", "blue", "pink", "purple", "black"]
# colors = ["red", "green", "blue"]
colors = ["red", "white", "black"]

turtles = []
for i in range(180):
    turtles.append(trtl.Turtle())

col = 0
for trt in turtles:
    # trt.pencolor(rnd.choice(colors))
    trt.pencolor(colors[col])
    # print(col)
    trt.speed(50)
    trt.pensize(2)

    col += 1
    if col == len(colors):
        col = 0

for i in range(len(turtles)):
    turtles[i].left((360/len(turtles))*i)

for i in range(10):
    for trt in turtles:
        trt.forward(25)
        trt.left(20)

# get the screen object and make it persistent
wn = trtl.Screen()
wn.mainloop()