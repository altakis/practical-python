# pcost.py
#
# Exercise 1.27
import sys
import csv
def portfolio_cost(filename):
    'Returns the total value of an inventory of the name,shares,cost format'
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        total = 0
        for row in rows:
                print(row)
                # line = row.split(',')                
                try:              
                    total += float(row[1]) * float(row[2])
                except ValueError:
                    print("\nCouldn't parse, please sanitize file.\nError line:",row,"\n")            

    print('The total inventory value is: ',total)

    if f.closed:
        print('file is closed')
    else:
        print('file is open')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = './Data/portfolio.csv'

portfolio_cost(filename)