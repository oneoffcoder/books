import csv

with open('scores.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
