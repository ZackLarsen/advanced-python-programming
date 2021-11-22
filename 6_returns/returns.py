# returns.py
#
# Objective: Explore function evaluation, delayed evaluation, error
# handling, composition of operations, and the problem of
# communicating results.  Plus, a tiny bit of concurrency.
# -----------------------------------------------------------------------------
#
# Mary has been pondering the mysteries of the universe, time, and
# function evaluation. In this project, we're going to sneak in and
# join her.  Let's peek inside her mind...
#
# ... ah, we see that Mary is currently pondering the following
# function.  It accepts a time delay and a function callback.  The
# evaluation of the supplied function is delayed and its result
# returned. Very exciting! Maybe it's meant to make a normal function
# mimic the performance of a microservice in the "cloud."

import time

def after(seconds, func):
    time.sleep(seconds)
    return func()

# Proceed to exercise 1 in ex1.py







