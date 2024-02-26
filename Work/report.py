# report.py
#
# Exercise 2.4
import csv

portfolio_file = "Data/portfolio.csv"
prices_file = "Data/prices.csv"


def read_portfolio_tuple(filename: str) -> list:
    """
    Reads a portfolio's data from a csv file and return a list of tuples
    """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            entry = row[0], int(row[1]), float(row[2])
            portfolio.append(entry)
    return portfolio


def read_portfolio_dict(filename: str) -> list:
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            entry = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(entry)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row):
                prices[row[0]] = float(row[1])
    return prices


def calculate_portfolio_value(portfolio_filename, prices_filename):
    total = 0
    portfolio = read_portfolio_tuple(portfolio_filename)
    prices = read_prices(prices_filename)
    for name, shares, price in portfolio:
        total += shares * (prices[name] - price)
    return total


def make_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio_tuple(portfolio_filename)
    prices = read_prices(prices_filename)
    report = []
    for name, shares, price in portfolio:
        change = shares * (prices[name] - price)
        entry = name, shares, price, change
        report.append(entry)
    return report


def print_report(report):
    headers = ['Name', 'Shares', 'Price', 'Change']
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{"":->10} {"":->10} {"":->10} {"":->10}')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {f'${price:.2f}':>9s} {change:>10.2f}')


def portfolio_report(portfolio_file, prices_file):
    report = make_report(portfolio_file, prices_file)
    print_report(report)


portfolio_report(portfolio_file, prices_file)
