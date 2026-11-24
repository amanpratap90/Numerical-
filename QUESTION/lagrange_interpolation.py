print("Lagrange interpolation")
n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))

xp = float(input("Enter interpolation point xp: "))
result = 0.0

for i in range(n):
    term = y[i]
    for j in range(n):
        if i != j:
            term = term * (xp - x[j]) / (x[i] - x[j])
    result = result + term

print("Interpolated value =", round(result, 8))
