#!/usr/bin/python3
def safe_print_integer_err(value):
    ''' prints an integer'''
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (False)
    else:
        return (True)
