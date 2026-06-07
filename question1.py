import pandas as pd
import numpy as np
data = {
    'Maths': [85, 90, np.nan, 78, 88],
    'Science': [92, np.nan, 75, 80, 85],
    'English': [88, 76, 90, np.nan, 82]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\nMissing Values:")
print(df.isnull())

print("\nNumber of Missing Values in Each Column:")
print(df.isnull().sum())

df_mean = df.fillna(df.mean())
print("\nDataFrame after Replacing Missing Values with Mean:")
print(df_mean)
df_median = df.fillna(df.median())
print("\nDataFrame after Replacing Missing Values with Median:")
print(df_median)
df_dropped = df.dropna()
print("\nDataFrame after Dropping Rows with Missing Values:")
print(df_dropped)