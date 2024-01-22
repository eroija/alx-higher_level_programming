#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0

    for i in my_list:
        try:
            if isinstance(i, int):
                print("{:d}".format(i), end="")
                total += 1
        except ValueError:
            pass
    print()
    return total
