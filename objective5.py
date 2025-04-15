# Objective5: To create a correlation heatmap between various pollutants (SO₂, NO₂, PM10, SPM) to 
# check their relationship with each other
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = "cleaned_merged_dataset.xlsx"  
xls = pd.ExcelFile(file_path)
df = xls.parse(xls.sheet_names[0])


pollutants = ['SO2', 'NO2', 'PM10', 'SPM']

# Compute correlation matrix
correlation_matrix = df[pollutants].corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Pollutants')
plt.tight_layout()
plt.show()


# Conclusion

# The heatmap shows a strong positive correlation between NO₂, PM10, and SPM, 
# indicating they likely originate from similar sources like traffic and industry. 
# SO₂ has a weaker correlation with the others, suggesting different or more 
# localized sources. These insights can help in designing targeted pollution control strategies.
