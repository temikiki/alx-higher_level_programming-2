#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = none
    finally:
        print("inside result: {}".format(result))
    return (result)
