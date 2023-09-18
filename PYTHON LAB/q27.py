import pandas as pd

# Create the DataFrame Sales
data = {
    '2018': [110, 205, 177, 189],
    '2019': [130, 165, 175, 190],
    '2020': [115, 206, 157, 179],
    '2021': [118, 198, 183, 169]
}

salespersons = ['Kapil', 'Kamini', 'Shikhar', 'Mohini']

sales = pd.DataFrame(data, index=salespersons)

# Display the row labels of Sales
row_labels = sales.index
print("Row Labels:")
print(row_labels)
print()

# Display the column labels of Sales
column_labels = sales.columns
print("Column Labels:")
print(column_labels)
print()

# Display the data types of each column of Sales
data_types = sales.dtypes
print("Data Types:")
print(data_types)
print()

# Display the dimensions, shape, size, and values of Sales
dimensions = sales.ndim
shape = sales.shape
size = sales.size
values = sales.values

print("Dimensions:", dimensions)
print("Shape:", shape)
print("Size:", size)
print("Values:")
print(values)