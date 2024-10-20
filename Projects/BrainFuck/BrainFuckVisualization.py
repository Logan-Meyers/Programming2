import time, os, readchar, sys
clr = lambda: os.system("clear")
timeDelay = 0


def flip(boolVal):
    if boolVal:
        return False
    else:
        return True

class bcolors:
    BOLD = '\033[01m'
    DARK = '\033[02m'
    ITALIC = '\033[03m'
    UNDERLINE = '\033[04m'
    STRIKE = '\033[09m'

    Black = '\033[30m'
    Red = '\033[31m'
    Green = '\033[32m'
    Yellow = '\033[33m'
    Blue = '\033[34m'
    Purple = '\033[35m'
    BlueGreen = '\033[36m'
    Grey = '\033[90m'
    Pink = '\033[91m'
    Lime = '\033[92m'
    BrightYellow = '\033[93m'
    BrightBlue = '\033[94m'
    BrightMagenta = '\033[95m'
    BrightCyan = '\033[96m'
    White = '\033[97m'
    Invert = '\033[07m'
    
    ENDC = '\033[00m'
    Default = '\033[99m'

    def custom(fg, bg=None, bold=False, italic=False, underline=False, strike=False):
        fgVals = {
            "Black": "30",
            "Red": "31",
            "Green": "32",
            "Yellow": "33",
            "Blue": "34",
            "Magenta": "35",
            "Cyan": "36",
            "White": "37",
            "bBlack": "90",
            "bRed": "91",
            "bGreen": "92",
            "bYellow": "93",
            "bBlue": "94",
            "bMagenta": "95",
            "bCyan": "96",
            "bWhite": "97"
        }
        bgVals = {
            "Black": "40",
            "Red": "41",
            "Green": "42",
            "Yellow": "43",
            "Blue": "44",
            "Magenta": "45",
            "Cyan": "46",
            "White": "47",
            "bBlack": "100",
            "bRed": "101",
            "bGreen": "102",
            "bYellow": "103",
            "bBlue": "104",
            "bMagenta": "105",
            "bCyan": "106",
            "bWhite": "107"
        }
        color = '\033[' + str(fgVals[fg])
        if bg:
            color +=  ";" + str(bgVals[bg])
        color += ";01" if bold else ""
        color += ";03" if italic else ""
        color += ";04" if underline else ""
        color += ";09" if strike else ""
        color += "m"
        return color

class bfData:
    def __init__(self, memoryLength):
        self.data = []
        self.resetMemory(memoryLength)
        self.ptr = 0
        self.output = ""
        self.warn = ""
        self.constUpdating = True
        self.programRunning = True
        self.memColor = bcolors.BlueGreen
        self.ptrColor = bcolors.Invert
    
    def setUpdating(self, val):
        self.constUpdating = val

    def setWarn(self, message):
        self.warn = message
    
    def clrWarn(self):
        self.warn = ""

    def resetMemory(self, memLen):
        self.data = []
        for i in range(memLen):
            self.data.append(0)
    
    def getData(self):
        return self.data[self.ptr]

    def setMemory(self, val):
        self.data[self.ptr] = val
        
        for i in range(len(self.data)):
            if self.data[i] > 255:
                self.data[i] = self.data[i] - 256
            elif self.data[i] < 0:
                self.data[i] = 256 + (self.data[i])

    def printMemory(self):
        dataLine = ""
        dataLine += self.memColor
        
        for i in range(len(self.data)):
            if i == self.ptr:
                dataLine += self.ptrColor
            dataLine += ("[" + str(self.data[i]) + "]")
            if i == self.ptr:
                dataLine += bcolors.ENDC
                dataLine += self.memColor

        dataLine += bcolors.ENDC
        clr()
        print(dataLine)
        print(f"{bcolors.BrightYellow}Output: {self.output}{bcolors.ENDC}")
        if len(self.warn) > 0:
            # print("WARN: " + self.warn)
            print(f"{bcolors.Red}WARN: {self.warn}{bcolors.ENDC}")

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
        return None

def printCommands():
    clr()
    print("Command : What it does\n\n+ : add one to the memory slot selected\n- : sub one from the memory slot selected\n> : move the pointer right one\n< : move the pointer left one\n, : get one character of input and set it at the pointer position\n. : print whatever value in memory the pointer is at")
    input("\n--- Press enter to continue ---\n$ ")

