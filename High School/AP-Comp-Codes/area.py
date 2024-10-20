import math

side1 = float(input("side 1: "))
side2 = float(input("side 2: "))
side3 = float(input("side 3: "))

s = (side1 + side2 + side3) / 2
heron = math.sqrt((s * (s - side1) * (s - side2) * (s - side3)))
print(f"answer: {heron}")