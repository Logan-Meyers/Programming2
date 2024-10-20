# Imports
from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape
import turtle as trtl
import random as rand
import math
# Weird TKinter stuff that I don't understand but it makes a square
screen = Screen()
larger = PhotoImage(file="redSquare.gif").subsample(30,30)
screen.addshape("larger", Shape("image",larger))
# Square turtle
square = Turtle("larger")
square.hideturtle()
square.penup()
# Turtle to show upcoming shape
nextShape = Turtle("larger")
nextShape.hideturtle()
nextShape.penup()
nextShape.goto(200,107)
# Make it run fast
trtl.tracer(False)
square.speed(0)
nextShape.speed(0)
# List of key inputs
letterList = ["a", "d"]
# Game list
global gameList
gameList = []
'''
gameList = [1,0,0,0,0,0,0,0,0,0,
            0,1,0,0,0,0,0,0,0,0,
            0,0,1,0,0,0,0,0,0,0,
            0,0,0,1,0,0,0,0,0,0,
            0,0,0,0,1,0,0,0,0,0,
            0,0,0,0,0,1,0,0,0,0,
            0,0,0,0,0,0,1,0,0,0,
            0,0,0,0,0,0,0,1,0,0
            0,0,0,0,0,0,0,0,1,0
            0,0,0,0,0,0,0,0,0,1
            1,0,0,0,0,0,0,0,0,0,
            0,1,0,0,0,0,0,0,0,0,
            0,0,1,0,0,0,0,0,0,0,
            0,0,0,1,0,0,0,0,0,0,
            0,0,0,0,1,0,0,0,0,0,
            0,0,0,0,0,1,0,0,0,0,
            0,0,0,0,0,0,1,0,0,0,
            0,0,0,0,0,0,0,1,0,0
            0,0,0,0,0,0,0,0,1,0
            0,0,0,0,0,0,0,0,0,1]
'''
# Shape lists
lineShape = [1,0,0,0,
             1,0,0,0,
             1,0,0,0,
             1,0,0,0]
tShape = [1,0,0,0,
         1,1,0,0,
         1,0,0,0,
         0,0,0,0]
squareShape = [1,1,0,0,
              1,1,0,0,
              0,0,0,0,
              0,0,0,0]
lShape = [1,1,0,0,
         1,0,0,0,
         1,0,0,0,
         0,0,0,0]
shape = []

#-----Functions-----#
# Algorithm for moving squares down one
def moveNums():
  global gameList
  for num1 in range(19): # I used 19 because I don't need it to check the bottom row seeing as those squares are already as far down as they can go
    for num2 in range(10):
      if gameList[10*num1+num2] == 1 and gameList[10*num1+num2+10] == 0: # If there is a square with an empty space below it
        gameList[10*num1+num2] = 0 # Take away the square
        gameList[10*num1+num2+10] = 2 # Add a temporarily immovable square below it
        
# draws the squares
def drawGrid():
  global gameList
  # Runs through every item on the list
  for num1 in range(20):
    for num2 in range(10):
      square.goto(23*num2-75, -23*num1+200)
      if gameList[10*num1+num2] == 1: # If there is a square there then stamp the square image
        square.stamp() 
        
# Run the square moving algorithm
# Converts temporarily immovable squares into movable ones
def moveNumsFull():
  global gameList
  for num1 in range(20):
    moveNums()
  for num1 in range(len(gameList)):
    if gameList[num1] == 2:
      gameList[num1] = 1
      
# Clear any full rows
def clearRows():
  global gameList
  for num1 in range(20):
    clear = 0
    for num2 in range(10):
      if gameList[10*num1+num2] == 1:
        clear += 1 # Add one to clear if there is a square (full rows will have 10)
    if clear == 10: # If there is a full row then clear it
      for num2 in range(10):
        gameList[10*num1+num2] = 0
        
# Move the squares, clears full rows, and draws the squares
def loopFunction():
  global gameList
  moveNumsFull()
  clearRows()
  square.clear()
  drawGrid()
  screen.update()

# Plomp the shape into the game list whre the player clicked
def addShape():
  global xPos
  global gameList
  global shape
  for num1 in range(4):
    for num2 in range(4):
      if shape[4*num1+num2] == 1: # Only change game list if the shape has a square there
        gameList[10*num1+xPos+num2] = shape[4*num1+num2]
        
# Pick a random upcoming shape and draw it
def getRandShape():
  # Pick a random number (0-3)
  global shape, randShape, nextShape
  randShape = rand.randint(0,3)
  shape = []                            ###### mmmmmmm... turns out, it is important to clear this list first! lol :D ######
  # Use random number, take preset list and add them to shape list
  for num1 in range(4):
    for num2 in range(4):
      if randShape == 0:
        shape.append(lineShape[4*num1+num2])
      elif randShape == 1:
        shape.append(squareShape[4*num1+num2])
      elif randShape == 2:
        shape.append(tShape[4*num1+num2])
      else:
        shape.append(lShape[4*num1+num2])      
  # Draw shape list to the right of playspace
  for num1 in range(4):
    for num2 in range(4):
      nextShape.goto(23*num2+200, -23*num1+107)
      if shape[4*num1+num2] == 1:
        nextShape.stamp()
        
# Gets the position of mouse click
def placeShape(x,y):
  global xPos
  if x > -87 and x < 143:
    xPos = math.floor((x+87)/23)
  addShape()
  nextShape.clear()
  getRandShape()
  screen.update()
        
# random
for num in range(200):
  gameList.append(rand.randint(0,1))
drawGrid()

getRandShape()

screen.onclick(placeShape)
# main loop
for num in range(10000):
  # game will run for 41 minutes and 40 seconds at a frame rate of 4 fps (250ms)
  screen.ontimer(loopFunction,250*num)
screen.mainloop()