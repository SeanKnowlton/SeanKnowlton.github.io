# import a csv file about jack the ripper

import csv
with open('csvs/jack_ripper.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
# this command(parameter) is to turn all characters to lowercase
    corpus_texts = [row for row in our_reader]

for row in corpus_texts:
    row[4] = row[4].lower()

with open('csvs/jack_ripper_lower.csv', 'w') as fout:
    writer = csv.writer(fout)
    for row in corpus_texts:
        writer.writerow(row)
