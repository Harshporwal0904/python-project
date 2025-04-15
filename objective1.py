# Objective1: State-wise & City-wise Pollution Analysis
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

file_path = 'cleaned_merged_dataset.xlsx'  
df = pd.read_excel(file_path)

print(df.head()) # To display first five rows

# Grouping data by State and calculating the average pollution levels
state_pollution = df.groupby('State')[['SO2', 'NO2', 'PM10', 'SPM']].mean().sort_values(by='PM10', ascending=False)

print("\nAverage Pollution Levels State-wise:\n")
print(state_pollution)

# Grouping data by City and calculating the average pollution levels
city_pollution = df.groupby('City')[['SO2', 'NO2', 'PM10', 'SPM']].mean().sort_values(by='PM10', ascending=False)

print("\nAverage Pollution Levels City-wise:\n")
print(city_pollution)

# Printing the most polluted city (Highest PM10)
most_polluted_city = city_pollution.head(1)
print("\nMost Polluted City based on PM10:\n")
print(most_polluted_city)

# Printing the least polluted city (Lowest PM10)
least_polluted_city = city_pollution.tail(1)
print("\nLeast Polluted City based on PM10:\n")
print(least_polluted_city)

# Conclusion:
# From the above state-wise analysis:
# - The states with the highest average PM10 levels (most polluted) are at the top.
# - The states with the lowest PM10 levels (least polluted) are at the bottom.
# From the city-wise analysis:
# - The cities with the highest average PM10 levels are identified as the most polluted cities.
# - The cities with the lowest average PM10 levels are considered the least polluted.
# This analysis helps in identifying pollution hotspots across both states and cities.
