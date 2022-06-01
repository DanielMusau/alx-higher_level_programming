#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        newnumber = number % 10
    else:
        newnumber = number % -10
        newnumber *= -1

    print("{}".format(newnumber), end="")
    return newnumber
