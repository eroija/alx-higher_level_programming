#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0

    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end=" ")
                total += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        pass
    finally:
        print()
        return total
