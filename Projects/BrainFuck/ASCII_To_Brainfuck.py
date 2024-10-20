def convBinAscii(bin=None, ascii=None):  # binary is prioritized first
    chars = {
        "\n": 10,
        " ": 32,
        "!": 33,
        "\"": 34,
        "#": 35,
        "$": 36,
        "%": 37,
        "&": 38,
        "'": 39,
        "(": 40,
        ")": 41,
        "*": 42,
        "+": 43,
        ",": 44,
        "-": 45,
        ".": 46,
        "/": 47,
        "0": 48,
        "1": 49,
        "2": 50,
        "3": 51,
        "4": 52,
        "5": 53,
        "6": 54,
        "7": 55,
        "8": 56,
        "9": 57,
        ":": 58,
        ";": 59,
        "<": 60,
        "=": 61,
        ">": 62,
        "?": 63,
        "@": 64,
        "A": 65,
        "B": 66,
        "C": 67,
        "D": 68,
        "E": 69,
        "F": 70,
        "G": 71,
        "H": 72,
        "I": 73,
        "J": 74,
        "K": 75,
        "L": 76,
        "M": 77,
        "N": 78,
        "O": 79,
        "P": 80,
        "Q": 81,
        "R": 82,
        "S": 83,
        "T": 84,
        "U": 85,
        "V": 86,
        "W": 87,
        "X": 88,
        "Y": 89,
        "Z": 90,
        "[": 91,
        "\\": 92,
        "]": 93,
        "^": 94,
        "_": 95,
        "`": 96,
        "a": 97,
        "b": 98,
        "c": 99,
        "d": 100,
        "e": 101,
        "f": 102,
        "g": 103,
        "h": 104,
        "i": 105,
        "j": 106,
        "k": 107,
        "l": 108,
        "m": 109,
        "n": 110,
        "o": 111,
        "p": 112,
        "q": 113,
        "r": 114,
        "s": 115,
        "t": 116,
        "u": 117,
        "v": 118,
        "w": 119,
        "x": 120,
        "y": 121,
        "z": 122,
        "{": 123,
        "|": 124,
        "{": 125,
        "~": 126
    }

    if bin and bin >= 32 or bin == 10:
        print("going")
        for char in chars:
            if chars[char] == bin:
                return char
        return ""
    elif ascii:
        try:
            return chars[ascii]
        except KeyError:
            return ""
    else:
        return ""

def convertToBF(string):
    commands = ""
    timesSplit = 0
    # for each character
    for char in string:
        if len(commands) > (850 * (timesSplit + 1)):
            commands += "\n\n"
            timesSplit += 1
        commands += ">"
        commands += "+" * getFactorsOfNum(convBinAscii(ascii=char))[0]
        commands += "[-<"
        commands += "+" * getFactorsOfNum(convBinAscii(ascii=char))[1]
        commands += ">]"
    
    if len(commands) > (850 * (timesSplit + 1)):
        commands += "\n\n"
        timesSplit += 1
    commands += "<" * (len(string))
    commands += ".>" * len(string)
    
    return commands

def getFactorsOfNum(num):
    if num == 0:
        return [0, 0]
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    
    print(factors)
    if len(factors) % 2 == 0:
        mid = int(len(factors)/2)-1
        return [factors[mid], factors[mid+1]]  # if even
    else:
        mid = int((len(factors)-1)/2)
        return [factors[mid], factors[mid]]  # if odd
        
def getMemoryCellsNeeded(string):
    return len(string)+1

toConvert = input("Please enter a string of characters you want to be able to print in Brainfuck:\n$ ")
print(toConvert)

"""
for i in toConvert:
    print(getFactorsOfNum(convBinAscii(ascii=i)))
    print(getFactorsOfNum(convBinAscii(ascii=i)-32))
    print("-----")

print(getFactorsOfNum(32))
"""

print(convertToBF(toConvert))
print("\nCells of memory needed: " + str(getMemoryCellsNeeded(toConvert)))
