# -----------------------------------------------------------------------------
# Exercise 2 
#
# "Dad? Tuples? Accessor functions? Really? What is this?"
#
# Grumbling, Peter starts thinking about the general design problem of
# data abstraction.  Despite his use of tuples, the functionality of
# his code is still fairly well organized into layers.  For example,
# none of the core math functions (add_frac, sub_frac, mul_frac, etc.)
# know anything about tuples.  Instead, they use the accessor
# functions such as numerator(r) and denominator(r).  Fractions are
# always constructed using make_frac().  Abstraction is good.
#
# "I'll show her!" 
# 
# Peter decides that he can easily change his code to use dictionaries 
# without breaking anything else.  All he needs to do is change the
# make_frac(), numerator(), and denominator() functions.  Nothing else
# needs to change, including the tests.

def gcd(a, b):
    # Greatest common divisor
    while b: 
        a, b = b, a % b 
    return a

def make_frac(numer, denom):
    return { ... }         # Return a dictionary of some kind

def numerator(f):
    pass

def denominator(f):
    pass

# Paste the implementation of add_frac(), sub_frac(), mul_frac(), div_frac()
# from ex1.py here. MAKE NO CHANGES TO THAT CODE.


# Unit tests.  This is the same set of tests as before.  NO CHANGES MADE.    
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
