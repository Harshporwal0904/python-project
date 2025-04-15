import pandas as pd

# Load the dataset
file_path = 'merged_dataset.csv'  
df = pd.read_csv(file_path)


print("Before Cleaning:")
print(df.info())

# Rename columns for simplicity
df.rename(columns={
    'City/Town/Village/Area': 'City',
    'Location of Monitoring Station': 'Location',
    'Type of Location': 'Location_Type',
    'RSPM/PM10': 'PM10'
}, inplace=True)

# Drop unnecessary columns
df.drop(columns=['Stn Code', 'Agency'], inplace=True)

# Fill missing values in numeric columns with their mean
numeric_columns = ['SO2', 'NO2', 'PM10', 'SPM']
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Convert 'Sampling Date' to datetime format
df['Sampling Date'] = pd.to_datetime(df['Sampling Date'], errors='coerce')

# Drop rows with invalid dates
df.dropna(subset=['Sampling Date'], inplace=True)


print("After Cleaning:")
print(df.info())


output_path = 'cleaned_merged_dataset.xlsx'  
df.to_excel(output_path, index=False)

print(f"Cleaned data saved successfully to {output_path}")
