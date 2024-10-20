'''
Collision
By: Pekay DiLuciano
'''

from re import T
import turtle

#All the horizontal and vertical turtles
all_the_turtles = {
    'hor_turtles' : [],
    'dia_turtles' : [] 
    }

#List of horizontal turtles and their start coordinates
hturtle_x = 60
hturtle_y = 150

#List of vertical turtles and their start coordinates
vturtle_x = 30
vturtle_y = 40

#For loop that creates and places the horizontal turtles in their start positions
for hturtles in range(3):
    ht = turtle.Turtle()
    all_the_turtles['hor_turtles'].append(ht)
    ht.penup()
    ht.goto(hturtle_x,hturtle_y)
    ht.forward(50)
    ht.right(90)

    hturtle_x += 50 #Moves each turtle horizontally

#For loop that creates and places the vertical turtles in their start positions
for vturtles in range(3):
    vt = turtle.Turtle()
    all_the_turtles['dia_turtles'].append(vt)
    vt.penup()
    vt.goto(vturtle_x,vturtle_y)
    vt.forward(50)

    vturtle_y += 50 #Moves each turtle vertically

for t in all_the_turtles['dia_turtles'] + all_the_turtles['hor_turtles']:
    t.forward(10)

wn = turtle.Screen()
wn.mainloop()