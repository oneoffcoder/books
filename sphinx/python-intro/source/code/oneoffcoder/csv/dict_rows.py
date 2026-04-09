import csv

rows = [
    {'name': 'Ava', 'score': 95},
    {'name': 'Noah', 'score': 88},
]

with open('scores_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'score'])
    writer.writeheader()
    writer.writerows(rows)

with open('scores_dict.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['score'])
