import json

def filter_json(input_file, output_file1, output_file2, pid_list):
    with open(input_file, 'r') as f:
        data = json.load(f)

    matching_entries = []
    non_matching_entries = []

    for entry in data:
        if 'pid' in entry and entry['pid'] in pid_list:
            matching_entries.append(entry)
        else:
            non_matching_entries.append(entry)

    with open(output_file1, 'w') as f1:
        json.dump(matching_entries, f1, indent=4)

    with open(output_file2, 'w') as f2:
        json.dump(non_matching_entries, f2, indent=4)

    print("Filtered data saved successfully!")

# Example usage
input_file = 'data.json'
output_file1 = 'matching_entries.json'
output_file2 = 'non_matching_entries.json'
pid_list = [1, 3, 5]  # List of pids to match

filter_json(input_file, output_file1, output_file2, pid_list)
