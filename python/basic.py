#gonna do some importing of csv data
import csv
with open('csvs/basic.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    names = [row for row in our_reader]

#print(names[1][2])
print(len(names))

# find the length of each first names
for row in names:
    print(len(row[2]))

# find the longest first names
longest = ""
for row in names:
    if len(row[2]) > len(longest):
        longest = row[2]
print(longest)

# construct a new list consisting of only the first names we have here)
first_names = [row[2] for row in names]
first_names.reverse()
print(first_names)

#add a new row to basic.csv
new_row = [2, 'wayne', 'graham', 'meh']
names.append(new_row)
print(names)

# in [6] add another person to the csv
a_row = [3, 'fox', 'eliza', 'SO COOL']
print(names + a_row)
