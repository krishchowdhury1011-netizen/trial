
import pandas as pd

data = {
    'Age': ['18', '22', '25', '30', '35']
}

df = pd.DataFrame(data)

print("Before Conversion:")
print(df)
print(df.dtypes)

df['Age'] = df['Age'].astype(int)

print("\nAfter Conversion:")
print(df)
print(df.dtypes)