def runCommand(command):
    if command == "c":
        bf.output = ""
    if command == "q":
        bf.programRunning = False
    if command == "p":
        bf.setUpdating(flip(bf.constUpdating))
        if bf.constUpdating:
            bf.setWarn("Turned on constant display updating!")
        else:
            bf.setWarn("Turned off constant display updating!")
    if command == "r":
        print("Enter file name:\n$ ", end="")
        toRead = input()
        with open(toRead, "r") as cmdFile:
            fileCmds = cmdFile.read()
            print(fileCmds)
            input("Press return to continue ...")
            parse(fileCmds)
    if command == "+":
        bf.setMemory(bf.getData()+1)
    if command == "-":
        bf.setMemory(bf.getData()-1)
    if command == ">":
        if bf.ptr < len(bf.data)-1:
            bf.ptr += 1
    if command == "<":
        if bf.ptr > 0:
            bf.ptr -= 1
    if command == ",":
        bf.printMemory()
        print("Enter character:\n$ ", end="")
        # c = readchar.readchar()
        c = readchar.readkey()
        bf.setMemory(convBinAscii(ascii=c))
    if command == ".":
        try:
            bf.output += convBinAscii(bin=bf.getData())
        except TypeError:
            bf.setWarn("Not an ASCII character!")

    if bf.constUpdating:
        bf.printMemory()
        print(f"{bcolors.Green}Command: {command}{bcolors.ENDC}")
    time.sleep(timeDelay)

def parse(inp):
    if inp == "pointer":
        print(f"Pointer position: {bf.ptr}, press return to continue ...")
        input()
        return
    nextLoop = ""
    brackets = 0
    for cmd in inp:
        if cmd == "#":
            break
        if cmd == "[":
            if brackets > 0:
                nextLoop += cmd
            brackets += 1
        elif cmd == "]":
            if brackets > 1:
                nextLoop += cmd
            brackets -= 1
        else:
            if brackets > 0:
                nextLoop += cmd
            else:
                runCommand(cmd)
        if brackets == 0 and len(nextLoop) > 0:
            whileRunning = True
            while whileRunning:
                parse(nextLoop)
                if bf.getData() == 0:
                    whileRunning = False
            nextLoop = ""

def matchedBrackets(inp):
    brackets = 0
    for char in inp:
        if char == "[":
            brackets += 1
        elif char == "]":
            brackets -= 1
    
    if brackets == 0:
        return True
    elif brackets > 0:
        bf.setWarn("Unmatched [")
        return False
    else:
        bf.setWarn("Unmatched ]")
        return False

bf = bfData(int(input("How many slots for memory do you want to see?\n$ ")))
timeDelay = float(input("How much of a delay do you want between operations?\n$ "))
running = True

while bf.programRunning:
    bf.printMemory()
    userInput = input(f"{bcolors.Lime}Input:\n$ {bcolors.ENDC}")
    bf.clrWarn()
    if matchedBrackets(userInput):
        parse(userInput)

# Alphabet:
# > +++++++++++++ [-<++>] > +++++++++++++ [-<+++++>] << [->.+<]

#>++++[>++++++<-]>-[[<+++++>>+<-]>-]<<[<]>>>>--.<<<-.>>>-.<.<.>---.<<+++.>>>++.<<---.[>]<<.

# Hello World:
# >+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++.

# Backwards Name:
# +++++ [>,]

# Shift all values right until a zero is encountered, once
# start at last number, cannot be a 0
# [[->+<]<]

# Shift all values # of times until zero, start at counter (#)
"""
[               Start a loop: runs while counter != 0
    [[->+<]<]   Normal shift loop
    >[>]<-      Go to right end of group, sub 1
]               End loop

[[[->+<]<]>[>]<-]

Shift left:
[[[-<+>]>]<[<]>-]
"""

"""
Failed 2-number add program

,>>++++++[-<++++++++>]<[-<->]  # first number then sub 48
,>>++++++[-<++++++++>]<[-<->]  # second number then sub 48
	
<[-<+>]  # add numbers together

>++++++[-<++++++++>]<[-<+>]  # add 48

<  # move to answer

[->+>+<<]  # duplicate

>>>++++++[-<<<++++++++>>>]  # add 48 to cell 1

>+++++++[-<++++++++>]<+  # add 57 to cell 4

[-<->]

IF MORE THAN 9:

<[-<-<+>>]<<.>.  # add carries and print

FINAL:

,>>++++++[-<++++++++>]<[-<->],>>++++++[-<++++++++>]<[-<->]<[-<+>]>++++++[-<++++++++>]<[-<+>]<[->+>+<<]>>>++++++[-<<<++++++++>>>]>+++++++[-<++++++++>]<+[-<->]
"""

"""
>>+>+>><<<<<++++++++++++++++[->>>[-]<[->>>+<<<]>>>[-<<+<+>>>]<<<<[->>>>+<<<<]>>>>[-<+>]<<<[->>>+<<<]>>>[-<<<+<+>>>>]<<<[-]>>><[->+<]>[-<+<<+>>>]<<<<<]>>>>.
"""