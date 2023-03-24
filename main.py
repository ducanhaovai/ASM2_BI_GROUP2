import pandas as pd



def display_data():

    data = pd.read_csv("vgsales.csv", sep = "\t")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # Set display options to show all columns
    pd.set_option('display.max_colwidth', None)

    print(data.head(10))

def dataset_info():
    data = pd.read_csv("vgsales.csv", sep = "\t")
    print(data.info())

def dataset_stats():
    data = pd.read_csv("vgsales.csv" , sep = "\t")
    print(data.describe())

def blank_data():
    data = pd.read_csv("vgsales.csv")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # Set display options to show all columns
    pd.set_option('display.max_colwidth', None)

    missing_data = data[data.isna().any(axis=1)]

    # Display the missing data
    print(missing_data.head(20))
    # Display the next 5 rows of the DataFrame


def delete_colum():
    df = pd.read_csv("vgsales.csv" )
    columns = df.columns.tolist()
    # ask the user which column to delete
    print('Columns:')
    for i, column in enumerate(columns):
        print(i + 1, column)
    column_to_delete = int(input('Enter the number of the column to delete: '))
    # delete the selected column
    column_name = columns[column_to_delete - 1]
    df = df.drop(column_name, axis=1)
    # save the modified DataFrame to a new Excel file
    output_file = 'vgsales_delete_colum.csv'
    df.to_csv(output_file, index=False)
    # print a message indicating that the file was saved successfully
    print(f'The modified DataFrame was saved to {output_file}.')

def delete_rows():
        # Read CSV file
        df = pd.read_csv("vgsales.csv" )
        # Get input from user
        delete_rows = input("Enter the rows you want to delete (separated by commas): ")
        # Split input into a list of row numbers to delete
        delete_rows = delete_rows.split(",")
        # Convert row numbers to integers
        delete_rows = [int(i) for i in delete_rows]
        # Delete rows from DataFrame
        df = df.drop(delete_rows)
        # Write modified DataFrame to CSV file
        output_file = 'vgsales_delete_row.csv'
        df.to_csv(output_file, index=False)
        # Print message indicating successful save
        print(f'The modified DataFrame was saved to {output_file}.')

def clean_data():
    data = pd.read_csv("vgsales.csv" )
    cleaned_data = data.dropna()
    cleaned_data.to_csv("cleaned_data.csv", index=False)

while True:
    print("****** FILE CSV HANDLING PROGRAM ******")
    print("-------- FUNCTIONS OF PROGRAM ---------")
    print("1: Display data")
    print("2: Information of dataset")
    print("3: Statistics of dataset")
    print("4: Show Blank Table")
    print("5: Delete Colum")
    print("6: Delete Rows")
    print("7: Clean data")
    print("8: Exit")
    print("---------------------------------------")
    choice = input("> Your choice: ")

    if choice == "1":
        display_data()
    elif choice == "2":
        dataset_info()
    elif choice == "3":
        dataset_stats()
    elif choice == "4":
        blank_data()
    elif choice == "5":
        delete_colum()
    elif choice == "6":
        delete_rows()
    elif choice == "7":
        clean_data()
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please choose again.")

