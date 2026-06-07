from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = ["Red", "Blue", "Green", "Blue"]

df = pd.DataFrame(data, columns=["Color"])

print("Original Dataset:")
print(df)

label_encoder = LabelEncoder()
df["Encoded_Color"] = label_encoder.fit_transform(df["Color"])

print("\nDataset after Label Encoding:")
print(df)

print("\nLabel Mapping:")
for category, label in zip(label_encoder.classes_,
                           range(len(label_encoder.classes_))):
    print(f"{category} --> {label}")
