import numpy as np

data = [12, 15, 18, 20, 22, 25, 30, 100]

mean = np.mean(data)
std_dev = np.std(data)

print("Dataset:", data)
print("Mean =", round(mean, 2))
print("Standard Deviation =", round(std_dev, 2))

threshold = 3
outliers = []

print("\nZ-Scores:")
for x in data:
    z_score = (x - mean) / std_dev
    print(f"Value: {x} --> Z-Score: {z_score:.2f}")

    if abs(z_score) > threshold:
        outliers.append(x)

print("\nOutliers Detected:")
if outliers:
    print(outliers)
else:
    print("No outliers found.")