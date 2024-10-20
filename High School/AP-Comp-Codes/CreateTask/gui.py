import pygame
import constants as consts
import WaveAndSounds as waves
from typing import (Callable, Tuple, Any)
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import threading



###  ----- FUTURE GUI IMPROVEMENT IDEAS LIST    -----  ###
#
#  * 1.  overload inits
#  * 2.  allow more modularity with variable values
#  - 3.  add various QoL improvements such as base functions for user to use
#  * 4.  make custom class for coordinates/vectors/positions?
#  * 5.  make custom class for dynamic values that change over time
#  - 6.  make custom classes for counters, timers, etc?
#  * 7.  add docstrings to classes
#  - 8.  add more error handling and isinstance(other) 'ing
#    9.  make dynamic variable handling simpler
#
###  ----- FUTURE PROGAM IMPROVEMENT IDEAS LIST -----  ###
#
#    1.  add labels for notes
#    2.  make sharp and flat notes the same
#    3.  make scrollbars scroll on mouse scroll
#    4.  be able to loop song
#  - 5.  be able to load/save song
#    6.  add darker/thicker seperating lines for beat and octave seperation
#    7.  add longer note
#    8.  harmonize notes
#    9.  add layers
#
###  -----          TO BE IMPROVED ON!          -----  ###

### GENRAL ARGUMENT ORDER:
#   pos, width, height, colors, text, to call, other special

### Special data-tracking-or-holding classes

class Font:
    '''Make a font! Takes in font name, font size, and color

        Parameters:
            fontName (str): name of the font
            fontSize (int): size of the font
            color (list): the colors, in rgb values, for of the text
    '''
    def __init__(self, fontName: str, fontSize: int, color: list[int]):
        self.fontName = fontName
        self.fontSize = fontSize
        self.color = color
        self.initFont()
    
    def default():
        '''Return an object of Font that serves as a "default" font'''
        return Font(pygame.font.get_default_font(), 16, [0, 0, 0])

    def initFont(self):
        '''Load a font from PyGame'''
        self.pyFont = pygame.font.SysFont(self.fontName, self.fontSize)
    
    def render(self, content: str):
        '''Render and return and image, with the content as text, to be blit'd'''
        return self.pyFont.render(content, True, self.color)

class Coord2D:
    '''Make a 2D coordinate! Used to hold either a static int for x and y, or lambdas for dynamic x-and-y-getters
    
        Parameters:
            x (int or Callable): value for x
            y (int or Callable): value for y
            marginX (int): optional margin value for x
            marginY (int): optional margin value for y'''
    
    def __init__(self, x: int | Callable, y: int | Callable, marginX: int=0, marginY: int=0):
        # setup self values by calling self's set method
        self.set(x, y, marginX, marginY)

    def set(self, x: int | Callable, y: int | Callable, marginX: int=0, marginY: int=0):
        '''Setup the Coord2D object
    
        Parameters:
            x (int or Callable): value for x
            y (int or Callable): value for y
            marginX (int): optional margin value for x
            marginY (int): optional margin value for x'''
        
        # set margins
        self.marginX = marginX
        self.marginY = marginY
        
        # set x and y value lambdas based on whether an int or callable is passed in
        if isinstance(x, Callable):
            self.xGetter = lambda : x() + self.marginX
        else:
            self.xGetter = lambda : x + self.marginX
        
        if isinstance(y, Callable):
            self.yGetter = lambda : y() + self.marginY
        else:
            self.yGetter = lambda : y + self.marginY

    def get(self):
        '''Get the (x, y) values of the Coord2D'''
        return (self.xGetter(), self.yGetter())

### Simple shapes

class SimpleRect:
    '''A simple rectangle to draw over anything you need drawn over
    
        Parameters:
            pos (Tuple[int, int], Coord2D): the top-left position for the rectangle
            width (int, Callable): the width for the rectangle
            height (int, Callable): the height for the rectangle
            color (list): the rgb values for the color for the rectangle'''
    
    def __init__(self, pos: Tuple[int, int] | Coord2D, width: int | Callable, height: int | Callable, color: list[int] | tuple[int, int, int]):
        # assign position
        if isinstance(pos, Tuple):
            self.posGetter = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.posGetter = lambda : pos.get()
        
        # assign width
        if isinstance(width, int):
            self.widthGetter = lambda : width
        elif isinstance(width, Callable):
            self.widthGetter = lambda : width()
        
        # assign height
        if isinstance(height, int):
            self.heightGetter = lambda : height
        elif isinstance(height, Callable):
            self.heightGetter = lambda : height()
        
        # assign colors
        self.color = color

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # draw rectangle
        pygame.draw.rect(surface, self.color, (self.posGetter()[0], self.posGetter()[1], self.widthGetter(), self.heightGetter()))

### Text

class Text:
    '''Make some text to put on screen! Takes in 3 simple arguments
    
        Parameters:
            pos (tuple or coord2D): top-left position for text
            content (any): text to write out to the screen
            font (Font): font for text'''
    
    def __init__(self, pos: Tuple[int, int] | Coord2D, content: Any | Callable, font: Font):
        # set pos
        if isinstance(pos, tuple):
            self.pos = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
        
        # set content
        if isinstance(content, Callable):
            self.content = lambda : content()
        else:
            self.content = lambda : str(content)
        
        # set font obj
        self.font = font
    
    def getTextImg(self):
        '''Render and return the image of the text, rendered'''
        return self.font.render(self.content())

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # get rendrered image
        textImg = self.getTextImg()
        # blit image to surface
        surface.blit(textImg, self.pos())

