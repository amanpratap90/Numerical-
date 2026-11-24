import math

print("Trapezoidal rule")
expression = input("Enter f(x) (example: 1-x**2): ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals: "))

h = (b - a) / n
sum_value = 0.5 * (
    eval(expression, {"x": a, "__builtins__": {}}, vars(math)) +
    eval(expression, {"x": b, "__builtins__": {}}, vars(math))
)

for i in range(1, n):
    x = a + i * h
    sum_value = sum_value + eval(expression, {"x": x, "__builtins__": {}}, vars(math))

result = h * sum_value
print("Approximate integral =", round(result, 8))
