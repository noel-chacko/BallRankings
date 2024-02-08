import csv

def nickname():
    updated_rows = []

    dict = {"ace bailey": "Airious Bailey", 
            "johnuel \"boogie\" fland": "Boogie Fland",
            "johnuel fland": "Boogie Fland",
            "v.j. edgecombe": "VJ Edgecombe",
            "pat ngongba": "Patrick Ngongba",
            "patrick ngongba ii": "Patrick Ngongba",
            "k. annor boateng": "Annor Boateng",
            "naas cunningham": "Naasir Cunningham",
            "cam scott": "Cameron Scott",
            "donnie freeman": "Donavan Freeman",
            "john mobley jr": "John Mobley",
            "juni mobley": "John Mobley",
            "somtochukwu cyril": "Somto Cyril",
            "robert wright iii": "Robert Wright III",
            "liam mcneeley": "Liam McNeeley"
            }

    # Input and output file paths
    input_file = "combined.csv"
    output_file = "nameCorrected.csv"

    # Open the input CSV file for reading
    with open(input_file, mode='r', newline='') as file:
        reader = csv.reader(file)

        # Iterate through each row in the CSV
        for row in reader: 
            updated_row = []
            for cell in row:
                value = dict.get(cell.lower(),cell)
                updated_row.append(value)

            updated_rows.append(updated_row)

    # Open the output CSV file for writing and write the updated rows
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        for updated_row in updated_rows:
            writer.writerow(updated_row)

        print("String replacement in CSV complete. Check 'output.csv' for the result.")