class TextBox:
    '''Make a text box! It's a box of color, but with text in it!
    
        Parameters:
            pos (tuple or Coord2D): top-left position for text box, including margins
            content (any): text to be written out to the screen
            font (Font): font object for text
            bgColor (list): the rgb values for the color of the box
            margin (int): margin of box around text, all sides
            borderRadius (int): size of corner radius, all corners, straight edge default'''
    
    def __init__(self, pos: Tuple[int, int] | Coord2D, content: Any | Callable, font: Font, bgColor: list[int], margin: int=5, borderRadius: int=-1):
        # set pos based
        if isinstance(pos, tuple):
            self.pos = lambda : (pos[0], pos[1])
            textPos = (pos[0] + margin, pos[1] + margin)
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
            textPos = Coord2D(lambda : pos.get()[0] + margin, lambda : pos.get()[1] + margin)
        
        # set other text-related variables like text obj, colors, margin, and border radii
        self.text = Text(textPos, content, font)
        self.bgColor = bgColor
        self.margin = margin
        self.borderRad = borderRadius

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # get text image
        textImg = self.text.getTextImg()
        # draw background rectangle, including rounded corners
        pygame.draw.rect(surface, self.bgColor, (self.pos()[0], self.pos()[1], textImg.get_size()[0] + (self.margin * 2), textImg.get_size()[1] + (self.margin * 2)), border_radius=self.borderRad)
        # blit text onto surface
        self.text.draw(surface)

### Buttons

class Button:
    '''Make a button! Exactly like a text box, but with the functionality of calling a providable function to call on click
    
        Parameters:
            pos (tuple or Coord2D): top-left position for text box, including margins
            content (any): text to be written out to the screen
            font (Font): font object for text
            bgColor (list): the rgb values for the color of the box
            margin (int): margin of box around text, all sides
            borderRadius (int): size of corner radius, all corners, straight edge default'''

    def __init__(self, pos: Tuple[int, int] | Coord2D, text: Any | Callable, font: Font, margin: int=5, borderRadius: int=-1):
        # set pos
        if isinstance(pos, tuple):
            self.pos = lambda : (pos[0], pos[1])
            textPos = (pos[0] + margin, pos[1] + margin)
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
            textPos = Coord2D(lambda : pos.get()[0] + margin, lambda : pos.get()[1] + margin)
        
        self.textObj = Text(textPos, text, font)   # text obj
        self.bgColor = consts.BUTTON.BG            # colors
        self.hlColor = consts.BUTTON.BG_HIGHLIGHT
        self.clColor = consts.BUTTON.BG_ACTIVE
        self.margin = margin                       # margin
        self.borderRad = borderRadius              # border radii
        
        # function to call on click
        self.clickFunc = lambda : None

        # mouse state variables
        self.mouseHovering = False
        self.mouseClicked = False
    
    def onClick(self, toCall: Callable):
        '''Assign a function to call when clicked
        
            Parameters:
                toCall (Callable): function to call when clicked'''
        self.clickFunc = toCall
    
    def setColors(self, background: list[int], highlight: list[int], clicked: list[int]):
        '''Set colors for buttons
            
            Parameters:
                background, highlight, and clicked (list): rgb values for those colors'''
        self.bgColor = background
        self.hlColor = highlight
        self.clicked = clicked
    
    def getButtonRect(self):
        '''Return pygame Rect object for entire button'''
        textImg = self.textObj.getTextImg()
        return pygame.Rect(self.pos()[0], self.pos()[1], textImg.get_size()[0] + (self.margin * 2), textImg.get_size()[1] + (self.margin * 2))

    def handleEvents(self, pygameEvents):
        # check for events
        for event in pygameEvents:
            # check if mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # is is a left click?
                if pygame.mouse.get_pressed()[0]:
                    # check for collision with button
                    if self.getButtonRect().collidepoint(mousePos):
                        # collision, set clicked to true
                        self.mouseClicked = True
            # check if mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                # no more left click held?
                if not pygame.mouse.get_pressed()[0]:
                    # call function if previous mouse state was pressed
                    if self.mouseClicked:
                        self.clickFunc()
                    # no left click, set clicked to False
                    self.mouseClicked = False
    
    def update(self):
        # get mouse pos
        mousePos = pygame.mouse.get_pos()
        # set hovering to true if mouse hovering, else false
        if self.getButtonRect().collidepoint(mousePos):
            self.mouseHovering = True
        else:
            self.mouseHovering = False

    def draw(self, surface):
        # get text image to blit and get size from
        textImg = self.textObj.getTextImg()
        # define color to draw button of
        if self.mouseClicked:
            color = self.clColor
        elif self.mouseHovering:
            color = self.hlColor
        else:
            color = self.bgColor
        # draw outside of button
        pygame.draw.rect(surface, color, self.getButtonRect(), border_radius=self.borderRad)
        # draw text
        self.textObj.draw(surface)

### Scroll bars

