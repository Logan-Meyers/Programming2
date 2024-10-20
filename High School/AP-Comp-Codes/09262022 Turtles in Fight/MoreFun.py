my_courses = ["English", "Math", "CS"]

def getIntInput(course):
    while True:
        try:
            inp = input(f"Points -> ")
            inp = int(inp)
            return inp
        except ValueError:
            print("Please enter a number! Try again!")

# Segment 1
redo = "y"
while (redo == "y"):

    # Segment 3
    for course in my_courses:
        # Segment 2
        print("\nEnter your points for " + course)

        points = int(input("Points -> "))

        # Segment 4
        if (points >= 90):
            print("A")
        elif (points >= 80):
            print("B")
        elif (points >= 70):
            print("C")
        elif (points >= 60):
            print("D")
        else:
            print("F")

    redo = input("Do you need to re-do these grades? (y/n) ")