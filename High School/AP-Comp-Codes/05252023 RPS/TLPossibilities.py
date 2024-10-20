import random
'''The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''

strategy_name = "Evil"

def beatOpponentMove(prediction: str) -> str:
    if not prediction in "rps":
        print(f"Error in beatOpponentMove! Prediction {prediction} not in valid moves")
        return ''

    if prediction =='r':
        winning_move = 'p'
    elif prediction == 'p':
        winning_move = 's'
    else:
        winning_move = 'r'

    return winning_move

def calcPercentages(their_history: list) -> tuple:
    def calc(move: str):
        try:
            return their_history.count(move) / len(their_history)
        except ZeroDivisionError:
            return 0

    rock = calc("r")
    paper = calc("p")
    scissors = calc("s")
    
    return (rock, paper, scissors)

# straight from ChatGPT
def get_matching_indexes(lst, target):
    return [index for index, value in enumerate(lst) if value == target]

def predictByPercentage(their_history: list) -> str:
    # get percentage
    percentages = calcPercentages(their_history)

    # get max of percentages
    maxPercentage = max(percentages)

    # in the case of duplicates
    if percentages.count(maxPercentage):
        matchingIndexes = get_matching_indexes(percentages, maxPercentage)
        # return random from max possibles
        return random.choice(["rps"[matching] for matching in matchingIndexes])
    # otherwise return the most possible
    else:
        return "rps"[percentages.index(maxPercentage)]


def move(my_history: list, their_history: list) -> str:
    possibleOpponent = predictByPercentage(their_history)
    return beatOpponentMove(possibleOpponent)