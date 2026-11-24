import math

print("Q8 - Weddle's rule")
expression = input("Enter f(x): ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals (multiple of 6): "))

if n % 6 != 0:
    print("n must be a multiple of 6.")
else:
    h = (b - a) / n
    coefficients = [1, 5, 1, 6, 1, 5]
    sum_value = 0.0

    for i in range(n + 1):
        x = a + i * h
        value = eval(expression, {"x": x, "__builtins__": {}}, vars(math))
        coefficient = 1 if i % 6 == 0 or i == n else coefficients[i % 6]
        sum_value = sum_value + coefficient * value

    print("Integral =", round(3 * h * sum_value / 10, 8))
