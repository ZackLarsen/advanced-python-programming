# report.py
#
# Ben has decided to write a Python script to watch his
# stock portfolio.  The file "portfolio.csv" is a CSV file
# containing information about his stock holdings (name,
# number of shares, purchase price).   The file "prices.csv"
# is a CSV file containing current stock prices.   If you
# run this script, it makes a small report.  Try running it
# yourself.
#
#     shell % python report.py
#     ... look at output ...
#
# This file is the starting point for the project. You will be
# making NO MODIFICATIONS to this file.  However, you will be
# importing bits and pieces of it including the `print_report()`
# function near the end.  Start your work by going to `ex1.py` and
# following the instructions inside.

import csv

class Holding:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def __repr__(self):
        return f'Holding({self.name!r}, {self.shares!r}, {self.price!r})'

def read_portfolio(filename):
    portfolio = []
    with open(filename, "r") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            h = Holding(row[0], int(row[1]), float(row[2]))
            portfolio.append(h)
    return portfolio

def read_prices(filename):
    prices = { }
    with open(filename, "r") as file:
        rows = csv.reader(file)
        for row in rows:
            prices[row[0]] = float(row[1])
    return prices

def print_report(portfolio, prices):
    print('{:10} {:10} {:10} {:10}'.format('Name', 'Shares', 'Price', 'Change'))
    print(('-'*10 + ' ')*4)
    for h in portfolio:
        current_price = prices[h.name]
        change = current_price - h.price
        print(f'{h.name:>10} {h.shares:>10} {current_price:>10.2f} {change:>10.2f}')

    cost = sum(h.shares * h.price for h in portfolio)
    value = sum(h.shares * prices[h.name] for h in portfolio)
    print('\nSummary:\n')
    print(f'Initial cost: {cost:0.2f}')
    print(f'Current value: {value:0.2f}')
    print(f'Change: {value-cost:0.2f}')

if __name__ == '__main__':
    portfolio = read_portfolio('portfolio.csv')
    prices = read_prices('prices.csv')
    print_report(portfolio, prices)
    
