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
    
color = load_data('./data/colors.csv')

# print(df.head())  # Display the first few rows of the DataFrame

unique_colors = color["name"].nunique()  # Get unique values in the DataFrame or count() for each column
# unique_colors = df.count()  # Alternatively, use count() to get the number of non-null values in each column



print("Unique values in each column:")
print(unique_colors)  # Print the unique values count for each column

tran_colors = color.is_trans.value_counts()  # Get unique values in the "name" column

print("Total number of translucent colors:")
print(tran_colors)  # Print the total number of colors

sets =load_data('./data/sets.csv')  # Load the sets data

print("Sets data loaded successfully.")
# Display the first few rows of the sets DataFrame
print(sets.head())

oldest_set = sets.sort_values('year').head()  # Get the oldest set by year
print("Oldest set(s):")
print(oldest_set)  # Print the oldest set(s)

sets_first_year = sets[sets['year']== 1949]  # Get the first year for each set
print("Sets from the first year (1949):")
print(sets_first_year)  # Print the sets from the first year

largest_set = sets.sort_values('num_parts', ascending=False).head()  # Get the largest set by number of parts
print("Largest set(s) by number of parts:")
print(largest_set)  # Print the largest set(s)