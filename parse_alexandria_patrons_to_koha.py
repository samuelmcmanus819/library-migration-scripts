import csv
from datetime import datetime

# Open the input file in read mode
with open('patrons.csv', 'r') as input_file:
    # Create a CSV reader object with tab as the delimiter and skip the header row
    reader = csv.DictReader(input_file, delimiter='\t')

    destination_columns = ['cardnumber', 'surname', 'firstname', 'middle_name', 'address', 'address2', 'city', 'state', 'zipcode',
            'country', 'email', 'phone', 'mobile', 'dateofbirth', 'branchcode', 'categorycode', 'dateenrolled', 'dateexpiry', 
            'contactname', 'sex', 'password', 'userid', 'opacnote', 'contactnote', 'lastseen']

    with open('patrons_parsed.csv', 'w') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=destination_columns, delimiter=',')
        writer.writeheader()
        
        for row in reader:
            # Parse all of the dates to the format expected by Koha
            dob = row['Date of Birth']
            account_creation_date = row['Patron Accession Date']
            account_exp_date = row['Account Expiration']
            last_use_date = row['Last Use Date']
            if dob != '':
                dob = datetime.strptime(dob, '%b %d, %Y')
                dob = dob.strftime('%m/%d/%Y')
            account_creation_date = datetime.strptime(account_creation_date, '%b %d, %Y')
            account_creation_date = account_creation_date.strftime('%m/%d/%Y')
            account_exp_date = datetime.strptime(account_exp_date, '%b %d, %Y')
            account_exp_date = account_exp_date.strftime('%m/%d/%Y')
            last_use_date = datetime.strptime(last_use_date, '%b %d, %Y')
            last_use_date = datetime.strftime(last_use_date, '%m/%d/%Y')
            # Parse the gender
            if row['Sex'] == '1':
                sex = 'Male'
            elif row['Sex'] == '2':
                sex = 'Female'
            else:
                sex = 'None specified'
            # Change patron policies where appropriate
            if row['Username'] == '817':
                row['Policy'] = 'ADMIN'
            if row['Policy'] == 'STD':
                row['Policy'] = 'ADUL'

            # Create the row dict
            row_dict = {
                'cardnumber': row['Barcode'],
                'surname': row['Last Name'],
                'firstname': row['First Name'],
                'middle_name': row['Middle Name'],
                'address': row['Address'],
                'address2': row['Address 2'],
                'city': row['City'],
                'state': row['State'],
                'zipcode': row['Postal Code'],
                'country': row['Country'],
                'email': row['Primary Email'],
                'phone': row['Telephone'],
                'mobile': row['Mobile'],
                'dateofbirth': dob,
                'branchcode': row['Site'],
                'categorycode': row['Policy'],
                'dateenrolled': account_creation_date,
                'dateexpiry': account_exp_date,
                'contactname': row['Additional Contact'],
                'sex': sex,
                'password': row['Last Name'].lower(),
                'userid': row['Username'],
                'opacnote': row['General Notes'],
                'contactnote': row['Contact Notes'],
                'lastseen': last_use_date
            }

            # Write the row to the output file, omitting Alexandria system-defined users
            if row['Policy'] != 'SYS':
                writer.writerow(row_dict)
