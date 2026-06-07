
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = {
    'Age': [18, 22, 25, 30, 35],
    'Salary': [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


minmax_scaler = MinMaxScaler()
minmax_scaled = minmax_scaler.fit_transform(df)

minmax_df = pd.DataFrame(minmax_scaled, columns=df.columns)

print("\nMin-Max Scaled Dataset:")
print(minmax_df)

standard_scaler = StandardScaler()
standard_scaled = standard_scaler.fit_transform(df)

standard_df = pd.DataFrame(standard_scaled, columns=df.columns)

print("\nStandardized Dataset:")
print(standard_df)