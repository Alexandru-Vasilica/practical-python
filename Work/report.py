# report.py
#
# Exercise 2.4
import csv

import stock
import tableformat


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


def read_portfolio(filename: str) -> list:
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            entry = stock.Stock(row[0], int(row[1]), float(row[2]))
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


def print_report(report, formatter: tableformat.TableFormatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    # print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    # print(f'{"":->10} {"":->10} {"":->10} {"":->10}')
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
        # print(f'{name:>10s} {shares:>10d} {f'${price:.2f}':>9s} {change:>10.2f}')


def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    if fmt == 'txt':
        formatter = tableformat.TableFormatter()
    elif fmt == 'csv':
        formatter = tableformat.CSVTableFormatter()
    elif fmt == 'html':
        formatter = tableformat.HTMLTableFormatter()
    else:
        raise tableformat.FormatError(f'Invalid format: {fmt}')

    report = make_report(portfolio_file, prices_file)
    print_report(report, formatter)


def main(argv):
    portfolio_report("Data/portfolio.csv", "Data/prices.csv", fmt='csv')


if __name__ == "__main__":
    main(None)
