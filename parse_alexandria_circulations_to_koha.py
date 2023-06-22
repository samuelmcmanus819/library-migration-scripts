import csv
from datetime import datetime, timedelta

# Open the input file in read mode
with open('circulations.csv', 'r') as input_file:
    # Create a CSV reader object with tab as the delimiter
    reader = csv.DictReader(input_file, delimiter='\t')

    # Define the desired columns for output (including the new 'issue' column)
    desired_columns = ['Due Date', 'issue', 'Patron Barcode', 'Item Barcode']

    with open("master.koc", "r") as f:
        lines = f.readlines()
    with open("circulations_parsed.koc", "w") as f:
        for line in lines:
            if line.strip("\t") != "\n":
                f.write(line)

    # Open the output file in append mode
    with open('circulations_parsed.koc', 'a', newline='') as output_file:
        # Create a CSV writer object with tab as the delimiter
        writer = csv.DictWriter(output_file, fieldnames=desired_columns, delimiter='\t')

        # Iterate over each row in the input file
        for row in reader:
            # Get the current 'Due Date' value
            due_date_str = row['Due Date']

            # Convert the 'Due Date' string to a datetime object
            due_date = datetime.strptime(due_date_str, '%m/%d/%Y')

            # Subtract 21 days from the 'Due Date'
            new_due_date = due_date - timedelta(days=21)

            # Format the new due date as a string with time in 'yyyy/mm/dd hh:mm:ss' format
            new_due_date_str = new_due_date.strftime('%Y/%m/%d %H:%M:%S')

            # Filter the fields to desired columns
            filtered_row = {
                'Due Date': new_due_date_str,
                'issue': 'issue',
                'Patron Barcode': row['Patron Barcode'],
                'Item Barcode': row['Item Barcode']
            }

            # Write the modified row to the output file
            writer.writerow(filtered_row)
