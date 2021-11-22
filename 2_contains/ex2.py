# ex2.py
# -----------------------------------------------------------------------------
# Exercise 2 - The Columns
#
# Mel in the Data division has performed some experiments and found
# that reading data into a list of instances is rather inefficient
# with memory for very large files. However, she's found that the
# memory requirements seem to be a lot less if you read the data into
# separate columns--each represented as a list.  So, she wrote the
# following code that does just that:

import csv

def read_portfolio_as_columns(filename):
    columns = {
        'name': [],
        'shares': [],
        'price': []
    }
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        next(rows)    # Skip headers
        for row in rows:
            columns['name'].append(row[0])
            columns['shares'].append(int(row[1]))
            columns['price'].append(float(row[2]))
    return columns

# -----------------------------------------------------------------------------
# Task 1: Try running the above function on "portfolio.csv" and look
# at the resulting data structure.  Make sure you understand what's
# happening and how it's different than before.

columns = read_portfolio_as_columns('portfolio.csv')
print(columns)                                


# -----------------------------------------------------------------------------
# Task 2: Does Mel's claim of memory use hold true?  How would you find out?
# How much better is it?


# -----------------------------------------------------------------------------
# Task 3: Create a new Portfolio class that uses the above function to
# internally represent data.  However, this class must outwardly behave
# exactly the same as the `Portfolio` class in Exercise 1.  This means
# that you can use it in the unmodified report.py program.
#
# To emphasize, your class must internally store its data in the same
# form as returned by the read_portfolio_as_columns() function.  However,
# it must present the data in a form that's compatible with code in
# `report.py`.   So, you're going to need to figure out some way to
# perform some kind of adaptation of the data.

class PortfolioColumns:
    @classmethod
    def from_csv(cls, filename):
        ...
        self.data = read_portfolio_as_columns(filename)
        return self

    ...
    # More definitions will be needed

def main():
    import report
    import ex1
    portfolio = PortfolioColumns.from_csv("portfolio.csv")
    prices = ex1.PriceMap.from_csv("prices.csv")
    # This should work without modification
    report.print_report(portfolio, prices)

# Uncomment when ready
# main()


    
    

    
        


