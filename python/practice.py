import csv

# create a csv file called practice.csv using a write-out command and then put some content into it
with open('csvs/practice.csv', 'w', newline ='') as fout:
     csvwriter = csv.writer(fout)
     for i in range(0, 100, 10):
         csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20, i + 25, i + 30])

with open('csvs/practice.csv', 'r') as fin:
    our_reader = csv.reader(fin)
    data = [row for row in our_reader]
# print(data)

#replacing some numbers with names and writing them to the csv
data[3][5] = 'Ethan'
data[5][4] = 'Brandon'
data[2][6] = 'Tony the cat'

with open('csvs/practice.csv', 'w', newline = '') as fout:
    csvwriter = csv.writer(fout)
    for row in data:
        csvwriter.writerow(row)
print(data)
