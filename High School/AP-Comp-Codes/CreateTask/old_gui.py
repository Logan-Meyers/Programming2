

if isinstance(aaa, int):
    self.aaa = lambda : aaa
elif isinstance(aaa, Callable):
    self.aaa = lambda : aaa()


class TextInputBox:
    def __init__(self, pos: list, fontSize: int, font: str="-1", content="", minWidth: int=100, padding: int=3, isActive: bool=False):
        self.pos = pos
        self.minWidth = minWidth
        self.padding = padding
        self.content = content
        self.active = isActive
        self.highlighted = False
        self.collisionBox = pygame.Rect(0, 0, 0, 0)
        self.reliantText = ReliantText(self.getContentStr, consts.TEXT_BOX.TEXT, [self.pos[0]+self.padding*2, self.pos[1]+self.padding*2], fontSize, font)

        self.updateCollisionBox(self.reliantText.renderText().get_rect())
    
    def updateCollisionBox(self, textRect):
        width = max(self.minWidth, (textRect.width+(self.padding*4)))
        height = max(self.reliantText.fontSize, (textRect.height+(self.padding*2)))
        self.collisionBox = pygame.Rect(self.pos[0], self.pos[1], width, height)

    def getContentStr(self):
        return self.content

    def handleEvents(self, pygameEvents):
        # mouse events handled in update

        for event in pygameEvents:
            # check for non-text keypresses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # set content to itself except for the last character
                    if self.active:
                        self.content = self.content[:-1]
            # otherwise check for text input
            if event.type == pygame.TEXTINPUT:
                # get and add unicode of event to self content, if active
                if self.active:
                    self.content += event.text

    def update(self):
        textRect = self.reliantText.renderText().get_rect()
        mouse_pos = pygame.mouse.get_pos()

        self.updateCollisionBox(textRect)
        
        self.highlighted = False
        # mouse clicked, update activity if colliding
        if (pygame.mouse.get_pressed()[0]):
            if (self.collisionBox.collidepoint(mouse_pos[0], mouse_pos[1])):
                self.active = True
            else:
                self.active = False
        # else update highlight if mouse hovering
        else:
            if (self.collisionBox.collidepoint(mouse_pos[0], mouse_pos[1])):
                self.highlighted = True

    def draw(self, surface):
        # define a background color based on whether highlighted or active
        if (self.highlighted):
            bgColor = consts.TEXT_BOX.BG_HIGHLIGHT
        else:
            bgColor = consts.TEXT_BOX.BG

        if (self.active):
            borderColor = consts.TEXT_BOX.BORDER_ACTIVE
        else:
            borderColor = consts.TEXT_BOX.BORDER

        # draw border rect
        pygame.draw.rect(surface, borderColor, (self.pos[0], self.pos[1], self.collisionBox.width, self.collisionBox.height), border_radius=10)
        # draw inside rect
        pygame.draw.rect(surface, bgColor, (self.pos[0]+self.padding, self.pos[1]+self.padding, self.collisionBox.width-(self.padding*2), self.collisionBox.height-(self.padding*2)), border_radius=10)
        # draw text
        self.reliantText.draw(surface)

class HBorder:
    def __init__(self, yPos: int, thickness: int=2, draggable: bool=True, dragRegionThickness: int=4):
        self.yPos = yPos
        self.thickness = thickness
        self.draggable = draggable
        self.dragRegionTol = dragRegionThickness
        self.beingDragged = False
    
    def getYPosInt(self):
        return self.yPos

    def handleEvents(self, pygameEvents):
        # exit if cannot be dragged- nothing to do
        if not self.draggable:
            return
        
        for event in pygameEvents:
            # check if mouse button pressed down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if left click
                if (pygame.mouse.get_pressed()[0]):
                    # get mouse pos
                    mousePos = pygame.mouse.get_pos()
                    # define some y positions for readability
                    topAllowed = self.yPos - (self.thickness / 2) - self.dragRegionTol
                    bottomAllowed = self.yPos + (self.thickness / 2) + self.dragRegionTol
                    # is in region? if so set being dragged
                    if (topAllowed < mousePos[1] < bottomAllowed):
                        self.beingDragged = True
            # check if mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                # check if no more left click
                if (not pygame.mouse.get_pressed()[0]):
                    self.beingDragged = False

    def update(self):
        # get mouse pos
        mousePos = pygame.mouse.get_pos()
        # if being dragged, change pos
        if (self.beingDragged):
            self.yPos = mousePos[1]
            
    def draw(self, surface):
        pygame.draw.rect(surface, consts.BORDER.BG, (0, self.yPos, surface.get_size()[0], self.thickness))

