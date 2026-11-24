import math

print("Q7 - Simpson 1/3 rule")
expression = input("Enter f(x): ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals (even): "))

if n % 2 != 0:
    print("n must be even.")
else:
    h = (b - a) / n
    sum_value = eval(expression, {"x": a, "__builtins__": {}}, vars(math))
    sum_value = sum_value + eval(expression, {"x": b, "__builtins__": {}}, vars(math))

    for i in range(1, n):
        x = a + i * h
        value = eval(expression, {"x": x, "__builtins__": {}}, vars(math))
        sum_value = sum_value + (4 if i % 2 else 2) * value

    print("Integral =", round(h * sum_value / 3, 8))
