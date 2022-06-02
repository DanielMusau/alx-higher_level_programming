#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{}".format(i))
    elif i == 1:
        print("{}".format(sys.argv[i]))
    elif i > 1:
        sum = 0
        for a in sys.argv:
            if a != sys.argv[0]:
                sum += int(a)
        print(sum)
