print("Q1 - Number of students between 100 and 110")
n = int(input("Enter number of class intervals: "))

lower = []
upper = []
frequency = []

for i in range(n):
    lower.append(float(input(f"Enter lower limit of interval {i + 1}: ")))
    upper.append(float(input(f"Enter upper limit of interval {i + 1}: ")))
    frequency.append(float(input(f"Enter frequency of interval {i + 1}: ")))

target_lower = float(input("Enter required lower limit: "))
target_upper = float(input("Enter required upper limit: "))
count = 0.0

for i in range(n):
    overlap = min(upper[i], target_upper) - max(lower[i], target_lower)
    if overlap > 0:
        proportion = overlap / (upper[i] - lower[i])
        count = count + proportion * frequency[i]

print("Estimated number of students =", round(count, 4))
