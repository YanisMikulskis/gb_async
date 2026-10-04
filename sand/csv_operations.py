import csv

with open('file_csv.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    csv_headers = next(csv_reader)
    print(f'headers = {csv_headers}')
    for row in csv_reader:
        print(row)

print(f'-----')

with open('file_csv.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    # csv_headers = next(csv_reader)
    # print(f'headers = {csv_headers}')
    for k in csv_reader:
        print(k['fff'])



data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', "Moscow str"]]
with open('new_csv.csv', 'w') as new_f:
    file_writer = csv.writer(new_f)
    for row in data:
        file_writer.writerow(row)


with open('new_csv.csv') as f:
    print(f.read())


print(f'00------')

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', 2960, "Moscow str"]
            ]
with open('new_csv2.csv', 'w') as new_f:
    file_writer = csv.writer(new_f, quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        file_writer.writerow(row)


with open('new_csv2.csv') as f:
    print(f.read())





print(f'11------')

data = [['hostname!', 'vendor!', 'model!', 'location!'],
        ['kp1!', 'Cisco!', 2960, "Moscow str!"],
        ['kp2!', 'Cisco2!', 2961, "Moscow str3!"]]
with open('new_csv3.csv', 'w') as new_f:
    file_writer = csv.writer(new_f, quoting=csv.QUOTE_NONNUMERIC)

    file_writer.writerows(data)

print(f'22------')
with open('new_csv4.csv', 'r') as new_f:
    file_reader = csv.reader(new_f, delimiter='!')
    for row in file_reader:
        print(row)