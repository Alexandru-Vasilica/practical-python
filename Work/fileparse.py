# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_header=False, delimiter=','):
    """
    Parse a CSV file into a list of records
    """

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []
        if has_header:
            header = next(rows)
            if not select:
                indexes = range(len(header))
            else:
                indexes = [header.index(s) for s in select]
            for row in rows:
                if not row:
                    continue
                row = [row[i] for i in indexes]
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                record = dict(zip(select, row))
                records.append(record)
        else:
            for row in rows:
                record = tuple(row)
                records.append(record)

    return records


# print(parse_csv("Data/portfolio.csv", select=['name', 'price', 'shares'], types=[str, float, int]))

print(parse_csv("Data/portfolio.dat", delimiter=' '))
