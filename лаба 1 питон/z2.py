def z21():
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

def z22():
	chislo=float(input("введите положительное вещественное число: "))
	n1=chislo*10%10//1
	n2=chislo*100%10//1
	n4=chislo*10000%10//1
	nsum=n1+n4
	if n2==nsum:
		print("2 цифра после запятой РАВНА сумме 2 и 4 цифр после запятой")
	else:
		print("2 цифра после запятой НЕ РАВНА сумме 2 и 4 цифр после запятой")

vibor=input("Введите номер желаемого задания задания:\n1 - z2.1\n2 - z2.2\n")
if vibor=='1':
	z21()
elif vibor=='2':
	z22()