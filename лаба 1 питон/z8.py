# Записать 2 варианта (с циклами while, for) программы вычисления условной функции в точках. Вывод результатов обеспечить в виде таблиц с указанием номера ветви, для которой он получен.
#	xi E [x0,xn]	xi=x0+i*deltaX	i=0,1....
#		|ax-lg(ax)	ax<1
#	Q = |1			ax=1		x0=0,2	xn=2	deltaX=0,2	a=1,2
#		|ax+lg(ax)	ax>1
import math

def Qfunc(a,x):
	if a*x<1:
		Q=a*x-math.log(a*x)
		return Q
	elif a*x==1:
		Q=1
		return Q
	else:
		Q=a*x+math.log(a*x)
		return Q

x0=0.2
xn=2
dx=0.2
a=1.2
x=float(input("Введите значение x: "))
x=x0

for i in range(10):
	if xn + dx / 2:
		print("| %.1f" % x,'|',Qfunc(a,x),'\t','|')
		x+=dx