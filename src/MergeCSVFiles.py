import csv

def merge_csv_files(csv_files, merged_file_path):
    merged_data = []
    headers = set()

    for file_path in csv_files:
        with open(file_path, 'r', newline='') as file:
            csv_reader = csv.DictReader(file)
            file_headers = csv_reader.fieldnames
            headers.update(file_headers)
            for row in csv_reader:
                merged_data.append(row)

    with open(merged_file_path, 'w', newline='') as merged_file:
        writer = csv.DictWriter(merged_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(merged_data)

# Test the function:
csv_files = ['.\\assets\\class1.csv', '.\\assets\\class2.csv']
merged_file_path = '.\\assets\\merged_file.csv'
merge_csv_files(csv_files, merged_file_path)
print(f"Merged file saved at: {merged_file_path}")
