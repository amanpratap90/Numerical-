n = int(input("Enter the value of n: "))

x=[]
y=[]
for i in range (n):
     a = float(input(f"enter the value ofx[{i}]"))
     b = float(input(f"enter the value of y[{i}]"))
     x.append(a)
     y.append(b)

xp = float(input("Enter the value of xp: "))
result =0

for i in range (n):
    term =y[i]
    for j in range (n):
        if j!=i:
            term = term*(xp - x[j])/(x[i] - x[j])
    result = result +term
print("interv=polated value ",result)

      

