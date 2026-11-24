import math

print("Bisection method")
expression = input("Enter f(x) (example: x**3-3*x+1): ")
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
tolerance = float(input("Enter tolerance: "))
maximum_iterations = int(input("Enter maximum iterations: "))

fa = eval(expression, {"x": a, "__builtins__": {}}, vars(math))
fb = eval(expression, {"x": b, "__builtins__": {}}, vars(math))

if fa * fb > 0:
    print("The chosen interval does not bracket a root.")
else:
    for iteration in range(1, maximum_iterations + 1):
        c = (a + b) / 2
        fc = eval(expression, {"x": c, "__builtins__": {}}, vars(math))

        if abs(fc) < tolerance or (b - a) / 2 < tolerance:
            print("Root =", round(c, 8))
            print("f(root) =", fc)
            print("Iterations =", iteration)
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    else:
        print("Method did not converge.")
