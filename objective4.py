# Objective4: To calculate the overall average pollution level of each pollutant across all cities and visualize it using bar chart or pie chart
import pandas as pd
import matplotlib.pyplot as plt

file_path = "cleaned_merged_dataset.xlsx"  # Adjust the path if needed
xls = pd.ExcelFile(file_path)

# Load the data from the first sheet
df = xls.parse(xls.sheet_names[0])

# List of pollutants
pollutants = ['SO2', 'NO2', 'PM10', 'SPM']

# Calculate average pollution level for each pollutant across all cities
average_pollution = df[pollutants].mean()

# Plotting bar chart
plt.figure(figsize=(10, 6))
average_pollution.plot(kind='bar', color='skyblue')
plt.title('Average Pollution Level of Each Pollutant Across All Cities')
plt.ylabel('Average Level (µg/m³)')
plt.xlabel('Pollutant')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
