#3.	Создать программу, которая выводит на экран в возрастающем порядке все  трехзначные числа,  в десятичной записи которых нет одинаковых цифр.
chislo=100
while (i<1000):
	chislo1=chislo//100
	chislo2=chislo//10
	chislo3=chislo%10
	if(chislo1!=chislo2 and chislo1!=chislo3 and chislo3!=chislo2):
		print(chislo)
	i++