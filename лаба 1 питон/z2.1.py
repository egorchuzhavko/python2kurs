#8. Дано четырехзначное натуральное n. Верно ли, что все цифры числа одинаковые? 
while True:
	try:
		chislo=int(input("Введите чётырёхзначное число: "))
		if 999 < chislo < 10000:
			break;
		else:
			print("Вы ввели не то")
	except ValueError:
		print("Вы ввели не то")
chislo1=chislo//1000
chislo2=chislo//100%10
chislo3=chislo//10%10
chislo4=chislo%10
#print("chislo1 ",chislo1,"\nchislo2 ",chislo2,"\nchislo3 ",chislo3,"\nchislo4 ",chislo4)
if chislo2 == chislo1 & chislo3 == chislo1 & chislo4 == chislo1:
	print("Одинаковые")
else:
	print("Не одинаковые")
	