class HSlider:
    def __init__(self, pos: list, width: int, height: int, minVal: int, maxVal: int, startVal: int, showValueAsText: bool=False):
        self.pos = pos
        self.width = width
        self.height = height
        self.minVal = minVal
        self.maxVal = maxVal
        self.valRange = abs(minVal) + abs(maxVal)
        self.currentVal = startVal
        self.mouseDragging = False
        # self.mouseOffset = (0, 0)
    
    # calc : value from position
    # set : position from mouse pos (constrain)
    # set : position from percent (scale, set pos)

    # get : percent from value
    # get : current value

    def getValueAsStr(self):
        return str(self.currentVal)

    def getPercentFromValue(self):
        # leftPos = self.pos[0] + (self.height / 2)
        # rightPos = self.pos[0] + (self.width - (self.height / 2))
        
        # posRange = rightPos - leftPos
        # xPosAdjusted = self.currXPos - leftPos
        # percent = xPosAdjusted / posRange
        # return percent
        percent = self.currentVal / self.valRange
        return percent

    def setValueFromMousePosition(self, mousePos):
        # define some constraints and bounds for x position of mouse
        leftMax = self.pos[0] + (self.height / 2)
        rightMax = self.pos[0] + (self.width - (self.height / 2))

        # cap/constrain new x based on before defined bounds
        if (mousePos[0] < leftMax):
            newX = leftMax
        elif (mousePos[0] > rightMax):
            newX = rightMax
        else:
            newX = mousePos[0]
        
        # calculate value based on where new x is in relation to other self values
        posRange = rightMax - leftMax
        newXPosAdjusted = newX - leftMax
        percent = newXPosAdjusted / posRange
        self.currentVal = self.valRange * percent

    def getBarRect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)

    def getCircleRect(self):
        valuePercent = self.getPercentFromValue()
        left = self.pos[0] + ((self.width - self.height) * valuePercent)  # - (self.height / 2)
        top = self.pos[1]
        right = left + self.height
        bottom = self.pos[0] + self.height
        return pygame.Rect(left, top, self.height, self.height)

    def handleEvents(self, pygameEvents):
        for event in pygameEvents:
            # check for mouse button down
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check for left click
                if (pygame.mouse.get_pressed()[0]):
                    mousePos = pygame.mouse.get_pos()
                    # check for collision on either bar or circle rects
                    if (self.getBarRect().collidepoint(mousePos[0], mousePos[1])):
                        self.mouseDragging = True
                    if (self.getCircleRect().collidepoint(mousePos[0], mousePos[1])):
                        self.mouseDragging = True
            # check for mouse button release/up
            if event.type == pygame.MOUSEBUTTONUP:
                # check for no more left click
                if (not pygame.mouse.get_pressed()[0]):
                    # disable self dragging
                    self.mouseDragging = False
    
    def update(self):
        # update positions based on mouse position if mouse is dragging
        if (self.mouseDragging):
            self.setValueFromMousePosition(pygame.mouse.get_pos())
            
    def draw(self, surface):
        # draw the bar then the circle rect
        pygame.draw.rect(surface, consts.SLIDER.BORDER, self.getBarRect())
        pygame.draw.rect(surface, consts.SLIDER.CIRCLE_BG, self.getCircleRect())

