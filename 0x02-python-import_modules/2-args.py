#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num = len(sys.argv) - 1

    if num < 1:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{} argument: ".format(num))
    else:
        print("{} arguments:".format(num))

    for i in range(1, num):
        print("{}: {}".format(i, sys.argv[i]))
