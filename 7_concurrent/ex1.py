# -----------------------------------------------------------------------------
# Exercise 1 - Concurrency
#
# Consider the following two functions.

import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        time.sleep(1)
        n -= 1

def countup(stop):
    x = 0
    while x < stop:
        print('Up we go', x)
        time.sleep(3)
        x += 1

# Normally, functions execute sequentially--meaning one after the
# other.  For example, observe the output of the following code.

countdown(15)
countup(5)

# -----------------------------------------------------------------------------
# YOUR TASK:
#
# Figure out a way for both of the above functions to execute
# concurrently, producing interleaved output like this:
#
#    T-minus 15      (1 sec delay)
#    Up we go 0      (3 sec delay)
#    T-minus 14      (1 sec delay)
#    Up we go 1      (3 sec delay)
#    T-minus 13
#    Up we go 2
#    T-minus 12
#    Up we go 3
#    T-minus 11
#    Up we go 4
#    T-minus 10
#    T-minus 9
#    T-minus 8
#    ...
#    T-minus 1
#
# THE CATCH: You are not allowed import any outside module to do it.
# Moreover, you're not allowed to use any feature of Python other than
# ordinary function calls.  That means no threading, no subprocesses,
# no async, no generators, or anything else. You need to figure out
# how to get something resembling concurrency to work all on your own
# without the support of any library.
# 
# You ARE allowed to change the implementation of the original functions
# and to write any other supporting code you might need to do it--as
# long as that support code only involves normal Python functions.

