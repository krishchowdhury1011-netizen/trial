

import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    'Age': [18, 22, 25, 30, 35],
    'Salary': [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

print("\nScaled Dataset (Standardized):")
print(scaled_df)