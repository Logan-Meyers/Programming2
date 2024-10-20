import math

# print beginning information for user
print("I will ask you to enter numbers, here is the format:")
print("[number]")
print("for just one number, or:")
print("[number]x[amount]")
print("For multiple of those data points.")
print("When you're done, type either \"done\", \"q\" or \"quit\" to stop number collection and calculate the standard deviation.")

# variable setup
numbers = []
number_average = 0
n = 0
n_minus_1 = 0
s_squared = 0
s = 0

# get input from user
while True:
  try:
    # get input
    inp = input("\nEnter input: ")
    
    # check if user wants to stop collection
    if inp == "done" or inp == "q" or inp == "quit":
      break
      
    # check for multiple numbers entered
    if "x" in inp:
      # split input into two parts
      inp_split = inp.split("x")
      # get the number
      number = float(inp_split[0])
      # get the amount of numbers
      try:      
        amount = int(inp_split[1])
      except ValueError:
        print("Please enter a whole number for the amount!")
        continue
      # add the number to the list
      for _ in range(amount):
        numbers.append(number)
    else:
      numbers.append(float(inp))
  except ValueError:
    print("Please enter a number (whole or decimal)!")

# calculate variables
number_average = sum(numbers) / len(numbers)
n = len(numbers)
n_minus_1 = n-1

# calculate Sample Variance
s_squared = sum([(x - number_average)**2 for x in numbers])/n_minus_1
s = math.sqrt(s_squared)

# print results
print("\nYour Numbers: " + str(numbers))
print("Number of data points (n): " + str(n))
print("The average/mean (x̄): " + str(number_average))
print("The Sample Variance: (s²): " + str(s_squared))
print("The Standard Deviation (s): " + str(s))
