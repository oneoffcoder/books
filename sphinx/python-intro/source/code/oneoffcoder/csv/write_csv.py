import csv

rows = [
    ['name', 'score'],
    ['Ava', 95],
    ['Noah', 88],
    ['Mia', 91],
]

with open('scores.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
