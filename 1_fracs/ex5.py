# -----------------------------------------------------------------------------
# Exercise 5
#
# The function make_frac() is used to construct fractions. One feature
# of make_frac() is that it puts a fraction number into lowest terms and
# normalizes the sign to always appear in the numerator.  For example:
#
#    >>> a = make_frac(4, -6)
#    >>> a.numerator
#    -2
#    >>> a.denominator
#    3
#    >>>
#
# How would you modify the Fraction namedtuple class to have the same 
# behavior if you used its normal constructor?
#
#    >>> a = Fraction(4, -6)
#    >>> a.numerator
#    -2
#    >>> a.denominator
#    3
#    >>>
#
# Disclaimer:  This is hard and not obvious.  But, it points to deeper
# problems. Maybe NamedTuple is not the solution we seek. 
# -----------------------------------------------------------------------------

from typing import NamedTuple

def gcd(a, b):
    # Greatest common divisor
    while b: 
        a, b = b, a % b 
    return a

class Fraction(NamedTuple):
    numerator : int
    denominator : int
    # You'll need to make modifications to pass the test below

def test_frac():
    a = Fraction(4, 6)
    assert a.numerator == 2
    assert a.denominator == 3

    b = Fraction(-3, -4)
    assert b.numerator == 3
    assert b.denominator == 4

    c = Fraction(3, -4)
    assert c.numerator == -3
    assert c.denominator == 4

    print("Good fractions")

test_frac()

