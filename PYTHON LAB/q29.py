import matplotlib.pyplot as plt

# Data
batsmen = ['Virat Kohli', 'Steve Smith', 'Babar Azam', 'Rohit Sharma', 'Kane Williamson', 'Jos Butler']
years = ['2017', '2018', '2019', '2020']
virat_scores = [2501, 1855, 2203, 1223]
steve_scores = [2340, 2250, 2003, 1153]
babar_scores = [1750, 2147, 1896, 1008]
rohit_scores = [1463, 1985, 1854, 1638]
kane_scores = [1256, 1785, 1874, 1974]
jos_scores = [1125, 1853, 1769, 1436]

# Set custom widths for the bars
bar_width = 0.15

# Create a bar chart for Virat Kohli and Rohit Sharma
plt.bar(years, virat_scores, width=bar_width, color='blue', label='Virat Kohli')
plt.bar(years, rohit_scores, width=bar_width, color='red', label='Rohit Sharma')

# Set chart title and axis labels
plt.title("Batsmen Performance Over Years")
plt.xlabel("Year")
plt.ylabel("Runs Scored")

# Display legends
plt.legend()

# Display the bar chart for Steve Smith, Kane Williamson, and Jos Butler
x_pos = [i + bar_width for i in range(len(years))]

plt.bar(x_pos, steve_scores, width=bar_width, color='green', label='Steve Smith')
plt.bar(x_pos, kane_scores, width=bar_width, color='orange', label='Kane Williamson')
plt.bar(x_pos, jos_scores, width=bar_width, color='purple', label='Jos Butler')

# Update x-axis ticks and labels
plt.xticks([i + bar_width for i in range(len(years))], years)

# Display legends
plt.legend()

# Show the chart
plt.show()

# Display data of all players for the specific year (e.g., 2019)
specific_year = '2019'

# Get the index of the specific year
year_index = years.index(specific_year)

# Get the scores of all players for the specific year
specific_year_scores = [virat_scores[year_index], steve_scores[year_index], babar_scores[year_index], rohit_scores[year_index], kane_scores[year_index], jos_scores[year_index]]

# Create a bar chart for the specific year
plt.bar(batsmen, specific_year_scores, color='maroon')

# Set chart title and axis labels
plt.title("Runs Scored in " + specific_year)
plt.xlabel("Batsman")
plt.ylabel("Runs Scored")

# Show the chart
plt.show()