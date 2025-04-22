import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('dirty_cafe_sales.csv')

# Drop rows with missing 'Transaction Date' and convert types
df.dropna(subset=['Transaction Date'], inplace=True)
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')
df['Total Spent'] = pd.to_numeric(df['Total Spent'], errors='coerce')

# Identify columns
numerical = df.select_dtypes(include=np.number).columns.tolist()
categorical = df.select_dtypes(include='object').columns.tolist()

# Replace error strings with NaN
df.replace(['ERROR', 'UNKNOWN'], np.nan, inplace=True)

# Fill missing numerical values with mean (except 'Total Spent')
for col in numerical:
    if col != 'Total Spent':
        df[col].fillna(df[col].mean(), inplace=True)

# Recalculate missing 'Total Spent'
df['Total Spent'].fillna(df['Price Per Unit'] * df['Quantity'], inplace=True)

# Fill missing categorical values with mode
for col in categorical:
    df[col].fillna(df[col].mode(dropna=True)[0], inplace=True)

# Final check
print("Missing values (%):\n", df.isna().mean() * 100)
print("Cleaned shape:", df.shape)
