import turtle as trtl


txt = trtl.Turtle()
wn = trtl.getscreen()

# returns a function object
def getDrawLetterFunc(letter):
  def drawLetter():
    # just prints out the letter
    txt.color("red")
    txt.goto(0, 100)
    txt.write(letter, font=("Arial", 74, "bold"))
  # return the function of typeLetter;
  # since we pass in var letter as an argument, that argument
  # is used iin the typeLetter function object we return here
  return drawLetter

# all alphabet letters
keyboard_keys = "qwertyuiopasdfghjklzxcvbnm"
# for each letter in the string:
for letter in keyboard_keys:
  # have wn look for that letter to be pressed, then:
  # call the function returned by getFunc(letter) with our specific letter
  wn.onkeypress(getDrawLetterFunc(letter), letter)