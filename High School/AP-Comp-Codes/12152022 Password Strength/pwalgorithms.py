# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze/find a simple two-words password
def two_words(password):
  # get all commonly used words
  words = get_dictionary()
  guesses = 0
  # iterate through all words using a outside loop then a nested inside loop
  for wordA in words:
    for wordB in words:
      # increment guesses by one, check for password, return true + guesses if true
      guesses += 1
      if (wordA + wordB == password):
        return True, guesses
  # otherwise if the algorithm couldn't find the password, return false + guesses.
  return False, guesses
    
# analyze/find a more complicated two-word password, with one digit in the beginning and end
def two_words_and_digit(password):
  # get all commonly used words
  words = get_dictionary()
  # list of additional numbers, as well as nothing incase the password doesn't have a number there
  additional_numbers = ["", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # 0-9 plus none
  guesses = 0
  # iterate through all words using a outside loop then a nested inside loop
  for wordA in words:
    for wordB in words:
      # then, iterate through all numbers for the beginning
      for beginning_digit in additional_numbers:
        # and iterate through all number for the end
        for ending_digit in additional_numbers:          
          # increment guesses by one, check for password, return true + guesses if true
          guesses += 1
          if (beginning_digit + wordA + wordB + ending_digit == password):
            return True, guesses

  # otherwise if the algorithm couldn't find the password, return false + guesses.
  return False, guesses
