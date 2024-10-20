import turtle as trtl

import functions as funcs

# screen is about 800 x 750 pixels
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 750
GRID_WIDTH = 400
GRID_HEIGHT = 750

def gridToScreen(gridCoords, offset):
    x = -GRID_WIDTH+(gridCoords[0]*rectSize)+offset[0]
    y = GRID_HEIGHT/2-(gridCoords[1]*rectSize)+offset[1]
    return (x, y)

###

# initial setup
setupPainter = trtl.Turtle()
setupPainter.speed(0)
setupPainter.penup()
setupPainter.goto(-400, 375)
setupPainter.color("#000000", "#cccccc")
setupPainter.pensize(4)
setupPainter.pendown()
funcs.rectangle(setupPainter, 400, 750, fill=True)
setupPainter.penup()
setupPainter.forward(400)
setupPainter.pendown()
funcs.rectangle(setupPainter, 400, 750)

rectSize = 50
# grid total 8x15

blueSquareCoords = [(2, 2), (7, 1), (2, 8), (5,11), (1, 14)]
greySquareCoords = [(4, 0), (1, 1), (2, 1), (4, 1), (6, 1), (1, 2), (4, 2), (6, 2), (1, 3), (3, 3), (4, 3), (6, 3), (1, 4), (6, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (1, 6), (1, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (1, 8), (6, 8), (7, 8), (2, 9), (3, 9), (6, 9), (7, 9), (0, 10), (3, 10), (5, 10), (6, 10), (7, 10), (0, 11), (1, 11), (3, 11), (6, 11), (7, 11), (3, 12), (4, 12), (7, 12), (0, 13), (1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (7, 13), (0, 14), (7, 14)]

oldTracer = trtl.tracer()
trtl.tracer(10)

for horizontalLine in range(int(GRID_WIDTH/rectSize)-1):
    setupPainter.penup()
    setupPainter.goto(-GRID_WIDTH+(horizontalLine*rectSize)+rectSize, GRID_HEIGHT/2)
    setupPainter.setheading(270)
    setupPainter.pendown()
    setupPainter.forward(GRID_HEIGHT)

for verticalLine in range(int(GRID_HEIGHT/rectSize)-1):
    setupPainter.penup()
    setupPainter.goto(-GRID_WIDTH, GRID_HEIGHT/2-(verticalLine*rectSize)-rectSize)
    setupPainter.setheading(0)
    setupPainter.pendown()
    setupPainter.forward(GRID_WIDTH)

for coord in greySquareCoords:
    setupPainter.penup()
    setupPainter.goto(-GRID_WIDTH+(coord[0]*rectSize), GRID_HEIGHT/2-(coord[1]*rectSize))
    setupPainter.fillcolor("#333333")
    setupPainter.pendown()
    funcs.rectangle(setupPainter, rectSize, rectSize, fill=True)

for coord in blueSquareCoords:
    setupPainter.penup()
    setupPainter.goto(-GRID_WIDTH+(coord[0]*rectSize), GRID_HEIGHT/2-(coord[1]*rectSize))
    setupPainter.fillcolor("#00c3ff")
    setupPainter.pendown()
    funcs.rectangle(setupPainter, rectSize, rectSize, fill=True)

setupPainter.hideturtle()

### Set up blue turtles
blueTurtleTemp = trtl.Turtle()
blueTurtleTemp.speed(0)
blueTurtleTemp.color("black", "#3477ff")
blueTurtleTemp.left(45)
blueTurtleTemp.shape("square")
blueTurtleTemp.penup()
blueTurtle1 = blueTurtleTemp.clone()
blueTurtle1.goto(gridToScreen(blueSquareCoords[0], (rectSize/2, -rectSize/2)))
blueTurtle2 = blueTurtleTemp.clone()
blueTurtle2.goto(gridToScreen(blueSquareCoords[1], (rectSize/2, -rectSize/2)))
blueTurtle3 = blueTurtleTemp.clone()
blueTurtle3.goto(gridToScreen(blueSquareCoords[2], (rectSize/2, -rectSize/2)))
blueTurtle4 = blueTurtleTemp.clone()
blueTurtle4.goto(gridToScreen(blueSquareCoords[3], (rectSize/2, -rectSize/2)))
blueTurtle5 = blueTurtleTemp.clone()
blueTurtle5.goto(gridToScreen(blueSquareCoords[4], (rectSize/2, -rectSize/2)))
blueTurtleTemp.goto(100000, 0)

### Set up maze runner

mazeRunner = trtl.Turtle()
mazeRunner.shape("triangle")
mazeRunner.color("#000000", "#dd1111")
mazeRunner.penup()
mazeRunner.speed(0)
# mazeRunner.goto(-GRID_WIDTH-rectSize, GRID_HEIGHT/2-(12*rectSize))
mazeRunner.goto(-425, -250)
mazeRunner.speed(0)
mrGridCoord = (-1, 12)
print(mrGridCoord)
beenToCoords = []

startYN = input("Start exploration? (y/n)?\n$ ").lower()
if startYN == "n":
    quit()
print("Ok, let's start the Maze Runner!")

trtl.tracer(1)

xStartGradient = None
xEndGradient = None
yStartGradient = None
yEndGradient = None

while True:
    mazeRunner.forward(rectSize)
    mrGridCoord = funcs.calcNewGridCoord(mazeRunner, mrGridCoord)
    if (mrGridCoord in greySquareCoords) or (mrGridCoord in beenToCoords) or funcs.isOutsideBorders(mazeRunner.heading(), mrGridCoord, GRID_WIDTH/rectSize, GRID_HEIGHT/rectSize):
        mazeRunner.back(rectSize)
        mrGridCoord = funcs.calcNewGridCoord(mazeRunner, mrGridCoord, back=True)
        mazeRunner.right(90)
    beenToCoords.append(mrGridCoord)
    mazeRunner.dot()
    
    if (abs(mazeRunner.xcor() - blueTurtle1.xcor())<25) and (abs(mazeRunner.ycor() - blueTurtle1.ycor())<25):
        if not xStartGradient:
            xStartGradient = input("Enter a color: ")
        trtl.tracer(5)
    if (abs(mazeRunner.xcor() - blueTurtle2.xcor())<25) and (abs(mazeRunner.ycor() - blueTurtle2.ycor())<25):
        if not xEndGradient:
            xEndGradient = input("Enter a color: ")
    if (abs(mazeRunner.xcor() - blueTurtle3.xcor())<25) and (abs(mazeRunner.ycor() - blueTurtle3.ycor())<25):
        if not yStartGradient:
            yStartGradient = input("Enter a color: ")
    if (abs(mazeRunner.xcor() - blueTurtle4.xcor())<25) and (abs(mazeRunner.ycor() - blueTurtle4.ycor())<25):
        if not yEndGradient:
            yEndGradient = input("Enter a color: ")
    if (abs(mazeRunner.xcor() - blueTurtle5.xcor())<25) and (abs(mazeRunner.ycor() - blueTurtle5.ycor())<25):
        break
    # print(beenToCoords)
    
###

trtl.tracer(1000)

someColors = {
    "red":        "#ff0000",
    "orange":     "#ff7700",
    "yellow":     "#ffe800",
    "green":      "#00ca20",
    "lightgreen": "#00ff00",
    "blue":       "#0000ff",
    "lightblue":  "#00a0ff",
    "cyan":       "#00ffff",
    "purple":     "#a200ff",
    "pink":       "#ff00dd",
    "white":      "#ffffff",
    "black":      "#000000",
    "grey":       "#777777"
}

xPainter = trtl.Turtle()
xPainter.penup()
xPainter.pensize(4)
xPainter.ht()
xPainter.goto(1.5, (GRID_HEIGHT/2)-1.5)
#xGradient = funcs.makeHexGradient(someColors[xStartGradient], someColors[xEndGradient], GRID_WIDTH)

steps = int((GRID_HEIGHT)/4)
leftGradient = funcs.makeHexGradient(someColors[xStartGradient], someColors[xEndGradient], steps)
rightGradient = funcs.makeHexGradient(someColors[yStartGradient], someColors[yEndGradient], steps)

gradients = []

for yPixel in range(len(leftGradient)):
    gradients.append(funcs.makeHexGradient(leftGradient[yPixel], rightGradient[yPixel], int((GRID_WIDTH-3)/4)))

for yPixel in range(len(leftGradient)):
    xPainter.pendown()
    for xPixel in range(len(gradients[yPixel])):
        xPainter.color(gradients[yPixel][xPixel])
        xPainter.forward(4)
    xPainter.penup()
    xPainter.goto(1.5, xPainter.ycor()-4)

###

setupPainter.penup()
setupPainter.goto(0, 0)
trtl.mainloop()