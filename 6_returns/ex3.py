# -----------------------------------------------------------------------------
# Exercise 3
#
# You're the designer of the after() function.  What is your suggested
# "best solution" for making the function easy to use with *any*
# function that a user might provide?
#
# This is a surprisingly nuanced problem because Python functions can
# be called in many different ways.  For example:
#
#     def func(x, y z):
#         ...
#
#     func(1, 2, 3)          # Positional arguments
#     func(x=1, y=2, z=3)    # Keyword arguments
#     func(1, z=3, y=2)      # Position/keyword argument mix
#
#     args = (1,2,3)
#     func(*args)            # Passing a tuple as positional arguments
#
#     kwargs = { 'x': 1, 'y':2, 'z': 3 }
#     func(**kwargs)         # Passing a dict as keyword arguments
#
# To make matters even more complicated, a function can force the
# use of keyword argumentss:
#
#     def func(x, *, y):
#         ...
#
#     func(1, 2)                # Error. y not supplied by keyword
#     func(1, y=2)              # Ok!
#
# Plus, there are functions that accept any number of positional
# or keyword arguments:
#
#     def func(*args, **kwargs):
#         ...
#
# And in more recent versions of Python, positional-only functions:
#
#     def func(x, y, /, z):
#         ...
#
#     func(1, 2, 3)     # OK
#     func(1, 2, z=3)   # OK
#     func(1, y=2, z=3) # ERROR.
#
# -----------------------------------------------------------------------------

import time

# Modify this function as appropriate to make it easy for a user to
# supply a function with any combination of arguments.

def after(seconds, func):
    time.sleep(seconds)
    return func()

# Show how you would call the following functions with your modified after()
# function.  A solution involving lambda is shown below.  You're allowed to
# change any part of this that you want.  Can you make something that's
# nice to use, but which doesn't involve lambda?

# Simple function taking two arguments
def add(x, y):
    print(f'Adding {x} + {y} -> {x + y}')
    return x + y

r = after(5, lambda: add(2, 3))

# Simple function taking keyword-only  arguments
def duration(*, hours, minutes, seconds):
    x = 3600*hours + 60*minutes + seconds
    print('Duration:', x)
    return x

d = after(5, lambda: duration(hours=2, minutes=5, seconds=37))
print(d)

# How would you use your after() function to carry out the following
# operation after 5 seconds?

r = after(5, add(add(1,2), add(3,4)))
