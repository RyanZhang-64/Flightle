import csv

# Open the input CSV file and the output CSV file with utf-8 encoding
with open('airports.csv', 'r', newline='', encoding='utf-8') as infile, open('output.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write the header to the output file
    header = next(reader)
    writer.writerow(header)
    
    # Iterate through each row in the original CSV
    for row in reader:
        # Check if the third column contains 'large_airport'
        if 'large_airport' in row[2] or 'medium_airport' in row[2]:
            writer.writerow(row)