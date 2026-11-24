print("Newton forward difference interpolation")
n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))

xp = float(input("Enter interpolation point xp: "))
h = x[1] - x[0]
u = (xp - x[0]) / h

difference = [y]
for i in range(1, n):
    row = []
    for j in range(n - i):
        row.append(difference[i - 1][j + 1] - difference[i - 1][j])
    difference.append(row)

result = y[0]
term = 1.0
for i in range(1, n):
    term = term * (u - i + 1) / i
    result = result + term * difference[i][0]

print("Interpolated value =", round(result, 8))
