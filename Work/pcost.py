# pcost.py
#
# Exercise 1.27
with open('./Data/portfolio.csv','rt') as f:
    headers = next(f).split(',')
    print(headers)
    total = 0
    for line in f:
        row = line.split(',')
        print(row)  
        total += float(row[1]) * float(row[2])
    print('The total inventory value is: ',total)

if f.closed:
    print('file is closed')
else:
    print('file is open')