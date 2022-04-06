"""
CP1404/CP5632 - Practical
Program that allows user to enter number of items and its price, then calculating the total
"""
total = 0
items = int(input("Number of item(s): "))
while items < 0:
    print("Invalid number.")
    items = int(input("Number of item(s): "))

for i in range(items):
    price = float(input("Price of item: $"))
    total += price

if total > 100:
    discount = 0.1 * total
    total -= discount

print("Total price for " + str(items) + " items is ${:.2f}".format(total))