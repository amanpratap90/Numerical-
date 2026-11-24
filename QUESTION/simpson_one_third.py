import math

print("Simpson's 1/3 rule")
expression = input("Enter f(x) (example: 1/(1+x**2)): ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter even number of subintervals: "))

if n % 2 != 0:
    print("Simpson's 1/3 rule requires an even number of subintervals.")
else:
    h = (b - a) / n
    sum_value = eval(expression, {"x": a, "__builtins__": {}}, vars(math))
    sum_value = sum_value + eval(expression, {"x": b, "__builtins__": {}}, vars(math))

    for i in range(1, n):
        x = a + i * h
        value = eval(expression, {"x": x, "__builtins__": {}}, vars(math))
        if i % 2 == 0:
            sum_value = sum_value + 2 * value
        else:
            sum_value = sum_value + 4 * value

    result = h * sum_value / 3
    print("Approximate integral =", round(result, 8))
