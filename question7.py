import pandas as pd

data = {
    'City': ['Kolkata', 'Delhi', 'Mumbai', 'Chennai']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
one_hot_encoded = pd.get_dummies(df, columns=['City'])

print("\nDataset after One-Hot Encoding:")
print(one_hot_encoded)