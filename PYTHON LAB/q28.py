import matplotlib.pyplot as plt

# Data
months = ['January', 'February', 'March', 'April', 'May']
sales = [510, 350, 475, 580, 600]

# Customize the line chart
plt.plot(months, sales, color='blue', linestyle='--', marker='D')

# Set chart title and axis labels
plt.title("The Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")

# Display legends
plt.legend(["Sales"])

# Display the line chart
plt.show()