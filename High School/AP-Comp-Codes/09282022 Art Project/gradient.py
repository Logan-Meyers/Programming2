import turtle as trtl

def hexToRGB(hex):
    return tuple(int(hex[i:i + 2], 16) for i in (1, 3, 5))

def RGBToHex(rgb):
    return f'#{int(rgb[0]):02x}{int(rgb[1]):02x}{int(rgb[2]):02x}'

def makeHexGradient(start, end, steps):
    gradient = []
    baseMultiplier = 1/(steps-1)
    startList = [hexToRGB(start)[0], hexToRGB(start)[1], hexToRGB(start)[2]]
    endList = [hexToRGB(end)[0], hexToRGB(end)[1], hexToRGB(end)[2]]
    
    for step in range(steps):
        nextColor = []
        for val in range(3):
            nextColor.append(round((startList[val]*(1-(baseMultiplier*step)))+(endList[val]*(baseMultiplier*step))))
        gradient.append(RGBToHex(nextColor))
    
    return gradient
        
turtles = []

turtleAmount = 100
steps = 100

trtl.tracer(100)

for i in range(turtleAmount):
    newTurtle = trtl.Turtle()
    newTurtle.hideturtle()
    newTurtle.speed(0)
    newTurtle.pensize(5)
    newTurtle.penup()
    newTurtle.goto(-400, 250-(5*i))
    newTurtle.pendown()
    turtles.append(newTurtle)

trtl.tracer(100)

st1Col = "#ffa62e"
st2Col = "#f00b51"
end1Col = "#f00b51"
end2Col = "#ffcf18"

startColors = makeHexGradient(st1Col, st2Col, turtleAmount)
endColors = makeHexGradient(end1Col, end2Col, turtleAmount)

gradients = []

for i in range(turtleAmount):
    gradients.append(makeHexGradient(startColors[i], endColors[i], steps))

for turtleNum in range(len(turtles)):
    for step in range(steps):
        turtle = turtles[turtleNum]
        turtle.pencolor(gradients[turtleNum][step])
        turtle.forward(5)

trtl.mainloop()