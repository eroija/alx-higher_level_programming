#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0

    try:
        for i in range(x):
            try:
                value = my_list[i]
                print("{:d}".format(value), end=" ")
                total += 1
            except ValueError:
                pass
    except IndexError:
        pass
    finally:
        print()
        return total
