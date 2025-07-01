import csv
import statistics

with open('48.csv', 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader, 1):
        if len(row) >= 3:  # Skip header and empty rows
            try:
                values = [float(x) for x in row]
                mean = statistics.mean(values)
                stdev = statistics.stdev(values) if len(values) > 1 else 0
                print(f"Row {i}: mean={mean:.2f}, stdev={stdev:.2f}")
            except ValueError:
                print(f"Row {i}: Skipping header row")