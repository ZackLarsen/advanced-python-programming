# -----------------------------------------------------------------------------
# Exercise 4
#
# An alternative approach to the concurrency approach is to use a 
# clever hack involving generator functions.  Normally, generator
# functions are used for custom iteration patterns.  For example:
#
#     def countdown(n):
#         while n > 0:
#             yield n
#             n -= 1
# 
#     for x in countdown(5):
#         print('T-minus', x)
#
#
# However, they can also be used to implement concurrency. 
# Consider the following two generators:

import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        time.sleep(1)
        n -= 1
        yield

def countup(stop):
    x = 0
    while x < stop:
        print('Up we go', x)
        time.sleep(3)
        x += 1
        yield

# These are the same two functions that you had in the last part.
# Just one extra "yield" statement has been added.   Here's an
# example of running the two functions concurrently.

def run_generators():
    generators = [ countdown(15), countup(5) ]
    while generators:
        gen = generators.pop(0)
        try:
            next(gen)
            generators.append(gen)
        except StopIteration:
            pass

run_generators()         # Comment out later

# -----------------------------------------------------------------------------
# YOUR TASK:
#
# Now, you might be thinking... maybe we could reinvent our whole
# approach to concurrency to use generator functions instead of all of
# that mess with callbacks.  You would be wrong.  Your challenge is to
# define a single class "Task" that wraps a generator and makes it run
# IN THE CONCURRENCY CODE YOU ALREADY WROTE (ex2.py).  You are
# not allowed to change that code in any way.  You can only import it
# here.  Moreover, you're not allowed to change any of the above
# generator functions either.

class Task:
    ...   # You implement.  This class is the only code you can define.


def run_tasks():
    import ex2
    t1 = Task(countdown(15))
    t2 = Task(countup(5))
    # Make t1 and t2 run concurrently using earlier code. No modifications.
    # ex2.???               
    # ex2.???
    # ex2.run(???)

# run_tasks()          # Uncomment

