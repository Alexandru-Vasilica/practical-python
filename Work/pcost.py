# pcost.py
#
# Exercise 1.27

import csv
import sys


def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as file:
        rows = csv.reader(file)
        header = next(rows)
        for line, row in enumerate(rows):
            try:
                record = dict(zip(header, row))
                total += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {line}: Could not convert {row}')

    return total


if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = input("Provide a filename:")
try:
    cost = portfolio_cost(filename)
    print(cost)
except FileNotFoundError:
    print("Invalid filename")