class MusicGrid:
    def __init__(self, posGetter, widthGetter, heightGetter, rows: int, columns: int, squareSize: int, rowColors: list, rowNoteLetters: list):
        self.posGetter = posGetter
        self.widthGetter = widthGetter
        self.heightGetter = heightGetter
        self.columns = columns
        self.rows = rows
        self.squareSize = squareSize
        self.rowColors = rowColors
        self.rowNoteLetters = rowNoteLetters
        self.noteSquares = []
        self.mouseSetAction = 1
        self.mouseClicked = False

        self.resetNoteGrid()
    
    def resetNoteGrid(self, newState=0):
        self.noteSquares = arr = [[newState for i in range(self.columns)] for j in range(self.rows)]
    
    def fillNoteGrid(self, newState):
        for row in range(len(self.noteSquares)):
            for col in range(len(self.noteSquares[row])):
                self.noteSquares[row][col] = newState

    def getPositionsAtNote(self, row, col):
        left = self.posGetter()[0]
        top = self.posGetter()[1]
        squareTop = top + (self.squareSize * row)
        squareBottom = squareTop + self.squareSize
        squareLeft = left + (self.squareSize * col)
        squareRight = squareLeft + self.squareSize
        
        return {
            "left": left,
            "top": top,
            "squareLeft": squareLeft,
            "squareTop": squareTop,
            "squareBottom": squareBottom,
            "squareRight": squareRight
        }

    def getRowColAtPos(self, mousePos):
        for row in range(len(self.noteSquares)):
            for col in range(len(self.noteSquares[row])):
                # get poses to check with later
                poses = self.getPositionsAtNote(row, col)
                # check x direction
                if (poses["squareLeft"] < mousePos[0] < poses["squareRight"]):
                    # check y direction
                    if (poses["squareTop"] < mousePos[1] < poses["squareBottom"]):
                        # return row and column
                        return (row, col)
        
        return (-1, -1)
        
    def getNoteAtPosState(self, mousePos):
        row, col = self.getRowColAtPos(mousePos)
        return self.noteSquares[row][col]
    
    def setNoteAtPosState(self, mousePos, targetState):
        row, col = self.getRowColAtPos(mousePos)
        if ((row == -1) and (col == -1)):
            return
        self.noteSquares[row][col] = targetState
    
    def flipState(self, currentState):
        if currentState == 1:
            return 0
        return 1

    def handleEvents(self, pygameEvents):
        for event in pygameEvents:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                if ((self.posGetter()[0] < mousePos[0] < self.posGetter()[0] + (self.rows * self.squareSize)) and (self.posGetter()[1] < mousePos[1] < self.posGetter()[1] + (self.columns * self.squareSize))):
                    if (pygame.mouse.get_pressed()[0]):
                        self.mouseClicked = True
                        currentState = self.getNoteAtPosState(mousePos)
                        newState = self.flipState(currentState)
                        self.mouseSetAction = newState
                        print("started mouse clicked")
            if (event.type == pygame.MOUSEBUTTONUP):
                if (not pygame.mouse.get_pressed()[0]):
                    self.mouseClicked = False

    def update(self):
        ### update square values if clicked
        # if mouse clicked?
        if (self.mouseClicked):
            self.setNoteAtPosState(pygame.mouse.get_pos(), self.mouseSetAction)

    def draw(self, surface):
        left, top = self.posGetter()
        width = self.widthGetter()
        height = self.heightGetter()

        # draw each square
        for row in range(len(self.noteSquares)):
            for col in range(len(self.noteSquares[row])):
                squareTop = top + (self.squareSize * row)
                squareLeft = left + (self.squareSize * col)

                if ((squareLeft > width) or (squareTop > height)):
                    continue

                # draw black border
                pygame.draw.rect(surface, (0, 0, 0), (squareLeft, squareTop, self.squareSize, self.squareSize))
                # if activated? draw colorful
                if (self.noteSquares[row][col]) == 1:
                    pygame.draw.rect(surface, self.rowColors[row%len(self.rowColors)], (squareLeft+1, squareTop+1, self.squareSize-2, self.squareSize-2))
                # else dark
                else:
                    pygame.draw.rect(surface, (50, 50, 50), (squareLeft+1, squareTop+1, self.squareSize-2, self.squareSize-2))

