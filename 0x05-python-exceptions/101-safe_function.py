#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error_error:
        print("Exception: {}".format(error_error), file=sys.stderr)
        return None
