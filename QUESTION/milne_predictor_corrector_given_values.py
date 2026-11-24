import math

print("Milne predictor-corrector with given starting values")
expression = input("Enter dy/dx (example: (1+x**2)*y): ")
n = int(input("Enter number of starting values: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))

h = x[1] - x[0]
target = float(input("Enter target x: "))

while x[-1] < target - 1e-12:
    if len(y) < 4:
        print("Milne's method requires at least four starting values.")
        break

    f = []
    for i in range(len(y)):
        f.append(eval(expression, {"x": x[i], "y": y[i], "__builtins__": {}}, vars(math)))

    predictor = y[-4] + 4*h*(2*f[-3] - f[-2] + 2*f[-1]) / 3
    x_next = x[-1] + h
    f_next = eval(expression, {"x": x_next, "y": predictor, "__builtins__": {}}, vars(math))
    corrector = y[-2] + h*(f[-2] + 4*f[-1] + f_next) / 3

    for iteration in range(100):
        f_next = eval(expression, {"x": x_next, "y": corrector, "__builtins__": {}}, vars(math))
        new_corrector = y[-2] + h*(f[-2] + 4*f[-1] + f_next) / 3
        if abs(new_corrector - corrector) < 1e-10:
            corrector = new_corrector
            break
        corrector = new_corrector

    x.append(x_next)
    y.append(corrector)

print("y(", round(target, 8), ") =", round(y[-1], 8))
