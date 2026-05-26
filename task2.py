import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Missing values before cleaning
print("Missing values before cleaning:")
print(df.isnull().sum())

# Heatmap
sns.heatmap(df.isnull(), cbar=False)
plt.show()

# Numerical columns → fill with mean
num_cols = df.select_dtypes(include=['number']).columns
imputer = SimpleImputer(strategy='mean')
df[num_cols] = imputer.fit_transform(df[num_cols])

# Categorical columns → fill with mode
cat_cols = df.select_dtypes(include=['object', 'string']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Save cleaned file
df.to_csv("cleaned_titanic.csv", index=False)

print("Cleaning completed. File saved as cleaned_titanic.csv")