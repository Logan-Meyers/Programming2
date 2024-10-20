import turtle as trtl

painter = trtl.Turtle()

print("making a circle...")

color = input("What color would you like your circle to be?\n$ ")
radius = input("\nWhat radius would you like your circle to be?\n$ ")

painter.pencolor(color)
painter.circle(float(radius))

wn = trtl.Screen()
wn.mainloop()