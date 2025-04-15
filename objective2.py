# Objective2: Time Series Analysis of Pollution Trends
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

file_path = 'cleaned_merged_dataset.xlsx'
df = pd.read_excel(file_path)

# Check available columns
print(df.columns)

# Convert it to datetime format
df['Date'] = pd.to_datetime(df['Sampling Date'], errors='coerce')

# Extract year from date column
df['Year'] = df['Date'].dt.year

# Drop rows where year is NaN
df = df.dropna(subset=['Year'])

# Group by Year and calculate average pollution levels
yearly_pollution = df.groupby('Year')[['SO2', 'NO2', 'PM10', 'SPM']].mean()

print("\nAverage Pollution Levels Year-wise:\n")
print(yearly_pollution)

# Plotting the trends
plt.figure(figsize=(12, 6))
plt.plot(yearly_pollution.index, yearly_pollution['SO2'], marker='o', label='SO2')
plt.plot(yearly_pollution.index, yearly_pollution['NO2'], marker='o', label='NO2')
plt.plot(yearly_pollution.index, yearly_pollution['PM10'], marker='o', label='PM10')
plt.plot(yearly_pollution.index, yearly_pollution['SPM'], marker='o', label='SPM')

plt.title('Year-wise Pollution Trend Analysis')
plt.xlabel('Year')
plt.ylabel('Average Pollution Level')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Conclusion:

# This graph shows the pollution trend year-wise.
# Increasing lines → Pollution Increasing.
# Decreasing lines → Pollution Decreasing.
