# -----------------------------------------------------------------------------
# Exercise 2
#
# It seems that the after() function only works if you give it a
# function taking no arguments.  Is there any way to make it work with
# a function that takes any set of arguments?  Can you do this without
# making any code changes?

import time

def after(seconds, func):
    time.sleep(seconds)
    return func()

def add(x, y):
    print(f'Adding {x} + {y} -> {x + y}')
    return x + y

# This doesn't work. Why?  Can you fix it in some way?
result = after(10, add(2, 3))

