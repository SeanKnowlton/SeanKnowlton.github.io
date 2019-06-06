# import a csv file about jack the ripper

import csv
with open('csvs/jack_ripper.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
# this command(parameter is to identify only the text of the reports and print all of it out)
#    all_texts = [row[4] for row in our_reader]
#print(all_texts)
    dates = [row[3] for row in our_reader]

# find the earliest date of published reports
earliest_date = ''
for row in dates:
    if len(row[3]) < len(earliest):
        earliest = row[3]
print(earliest_date)
