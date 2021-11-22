# ------------------------------------------------------------------------------
# Exercise 1
#
# Try calling the after function with a simple "Hello World" example. Make
# sure you understand how it works.
# -----------------------------------------------------------------------------

import time

def after(seconds, func):
    time.sleep(seconds)
    return func()

def greeting():
    print('Hello World')

# How do you use the greeting() function with the after() function above?
# That is, have the after() function call greeting() after 10 seconds.
