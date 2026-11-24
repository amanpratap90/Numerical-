import math

print("Milne predictor-corrector method")
expression = input("Enter dy/dx (example: 1+x**2*y): ")
n = int(input("Enter number of starting points: "))
x = []
y = []

for i in range(n):
    x.append(float(input(f"Enter x[{i}]: ")))
    y.append(float(input(f"Enter y[{i}]: ")))

target = float(input("Enter target x: "))
h = x[1] - x[0]

while x[-1] < target - 1e-12:
    fx = []
    for i in range(len(x)):
        fx.append(eval(expression, {"x": x[i], "y": y[i], "__builtins__": {}}, vars(math)))

    if len(y) < 4:
        print("Milne's method requires at least four starting values.")
        break

    predictor = y[-4] + 4*h*(2*fx[-3] - fx[-2] + 2*fx[-1]) / 3
    x_next = x[-1] + h
    corrector = y[-2]

    for iteration in range(100):
        fx_next = eval(expression, {"x": x_next, "y": predictor, "__builtins__": {}}, vars(math))
        corrector_new = y[-2] + h*(fx[-2] + 4*fx[-1] + fx_next) / 3
        if abs(corrector_new - corrector) < 1e-8:
            corrector = corrector_new
            break
        corrector = corrector_new
        predictor = corrector

    x.append(x_next)
    y.append(corrector)

print("y(", round(target, 8), ") =", round(y[-1], 8))
