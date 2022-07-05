def z31():
	#8.	ни одно из целых чисел x, y, z не является положительным;
	while True:
		try:
			x=int(input("Введите число: "))
			break;
		except ValueError:
			print("Вы ввели не то")

	while True:
		try:
			y=int(input("Введите число: "))
			break;
		except ValueError:
			print("Вы ввели не то")

	while True:
		try:
			z=int(input("Введите число: "))
			break;
		except ValueError:
			print("Вы ввели не то")


	print(True) if (x < 1 and y < 1 and z < 1) else print(False)

	print(x," ",y," ",z," ")

def z32nerernarniy():
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

def z32ternarniy():
	x1=int(input("x1: "))
	x2=int(input("x2: "))
	x3=int(input("x3: "))
	x4=int(input("x4: "))

	x2,x3 = (x3, x2) if (x2<x3) else (x2, x3)
	x3,x4 = (x4, x3) if (x3<x4) else (x3, x4)
	x1,x2 = (x2, x1) if (x1>x2) else (x1, x2)
	x2,x3 = (x3, x2) if (x2<x3) else (x2, x3)

	print(x1,x2,x3,x4)

vibor=input("Введите номер желаемого задания задания:\n1 - 3.1\n2 - 3.2 (через if)\n3 - 3.2 (тернарный оператор)\n")
if vibor=='1':
	z31()
elif vibor=='2':
	z32nerernarniy()
elif vibor=='3':
	z32ternarniy()