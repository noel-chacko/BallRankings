import pandas as pd

def toHTML():

    # Load your CSV data into a DataFrame
    csv_file = 'rankings.csv'  # Replace with the path to your CSV file
    df = pd.read_csv(csv_file)

    # Create a new DataFrame with "Rankings" as the first column
    rankings = list(range(1, len(df) + 1))
    df = pd.DataFrame({'Rankings': rankings}).join(df)

    # Rename the second column to "Names" and convert it to HTML with the "names" class
    df.rename(columns={df.columns[1]: 'Names'}, inplace=True)
    df['Names'] = df['Names'].apply(lambda x: f'<span class="names">{x}</span>')

    # Convert the DataFrame to an HTML table
    html_table = df.to_html(escape=False, classes='table table-striped', index=False)  # You can customize the table classes

    # Define the CSS file path (relative to the HTML file)
    css_file = 'tableStyle.css'

    # Create the complete HTML content with the CSS link
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="{css_file}">
    </head>
    <body>
    {html_table}
    </body>
    </html>
    """

    # Save the HTML to a file
    html_file = 'C:/Users/Noel/Desktop/BallRankings/website/output.html'
    with open(html_file, 'w') as f:
        f.write(html_content)

    print(f"CSV file '{csv_file}' has been converted to HTML with 'Rankings' as the first column and 'Names' as the second column with the 'names' class. HTML saved as '{html_file}'.")
