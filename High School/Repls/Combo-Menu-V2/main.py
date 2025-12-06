# iteration 2, cleaned up code, added lists and the removing of items by user choice

order = []
orderTotal = 0
# 0 = burger, 1 = drink, 2 = fries, 3 = ketchup (quantity)

def orderCalc():
  # burger
  global orderTotal
  orderTotal = 0  # resetting to avoid being a bad restaurant
  if order[0] == "Chicken":
    orderTotal += 5.25
  elif order[0] == "Beef":
    orderTotal += 6.25
  elif order[0] == "Tofu":
    orderTotal += 5.75
  # drink
  if order[1] == "Small":
    orderTotal += 1.00
  elif order[1] == "Medium":
    orderTotal += 1.75
  elif order[1] == "Large":
    orderTotal += 2.25
  # fries
  if order[2] == "Small":
    orderTotal += 1.00
  elif order[2] == "medium":
    orderTotal += 1.75
  elif order[2] == "Large":
    orderTotal += 2.25
  elif order[2] == "Mega":
    orderTotal += 1.00
  # Ketchup
  orderTotal += order[3]*0.25

# Burger
print("Which type of sanwich would you like to order?")
print("1- Chicken | ($5.25)")
print("2- Beef    | ($6.25)")
print("3- Tofu    | ($5.75)")
burgSel = int(input("$ "))
if burgSel == 1:
  order.append("Chicken")
elif burgSel == 2:
  order.append("Beef")
else:
  order.append("Tofu")

# Drink
ynDrink = input("\nWould you like a drink? (Y/n)\n$ ")
if not ynDrink or ynDrink.lower() == "y":
	print("\nWhat size drink?")
	print("1- Small  | ($1.00)")
	print("2- Medium | ($1.75)")
	print("3- Large  | ($2.25)")
	drinkSel = int(input("$ "))
else:
	order.append("No Drink")

if drinkSel == 1:
  order.append("Small")
elif drinkSel == 2:
  order.append("Medium")
else:
  order.append("Large")

# Fries
ynFries = input("\nWould you like fries? (Y/n)\n$ ")
if not ynFries or ynFries.lower() == "y":
  print("\nWhat size fries?")
  print("1- Small  ($1.00)")
  print("2- Medium ($1.50)")
  print("3- Large  ($2.00)")
  friesSel = int(input("$ "))
  # ooo here comes the nesting so scarryyryry! ._.
  if friesSel == 1:
    ynMegaFries = input("\nWould you like to mega-size your fries? (Y/n)\n$ ")
    if not ynMegaFries or ynMegaFries.lower():
      order.append("Mega")
      print("-- Fries have been Mega-Sized! --")
    else:
      order.append("Small")
      print("-- Fries not Mega-d --")
  elif friesSel == 2:
    order.append("Medium")
  else:
    order.append("Large")
else:
  order.append("No Fries")

# Ketchup
ynKetchup = input("\nWould you like any ketchup packets? (Y/n)\n$ ")
if not ynKetchup or ynKetchup.lower() == "y":
  order.append(int(input("\nHow many? ($0.25/packet)\n$ ")))
else:
  print("-- No Ketcup Selected --")
  order.append(0)

print("\n/-/-/-/-/-/-/-/-/-/-/\n\nYou chose: ")
print("\nBURGER:\n- " + order[0])
print("\nDRINK:\n- " + order[1])
print("\nFRIES:\n- " + order[2])
print("\nKETCHUP:\n- " + str(order[3]) + " packets")

orderCalc()

if order[0] != "No Burger" and order[1] != "No Drink" and order[2] != "No Fries":
  orderTotal -= 1.00
  print("-- $1.00 DISCOUNT for ordering combo")
print("\nTOTAL: $" + str(orderTotal))

print("\nDo you want to remove anything? (Y/n)")
removeYN = input("$ ")

# removing items from list
if not removeYN or removeYN.lower() == "y":
  rm = input("Which would you like to remove?\n$ ")
  if rm == "Beef" or rm == "Chichen" or rm == "Tofu":
    order[0] = "No Burger"
  if rm == "Small" or rm == "Medium" or rm == "Large":
    order[1] = "No Drink/Fries"
  if rm == "Mega":
    order[2] = "No Fries"
  if rm == str(order[3]):
    order[3] = 0

orderCalc()

print("\nBURGER:\n- " + order[0])
print("\nDRINK:\n- " + order[1])
print("\nFRIES:\n- " + order[2])
print("\nKETCHUP:\n- " + str(order[3]) + " packets")

if order[0] != "No Burger" and order[1] != "No Drink" and order[2] != "No Fries":
  orderTotal -= 1.00
  print("-- $1.00 DISCOUNT for ordering combo")
print("\nTOTAL: $" + str(orderTotal))
print("Enjoy your food :3")
