
values = [12, 25, 40, 55, 70]
x_min = min(values)
x_max = max(values)
normalized_values = []

for x in values:
    x_prime = (x - x_min) / (x_max - x_min)
    normalized_values.append(round(x_prime, 4))

print("Original Values:", values)
print("Normalized Values:", normalized_values)