class HScrollBar:
    '''Make a (horizontal) scroll bar! Define some poses and sizes, along with min & max values, and you'll get an adjustable, dynamic scroll bar
    
        Paramters:
            pos (tuple or Coord2D): top-left pos of scroll bar
            borderRadius (int): size in pixels of roundness of corners
            width (int or Callable): width of entire scroll bar
            height (int or Callable): height of entire scroll bar
            minVal (int or Callable): minimum value for value range
            maxVal (int or Callable): maximum value for value range
            valWindow (int or Callable): value for how much of the range can be seen'''

    def __init__(self, pos: Tuple[int, int] | Coord2D, borderRadius: int | str, width: int | Callable, height: int | Callable, minVal: int | Callable, maxVal: int | Callable, valWindow: int | Callable):
        # top-left pos
        if isinstance(pos, Tuple):
            self.pos = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
        
        # width
        if isinstance(width, int):
            self.width = lambda : width
        elif isinstance(width, Callable):
            self.width = lambda : width()
        
        # height
        if isinstance(height, int):
            self.height = lambda : height
        elif isinstance(height, Callable):
            self.height = lambda : height()

        # min val
        if isinstance(minVal, int):
            self.minVal = lambda : minVal
        elif isinstance(minVal, Callable):
            self.minVal = lambda : minVal()

        # max val
        if isinstance(maxVal, int):
            self.maxVal = lambda : maxVal
        elif isinstance(maxVal, Callable):
            self.maxVal = lambda : maxVal()

        # val window
        if isinstance(valWindow, int):
            self.valWindow = lambda : valWindow
        elif isinstance(valWindow, Callable):
            self.valWindow = lambda : valWindow()

        # scrollbar width getter
        self.barWidth = lambda : self.getBarWidth()

        # border radius
        if isinstance(borderRadius, int):
            self.borderRad = lambda : int(min(borderRadius, self.height()/2))
        elif isinstance(borderRadius, str):
            if borderRadius == "max":
                self.borderRad = lambda : int(self.height()/2)
            elif borderRadius == "half max":
                self.borderRad = lambda : int(self.height()/4)
            else:
                self.borderRad = lambda : 0
        
        # colors
        self.colorFG = consts.SCROLLBAR.FG
        self.colorBG = consts.SCROLLBAR.BG

        # mouse interaction variables
        self.mouseDragging = False
        self.mouseXPosOffset = 0
        self.barXPos = self.pos()[0]  # default value, far left
    
    def setColors(self, colorBG: list[int], colorFG: list[int]):
        '''Set scroll bar colors. Takes in lists of rgb values, as ints'''
        self.colorBG = colorBG
        self.colorFG = colorFG

    def getValue(self):
        '''Returns, as a float, the value the scroll bar is currently outputting, given min and max val range, and it's position'''

        # get pos percentage
        barPosPercent = self.getPercent()

        # get zero offset for easy value range finding
        toZeroOffset = min(self.minVal(), self.maxVal())
        # calculate range
        valueRange = (self.maxVal()-toZeroOffset) - (self.minVal()-toZeroOffset)
        # scale range by percentage
        value = barPosPercent * valueRange
        # offset back from zero
        value += toZeroOffset

        # return
        return value

    def getValueStr(self):
        '''Returns, as a string, the value the scroll bar is currently outputting, given min and max val range, and it's position'''
        return str(self.getValue())

    def getPercent(self):
        '''Returns the percentage from left-to-right, of how far along the scroll bar is currently'''

        # get distance to left
        toLeft = self.pos()[0]
        # half of bar width for centering
        halfBar = self.barWidth() / 2
        # left, offset by half bar ("center")
        leftCtr = halfBar
        # center of bar, offset by to-left amount
        barCtr = (self.barXPos + halfBar) - toLeft
        # right, offset by half bar ("center")
        rightCtr = self.width() - halfBar
        
        # calculate value based on position ratio and min/maxes
        try:
            percent = (barCtr - leftCtr) / (rightCtr - leftCtr)
        # catch zero division error by defaulting to 0
        except ZeroDivisionError:
            percent = 0

        # return
        return percent

    def getBarWidth(self):
        '''Returns, as a float or int, the width of the draggable scroll bar'''

        try:
            # base width off of percentage/ratio
            width = self.width() * (self.valWindow() / (self.maxVal() - self.minVal()))
        except ZeroDivisionError:
            # max width
            width = self.width()
        
        # also max width
        if width > self.width():
            width = self.width()

        # return
        return width

    def getEntireRect(self):
        '''Returns a pygame Rect of the entire scroll bar'''

        # left-top by width by height
        return pygame.Rect(self.pos()[0], self.pos()[1], self.width(), self.height())

    def getBarRect(self):
        '''Returns a pygame Rect of the draggable part of the scroll bar'''

        # xpos-top by barWidth() by height
        return pygame.Rect(self.barXPos, self.pos()[1], self.barWidth(), self.height())

    def clampBar(self):
        '''Make sure draggable part of the scroll bar is within its bounds'''

        # target pos past left bounds
        if (self.barXPos) < self.pos()[0]:
            self.barXPos = self.pos()[0]
        # target pos past right bounds
        elif (self.barXPos + self.barWidth()) > (self.pos()[0] + self.width()):
            self.barXPos = (self.pos()[0] + self.width()) - self.getBarWidth()
        # within bounds, do nothing
        else:
            pass

    def handleEvents(self, pygameEvents):
        # check for events
        for event in pygameEvents:
            # check if mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # is is a left click?
                if pygame.mouse.get_pressed()[0]:
                    # check for collision with little bar
                    if self.getBarRect().collidepoint(mousePos):
                        # collision, set dragging to true
                        self.mouseDragging = True
                        # offset set to mouse offset from bar, for intuitive dragging
                        self.mouseXPosOffset = pygame.mouse.get_pos()[0] - self.barXPos
                    # check for collision with entire bar
                    elif self.getEntireRect().collidepoint(mousePos):
                        # collision, set dragging values
                        self.mouseDragging = True
                        # offset set to half of bar, bar will jump to mouse pos (acts like most scrollbars)
                        self.mouseXPosOffset = self.barWidth() / 2
            # check if mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                # no more left click held?
                if not pygame.mouse.get_pressed()[0]:
                    # no left click, set dragging to False
                    self.mouseDragging = False

    def update(self):
        # check for mouse dragging
        if self.mouseDragging:
            # set self x pos to clamped values based on mouse position
            newX = pygame.mouse.get_pos()[0]
            
            # set variable
            self.barXPos = newX - self.mouseXPosOffset

        # always clamp bar pos
        self.clampBar()

    def draw(self, surface):
        # draw outer, inactive rect
        pygame.draw.rect(surface, self.colorBG, self.getEntireRect(), border_radius=self.borderRad())

        # draw inner, active rect (draggable part)
        pygame.draw.rect(surface, self.colorFG, self.getBarRect(), border_radius=self.borderRad())

