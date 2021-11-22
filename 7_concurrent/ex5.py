# -----------------------------------------------------------------------------
# Exercise 5
#
# What about the time.sleep() calls in the Exercise 4 code.   Is there some way
# to implement that functionality in some way that actually works?  (Meaning
# that the countdown generator produces output 3 times faster than the 
# countup generator).  
#

# Paste your code from Exercise 4 here.  You will modify it slightly.


# Your task is to implement a generator based sleep() function below.
# This function can only use a single "yield" statement with no
# arguments.  It can only use functionality that you already wrote and
# possibly the Task class above.

def sleep(seconds):
    ...    # You implement
    yield

# The countdown() and countup() functions will be modified to use "yield from"
# as follows.  Note: "yield from" is a way to make one generator call
# another one as a kind of subroutine.

def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield from sleep(1)
        n -= 1

def countup(stop):
    x = 0
    while x < stop:
        print('Up we go', x)
        yield from sleep(3)
        x += 1

        
# Try running these tasks using your new code.  See if you
# get the correct behavior where countdown() outputs three times
# as fast as countup.

# run_tasks()       # Uncomment

