#!/usr/bin/python3
def safe_print_integer_err(value):
    line = 0
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        print("Exception: {}".format(sy.exc_info()[1]), file=sys.stderr)
        return (False)

    

