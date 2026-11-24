import math

print("Weddle's rule")
expression = input("Enter f(x): ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals (multiple of 6): "))

if n % 6 != 0:
    print("Weddle's rule requires n to be a multiple of 6.")
else:
    h = (b - a) / n
    sum_value = 0.0

    for i in range(n + 1):
        x = a + i * h
        value = eval(expression, {"x": x, "__builtins__": {}}, vars(math))
        if i % 6 == 0:
            coefficient = 1
        elif i % 6 == 1:
            coefficient = 5
        elif i % 6 == 2:
            coefficient = 1
        elif i % 6 == 3:
            coefficient = 6
        elif i % 6 == 4:
            coefficient = 1
        elif i % 6 == 5:
            coefficient = 5
        else:
            coefficient = 1
        sum_value = sum_value + coefficient * value

    result = 3 * h * sum_value / 10
    print("Approximate integral =", round(result, 8))
