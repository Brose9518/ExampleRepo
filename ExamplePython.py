import csv

file_path = r'C:\Users\student\Downloads\names.txt'

with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

csv_file_path = r'C:\Users\student\Downloads\names.txt'

with open(csv_file_path, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 3:
            rank, boy_name, girl_name = row
            print(f"Rank: {rank}")
            print(f"Boy Name: {boy_name}")
            print(f"Girl Name: {girl_name}")
            print('-' * 30)
        else:
            print("Invalid row format:", row)
