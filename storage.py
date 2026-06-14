import csv


data = [
    {'date': '2026-06-01', 'category': 'Rent', 'amount': '15000'},
    {'date': '2026-06-02', 'category': 'Electricity', 'amount': '1200'},
    {'date': '2026-06-03', 'category': 'Raw Materials', 'amount': '5000'},
    {'date': '2026-06-04', 'category': 'Rent', 'amount': '15000'},
    {'date': '2026-06-05', 'category': 'Internet', 'amount': '1000'},
    {'date': '2026-06-01', 'category': 'Electricity', 'amount': '5500'},
    {'date': '2026-06-03', 'category': 'Food', 'amount': '7000'},
{'date': '2026-06-01', 'category': 'Rent', 'amount': '1599'},
    {'date': '2026-06-07', 'category': 'Electricity', 'amount': '900'}]



with open('expenses.csv', mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['date', 'category', 'amount']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)
    print("Done")


data1 = []
def load_csv():
    with open("expenses.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data1.append(row)

