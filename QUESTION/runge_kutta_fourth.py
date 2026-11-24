import math

print("Fourth-order Runge-Kutta method")
expression = input("Enter dy/dx: ")
x0 = float(input("Enter initial x0: "))
y0 = float(input("Enter initial y0: "))
h = float(input("Enter step h: "))
target = float(input("Enter target x: "))

x = x0
y = y0
while abs(target - x) > 1e-12:
    direction = 1 if target >= x else -1
    signed_h = abs(h) * direction
    step = signed_h if abs(signed_h) < abs(target - x) else target - x

    k1 = eval(expression, {"x": x, "y": y, "__builtins__": {}}, vars(math))
    k2 = eval(expression, {"x": x + step/2, "y": y + step*k1/2, "__builtins__": {}}, vars(math))
    k3 = eval(expression, {"x": x + step/2, "y": y + step*k2/2, "__builtins__": {}}, vars(math))
    k4 = eval(expression, {"x": x + step, "y": y + step*k3, "__builtins__": {}}, vars(math))

    y = y + step * (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + step

print("y(", target, ") =", round(y, 8))