class VScrollBar:
    '''Make a (vertical) scroll bar! Define some poses and sizes, along with min & max values, and you'll get an adjustable, dynamic scroll bar
    
        Paramters:
            pos (tuple or Coord2D): top-left pos of scroll bar
            borderRadius (int): size in pixels of roundness of corners
            width (int or Callable): width of entire scroll bar
            height (int or Callable): height of entire scroll bar
            minVal (int or Callable): minimum value for value range
            maxVal (int or Callable): maximum value for value range
            valWindow (int or Callable): value for how much of the range can be seen'''

    def __init__(self, pos: Tuple[int, int] | Coord2D, borderRadius: int | str, width: int | Callable, height: int | Callable, minVal: int | Callable, maxVal: int | Callable, valWindow: int | Callable):
        # top-left pos
        if isinstance(pos, Tuple):
            self.pos = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()
        
        # width
        if isinstance(width, int):
            self.width = lambda : width
        elif isinstance(width, Callable):
            self.width = lambda : width()
        
        # height
        if isinstance(height, int):
            self.height = lambda : height
        elif isinstance(height, Callable):
            self.height = lambda : height()

        # min val
        if isinstance(minVal, int):
            self.minVal = lambda : minVal
        elif isinstance(minVal, Callable):
            self.minVal = lambda : minVal()

        # max val
        if isinstance(maxVal, int):
            self.maxVal = lambda : maxVal
        elif isinstance(maxVal, Callable):
            self.maxVal = lambda : maxVal()

        # val window
        if isinstance(valWindow, int):
            self.valWindow = lambda : valWindow
        elif isinstance(valWindow, Callable):
            self.valWindow = lambda : valWindow()

        # scrollbar width getter
        self.barHeight = lambda : self.getBarHeight()

        # border radius
        if isinstance(borderRadius, int):
            self.borderRad = lambda : int(min(borderRadius, self.width()/2))
        elif isinstance(borderRadius, str):
            if borderRadius == "max":
                self.borderRad = lambda : int(self.width()/2)
            elif borderRadius == "half max":
                self.borderRad = lambda : int(self.width()/4)
            else:
                self.borderRad = lambda : 0
        
        # colors
        self.colorFG = consts.SCROLLBAR.FG
        self.colorBG = consts.SCROLLBAR.BG

        # mouse interaction variables
        self.mouseDragging = False
        self.mouseYPosOffset = 0
        self.barYPos = self.pos()[1]  # default value, very top
    
    def setColors(self, colorBG: list[int], colorFG: list[int]):
        '''Set scroll bar colors. Takes in lists of rgb values, as ints'''
        self.colorBG = colorBG
        self.colorFG = colorFG

    def getValue(self):
        '''Returns, as a float, the value the scroll bar is currently outputting, given min and max val range, and it's position'''
        
        # get pos percentage
        barPosPercent = self.getPercent()

        # get zero offset for easy value range finding
        toZeroOffset = min(self.minVal(), self.maxVal())
        # calculate range
        valueRange = (self.maxVal()-toZeroOffset) - (self.minVal()-toZeroOffset)
        # scale range by percentage
        value = barPosPercent * valueRange
        # offset back from zero
        value += toZeroOffset

        # return
        return value

    def getValueStr(self):
        '''Returns, as a float, the value the scroll bar is currently outputting, given min and max val range, and it's position'''
        
        return str(self.getValue())

    def getPercent(self):
        '''Returns the percentage from top-to-bottom, of how far along the scroll bar is currently'''
        
        # get distance to top
        toTop = self.pos()[1]
        # half of bar width for centering
        halfBar = self.barHeight() / 2
        # top, offset by half bar ("center")
        topCtr = halfBar
        # center of bar, offset by to-top amount
        barCtr = (self.barYPos + halfBar) - toTop
        # bottom, offset by half bar ("center")
        bottomCtr = self.height() - halfBar
        
        # calculate value based on position ratio and min/maxes
        try:
            percent = (barCtr - topCtr) / (bottomCtr - topCtr)
        # catch zero division error by defaulting to 0
        except ZeroDivisionError:
            percent = 0

        # return
        return percent

    def getBarHeight(self):
        '''Returns, as a float or int, the height of the draggable scroll bar'''
        
        try:
            # base width off of percentage/ratio
            height = self.height() * (self.valWindow() / (self.maxVal() - self.minVal()))
        except ZeroDivisionError:
            # max height
            height = self.height()
        
        # also max height
        if height > self.height():
            height = self.height()

        # return
        return height

    def getEntireRect(self):
        '''Returns a pygame Rect of the entire scroll bar'''
        
        # left-top by width by height
        return pygame.Rect(self.pos()[0], self.pos()[1], self.width(), self.height())

    def getBarRect(self):
        '''Returns a pygame Rect of the draggable part of the scroll bar'''
        
        # left-ypos by width by barHeight()
        return pygame.Rect(self.pos()[0], self.barYPos, self.width(), self.barHeight())

    def clampBar(self):
        '''Make sure draggable part of the scroll bar is within its bounds'''
        
        # target pos past left bounds
        if (self.barYPos) < self.pos()[1]:
            self.barYPos = self.pos()[1]
        # target pos past right bounds
        elif (self.barYPos + self.barHeight()) > (self.pos()[1] + self.height()):
            self.barYPos = (self.pos()[1] + self.height()) - self.barHeight()
        # within bounds, do nothing
        else:
            pass

    def handleEvents(self, pygameEvents):
        # check for events
        for event in pygameEvents:
            # check if mouse button pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # is it a left click?
                if pygame.mouse.get_pressed()[0]:
                    # check for collision with little bar
                    if self.getBarRect().collidepoint(mousePos):
                        # collision, set dragging to true
                        self.mouseDragging = True
                        # offset set to mouse offset from bar, for intuitive dragging
                        self.mouseYPosOffset = pygame.mouse.get_pos()[1] - self.barYPos
                    # check for collision with entire bar
                    elif self.getEntireRect().collidepoint(mousePos):
                        # collision, set dragging values
                        self.mouseDragging = True
                        # offset set to half of bar, bar will jump to mouse pos (acts like most scrollbars)
                        self.mouseYPosOffset = self.barHeight() / 2
            # check if mouse button released
            if event.type == pygame.MOUSEBUTTONUP:
                # no more left click held?
                if not pygame.mouse.get_pressed()[0]:
                    # no left click, set dragging to False
                    self.mouseDragging = False

    def update(self):
        # check for mouse dragging
        if self.mouseDragging:
            # set self x pos to clamped values based on mouse position
            newY = pygame.mouse.get_pos()[1]
            
            # set variable
            self.barYPos = newY - self.mouseYPosOffset

        # always clamp bar pos
        self.clampBar()

    def draw(self, surface):
        # draw outer, inactive rect
        pygame.draw.rect(surface, self.colorBG, self.getEntireRect(), border_radius=self.borderRad())

        # draw inner, active rect (draggable part)
        pygame.draw.rect(surface, self.colorFG, self.getBarRect(), border_radius=self.borderRad())

