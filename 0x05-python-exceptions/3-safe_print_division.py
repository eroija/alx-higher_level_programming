#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Exception: {e}", file=sys.stderr)
        result = None
    else:
        print("Inside result: {}".format(result))
        return result
