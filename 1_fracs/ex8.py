# -----------------------------------------------------------------------------
# Exercise 8 - Fractran
#
# John Conway, perhaps most well known in programmer circles for the "game of
# life" (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is also
# the inventor of Fractran, a programming language wherein programs are
# represented entirely by lists of fractions (see https://en.wikipedia.org/wiki/FRACTRAN)
#
# The rules of evaluation as follows:
#
# For a given integer n, scan a list of fractions and compute n*f.
# For the first fraction where n*f is an integer, replace n with n*f
# and repeat the process from the beginning.  Continue in this manner
# until no fraction f produces n*f as an integer. Return the last
# value of n.
#
# See if your fraction implementation can run Fractran

from ex7 import Fraction

# The evaluator
def run(prog, n):
    while True:
        for f in prog:
            nf = f * n
            if nf.denominator == 1:
                n = nf
                break
        else:
            return n

# Here is a sample Fractran program that computes Fibonacci numbers
fibcode = [ 
    Fraction(17, 65),
    Fraction(133, 34),
    Fraction(17, 19),
    Fraction(23, 17),
    Fraction(2233, 69),
    Fraction(23, 29),
    Fraction(31, 23), 
    Fraction(74, 341),
    Fraction(31, 37),
    Fraction(41, 31),
    Fraction(129, 287),
    Fraction(41, 43),
    Fraction(13, 41),
    Fraction(1, 13),
    Fraction(1, 3)
    ]

# High-level function that calls the fibonacci code and returns a result
def fibonacci(n):
    import math
    result = run(fibcode, 78 * 5**(n - 1))
    return math.log2(int(result))

# Try it out
for n in range(1, 16):
    print(fibonacci(n))
