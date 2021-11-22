# -----------------------------------------------------------------------------
# Exercise 4
#
# "Dad, have you ever considered using a named tuple?"  For example:

from typing import NamedTuple

class Fraction(NamedTuple):
    numerator : int
    denominator : int

def gcd(a, b):
    # Greatest common divisor
    while b: 
        a, b = b, a % b 
    return a

def make_frac(numer, denom):
    ... # You define

def numerator(f):
    ... # You define

def denominator(f):
    ... # You define

# Paste in your earlier code for add_frac, sub_frac, mul_frac, div_frac.
# It should work without modification.

# Unit tests. These are the same tests as before. NO CHANGES MADE.
def test_frac():
    a = make_frac(4, 6)
    assert (numerator(a), denominator(a)) == (2, 3)

    b = make_frac(-3, -4)
    assert (numerator(b), denominator(b)) == (3, 4)

    c = make_frac(3, -4)
    assert (numerator(c), denominator(c)) == (-3, 4)

    d = add_frac(a, b)
    assert (numerator(d), denominator(d)) == (17, 12)

    e = sub_frac(a, b)
    assert (numerator(e), denominator(e)) == (-1, 12)

    f = mul_frac(a, b)
    assert (numerator(f), denominator(f)) == (1, 2)

    g = div_frac(a, b)
    assert (numerator(g), denominator(g)) == (8, 9)

    print("Good fractions")

test_frac()

# ----------------------------------------------------------------------
# Did you know that the math functions can now also work with normal 
# integers if you implement the accessor functions so that they use
# the dot (.) for attribute access?  Try this:
#
#     def numerator(a):
#         return a.numerator
#
#     def denominator(a):
#         return a.denominator
#
# Verify that it works:
#
#     >>> a = make_frac(2, 3)
#     >>> b = add_frac(a, 1)
#     >>> b
#     Fraction(numerator=5, denominator=3)
#     >>>
#
# Can you explain why this works?

