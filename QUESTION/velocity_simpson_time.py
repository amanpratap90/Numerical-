print("Q6 - Time using Simpson 1/3 rule")
n = int(input("Enter number of velocity data intervals (must be even): "))
s = []
v = []

for i in range(n + 1):
    s.append(float(input(f"Enter distance s[{i}] in meters: ")))
    v.append(float(input(f"Enter velocity v[{i}] in m/s: ")))

if n % 2 != 0:
    print("Simpson 1/3 rule requires an even number of intervals.")
else:
    h = s[1] - s[0]
    sum_value = 1/v[0] + 1/v[n]

    for i in range(1, n):
        if i % 2 == 0:
            sum_value = sum_value + 2 / v[i]
        else:
            sum_value = sum_value + 4 / v[i]

    time = h * sum_value / 3
    print("Time =", round(time, 8), "seconds")
