from collections import Counter
import csv

def write_id(csv_output, data):
    for key, value in data.items():
        csv_output.writerow([*key, value])
    data.clear()


data = Counter()
current_id = None

with open('input.csv') as f_input, open('output.csv', 'w', newline='') as f_output:
    csv_input = csv.reader(f_input)
    csv_output = csv.writer(f_output)
    
    header = next(csv_input)
    csv_output.writerow(header)
    
    for row in csv_input:
        if current_id and row[0] != current_id:
            write_id(csv_output, data)
            
        data[tuple(row[:3])] += int(row[3])
        current_id = row[0]
        
    write_id(csv_output, data)        
