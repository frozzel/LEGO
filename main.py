import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
df = load_data('./data/colors.csv')

# print(df.head())  # Display the first few rows of the DataFrame

unique_colors = df["name"].nunique()  # Get unique values in the DataFrame or count() for each column
# unique_colors = df.count()  # Alternatively, use count() to get the number of non-null values in each column



print("Unique values in each column:")
print(unique_colors)  # Print the unique values count for each column

tran_colors = df.is_trans.value_counts()  # Get unique values in the "name" column

print("Total number of translucent colors:")
print(tran_colors)  # Print the total number of colors