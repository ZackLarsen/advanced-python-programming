# -----------------------------------------------------------------------------
# Exercise 6
#
# Discussion: Are named tuples the right data structure for this?
# Representing a fraction as a tuple might be convenient, but
# it's also kind of weird. Tuples support a variety of "mathy"
# operations that don't align with fractions. For example:
#
#     >>> a = make_frac(2, 3)
#     >>> a * 2
#     (2, 3, 2, 3)
#     >>> b = make_frac(4, 5)
#     >>> a + b
#     (2, 3, 4, 5)
#
# Tuples also support operations that don't make sense for numbers at all.
# For example, iteration:
#
#     >>> for x in a:
#     ...     print(x)
#     ...  
#     2
#     3
#     >>>
# 
# Replace tuples with a properly defined "Fraction" class that's NOT a
# named tuple.  Only change the Fraction class.  MAKE NO OTHER CHANGES
# TO EXISTING CODE.  A major principle of data abstraction is that you
# should be able to swap out a different data representation without
# breaking everything as long as you're following the same API. As
# long as your new class provides .numerator and .denominator
# attributes, all of the existing functions such as add_frac(),
# mul_frac(), etc. should continue to work after you've made the
# change.
#
# Discussion: Duck typing.  As a dynamically typed language, Python
# doesn't care so much about the "types" of objects as it does about
# the appearance of objects.  If you provide an object that has the
# required .numerator and .denominator attributes, it doesn't really
# matter what it is.  The functions such as add_frac() aren't coded or
# compiled to use any specific type.  This is why the integers worked:
#
#     >>> a = make_frac(2, 3)
#     >>> b = add_frac(a, 1)       # Add an integer
#     >>> b.numerator, b.denominator
#     (5, 3)
#     >>>
#
# Integers happen to provide .numerator and .denominator attributes
# so it just started "working" as if by magic.
# -----------------------------------------------------------------------------

def gcd(a, b):
    # Greatest common divisor
    while b:
        a, b = b, a % b
    return a

class Fraction:
#    ... # You complete

# Do not change any of the other functions.  Paste from earlier exercises.

# Unit tests must still pass
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
