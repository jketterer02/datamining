import csv 
import os
import statistics

def parse_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    
    data = []
    numeric_fields = ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences"]
    numeric_data = {field: [] for field in numeric_fields}
    
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            parsed_row = {}
            for key, value in row.items():
                if value.isdigit():
                    parsed_row[key] = int(value)
                    if key in numeric_fields:
                        numeric_data[key].append(int(value))
                else:
                    parsed_row[key] = value.strip('"')
            data.append(parsed_row)
    
    return data, numeric_data

def desc_stats(numeric_data):
    stats = {field: {"mean": statistics.mean(numeric_data[field]),
                     "median": statistics.median(numeric_data[field]),
                     "std_dev": statistics.stdev(numeric_data[field])} 
             for field in numeric_data if numeric_data[field]}
    
    for field, values in stats.items():
        print(f"{field}: Mean = {values['mean']:.2f}, Median = {values['median']:.2f}, Std Dev = {values['std_dev']:.2f}")
    
    return stats
#Get the data
data, numeric_data = parse_csv('student-mat.csv')
print("1.Exploritory Data Analysis (EDA) Output:")
stats = desc_stats(numeric_data)

