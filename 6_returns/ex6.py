
# -----------------------------------------------------------------------------
# Exercise 6 - "The Chain"
#
# Although it's maybe a bit unusual in terms of Python style, one
# possibly nice thing about exercise 5 is that the after() function is
# very easy to reason about.  You give it a function as input, and it
# always returns a Result.  It doesn't raise any exceptions or return
# anything else.  That's it.
#
# However, in programming, it's also common to perform step-by-step
# sequencing of operations. For example, consider these three
# functions (type hints added to emphasize the kind of data expected):

from ex5 import Result, after

def A(x: int) -> int:
    return x + 10

def B(x: int) -> int:
    return x * 2

def C(x:int) -> int:
    return x * x

# Now, suppose you had some code that called each function, one after the other,
# feeding the output of one function into the input of the next function.

def chained(x:int) -> int:
    a = A(x)
    b = B(a)
    c = C(b)
    return c

assert chained(2) == 576

# Or alternatively, as a single composed operation (for improved job security):

def chained(x:int) -> int:
    return C(B(A(x)))

assert chained(2) == 576

# How would this kind of chaining work if you also included the use of
# the after() function above?  For example, if you wanted to do the
# same calculation, but with time delays. Note: This is expressed as
# pseudocode--it doesn't work as shown. You'll need to modify it to
# work with the after() function in Exercise 5.

def chained_after(x:int) -> int:
    a = after(1, A(x))     # Call a = A(x) after 1 second   (must modify)
    b = after(2, B(a))     # Call b = B(a), 2 seconds after that (must modify)
    c = after(3, C(b))     # Call c = C(b), 3 seconds after that (must modify)
    return c

# assert chained_after(2) == 576        # Uncomment

# Ponder your solution code for a bit.   Can you also rewrite it as
# a single composed expression? (i.e., like C(B(A(x))) above).
# Special bonus if you can also do it using nothing more than
# passing zero-argument lambda functions to after().

def chained_after_single_expr(x):
    return ... # everything above as a single expression

# assert chained_after_single_expr(2) == 576   # Uncomment

# One problem with the idea of chaining is that the syntax is messy.
# Even in the simple case, it reads backwards.  For example, it's
# written as:
#
#     C(B(A(x)))
#
# When the actual flow of data is as follows:
#
#     x -> A -> B -> C -> result
#
# Can you abuse Python's syntax to create some scheme for
# expressing a computation chain like this using your Result
# object?  For example:
#
#    r = Result(x) >> A >> B >> C
#    print(r.unwrap())           # Prints
#

def chained(x):
    r = Result(x) >> A >> B >> C
    return r.unwrap()

# assert chained(2) == 576    # Uncomment

# Challenge:
#
# Can you come up with some syntactic scheme that allows you to
# chain the after() function in the same manner.  For example:
#
#   A after 1 second -> B after 2 seconds -> C after 3 seconds
#
