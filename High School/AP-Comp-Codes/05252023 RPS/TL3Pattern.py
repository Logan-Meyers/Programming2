import random
'''The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''

strategy_name = "Evil"

def beat_opponent_move(prediction: str) -> str:
    """
    Determines the move that beats the opponent's predicted move.
    """
    if prediction not in "rps":
        print(f"Error in beat_opponent_move! Prediction {prediction} not in valid moves")
        return ''

    if prediction == 'r':
        winning_move = 'p'
    elif prediction == 'p':
        winning_move = 's'
    else:
        winning_move = 'r'

    return winning_move

def decide_best_move(their_history: list) -> str:
    """
    Analyzes the opponent's move history and makes a decision based on patterns.
    """
    if len(their_history) < 3:
        return random.choice(["r", "p", "s"])
    else:
        last_three_moves = their_history[-3:]
        
        if last_three_moves == ['r', 's', 'p']:
            return 's'  # Counter the pattern with scissors
        elif last_three_moves == ['s', 'p', 'r']:
            return 'r'  # Counter the pattern with rock
        elif last_three_moves == ['p', 'r', 's']:
            return 'p'  # Counter the pattern with paper

        return random.choice(["r", "p", "s"])

def move(my_history: list, their_history: list) -> str:
    """
    Determines the next move based on the opponent's move history.
    """
    return decide_best_move(their_history)