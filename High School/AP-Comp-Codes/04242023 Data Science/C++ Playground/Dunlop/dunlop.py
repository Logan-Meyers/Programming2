# module used for finding all permutations of operators
import itertools


def evalNumbers(numA, numB, operation):
    """
    Function to evaluate numA against numB u=by the operation given

    Parameters:
        numA: number A
        numB: number B
        operation: operation to be applied
    """
    # I'm sure there's a better way to do this but I refuse to find it
    if operation == "+":
        return numA + numB
    elif operation == "-":
        return numA - numB
    elif operation == "*":
        return numA * numB
    elif operation == "/":
        if numB == 0: return float('inf')
        else:         return numA / numB

def makeNewEquation(oldEquation, operationIndex, evaluatedNumber):
    """
    Function to make a new equation. Essentially, it replaces two number and the operation between them with the answer

    Parameters:
        oldEquation: list of old equation elements
        operationIndex: index of the operation completed in the list
        evaluatedNumber: the answer to the number to the left and right agains the operation
    """
    # make left and right segments
    left = oldEquation[:operationIndex-1]
    right = oldEquation[operationIndex+2:]

    # make new equation by combining left, middle (evaluated), and right segments
    newEquation = left
    newEquation.append(evaluatedNumber)
    newEquation += right

    return newEquation

def evalEquation(equation):
    """
    Function to evaluate a given equation to a number.
    
    Parameters:
        equation: the list of numbers and operations. An example might be [10, "/", 2, "+" 13] for 10/2+13
    """

    while len(equation) > 1:
        # check for both division and multiplication
        if ("*" in equation) and ("/" in equation):
            operationIndex = min(equation.index("*"), equation.index("/"))
            operation = equation[operationIndex]
            answer = evalNumbers(equation[operationIndex-1], equation[operationIndex+1], operation)
            equation = makeNewEquation(equation, operationIndex, answer)
            # print(f"Operation {operation} found, answer is {answer} and new equation in {equation}")
        # else check for both addition and subtraction
        elif ("+" in equation) and ("-" in equation):
            operationIndex = min(equation.index("+"), equation.index("-"))
            operation = equation[operationIndex]
            answer = evalNumbers(equation[operationIndex-1], equation[operationIndex+1], operation)
            equation = makeNewEquation(equation, operationIndex, answer)
        # else go through each other operation from multiplication to subtraction
        else:
            for operation in OPERATIONS:
                if operation in equation:
                    operationIndex = equation.index(operation)
                    operation = equation[operationIndex]
                    answer = evalNumbers(equation[operationIndex-1], equation[operationIndex+1], operation)
                    equation = makeNewEquation(equation, operationIndex, answer)
                    break
    
    # print("Final equation reached, equation:", equation)
    return equation[0]

def solveForOperationCombo(numbers, expectedAnswer):
    """
    Main function to call when looking for right equation. Given the numbers and expected answer, it will go through all possible combinations of operators between the numbers and test each one.
    
    Returns:
        A list: will return a list (for an equation) if it has found a fitting equation
        None: will return None if no fitting equation has been found
    
    Parameters:
        numbers: the list of numbers (usually float or int, or another number type) to put operations between
        expectedAnswer: the number the correct equation should evaluate to (usually a float or int, or another number type)
    """

    # get all possible permutations of the operations for the length of numbers we have
    possibleOperationPermutations = itertools.product(OPERATIONS, repeat=len(numbers))

    # a number to hold how many equations we've searched through
    equationsSearched = 0
    
    # go through each possible permutation of operation orders
    for permutations in possibleOperationPermutations:
        # increment permutation counter
        equationsSearched += 1
        # telling user how far we are, so we can see progress going or not
        print(f"At Equation #{equationsSearched}")
        # set possibleEquation to the initial numbers given
        possibleEquation = [num for num in numbers]
        # insert operations between numbers
        for i in range(len(numbers)-1):
            possibleEquation.insert(1+(i*2), permutations[i])

        # evaluate possible equation
        possibleAnswer = evalEquation(possibleEquation)
        # check if answer is correct
        if possibleAnswer == expectedAnswer:
            # tell user how many equations were searched
            print("Equations searched:", equationsSearched)
            # return correct equation
            return possibleEquation
    
    # return None, meaning no equation was found
    return None

def formatEquation(equation, answer):
    """
    A function to format an equation into a more readable form

    Parameters:
        equation: the list of numbers and operations for the equation
        answer: the (usually float) answer to the equation (usually based on equation)
    """

    # initial string
    formatted = ""
    # add each item to string, plus some space at the end
    for item in equation:
        formatted += str(item) + " "
    # add an equals sign and the answer
    formatted += "= " + str(answer)
    # return formatted equation
    return formatted

OPERATIONS = ["*", "/", "+", "-"]  # in no particular order

### USER INPUT - getting numbers
# get user input
numberString = input("Please enter some numbers, seperated by all spaces or all commas:\n --> ")
# split by spaces or commas
numberSplit = numberString.split(sep=", ") if "," in numberString else numberString.split(" ")
# remove any empty values from input+split errors
while "" in numberSplit: numberSplit.remove("")
# make a new list, NUMBERS, that holds float versions of the numbers entered
NUMBERS = [float(num) for num in numberSplit]

### USER INPUT - getting expected answer
# get user input
answerString = input("\nPlease enter the expected answer to the equation when evaluated:\n --> ")
# set a new constant, ANSWER, to the value of the expected answer- as a float
ANSWER = float(answerString)

### SOLVE FOR ANSWER
# call function, get possible equation solution
answer = solveForOperationCombo(NUMBERS, ANSWER)
# check for none state
if answer == None:
    print("I'm sorry, I've gone through all possibilities and there is no equation that evaluates to:", ANSWER)
else:
    formattedEquation = formatEquation(answer, ANSWER)
    print(f"Good news! I've gone through all possibilities and found a solution:\n{formattedEquation}")
