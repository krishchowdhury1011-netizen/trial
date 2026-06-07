import pandas as pd
data = {
    'ID': [101, 102, 103, 102, 104, 103],
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'David', 'Charlie'],
    'Marks': [85, 90, 78, 90, 88, 78]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

duplicates = df.duplicated()

print("\nDuplicate Entries:")
print(duplicates)

print("\nRows that are Duplicates:")
print(df[duplicates])

df_no_duplicates = df.drop_duplicates()

print("\nDataset After Removing Duplicate Rows:")
print(df_no_duplicates)