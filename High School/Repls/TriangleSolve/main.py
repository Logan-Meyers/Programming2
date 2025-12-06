import math


def drawTriangle(info):
    def paddChar(ltr):
        if info[ltr] != 0:
            return ((" " * (maxLenNum - len(str(info[ltr])))) + str(info[ltr]))
        else:
            return ((" " * (maxLenNum - 1)) + ltr)
    
    def paddSpace(maxLenNum):
        return (" " * maxLenNum)

    maxLenNum = max(len(str(info["A"])), len(str(info["b"])), len(str(info["C"])))

    # "A ┌\n  │\\\n  │ \\\n  │  \\\n  │   \\\nb │    \\ c\n  │     \\\n  │      \\\n  │       \\\n  │        \\\nC └─────────┘ B\n       a"
    print("", paddChar("A"), "┌\n", paddSpace(maxLenNum), "│\\\n", paddSpace(maxLenNum), "│ \\\n", paddSpace(maxLenNum), "│  \\\n", paddSpace(maxLenNum), "│   \\\n", paddChar("b"), "│    \\", (info["c"] if info["c"] != 0 else "c"), "\n", paddSpace(maxLenNum), "│     \\\n", paddSpace(maxLenNum), "│      \\\n", paddSpace(maxLenNum), "│       \\\n", paddSpace(maxLenNum), "│        \\\n", paddChar("C"), "└─────────┘", (info["B"] if info["B"] != 0 else "B"), "\n", (" " * (maxLenNum + int(math.ceil(11 - len(str(info["a"])))/2))), (info["a"] if info["a"] != 0 else "a"))

# solving sin/cos/tan
def solveSin(ang, opp, hyp):
    if opp == 0:
        return hyp * math.sin(ang)
    else:
        return opp / math.sin(ang)

def solveCos(ang, adj, hyp):
    if adj == 0:
        return hyp * math.cos(ang)
    else:
        return adj / math.cos(ang)

def solveTan(ang, opp, adj):
    if opp == 0:
        return adj * math.tan(ang)
    else:
        return opp / math.tan(ang)

# solving sin/cos/tan inverse
def solveSinI(opp, hyp):
    return math.asin(opp/hyp)

def solveCosI(adj, hyp):
    return math.acos(adj/hyp)

def solveTanI(opp, adj):
    return math.atan(opp/adj)

# solving logic
def getOpposite(info, angle):
    return info[angle.lower()]

def getAdjacent(info, angle):
    if angle == "A":
        return info["b"]
    elif angle == "B":
        return info["a"]
    else:
        return info["c"]

def solve(info):
    solvedAngles = []
    solvedSides = []
    for var in info:
        if info[var] != 0:
            if var in "ABC":
                solvedAngles.append(var)
            else:
                solvedSides.append(var)
    
    solved = solvedAngles + solvedSides
    
    print("solved", solvedAngles, solvedSides, solved)

    if len(solvedSides) + len(solvedAngles) < 3:
        print("Not enough information!")
        return
    
    # first, easy ones
    if len(solvedAngles) == 2:  # solve for the other angle by simple math
        notSolved = "A" if not "A" in solvedAngles else "B" if not "B" in solvedAngles else "C"
        info[notSolved] = (180-(info[solvedAngles[0]] + info[solvedAngles[1]]))
    
    if len(solvedSides) == 2:  # solve for the other side by simple a^2 + b^2 = c^2 stuff
        notSolved = "a" if not "a" in solvedSides else "b" if not "b" in solvedSides else "c"
        if notSolved == "c":
            info["c"] = math.sqrt(info["a"]**2 + info["b"]**2)

    # sin and cos crap
    for val in "ABCabc":
        if not val in solved:
            # if val == "A"
            pass

triangleInfo = {
    "A": 0,
    "B": 0,
    "C": 0,
    "a": 0,
    "b": 0,
    "c": 0,
}

triangleAscii = ["A ┌",
                 "  │\\",
                 "  │ \\",
                 "  │  \\",
                 "  │   \\",
                 "b │    \\ c",
                 "  │     \\",
                 "  │      \\",
                 "  │       \\",
                 "  │        \\",
                 "C └─────────┘ B",
                 "       a        "]

running = True
while running:
    drawTriangle(triangleInfo)

    print("Enter command (e.x. \"quit\", \"A=#\", \"solve _\"):")
    inp = input("$ ")
    print()

    if inp == "q" or inp == "quit":
        running = False
    elif inp == "clear":
        for val in "ABCabc":
            triangleInfo[val] = 0
    elif inp.startswith("solve"):
        solve(triangleInfo)
    else:
        for var in "ABCabc":
            if inp.startswith(var + "="):
                try:
                    triangleInfo[var] = float(inp[2:])
                except ValueError:
                    break
