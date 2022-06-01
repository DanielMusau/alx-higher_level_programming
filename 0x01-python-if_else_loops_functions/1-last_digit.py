#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
	newnumber = number % 10
else:
	newnumber = number % -10


if newnumber > 5:
	print("Last digit of {:d} is {:d} and is greater than 5".format(number, newnumber))
elif newnumber == 0:
	print("Last digit of {:d} is {:d} and is 0".format(number, newnumber))
elif newnumber < 6 and newnumber != 0:
	print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, newnumber))
