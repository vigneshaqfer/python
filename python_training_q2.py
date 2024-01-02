import csv

class Format:
    def __init__(self, name):
        self.name = name

class CSV(Format):
    def __init__(self, name, filename, delimiter):
        super().__init__(name)
        self.filename = filename
        self.delimiter = delimiter

    def process_csv(self):
        try:
            with open(self.filename, 'r', newline='') as file:
                # Read the entire content for printing
                file_contents = file.read()

                # Print the contents of the file
                print("File Contents:")
                print(file_contents)

                # Reset the file pointer to the beginning
                file.seek(0)

                # Check if the file is a valid CSV file
                csv.Sniffer().sniff(file_contents)
                file.seek(0)

                reader = csv.reader(file, delimiter=self.delimiter)

                # Extract header
                header = next(reader, None)

                # Count rows
                row_count = sum(1 for row in reader)

                return {
                    'valid': True,
                    'header': header,
                    'row_count': row_count
                }

        except csv.Error:
            return {
                'valid': False,
                'header': None,
                'row_count': 0
            }

# Example Usage
csv_instance = CSV(name="CSV Format", filename="/Users/vigneshkumars/example.csv", delimiter=",")

result = csv_instance.process_csv()

print(f"CSV File is Valid: {result['valid']}")
print(f"Header: {result['header']}")
print(f"Row Count: {result['row_count']}")

