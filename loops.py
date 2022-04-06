"""
CP1404/CP5632 - Practical
Loops exercises
"""
#sequence of odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#sequence in 10s from 0 to 100
for t in range(0, 101, 10):
    print(t, end=' ')
print()

#descending sequence from 20 to 1
for x in range(20, 0, -1):
    print(x, end=' ')

#asks user for a specific number and print that much stars
amount = int(input("Number of stars: "))
for s in range(amount):
    print('*', end=' ')
print()

#asks user for a specific number and print n lines of increasing stars
amount = int(input("Number of stars: "))
for y in range(1, amount + 1):
    print('*' * y)
print()