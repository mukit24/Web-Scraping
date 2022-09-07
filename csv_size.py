import csv
with open('banglatech_data.csv',"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)
    print(row_count)