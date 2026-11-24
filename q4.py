def(x):
    return x*x
a = float( input("enter the value of a "))
b = float (input("enter the value of b "))
n =int(input("enter the value of n"))

h =(b-a)/n
s = f(a)+f(b)

for i in range (n):
    x = a +i*h
    if i%2==0 :
     s= s + 2*f(x)
     else : 
        s = s + 4*f(x)
I = (h/3)*s
print ( I)   

# for velocity 
n = int ( input("enter the value of n "))
x =[],,
y=[]

for i in range (n+1):
    a = float(input(f"enetr the value 0f x[{i}]"))
    b= float(input(f"enter the value of  y[{i}]"))
    x.append(a)
    y.append(b)
h = x[n] -x[0]/n 

s = 1/x[0] + 1/x[n]


