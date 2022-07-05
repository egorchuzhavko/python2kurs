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

