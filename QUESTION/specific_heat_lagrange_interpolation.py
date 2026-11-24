print("Q3 - Specific heat interpolation")
n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter temperature x[{i}]: ")))
    y.append(float(input(f"Enter specific heat y[{i}]: ")))

xp = float(input("Enter required temperature: "))
result = 0.0

for i in range(n):
    term = y[i]
    for j in range(n):
        if i != j:
            term = term * (xp - x[j]) / (x[i] - x[j])
    result = result + term

print("Specific heat =", round(result, 8))