### Value selector

### Borders (They don't drag/resize/move currently)

class HBorder:
    '''Make a horizontal border! Essentially just a black seperating line
    
        Paramters:
            yPos (int or Callable): y-position for the top of the line
            thickness (int): thickness for the line (extends downward)'''

    def __init__(self, yPos: int | Callable, thickness: int=2):
        # set y pos
        if isinstance(yPos, int):
            self.yPos = lambda : yPos
        elif isinstance(yPos, Callable):
            self.yPos = lambda : yPos()

        # set thickness and height
        self.thickness = thickness
        self.width = None
    
    def setMaxWidth(self, max: int | Callable):
        '''Set max width of the border
        
            Parameters:
                max (int or Callable): max width of the border'''
        
        # set based on type
        if isinstance(max, int):
            self.width = lambda : max
        elif isinstance(max, Callable):
            self.width = lambda : max()
    
    def getYPosInt(self):
        '''Returns, as an int or float, the top y pos of the line'''

        return self.yPos()

    def getYPosStr(self):
        '''Returns, as a string, the top y pos of the line'''

        return str(self.getYPosInt())

    def handleEvents(self, pygameEvents): pass

    def update(self): pass

    def draw(self, surface):
        # if width getter is not set, get the width of the surface given
        if self.width == None:
            width = surface.get_size()[0]
        # else, get width
        else:
            width = self.width()
        
        # draw rectangle
        pygame.draw.rect(surface, consts.BORDER.BG, (0, self.yPos(), width, self.thickness))

### Music-related things

