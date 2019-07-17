#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error_error:
        print("Exception: {}".format(error_error.args[0]), file=sys.stderr)
        return False
    return True
