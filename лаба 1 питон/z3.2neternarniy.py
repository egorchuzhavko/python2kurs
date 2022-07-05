# 8.	Даны действительные числа x1, x2, x3, x4. Поменять значения переменных так, чтобы  x1 < x2 > x3 > x4.

x1=int(input("x1: "))
x2=int(input("x2: "))
x3=int(input("x3: "))
x4=int(input("x4: "))

if x2<x3:
	x2,x3=x3,x2
if x3<x4:
	x3,x4=x4,x3
if x1>x2:
	x1,x2=x2,x1
if x2<x3:
	x2,x3=x3,x2

print(x1,x2,x3,x4)