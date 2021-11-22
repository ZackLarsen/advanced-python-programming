# -----------------------------------------------------------------------------
# Exercise 1 - The requirements
#
# "Dad, I used the code in frac.py and I lost all sorts of points. For
# example, I produced one answer of (6, 12). The teacher wanted (1, 2)
# instead. Can you change the code to put answers in lowest terms?"
#
# "Also, the teacher told us to never put a negative number in the
# denominator.  So, you'd never write (2, -3).  Instead you'd write
# (-2, 3).  Also, (-2, -3) should just be written as (2, 3)."
#
# "And last, but not least, what is with that code you wrote?  I can
# hardly read anything that's going on in there with all of that tuple
# indexing."
#
# To fix all of these problems, you decide to introduce a few helper
# functions.  A make_frac() function will be used to construct the
# tuples and put things in lowest terms. To hide tuple indexing,
# you'll use numerator() and denominator() functions.

def gcd(a, b):
    # Greatest common divisor
    while b: 
        a, b = b, a % b 
    return a
    
def make_frac(numer, denom):
    d = gcd(numer, denom)
    return (numer // d, denom // d)

def numerator(f):
    return f[0]

def denominator(f):
    return f[1]

# Your task.  Rewrite the add_frac(), sub_frac(), mul_frac(), and
# div_frac() functions to ONLY use the above functions.  Then, make
# sure the unit tests below pass.  

def add_frac(a, b):
    pass

def sub_frac(a, b):
    pass

def mul_frac(a, b):
    pass

def div_frac(a, b):
    pass
    
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
