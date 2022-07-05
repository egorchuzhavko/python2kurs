# def func(kferz,lferz,mkon,nkon,r):
# 	if kferz==mkon:
# 		if r==1:
# 			print("Угрожает ферзь коню")
# 		else:
# 			print("Будет угрожать ферзь коню")
# 	elif lferz==nkon:
# 		if r==1:
# 			print("Угрожает ферзь коню")
# 		else:
# 			print("Будет угрожать ферзь коню")
# 	elif kferz+lferz==mkon+nkon:
# 		if r==1:
# 			print("Угрожает ферзь коню")
# 		else:
# 			print("Будет угрожать ферзь коню")
# 	elif kferz-mkon==lferz-nkon:
# 		if r==1:
# 			print("Угрожает ферзь коню")
# 		else:
# 			pprint("Будет угрожать ферзь коню")
# 	elif kferz+lferz==mkon+nkon+1:
# 		if r==1:
# 			print("Угрожает конь ферзю")
# 		else:
# 			print("Будет угрожать конь ферзю")
# 	elif kferz+lferz==mkon+nkon+3:
# 		if r==1:
# 			print("Угрожает конь ферзю")
# 		else:
# 			print("Будет угрожать конь ферзю")
# 	elif kferz+lferz==mkon+nkon-1:
# 		if r==1:
# 			print("Угрожает конь ферзю")
# 		else:
# 			print("Будет угрожать конь ферзю")
# 	elif kferz+lferz==mkon+nkon-3:	
# 		if r==1:
# 			print("Угрожает конь ферзю")
# 		else:
# 			print("Будет угрожать конь ферзю")
# 	else:
# 		if r==1:
# 			print("Сейчас никто никому не угрожает")
# 		else:
# 			print("В следующем ходу никто не будет никому угрожать")

# r=int(input("Кол-во ходов: "))
# for i in range(1,r+1):
# 	kferz=int(input("kferz= "))
# 	lferz=int(input("lferz= "))
# 	mkon=int(input("mkon= "))
# 	nkon=int(input("nkon= "))
# 	func(kferz,lferz,mkon,nkon,i)

import math

k=int(input("kferz= "))
l=int(input("lferz= "))
m=int(input("mkon= "))
n=int(input("nkon= "))
if (k==m or l == n or math.abs(k-n)==math.abs(lferz-n)):
	print('F win')
if ((math.abs(k-m)==2 and math.abs(l-n)==1) or (math.abs(k-n)==1 and math.abs(l-m)==1)):
	print('k win')