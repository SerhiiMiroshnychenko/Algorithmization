import csv
with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ім\'я', 'вік'])
    writer.writerow(['Іван', 25])
