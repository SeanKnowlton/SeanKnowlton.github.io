import csv
#
groceries = []
with open('csvs/shopping.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        groceries.append(row)
print(groceries)
