import math

print("Fourth-order RK: dy/dx = x*y")
expression = input("Enter dy/dx (example: x*y): ")
x = float(input("Enter initial x: "))
y = float(input("Enter initial y: "))
h = float(input("Enter step h: "))
target = float(input("Enter target x: "))

while abs(target - x) > 1e-12:
    step = h if abs(h) < abs(target - x) else target - x
    if (target - x) < 0:
        step = -abs(step)

    k1 = eval(expression, {"x": x, "y": y, "__builtins__": {}}, vars(math))
    k2 = eval(expression, {"x": x + step/2, "y": y + step*k1/2, "__builtins__": {}}, vars(math))
    k3 = eval(expression, {"x": x + step/2, "y": y + step*k2/2, "__builtins__": {}}, vars(math))
    k4 = eval(expression, {"x": x + step, "y": y + step*k3, "__builtins__": {}}, vars(math))

    y = y + step * (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + step

print("y(", target, ") =", round(y, 8))
