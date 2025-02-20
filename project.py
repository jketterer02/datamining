import csv 
import os


def parse_csv(file_path):
    if not os.path.exists(file_path):raise FileNotFoundError(f"The file '{file_path}' was not found.")
    
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            parsed_row = {}
            for key, value in row.items():
                # Gives actual values
                if value.isdigit(): parsed_row[key] = int(value)
                else: parsed_row[key] = value.strip('"')
            data.append(parsed_row)
    return data

#Get the data
data = parse_csv('student-mat.csv')
#Print first 5 rows
#print(data[:5])
print("1.Exploritory Data Analysis (EDA) Output:")
