#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a//b
    except (ZeroDivisionError, TypeError):
        result = none
    finally:
        print("inside results:{:d}".format(result))
    return (result)
