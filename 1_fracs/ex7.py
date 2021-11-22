# -----------------------------------------------------------------------------
# Exercise 7
#
# Modeling fractions as a data structure with a collection of
# standalone functions isn't very "Pythonic."  Python has a protocol
# for manipulating numbers via operators such as +, -, *, and /.
# These operators are mapped to methods such as __add__() and __mul__().
#
# Modify the Fraction class of Exercise 6 to behave like a proper
# Python number.  To do this, you'll need to implement a variety of
# so-called "magic" methods such as __add__, __sub__, __mul__, etc.
# Some later stages of the exercise have you make it a bit nicer
# to work with by implementing a few other methods.
#
# The following test function tests the features that you need to
# support. In adding these functions, you're not allowed to break old
# functionality. The old unit tests should still pass.
# -----------------------------------------------------------------------------

def gcd(a, b):
    # Greatest common divisor
    while b:
        a, b = b, a % b
    return a

class Fraction:
    ...

# The old unit tests must still pass (legacy code)
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


# New unit tests.  These manipulate fractions as proper Python numbers.
def test_math():
    a = Fraction(4, 6)
    assert (a.numerator, a.denominator) == (2, 3)

    b = Fraction(-3, -4)
    assert (b.numerator, b.denominator) == (3, 4)

    c = a + b
    assert (c.numerator, c.denominator) == (17, 12)

    d = a - b
    assert (d.numerator, d.denominator) == (-1, 12)

    e = a * b 
    assert (e.numerator, e.denominator) == (1, 2)

    f = a / b
    assert (f.numerator, f.denominator) == (8, 9)

    # Mixed type operations.  Note: Python integers
    # already have .numerator and .denominator attributes

    g = a + 1
    assert (g.numerator, g.denominator) == (5, 3)

    g = 1 + a
    assert (g.numerator, g.denominator) == (5, 3)

    h = a * 10
    assert (h.numerator, h.denominator) == (20, 3)

    h = 10 * a
    assert (h.numerator, h.denominator) == (20, 3)

    # Comparisons.  For these, you'll need to implement
    # methods such as __eq__(), __ne__(), __lt__(), __le__(),
    # __gt__(), and __ge__().
    #
    # To compare fractions you can perform comparisons like this:
    #
    # a = Fraction(2, 3)
    # b = Fraction(4, 5)
    #
    # a < b  ==> a.numerator * b.denominator < a.denominator * b.numerator

    assert a < b
    assert a <= b
    assert a != b
    assert b > a
    assert b >= a
    assert a == Fraction(2, 3)

    print('Good math')

test_math()

# -----------------------------------------------------------------------------
# Niceties
#
# There are certain things you can do to make your objects play nicer
# with the rest of Python.  These include nice printing, debugging, 
# and numeric conversions.
#
# Modify your Fraction class so that it additionally passes the following tests
# -----------------------------------------------------------------------------

def test_nice():
    a = Fraction(3, 2)

    assert str(a) == '3/2'                # Requires the __str__() method
    assert repr(a) == 'Fraction(3, 2)'    # Requires the __repr__() method
    assert float(a) == 1.5                # Requires the __float__() method
    assert int(a) == 1                    # Requires the __int__() method

    # Special cases of nice output
    b = Fraction(2, 1)
    assert str(b) == '2'

    c = Fraction(0, 2)
    assert str(c) == '0'

    print('Nice fractions')

# Uncomment when ready
# test_nice()


# -----------------------------------------------------------------------------
# Immutability
#
# One issue with the Fraction class is that it allows the .numerator and
# .denominator attributes to be mutated after creation.
#
#    >>> a = Fraction(2, 3)
#    >>> a.numerator = 1
#    >>> a
#    Fraction(1, 3)
#    >>>
#
# This is often not desired.  Fix Fraction so that these attributes
# can't be changed once set.  Also, make sure you can put Fractions in
# dictionaries and sets.   To do this, you need to make sure your class
# defines a __hash__() method as well as __eq__().
# -----------------------------------------------------------------------------

def test_immutability():
    a = Fraction(1, 2)
    try:
        a.denominator = 4
        assert False, "denominator is mutable"
    except AttributeError:
        pass

    try:
        a.numerator = 3
        assert False, "numerator is mutable"
    except AttributeError:
        pass

    # Test sets and dictionary keys
    d = { Fraction(1, 2) : 'a',
          Fraction(3, 4) : 'b' }

    assert d[Fraction(1,2)] == 'a'
    assert d[Fraction(3,4)] == 'b'

    e = { Fraction(1, 2), Fraction(3, 4) }

    assert Fraction(1, 2) in e
    assert Fraction(3, 4) in e

    print('Good immutability')

# Uncomment
# test_immutability()
