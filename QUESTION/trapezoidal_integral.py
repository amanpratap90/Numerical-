import math

print("Q5 - Trapezoidal rule")
expression = input("Enter f(x): ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals: "))

h = (b - a) / n
sum_value = (eval(expression, {"x": a, "__builtins__": {}}, vars(math)) +
             eval(expression, {"x": b, "__builtins__": {}}, vars(math))) / 2

for i in range(1, n):
    x = a + i * h
    sum_value = sum_value + eval(expression, {"x": x, "__builtins__": {}}, vars(math))

print("Integral =", round(h * sum_value, 8))
