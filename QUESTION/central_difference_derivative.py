print("Central difference derivative")
n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))

xp = float(input("Enter point xp: "))

order = sorted(range(n), key=lambda i: x[i])
x = [x[i] for i in order]
y = [y[i] for i in order]

if n < 2:
    print("At least two data points are required.")
else:
    exact = [i for i in range(n) if abs(x[i] - xp) < 1e-12]
    if exact:
        i = exact[0]
        if i == 0:
            derivative = (y[1] - y[0]) / (x[1] - x[0])
        elif i == n - 1:
            derivative = (y[-1] - y[-2]) / (x[-1] - x[-2])
        else:
            h_left = xp - x[i - 1]
            h_right = x[i + 1] - xp
            derivative = ((y[i] - y[i - 1]) / h_left +
                          (y[i + 1] - y[i]) / h_right) / 2
    else:
        right = next((i for i in range(n) if x[i] > xp), None)
        left = right - 1 if right is not None else None
        if right is None or left is None:
            print("The point must lie within the data range.")
        else:
            derivative = (y[right] - y[left]) / (x[right] - x[left])

if n >= 2:
    if exact or (right is not None and left is not None):
        print("Central difference derivative =", round(derivative, 8))
