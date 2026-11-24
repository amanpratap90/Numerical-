import math

print("Q9 - Gauss three-point quadrature")
expression = input("Enter f(x): ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))

points = [-math.sqrt(3/5), 0.0, math.sqrt(3/5)]
weights = [5/9, 8/9, 5/9]
midpoint = (a + b) / 2
half_range = (b - a) / 2

result = 0.0
for i in range(3):
    x = midpoint + half_range * points[i]
    value = eval(expression, {"x": x, "__builtins__": {}}, vars(math))
    result = result + weights[i] * value

result = half_range * result
print("Integral =", round(result, 8))
