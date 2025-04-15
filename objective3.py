# Visualization of Pollution Hotspots & Comparison
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

file_path = 'cleaned_merged_dataset.xlsx'
df = pd.read_excel(file_path)

# Group by City and calculate average pollution levels
city_pollution = df.groupby('City')[['SO2', 'NO2', 'PM10', 'SPM']].mean()

# Calculate overall average pollution for comparison
city_pollution['Total_Pollution'] = city_pollution[['SO2', 'NO2', 'PM10', 'SPM']].mean(axis=1)

# Sort cities based on pollution level
city_pollution_sorted = city_pollution.sort_values(by='Total_Pollution', ascending=False)

print("\nTop 10 Most Polluted Cities:\n")
print(city_pollution_sorted.head(10))

print("\nTop 10 Least Polluted Cities:\n")
print(city_pollution_sorted.tail(10))

# Plotting top 10 polluted cities
plt.figure(figsize=(12, 6))
sns.barplot(x=city_pollution_sorted.head(10).index, y=city_pollution_sorted['Total_Pollution'].head(10), palette='Reds_r')
plt.xticks(rotation=45)
plt.title('Top 10 Most Polluted Cities')
plt.ylabel('Average Pollution Level')
plt.xlabel('City')
plt.tight_layout()
plt.show()

# Plotting least polluted cities
plt.figure(figsize=(12, 6))
sns.barplot(x=city_pollution_sorted.tail(10).index, y=city_pollution_sorted['Total_Pollution'].tail(10), palette='Greens')
plt.xticks(rotation=45)
plt.title('Top 10 Least Polluted Cities')
plt.ylabel('Average Pollution Level')
plt.xlabel('City')
plt.tight_layout()
plt.show()

# Conclusion:
# - Top 10 Cities with highest average pollution levels are identified as Pollution Hotspots.
# - Least 10 Cities with lowest pollution levels are also identified.
# - Bar graphs provide a clear visual comparison of pollution levels city-wise.
