
import pandas as pd

file_path = 'cleaned_merged_dataset.xlsx'  
df = pd.read_excel(file_path)


print("Dataset Information:\n")
print(df.info())

print("\n----------------------------------\n")


print("Summary Statistics:\n")
print(df.describe())
