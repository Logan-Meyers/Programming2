# get two numbers from user
numOne = int(input("Please enter a number here:\n$ "))
numTwo = int(input("Please enter another number here:\n$ "))

print(numOne % numTwo)

# loop while the numbers are not divisible (the remainder is 0)
while numOne % numTwo != 0:
    print(f"\n{numOne} is not divisible by {numTwo}.")
    numOne = int(input("\nPlease enter a new number here:\n$ "))
    numTwo = int(input("Please enter another number here:\n$ "))

print(f"\n{numOne} is divisible by {numTwo}.")