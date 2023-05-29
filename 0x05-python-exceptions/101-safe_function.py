#!/usr/bin/python3
def safe_function(fct, *args):
    '''Executes a function safely'''
    try:
        result = fct(*args)
        return (result)
    except Exception as ex:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return None
