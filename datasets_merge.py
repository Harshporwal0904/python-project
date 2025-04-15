import pandas as pd
import os


folder_path = "E:\datasets"

# Create an empty dataframe
final_df = pd.DataFrame()

# Loop through all files
for file in os.listdir(folder_path):
    if file.endswith('.csv') or file.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path) 
        final_df = pd.concat([final_df, df], ignore_index=True)

# Now final_df has all combined data
print(final_df.shape)  # Check rows and columns
print(final_df.head())

# Save the merged file
final_df.to_csv('merged_dataset.csv', index=False)
