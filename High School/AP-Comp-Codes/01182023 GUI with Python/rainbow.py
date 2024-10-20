import tkinter as tk
import random

root = tk.Tk()
root.geometry("1588x1000")

frames = []
rgbVals = "0123456789abcdef"

for i in range(794):
    colors = "#"
    for j in range(6):
        colors += (random.choice(rgbVals))
    newFrame = tk.Frame(root, width=2, height=1000, background=colors)
    frames.append(newFrame)

for frameIndex in range(len(frames)):
    frames[frameIndex].grid(row=0, column=frameIndex)

root.mainloop()