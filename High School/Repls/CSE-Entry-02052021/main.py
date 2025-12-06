#This code is buggy =-( - as in, it doesn't work ** Your job is to fix it!
"""
I am very hungry, but I don't know what to eat. Maybe there is an algorithm that can help me with that
"""

# `int(...)` removed to keep string as string
hunger = input("Am I hungry? (yes/no) ")
 
if hunger.lower() == "yes":
 # added `)` to end of statement below, so both int and input have closing `)`s
 cash = int(input("How much $$ do I have in my pocket? "))
 if cash >= 10:
   # MINOR: added `(yes/no)` to prompt below to make how to answer more clear
   store = input("Do I want to go out for food? (yes/no) ")
   # added `=` to make an assignment operator a comparison operator of the sort
   if store.lower() == "yes":
     print("Cool lets go get food")
   else:
     print("Guess we check the fridge...")
 # added `:` below to fix problem with missing colon
 else:
   print("Low on cash... Guess we check the fridge")
else:
 print("Nah, we good")
