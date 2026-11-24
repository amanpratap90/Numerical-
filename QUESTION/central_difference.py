print("Central difference formula")
n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))

xp = float(input("Enter point at which derivative is required: "))
nearest = sorted(range(n), key=lambda i: abs(x[i] - xp))[:2]
i1, i2 = nearest
if x[i1] > x[i2]:
    i1, i2 = i2, i1

derivative = (y[i2] - y[i1]) / (x[i2] - x[i1])
print("Central difference derivative =", round(derivative, 8))
