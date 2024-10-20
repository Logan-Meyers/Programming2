letters = "abcdefghijklmnopqrstuvwxyz"
complete = ""

for i in range(len(letters)):
    complete += letters[i]*(i+1) + " "

print(complete)