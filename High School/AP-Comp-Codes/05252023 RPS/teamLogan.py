import random
import itertools
'''The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''


pk_color_func = lambda r, g, b, text: "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)
# strategy_name = "Evil"
rainbow_colors = [[255, 0, 0], [255, 100, 0], [255, 255, 0], [0, 255, 0], [0, 200, 255], [0, 0, 255], [128, 0, 255], [255, 0, 255]]
make_color_func_args = lambda color_index, text : [*rainbow_colors[color_index % len(rainbow_colors)], text]
strategy_name = "try { detect pattern; if pattern {play against pattern; } else { play random; }} except Error { play random; }"
strategy_name = "".join([pk_color_func(*make_color_func_args(i, strategy_name[i])) for i in range(len(strategy_name))])

MIN_PATTERN_LENGTH = 3
MAX_PATTERN_LENGTH = 7

def beat(opponent_move: str) -> str:
    """
    Determines the move that beats the opponent's predicted move.
    """
    if opponent_move not in "rps":
        print(f"Error in beat_opponent_move! Prediction {opponent_move} not in valid moves")
        return ''

    if opponent_move == 'r':
        winning_move = 'p'
    elif opponent_move == 'p':
        winning_move = 's'
    else:
        winning_move = 'r'

    return winning_move

def find_combinations(min_len: int, max_len: int):
    """
    Finds all possible combinations of "r", "p" and "s", from lengths min_len to max_len
    """
    def find_for_length(length):
        # from ChatGPT because I'm an idiot with -1 braincells
        combinations = list(itertools.product("rps", repeat=length))
        return [''.join(comb) for comb in combinations]
    
    all_combos = []

    for length in range(min_len, max_len):
        combos_for_length = find_for_length(length+1)
        all_combos += combos_for_length

    return all_combos

def decide_best_move(their_history: list) -> str:
    """
    Analyzes the opponent's move history and makes a decision based on patterns found.
    """
    if len(their_history) <= MIN_PATTERN_LENGTH:
        return random.choice(["r", "p", "s"])
    else:
        print(f"Deciding best move. At hist len {len(their_history)}")
        all_possible_combos = find_combinations(MIN_PATTERN_LENGTH, min(len(their_history), MAX_PATTERN_LENGTH))

        # try to find a matching pattern towards end of list
        for combo in all_possible_combos:
            # get starting index for match checking
            start_index = len(their_history) - len(combo)
            # get sublist from starting index
            sublist = their_history[start_index:]
            # look for match
            if sublist == combo:
                # return first item in pattern, anticipated to be next move
                return beat(combo[0])
            else:
                continue
        
        # at this point no pattern found, return random
        return random.choice(["r", "p", "s"])

def move(my_history: list, their_history: list) -> str:
    """
    Determines the next move based on the opponent's move history.
    """
    return decide_best_move(their_history)
