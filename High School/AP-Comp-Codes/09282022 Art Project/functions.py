import turtle as trtl

def rectangle(painter, width, height, fill=False):
    painter.setheading(0)
    if fill:
        painter.begin_fill()
    if width == height:
        for _ in range(4):
            painter.forward(width)
            painter.right(90)
    else:
        for _ in range(2):
            painter.forward(width)
            painter.right(90)
            painter.forward(height)
            painter.right(90)
    if fill:
        painter.end_fill()

def calcNewGridCoord(painter, oldCoords, back=False):
    if back:
        backFactor = -1
    else:
        backFactor = 1
    heading = painter.heading()
    newCoords = [oldCoords[0], oldCoords[1]]
    if heading == 0:
        newCoords[0] += 1 * backFactor
    elif heading == 180:
        newCoords[0] -= 1 * backFactor
    elif heading == 90:
        newCoords[1] -= 1 * backFactor
    elif heading == 270:
        newCoords[1] += 1 * backFactor
    print(newCoords)
    return (newCoords[0], newCoords[1])

def isOutsideBorders(heading, coords, gridW, gridY):
    if (heading == 0) and (coords[0] == gridW):
        return True
    if (heading == 180) and (coords[0] == -1):
        return True
    if (heading == 90) and (coords[1] == -1):
        return True
    if (heading == 270) and (coords[1] == gridY):
        return True

### Code for handling hex and rgb colors, along with gradients

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