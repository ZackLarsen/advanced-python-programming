# -----------------------------------------------------------------------------
# Exercise 7.
#
# "The Concurrent." Although Mary has been pondering the after()
# function, it turns out that her real task is a bit more complicated.
# What she *really* wants to implement is a delayed function evaluator
# that allows other parts of the program to run while the delayed
# function works in the background.   For this, she's decided to
# use threads.   Here's an example:

import threading
import time

def delayed(seconds, func):
    def helper():
        time.sleep(seconds)
        return func()
    threading.Thread(target=helper).start()

# If you haven't used threads before, the key idea is that a
# thread runs a function independently, and concurrently, with other
# code that happens to be running.  In the above example, the
# delayed() function returns immediately.  However, the internal
# helper() function continues to run in the background. 
#
# Here's an example, that illustrates how it works. Carefully study
# the output of running this.

def delayed_example():
    delayed(3, lambda: print("3 seconds have passed"))
    delayed(5, lambda: print("5 seconds have passed"))
    delayed(7, lambda: print("7 seconds have passed"))
    n = 10
    while n > 0:
        print('T-minus', n)
        time.sleep(1)
        n -=1
        
# Uncomment.  See what the above code produces.
# delayed_example()     

# This is all fine, but actually the problem is more complex.
# You see, Mary actually wants to be able to get a result back
# from the delayed function.  For example, something like this
# (pseudocode):

def add(x, y):
    return x + y

def delayed_results():
    r1 = delayed(3, lambda: add(2, 3))
    r2 = delayed(5, lambda: add(4, 5))
    r3 = delayed(7, lambda: add(6, 7))
    n = 10
    while n > 0:
        print('T-minus', n)
        time.sleep(1)
        n -=1
    print("r1=", r1)     # --> 5
    print("r2=", r2)     # --> 9
    print("r3=", r3)     # --> 13

# Your challenge:  How would you design and/or change the delayed()
# function to have it return a proper result from the delayed
# functions?   Just to be clear, those functions run in separate
# threads and allow other code to execute at the same time.
#
# Note: This is also a nuanced problem with many complexities.
# However, putting things in a box might help.
#
# Uncomment when ready
# delayed_results()

