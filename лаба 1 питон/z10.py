# Найти все пары двухзначных натуральных чисел М, N таких, что значение произведения М * N не изменится, если поменять местами цифры каждого из сомножителей.
m1=0
n1=0
for m in range(10,100):
	for n in range(10,100):
		m1=(m%10*10)+(m//10)
		n1=(n%10*10)+(n//10)
		if (m*n)==(m1*n1):
			print(m,n)