import math
def function(x):
	if x==0:
		try:
			y=((math.cos(math.pi*x**3)+math.log((1+x)**2))**4)*(math.exp(x**2)+((1/x)**1/2)+math.cos(math.exp(x)))
		except ZeroDivisionError:
			print("Невозможно деление на 0")
	elif x==-1.0:
		try:
			y=((math.cos(math.pi*x**3)+math.log((1+x)**2))**4)*(math.exp(x**2)+((1/x)**1/2)+math.cos(math.exp(x)))
		except ValueError:
			print("Натуральный логарифм не может считаться при -1")
	else:
		y=((math.cos(math.pi*x**3)+math.log((1+x)**2))**4)*(math.exp(x**2)+((1/x)**1/2)+math.cos(math.exp(x)))
		print("y =",y)

while True:
	try:
		x=float(input("Введите x: "))
		break
	except ValueError:
		print("Введите целочисленное число")

function(x)