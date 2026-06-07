import numpy as np
data = [12, 25, 40, 55, 70]

mean = np.mean(data)

std_dev = np.std(data)

z_scores = [(x - mean) / std_dev for x in data]

print("Original Data:", data)
print("Mean =", round(mean, 2))
print("Standard Deviation =", round(std_dev, 2))

print("\nZ-Score Normalized Data:")
for x, z in zip(data, z_scores):
    print(f"Value: {x} --> Z-Score: {z:.4f}")