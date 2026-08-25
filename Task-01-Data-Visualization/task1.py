import matplotlib.pyplot as plt

# Age data representing a sample population
ages = [
    12, 15, 18, 19, 21, 23, 25, 27, 29, 30,
    32, 34, 35, 37, 39, 40, 42, 44, 45, 47,
    49, 50, 52, 54, 55, 57, 59, 60, 62, 65
]

# Create histogram
plt.hist(ages, bins=6, edgecolor="black")

# Add labels and title
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.title("Age Distribution of Sample Population")

# Display the chart
plt.show()
