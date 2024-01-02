import yaml
from collections import defaultdict
from datetime import date

def process_input(input_data):
    # Initialize statistics variables
    event_counts = defaultdict(int)
    month_counts = defaultdict(int)
    year_counts = defaultdict(int)

    # Process each entry in the input data
    for entry in input_data:
        event_type = entry['event_type']
        
        
        # Check if the 'date' field is a string or datetime.date object
        if isinstance(entry['date'], date):
            year = entry['date'].year
            month = entry['date'].month
        else:
            date_parts = entry['date'].split('-')
            year = int(date_parts[0])
            month = int(date_parts[1])



        count = entry['count']

        # Update event counts
        event_counts[event_type] += count

        # Update month counts
        month_counts[(event_type, month)] += count

        # Update year counts
        year_counts[(event_type, year)] += count

    # Print statistics
    print("Event Type | Month | Total Event Count | Highest Year | Lowest Year")
    print("-" * 70)

    for event_type, month in month_counts:
        total_event_count = month_counts[(event_type, month)]
        highest_year = max(year for (e_type, year) in year_counts if e_type == event_type)
        lowest_year = min(year for (e_type, year) in year_counts if e_type == event_type)

        print(f"{event_type:11} | {month:5} | {total_event_count:17} | {highest_year:12} | {lowest_year:11}")

# Read input YAML file
with open('input.yaml', 'r') as file:
    input_data = yaml.safe_load(file)

# Process input and print statistics
process_input(input_data)

