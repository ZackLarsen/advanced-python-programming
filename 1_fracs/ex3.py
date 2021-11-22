# -----------------------------------------------------------------------------
# Exercise 3 
#
# During your coffee break, you decide to show your fraction code to a 
# Lisp programmer at the office.
#
# "You know, you could really shatter 5th grade minds if you
# represented fractions entirely as a function.  Here, something like
# this:"

def gcd(a, b):
    # Greatest common divisor
    while b: 
        a, b = b, a % b 
    return a

def make_frac(numer, denom):
    d = gcd(numer, denom)
    numer = numer // d
    denom = denom // d
    def frac(s):
        return numer if s else denom
    return frac

def numerator(f):
    return f(True)

def denominator(f):
    return f(False)

# What is this madness?  Paste your implementation of add_frac(),
# sub_frac(), mul_frac(), and div_frac() here.  MAKE NO CHANGES. 
# Verify that it still passes all of the unit tests--somehow.

... # Your code here

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

# As you collect the pieces of your brain, ponder the fact that those
# top level functions make_frac(), numerator(), and denominator()
# really saved you a lot of hassle here.   Yes, the underlying
# representation changed into something else, but none of the
# higher level code had to change.

