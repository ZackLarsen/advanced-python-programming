# frac.py
# -----------------------------------------------------------------------------
# Introduction:
#
# Peter needed to help his daughter Eva do her 5th grade math homework
# on fractions.  Remembering a bit of math, knowing that Python had
# tuples, and recalling a bit of code from an dusty blue Wizard CS
# textbook, he wrote the following functions and said "maybe these
# can help you:"

def add_frac(a, b):
    return (a[0]*b[1] + a[1]*b[0], a[1]*b[1])

def sub_frac(a, b):
    return (a[0]*b[1] - a[1]*b[0], a[1]*b[1])

def mul_frac(a, b):
    return (a[0]*b[0], a[1]*b[1])

def div_frac(a, b):
    return (a[0]*b[1], a[1]*b[0])

# In this code, fractions are stored as a tuple containing the
# numerator and denominator.  For example, the fraction 2/3 is
# written as follows:
#
#   >>> a = (2, 3)
#   >>>
#
# To perform various mathematical operations, the above functions
# are used. Here's a sample of how they work.

a = (2, 3)
b = (3, 4)
assert add_frac(a, b) == (17, 12)
assert mul_frac(a, b) == (6, 12)

# As a refresher, here are the rules for arithmetic with fractions:
#
#   n1   n2   n1*d2 + d1*n2
#   -- + -- = -------------
#   d1   d2       d1*d2
#
#   n1   n2   n1*d2 - d1*n2
#   -- - -- = -------------
#   d1   d2       d1*d2
#
#   n1   n2   n1*n2
#   -- * -- = -----
#   d1   d2   d1*d2
#
#   n1   n2   n1*d2
#   -- / -- = -----
#   d1   d2   d1*n2
#
# Take a look at the code, convince yourself that it probably works.

# -----------------------------------------------------------------------------
# Exercises
#
# We're going to work a series of 8 exercises, found in the files
# ex1.py - ex8.py.  Each of them build upon the idea of implementing
# Fractions, but in different ways and with different aspects of design.
# Be aware, you may have to copy/paste code between exercises.  They
# also get progressively more advanced as you go.  Expect discussion
# as we work on it.
