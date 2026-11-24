import math

print("Modified Euler method")
expression = input("Enter dy/dx (example: x**2+y**2): ")
x0 = float(input("Enter initial x0: "))
y0 = float(input("Enter initial y0: "))
h = float(input("Enter step h: "))
target = float(input("Enter target x: "))

x = x0
y = y0
while abs(target - x) > 1e-12:
    if (target - x) * h < 0:
        h = -h
    step = h if abs(h) < abs(target - x) else target - x

    f0 = eval(expression, {"x": x, "y": y, "__builtins__": {}}, vars(math))
    predictor = y + step * f0
    x_next = x + step
    corrected = y

    for iteration in range(100):
        f1 = eval(expression, {"x": x_next, "y": predictor, "__builtins__": {}}, vars(math))
        corrected_new = y + step * (f0 + f1) / 2
        if abs(corrected_new - corrected) < 1e-8:
            corrected = corrected_new
            break
        corrected = corrected_new
        predictor = corrected

    x = x_next
    y = corrected

print("y(", target, ") =", round(y, 8))
