n = int(input("enter the  value of n "))
value = 1995
x =[]
y =[]
for i in range(n):
   a = float (input (f"enetr the value of x[{i}]"))
   b = float (input (f"enter the value of y[{i}]"))
   x.append(a)
   y.append (b)
h=x[1] -x[0]
u = (value - x[0])/h

# differece table making
diff = [y]
for i in range(1,n):
  row = []
  for j in range (n-i):
       row.append (diff[i-1][j+1] - diff[i-1][j])
  diff.append(row)
  term =1
  result=y[0]
for i in range(1,n):
    term = term * (u-i+1)/i
    result = result + term * diff[i][0]
     
print("Interpolated value:", result) 