class NotesGrid:
    def __init__(self, pos: Tuple[int, int] | Coord2D, width: int | Callable, height: int | Callable, noteRows: int, noteColumns: int, squareSize: int, rowColors: list, rowNoteLetters: list):
        if isinstance(pos, tuple):
            self.pos = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()

        if isinstance(width, int):
            self.width = lambda: width
        elif isinstance(width, Callable):
            self.width = lambda : width()
        
        if isinstance(height, int):
            self.height = lambda : height
        elif isinstance(height, Callable):
            self.height = lambda : height()
        
        self.noteRows = noteRows
        self.noteColumns = noteColumns
        self.squareSize = squareSize
        self.rowColors = rowColors
        self.rowNoteLetters = rowNoteLetters

        self.noteSquares = []
        self.mouseSetAction = 1
        self.mouseClicked = False

        self.resetNoteGrid()
    
    def resetNoteGrid(self, newState=0):
        self.noteSquares = [[newState for row in range(self.noteRows)] for col in range(self.noteColumns)]
        
    def fillNoteGrid(self, newState):
        for col in range(len(self.noteSquares)):
            for row in range(len(self.noteSquares[col])):
                self.noteSquares[col][row] = newState
    


    def getRowColAtPos(self, mousePos):
        for col in range(len(self.noteSquares)):
            for row in range(len(self.noteSquares[col])):
                # get poses to check with later
                poses = self.getPositionsAtNote(col, row)
                # check x direction
                if (poses["squareLeft"] < mousePos[0] < poses["squareRight"]):
                    # check y direction
                    if (poses["squareTop"] < mousePos[1] < poses["squareBottom"]):
                        # return row and column
                        return (row, col)
        
        return (-1, -1)

    def getNoteAtPosState(self, mousePos):
        row, col = self.getRowColAtPos(mousePos)
        return self.noteSquares[col][row]

    def setNoteAtPosState(self, mousePos, targetState):
        row, col = self.getRowColAtPos(mousePos)
        if ((row == -1) and (col == -1)):
            return
        self.noteSquares[col][row] = targetState

    def flipState(self, currentState):
        if currentState == 1:
            return 0
        return 1

    def handleEvents(self, pygameEvents):
        for event in pygameEvents:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mousePos = pygame.mouse.get_pos()
                if ((self.pos()[0] < mousePos[0] < self.pos()[0] + (self.noteColumns * self.squareSize)) and (self.pos()[1] < mousePos[1] < self.pos()[1] + (self.noteRows * self.squareSize))):
                    if (pygame.mouse.get_pressed()[0]):
                        self.mouseClicked = True
                        currentState = self.getNoteAtPosState(mousePos)
                        newState = self.flipState(currentState)
                        self.mouseSetAction = newState
                        print("started mouse clicked")
            if (event.type == pygame.MOUSEBUTTONUP):
                if (not pygame.mouse.get_pressed()[0]):
                    self.mouseClicked = False

    def update(self):
        ### update square values if clicked
        # if mouse clicked?
        if (self.mouseClicked):
            self.setNoteAtPosState(pygame.mouse.get_pos(), self.mouseSetAction)

    def draw(self, surface):
        left, top = self.pos()
        width = self.width()
        height = self.height()

        # draw each square
        for col in range(len(self.noteSquares)):
            for row in range(len(self.noteSquares[col])):
                squareTop = top + (self.squareSize * row)
                squareLeft = left + (self.squareSize * col)

                if ((squareLeft > width) or (squareTop > height)):
                    continue

                # draw black border
                pygame.draw.rect(surface, (0, 0, 0), (squareLeft, squareTop, self.squareSize, self.squareSize))
                # if activated? draw colorful
                if (self.noteSquares[col][row]) == 1:
                    pygame.draw.rect(surface, self.rowColors[row%len(self.rowColors)], (squareLeft+1, squareTop+1, self.squareSize-2, self.squareSize-2))
                # else dark
                else:
                    pygame.draw.rect(surface, (50, 50, 50), (squareLeft+1, squareTop+1, self.squareSize-2, self.squareSize-2))