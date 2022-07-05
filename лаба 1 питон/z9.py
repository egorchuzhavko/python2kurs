	#Найти натуральное число от n до m с максимальной суммой делителей (n, m – натуральные числа).

while True:
	try:
		n=int(input("Введите n: "))
		break
	except ValueError:
		print("Введите целочисленное число")
while True:
	try:
		m=int(input("Введите m: "))
		break
	except ValueError:
		print("Введите целочисленное число")
		
chislosmaxsum=0
maxsumdel=0
sumdel=0
for chislo in range(n,m+1):
	for i in range(1,chislo+1):
		if chislo%i==0:
			sumdel+=i
		if sumdel>=maxsumdel:
			maxsumdel=sumdel
			chislosmaxsum=chislo
	sumdel=0
print("chislo s max sum del",chislosmaxsum)