#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    newnumber = number % 10
else:
    newnumber = number % -10

print("Last digit of", end=" ")
if newnumber > 5:
    print("{} is {} and is greater than 5".format(number, newnumber))
elif newnumber == 0:
    print("{} is {} and is 0".format(number, newnumber))
elif newnumber < 6 and newnumber != 0:
    print("{} is {} and is less than 6 and not 0".format(number, newnumber))
