import math

print("Milne predictor-corrector: dy/dx = x^2 + y^2 - 2")
expression = input("Enter dy/dx (example: x**2+y**2-2): ")
x = float(input("Enter initial x: "))
y = float(input("Enter initial y: "))
h = float(input("Enter step h: "))
target = float(input("Enter target x: "))

xs = [x]
ys = [y]

for i in range(3):
    k1 = eval(expression, {"x": xs[-1], "y": ys[-1], "__builtins__": {}}, vars(math))
    k2 = eval(expression, {"x": xs[-1] + h/2, "y": ys[-1] + h*k1/2, "__builtins__": {}}, vars(math))
    k3 = eval(expression, {"x": xs[-1] + h/2, "y": ys[-1] + h*k2/2, "__builtins__": {}}, vars(math))
    k4 = eval(expression, {"x": xs[-1] + h, "y": ys[-1] + h*k3, "__builtins__": {}}, vars(math))
    ys.append(ys[-1] + h*(k1 + 2*k2 + 2*k3 + k4)/6)
    xs.append(xs[-1] + h)

while xs[-1] < target - 1e-12:
    f = []
    for i in range(len(ys)):
        f.append(eval(expression, {"x": xs[i], "y": ys[i], "__builtins__": {}}, vars(math)))

    predictor = ys[-4] + 4*h*(2*f[-3] - f[-2] + 2*f[-1])/3
    x_next = xs[-1] + h
    corrector = ys[-2] + h*(f[-2] + 4*f[-1] +
        eval(expression, {"x": x_next, "y": predictor, "__builtins__": {}}, vars(math)))/3

    for iteration in range(100):
        f_next = eval(expression, {"x": x_next, "y": corrector, "__builtins__": {}}, vars(math))
        new_corrector = ys[-2] + h*(f[-2] + 4*f[-1] + f_next)/3
        if abs(new_corrector - corrector) < 1e-10:
            corrector = new_corrector
            break
        corrector = new_corrector

    xs.append(x_next)
    ys.append(corrector)

print("y(", target, ") =", round(ys[-1], 8))
