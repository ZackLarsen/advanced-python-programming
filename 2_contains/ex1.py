# ex1.py
# -----------------------------------------------------------------------------
# Exercise 1 - Custom Containers
#
# The `report.py` program makes use of built-in Python objects
# including lists and dictionaries.  For instance, the
# `read_portfolio()` function reads a file into a list of `Holding`
# instances.  The `read_prices()` function reads a file into a
# dictionary mapping stock names to prices.
#
# In this exercise, you're going to make higher-level abstractions
# for these functions.  Instead of `read_portfolio()`, you'll create a
# Portfolio class. Instead of `read_prices()`, you'll make a `PriceMap`
# class.   When you do this, you're going to preserve the existing
# code for `print_report()`.  In fact, that function should work
# without modification!
#
# This exercise makes use of class methods.  Please see the discussion
# at the end of this file for more details.
# -----------------------------------------------------------------------------

import report

class Portfolio:
    ...
    # You define (copy/adapt code from report.py)
    @classmethod
    def from_csv(cls, filename):
        ...
        # Adapt from the read_portfolio() function

class PriceMap:
    ...
    # You define
    @classmethod
    def from_csv(cls, filename):
        ...
        # Adapt from the read_prices() function

if __name__ == '__main__':
    # Create Portfolio and PriceMap objects from CSV files
    portfolio = Portfolio.from_csv('portfolio.csv')
    prices = PriceMap.from_csv('prices.csv')

    # Use `report.print_report()` to create output.  You're using this
    # function UNCHANGED.  It should work with the Portfolio and
    # PriceMap objects you defined above.  To do this, you may need to
    # implement a number of Python special methods such as
    # `__getitem__()`, `__len__()`, `__iter__()` and so forth.
    report.print_report(portfolio, prices)

# ----------------------------------------------------------------------
# Discussion:
#
# What you're doing in this exercise is establishing more "formal"
# abstractions for the data being used in the program.  You're giving
# these abstractions names--an identity of sorts.  It's a "Portfolio"
# not a list of Holding instances.  It's a "PriceMap" not a dict.
# This might not seem like much, but it gives us something to
# work with as we extend the code in new directions.
#
# And now a word about class methods...
#
# In this code, `from_csv()` has been defined as a class method.  This
# is a common technique of defining alternate initializers on a class
# and is common if there happens to be more than one way to create
# an object.  A common pattern would be to define a basic class
# with a simple `__init__()` method.   `from_csv()` would be a more
# special case.  For example:
#
# class Portfolio:
#     def __init__(self):
#         self.holdings = [ ]
#
#     def append(self, holding):
#         self.holdings.append(holding)
#
#     @classmethod
#     def from_csv(cls, filename):
#         self = cls()      # Create the instance
#         with open(filename) as file:
#              ...
#              self.append(Holding(name, shares, price))
#              ...
#         return self
#
# If there were other ways of creating a Portfolio, say from JSON or
# reading a database, those could be defined as other class methods.









