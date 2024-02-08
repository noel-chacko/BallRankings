import pandas as pd

def combine():
    # List of CSV files to combine
    csv_files = ['espn.csv', 'on3.csv', '247.csv', 'rivals.csv']
    # Initialize an empty list to store DataFrames
    dfs = []

    # Read and store each CSV file as a DataFrame in the list
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        dfs.append(df)

    # Concatenate the DataFrames along columns with a comma separator
    combined_df = pd.concat(dfs, axis=1, join='inner')  # Use 'join=inner' to combine only common columns

    # Write the combined DataFrame to a new CSV file
    combined_df.to_csv('combined.csv', index=False)

    #csv_files = ['espn.csv', 'on3.csv', '247.csv', 'rivals.csv']
