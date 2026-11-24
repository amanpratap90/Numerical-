import math

print("Modified Euler: dy/dx = x^2 + y^2")
expression = input("Enter dy/dx (example: x**2+y**2): ")
x = float(input("Enter initial x0: "))
y = float(input("Enter initial y0: "))
h = float(input("Enter step h: "))
target = float(input("Enter target x: "))

while abs(target - x) > 1e-12:
    step = h if abs(h) < abs(target - x) else target - x
    if (target - x) < 0:
        step = -abs(step)
    f0 = eval(expression, {"x": x, "y": y, "__builtins__": {}}, vars(math))
    x_next = x + step
    predictor = y + step * f0

    corrected = predictor
    for iteration in range(100):
        f1 = eval(expression, {"x": x_next, "y": predictor, "__builtins__": {}}, vars(math))
        corrected = y + step * (f0 + f1) / 2
        if abs(corrected - predictor) < 1e-10:
            break
        predictor = corrected

    x = x_next
    y = corrected

print("y(", target, ") =", round(y, 8))
