import math

print("Simpson's 3/8 rule")
expression = input("Enter f(x): ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals (multiple of 3): "))

if n % 3 != 0:
    print("Simpson's 3/8 rule requires n to be a multiple of 3.")
else:
    h = (b - a) / n
    sum_value = eval(expression, {"x": a, "__builtins__": {}}, vars(math))
    sum_value = sum_value + eval(expression, {"x": b, "__builtins__": {}}, vars(math))

    for i in range(1, n):
        x = a + i * h
        value = eval(expression, {"x": x, "__builtins__": {}}, vars(math))
        if i % 3 == 0:
            sum_value = sum_value + 2 * value
        else:
            sum_value = sum_value + 3 * value

    result = 3 * h * sum_value / 8
    print("Approximate integral =", round(result, 8))
