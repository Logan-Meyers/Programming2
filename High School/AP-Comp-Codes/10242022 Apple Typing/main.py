import turtle as trtl
import random

# -----setup-----
# create the window object and set it up; including images
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape("apple.gif")  # Make the screen aware of the new file
wn.addshape("pear.gif")

# create the lists necessary
apple_turtles = []
txt_turtles = []
assigned_keys = []
assignable_keys = "qwertyuiopasdfghjklzxcvbnm"
recent_inputs = []

# create the initial apple turtle to fall
apple = trtl.Turtle()
apple.penup()
# create the initial text turtle to fall
txt = trtl.Turtle()
txt.penup()
txt.hideturtle()

title_turtle = trtl.Turtle()
title_turtle.penup()

font_setup = ("Arial", 45, "bold")

# if the user fails to press the last assigned letter in time,
# put the letter back into the available letters to be chosen from
add_back_letter_if_fail = True

# turn the tracer off; we will update the screen manually in a loop
trtl.tracer(False)

# a custom data type to store play field information; self-explanatory...
class Playbounds:
	left = -300
	right = 300
	top = 200
	bottom = -200

# -----functions-----
# given a turtle, set that turtle to be shaped by the image file

def get_random_image():
	return random.choice(["apple.gif", "pear.gif"])

def set_random_shape(active_apple):
    active_apple.shape(get_random_image())
    wn.update()

# returns a function object
def get_key_pressed_func(letter):
	# function to print out a character;
	# var letter is already defined when calling getFunc()
	def on_press():
		global recent_inputs
		# just writes out the letter
		recent_inputs.append(letter)
	# return the function of typeLetter;
	# since we pass in var letter as an argument, that argument
	# is used in the typeLetter function object we return here
	return on_press

def calc_txt_pos(initial_pos):
	return (initial_pos[0]-15, initial_pos[1]-35)

def reset_apple(new_turtle=False):
	global assignable_keys, assigned_keys, apple_turtles, txt_turtles

	if new_turtle:
		apple_turtles.append(apple_turtles[-1].clone())
		txt_turtles.append(txt_turtles[-1].clone())
	else:
		if add_back_letter_if_fail:
			assignable_keys = assignable_keys + assigned_keys[-1]

	try:
		chosen_letter = random.choice(assignable_keys)
	except IndexError:
		chosen_letter = ""
	assignable_keys = assignable_keys.replace(chosen_letter, "")
	assigned_keys.append(chosen_letter)

	new_x = random.randint(Playbounds.left, Playbounds.right)

	apple_turtles[-1].goto(new_x, 200)
	txt_turtles[-1].goto(calc_txt_pos((new_x, Playbounds.top)))

	set_random_shape(apple_turtles[-1])

def apple_fall_loop():
	global apple_turtles, txt_turtles

	falling = True

	while falling:
		apple_turtles[-1].goto(apple_turtles[-1].xcor(), apple_turtles[-1].ycor()-7)
		txt_turtles[-1].goto(txt_turtles[-1].xcor(), txt_turtles[-1].ycor()-7)
		txt_turtles[-1].clear()
		txt_turtles[-1].write(assigned_keys[-1], font=font_setup)

		if apple_turtles[-1].ycor() < Playbounds.bottom:
			reset_apple(new_turtle=False)
			falling = False
			break
		
		try:
			if recent_inputs[-1] == assigned_keys[-1]:
				falling = False
				reset_apple(new_turtle=True)
		except IndexError:
			pass

		wn.update()

		wn.ontimer(apple_fall_loop(), 20)

def start_game():
	global title_turtle

	title_turtle.clear()
	title_turtle.hideturtle()
	apple_fall_loop()

# all alphabet letters
keyboard_keys = "qwertyuiopasdfghjklzxcvbnm"
# for each letter in the string:
for letter in keyboard_keys:
    # have wn look for that letter to be pressed, then:
    # call the function returned by getFunc(letter) with our specific letter
	wn.onkeypress(get_key_pressed_func(letter), letter)

wn.onkeypress(start_game, "space")

wn.listen()

apple_turtles.append(apple)
txt_turtles.append(txt)
reset_apple(new_turtle=False)

title_turtle.goto(-200, Playbounds.bottom-50)
title_turtle.write("Press space to start", font=font_setup)

wn.mainloop()
