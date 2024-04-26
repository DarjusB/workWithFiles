import csv

def fulllist():
    with open('sampleData.csv', encoding='utf8') as file:
        rows = csv.DictReader(file)
        for row in rows:
            print(row)