class NotesGrid:
    '''Make a notes grid! takes in some positional information, how many rows and columns to make, information on what note each row corrosponds to
    
        Parameters:
            pos (tuple or Coord2D): top-let position of notes grid
            width (int or Callable): max width of notes grid
            height (int or Callable): max height of notes grid
            noteRows (int): how many rows of notes for there to be
            noteColumns (int): how many coluns of notes for there to be
            squareSize (int): size for each note square to be (width and height)
            rowColors (list): a list of rgb values, top to bottom, (will repeat), for each note to be when active
            rowNoteLetters (list): a list of strings, top to bottom, (will repeat), for each note to corrospond to when active
            topOctave (int): top octave number, decrements as rows descend, based on length of row notes and colors'''

    def __init__(self, pos: Tuple[int, int] | Coord2D, width: int | Callable, height: int | Callable, noteRows: int, noteColumns: int, squareSize: int, rowColors: list, rowNoteLetters: list, topOctave: int):
        # set pos
        if isinstance(pos, tuple):
            self.pos = lambda : (pos[0], pos[1])
        elif isinstance(pos, Coord2D):
            self.pos = lambda : pos.get()

        # set width
        if isinstance(width, int):
            self.width = lambda: width
        elif isinstance(width, Callable):
            self.width = lambda : width()
        
        # set height
        if isinstance(height, int):
            self.height = lambda : height
        elif isinstance(height, Callable):
            self.height = lambda : height()
        
        # set row, column, and note informatio
        self.noteRows = noteRows
        self.noteColumns = noteColumns
        self.squareSize = squareSize
        self.rowColors = rowColors
        self.rowNoteLetters = rowNoteLetters
        self.topOctave = topOctave

        # x and y offsets, for scrolling
        self.xOffset = lambda : 0
        self.yOffset = lambda : 0

        # note squares list!
        self.noteSquares = []

        # mouse state variables
        self.mouseSetAction = 1
        self.mouseClicked = False

        # sound handler
        self.soundHandler = SoundHandler()
        self.soundHandler.recalculateNotes(consts.NOTES.lettersTopToBotton, consts.NOTES.topOctave, 3)

        # bpm
        self.bpmGetter = lambda : 40

        self.resetGrid()
    
    def resetGrid(self, newState=0):
        '''Reset the grid of notes to the new states, default is 0'''
        self.noteSquares = [[newState for row in range(self.noteRows)] for col in range(self.noteColumns)]
    
    def setOffsets(self, xOffset: int | Callable, yOffset: int | Callable):
        '''Set visual offsets for grid
        
            Paramters:
                xOffset (int or Callable): x offset (positive is left)
                yOffset (int or Callable): y offset (positive is up)'''
        
        # set x offset
        if isinstance(xOffset, int):
            self.xOffset = lambda : xOffset
        elif isinstance(xOffset, Callable):
            self.xOffset = lambda : xOffset()

        # set y offset
        if isinstance(yOffset, int):
            self.yOffset = lambda : yOffset
        elif isinstance(yOffset, Callable):
            self.yOffset = lambda : yOffset()

    def setBPM(self, bpm: int | Callable):
        '''Set bpm for notes and song
        
            Parameters:
                bpm (int or Callable): bpm for notes, note time will be calculate automatically by the sound handler'''

        if isinstance(bpm, int):
            self.bpmGetter = lambda : bpm
        elif isinstance(bpm, Callable):
            self.bpmGetter = lambda : bpm()

    def writeAndPlaySong(self):
        '''Process song! Will compile notes, write out to a .wav file called "new song.wav", and will play it automatically.'''

        # first recalculate notes to seperate files for user if they want to copy individual note files
        self.soundHandler.recalculateNotes(consts.NOTES.lettersTopToBotton, consts.NOTES.topOctave, 3)

        # define an initial list, which will holds notes per column
        # all notes = [[notes in col] x columns]
        notes = []
        # go through each columns
        for col in range(len(self.noteSquares)):
            # get the notes in the column by getting going through all rows and adding the note & octave to the list if the state is 1
            notesInCol = [self.getNoteOctaveAtRowCol(row, col) for row in range(len(self.noteSquares[col])) if self.getNoteAtRowColState(row, col) == 1]
            # append column's notes to the whole list
            notes.append(notesInCol)
        
        # define an initial list of frequencies
        # all frequencies = [[frequencies in the col] x columns]
        frequencies = []
        # go through each list of notes in all columns
        for colOfNotes in notes:
            # define an empty list of frequencies for the column
            colOfFrequencies = []
            # go through each note in the column
            for note in colOfNotes:
                # get the frequency given the note and octave
                frequency = self.soundHandler.getFrequencyForNote(note[0], note[1])
                # append the frequncy
                colOfFrequencies.append(frequency)
            # append list of frequencies to the entire list
            frequencies.append(colOfFrequencies)
        
        # define an initial list which will hold all all the samples for the waves, for the entire song
        songWaveData = []
        # go through each col of frequencies
        for colOfFrequencies in frequencies:
            # calculate wave data if there are notes in the column
            if len(colOfFrequencies) > 0:
                wavesForCol = waves.makeSines(colOfFrequencies, 44100, self.soundHandler.getNoteTime())
            # other wise, make some silence
            else:
                wavesForCol = waves.rest(44100, self.soundHandler.getNoteTime())
            
            # append the data to the entire song list (there is definitely a better way to do this)
            for sample in wavesForCol:
                songWaveData.append(sample)
        
        # turn the data into a numpy array for writing out with wavio
        npSongWaveData = np.array(songWaveData)
        # scale the song data down to 1, to avoid audio defacts from going over the -1 to 1 limit
        songScaled = waves.scale_to_1(npSongWaveData)

        # write the file out, using the wavio library
        waves.write_file("new song.wav", songScaled, 44100)

        # have the sound handler load and then play the song
        self.soundHandler.loadSong("new song.wav")
        self.soundHandler.playSong()

    def calcRowColToPos(self, row: int, col: int):
        '''Returns the on-screen x and y position for the top left of a square, given row and column number'''

        top = ((row * self.squareSize) + self.pos()[1]) - self.yOffset()
        left = ((col * self.squareSize) + self.pos()[0]) - self.xOffset()
        return (left, top)

    def calcPosToRowCol(self, pos):
        '''Returns row and column position of the square intersecting the on-screen point given (for example a mouse position)'''

        # check if pos is outside of possible drawing area
        if (pos[0] < self.pos()[0]) or (pos[0] > self.pos()[0] + self.width()):  # x
            return (-1, -1)
        if (pos[1] < self.pos()[1]) or (pos[1] > self.pos()[1] + self.height()):  # y
            return (-1, -1)
        
        # calculate the row and column
        # floor division ( // ) to "round" to the nearest square
        left, top = pos
        row = ((top + self.yOffset()) - self.pos()[1]) // self.squareSize
        col = ((left + self.xOffset()) - self.pos()[0]) // self.squareSize

        # check row or col outside of grid possibilities
        if (row > self.noteRows-1) or (col > self.noteColumns-1):
            return (-1, -1)

        # return
        return row, col

    def getNoteAtRowColState(self, row, col):
        '''Returns the state of a note or square given the row or column'''

        return self.noteSquares[col][row]

    def getNoteAtPosState(self, pos):
        '''Returns the state of an intersecting note or square given an on-screen position'''

        # find closest square's row and column
        closest = self.calcPosToRowCol(pos)

        # return the state
        return self.noteSquares[int(closest[1])][int(closest[0])]

    def setNoteAtPosState(self, pos, newState):
        '''Sets the intesecting note or square's state given an on-screen position and new state to go to.
        
            Returns -1 if pos is outside possibilities, 0 if nothing changed, or 1 if it was changed'''

        # get closest square's row and column
        closest = self.calcPosToRowCol(pos)
        if closest == (-1, -1):
            return -1
        if self.noteSquares[int(closest[1])][int(closest[0])] == newState:
            # return 0 because nothing changed
            return 0
        else:
            self.noteSquares[int(closest[1])][int(closest[0])] = newState
            # return 1 because it was changed
            return 1
    
    def flipState(self, currentState):
        '''Return the opposite of the current state, given'''

        if currentState == 1:
            return 0
        return 1

    def getNoteOctaveAtPos(self, pos):
        '''Returns the intersecting note or square's note and octave given an on-screen position'''

        # get closest square's row and column
        closest = self.calcPosToRowCol(pos)
        # find the note letter by modulus-ing the row number by the length of row note letters
        noteLetterIndex = closest[0] % len(self.rowNoteLetters)
        # find the octave by floor dividing the row number by the length of row note letters
        octavesDown = (closest[0] // len(self.rowNoteLetters))
        # then subtract the max octave by how many octaves down
        octave = self.topOctave - octavesDown

        # return a tuple of (note, letter)
        return self.rowNoteLetters[int(noteLetterIndex)], int(octave)

    def getNoteOctaveAtRowCol(self, row, col):
        '''Returns the note or square's note and octave given a row and column'''

        # find the note letter by modulus-ing the row number by the length of row note letters
        noteLetterIndex = row % len(self.rowNoteLetters)
        # find the octave by floor dividing the row number by the length of row note letters
        octavesDown = (row // len(self.rowNoteLetters))
        # then subtract the max octave by how many octaves down
        octave = self.topOctave - octavesDown
        
        # return a tuple of (note, letter)
        return self.rowNoteLetters[int(noteLetterIndex)], int(octave)

    def getMaxWidth(self):
        '''Returns the max possible width of the notes grid'''

        return self.noteColumns * self.squareSize

    def getMaxHeight(self):
        '''Returns the max possible height of the notes grid'''
        
        return self.noteRows * self.squareSize

    def handleEvents(self, pygameEvents):
        # check for events
        for event in pygameEvents:
            # is it a mouse button press?
            if (event.type == pygame.MOUSEBUTTONDOWN):
                # get mouse pos
                mousePos = pygame.mouse.get_pos()
                # check if closest row & col it is a valid
                if self.calcPosToRowCol(mousePos) != (-1, -1):
                    # closest is valid, check if it is a left click
                    if pygame.mouse.get_pressed()[0]:
                        self.mouseClicked = True
                        currentState = self.getNoteAtPosState(mousePos)
                        newState = self.flipState(currentState)
                        self.mouseSetAction = newState
                        print(f"mouse clicked at {self.calcPosToRowCol(mousePos)} and setting to {self.mouseSetAction}")
            # otherwise check for mouse button release
            if (event.type == pygame.MOUSEBUTTONUP):
                # check for no more left click
                if not pygame.mouse.get_pressed()[0]:
                    self.mouseClicked = False
    
    def update(self):
        # recalculate notes if necessary: when bpm changed
        currentBPM = self.soundHandler.musicbpm
        if self.bpmGetter() != currentBPM:
            # different bpm, set and recalculate
            self.soundHandler.setBpm(self.bpmGetter())
            self.soundHandler.recalculateNotes(consts.NOTES.lettersTopToBotton, consts.NOTES.topOctave, 3)

        # if mouse clicked, set square at mouse position
        if self.mouseClicked:
            # change state, and get whether or not the state was changed
            stateChanged = self.setNoteAtPosState(pygame.mouse.get_pos(), self.mouseSetAction)
            # if the state was changed and the new state is 1 for active
            if (stateChanged == 1) and (self.mouseSetAction == 1):
                # get the not and octave at the mouse pos
                note, octave = self.getNoteOctaveAtPos(pygame.mouse.get_pos())
                # if there's a sound handler assigned, play the note sound
                if isinstance(self.soundHandler, SoundHandler):
                    self.soundHandler.playNote(note, octave)

    def draw(self, surface):
        # get & define some positions
        left, top = self.pos()
        width = self.width()
        height = self.height()

        # define the max x and y value for squares, to limit unnecessary drawing
        maxX = left + width
        maxY = top + height

        # draw each square
        for col in range(len(self.noteSquares)):
            for row in range(len(self.noteSquares[col])):
                # define some current square values
                squareLeft, squareTop = self.calcRowColToPos(row, col)

                # continue through the loop if the current square is outside limits
                if (squareLeft > maxX) or (squareTop > maxY):
                    continue

                # draw border
                pygame.draw.rect(surface, (0, 0, 0), (squareLeft, squareTop, self.squareSize, self.squareSize))
                # if activated? draw colorful
                if self.getNoteAtRowColState(row, col) == 1:
                    pygame.draw.rect(surface, self.rowColors[row%len(self.rowColors)], (squareLeft+1, squareTop+1, self.squareSize-2, self.squareSize-2))
                # else dark
                else:
                    pygame.draw.rect(surface, (50, 50, 50), (squareLeft+1, squareTop+1, self.squareSize-2, self.squareSize-2))

class SoundHandler:
    '''A sound handler for the notes grid. This object handles writing individual wav files for notes, playing individual notes, and the entire song.'''

    def __init__(self):
        pygame.mixer.pre_init(22050, -16, 2, 4096)
        pygame.mixer.init()
        self.SAMPLERATE = 44100
        self.notesFreqs = {}
        self.noteWavObjs = {}
        self.songWavObj = None
        self.musicbpm = 120  # arbitrary default
    
    def setBpm(self, newBpm: int):
        '''Set the bpm for music; determines note length
        
            Parameters:
                newBpm (int): new bpm to be set'''
        
        self.musicbpm = newBpm
    
    def getNoteTime(self):
        '''Returns the length, in seconds as an int, of each note'''

        return (60 / self.musicbpm) / 4

    def formatNoteOctaveToStr(self, note: str, octave: str | int):
        '''Returns a simple string, formatted as note then octave
        
            Parameters:
                note (str): note letter
                octave (str or int): octave number'''
        
        return f"{note}{octave}"

    def recalculateNotes(self, noteLetters: list[str], topOctave: int, numOfOctaves: int):
        '''Calculate and write out the individual note .wav files
        
            Parameters:
                noteLetters (list): list of note letters
                topOctave (int): top octave
                numOfOctaves (int): how any octaves down to calculate for'''
        
        # empty the note dictionaries
        self.noteWavObjs = {}
        self.notesFreqs = {}
        # get the note time
        noteTime = self.getNoteTime()
        # go through each octave to be calculated
        for octave in range(topOctave-numOfOctaves+1, topOctave+1):
            # go through each note
            for note in noteLetters:
                # define some general note information
                noteFileName = f"Sounds/{note}{octave}.wav"
                noteStr = self.formatNoteOctaveToStr(note, octave)
                noteFreq = waves.noteToFrequency(note, octave)
                # set dict freq for note
                self.notesFreqs[noteStr] = noteFreq
                # get wave data for note
                waveData = waves.makeSines(noteFreq, self.SAMPLERATE, noteTime)
                # write file for note
                waves.write_file(noteFileName, waveData, self.SAMPLERATE)
                # load file and assign to dict at note
                noteFile = AudioSegment.from_wav(noteFileName)
                self.noteWavObjs[noteStr] = noteFile
                # debugging
                print(f"Wrote note {note} at octave {octave} with freq {noteFreq} to {noteFileName}")

    def loadSong(self, songFilePath: str):
        '''Load a song into the song obj variable given file name
        
            Paramters:
                songFilePath (str): string of path to song .wav file'''

        self.songWavObj = AudioSegment.from_wav(songFilePath)
    
    def playSong(self):
        '''Plays the already loaded song in a seperate thread'''

        # thread func
        def playThreadFunc():
            play(self.songWavObj)
        
        # define, initialize, and start thread for playing
        thread = threading.Thread(target=playThreadFunc)
        thread.start()
    
    def playNote(self, note: str, octave: int | str):
        '''Plays a note.
        
            Parameters:
                note (str): note letter to play
                octave (int or str): octave to play'''

        # get note as string, formatted for dict's
        noteStr = self.formatNoteOctaveToStr(note, octave)
        # function to play note
        def playThreadFunc():
            play(self.noteWavObjs[noteStr])
        
        # declare & initialize thread, then start it
        thread = threading.Thread(target=playThreadFunc)
        thread.start()

    def getFileNameForNote(self, noteLetter, octave):
        '''Returns the relative file path to the .wav file for a note, given note and octave'''

        return f"Sounds/{noteLetter}{octave}.wav"

    def getFrequencyForNote(self, noteLetter, octave):
        '''Return the frequency of a given note and octave'''

        return waves.noteToFrequency(noteLetter, octave)

### Main Display class

class Display:
    '''Main Display class! This will handle most event handling, updating and drawing of the main display as well as any other elements added to it.
    
        Parameters:
            caption (str): title of window
            dispX (int): x resolution of window
            dispY (int): y resolution of window
            isResizable (bool): whether or not to let the user resize the window'''
    
    def __init__(self, caption: str="Pygame GUI Window", dispX: int=1366, dispY: int=768, isResizable: bool=False):
        pygame.init()
        
        # setup pygame display
        self.dispSize = [dispX, dispY]
        if isResizable:
            self.surf = pygame.display.set_mode(self.dispSize, pygame.RESIZABLE)
        else:
            self.surf = pygame.display.set_mode(self.dispSize)
        pygame.display.set_caption(caption)

        # define an empty elements list
        self.elements = []

        # define a running variable to true
        self.running = True
    
    def addElement(self, element):
        '''Add an element to the display to render and handle.
        
            Parameters:
                element: any element to handle. Can by anything as long as it has handleEvents, update, and draw functions to call periodically'''
        
        self.elements.append(element)
    
    def addElements(self, elements: list):
        '''Add some elements to the display to render and handle.
        
            Parameters:
                elements (list): a list of elements to handle. An element can by anything as long as it has handleEvents, update, and draw functions to call periodically'''

        for element in elements:
            self.addElement(element)

    def handleEvents(self, pygameEvents):
        # display-related events
        for event in pygameEvents:
            # print(event)
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.WINDOWRESIZED:
                # resize self display size if window resized
                self.dispSize = self.surf.get_size()
        
        # call handleEvents functions in elements
        for element in self.elements:
            element.handleEvents(pygameEvents)

    def update(self):
        # draw window background
        pygame.draw.rect(self.surf, consts.WINDOW.BG, (0, 0, self.dispSize[0], self.dispSize[1]))

        # update then draw elements
        for element in self.elements:
            element.update()
            element.draw(self.surf)

        # update window surface
        pygame.display.update()
