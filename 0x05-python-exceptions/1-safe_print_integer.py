#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: You have to use \"{0:d}\".format()", file=sys.stderr)
        return False
