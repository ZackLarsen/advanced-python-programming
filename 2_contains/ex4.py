# -----------------------------------------------------------------------------
# Exercise 4 : Real-time prices challenge
#
# The report.py program is currently programmed to read stock prices
# from a file `prices.csv`.   However, could you create a custom
# PriceMap class that obtains the prices from some kind of
# online data source (i.e., website, API, etc.)?
#
# Note: This exercise is open-ended.  I don't actually know a good API
# from which to obtain stock prices.  You might need to use a libraries
# such as requests, beautifulsoup, and others to scrape it off
# a public website.

import report

class PriceMap:
    ...

def main():
    import report
    import ex1
    # Verify the mutability tests with a standard list
    portfolio = ex1.Portfolio.from_csv('portfolio.csv')
    prices = PriceMap(...)     # must modify
    report.print_report(portfolio, prices)
    
if __name__ == '__main__':
    main()
    
        
        




