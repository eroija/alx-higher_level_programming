#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import math

    result = 0
    vector = sys.argv - 1
    for i in vector:
        result += int(i)
        print("{}".format(result))
