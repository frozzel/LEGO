import pandas as pd
import matplotlib.pyplot as plt

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

sets_by_year = sets.groupby('year').size()  # Group sets by year and count them
print("Number of sets by year:")
print(sets_by_year.head())  # Print the number of sets by year

themes_by_year = sets.groupby('year')['theme_id'].nunique()  # Count unique themes by year

plt.plot(sets_by_year.index[:-2], sets_by_year.values[:-2])
plt.title('Number of Sets by Year')
plt.xlabel('Year')
plt.ylabel('Number of Sets')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(sets_by_year.index[:-2], sets_by_year.values[:-2], color='green', label='Number of Sets')
ax2.plot(themes_by_year.index[:-2], themes_by_year.values[:-2], color='blue', label='Number of Themes')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')

plt.show()