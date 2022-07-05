import random
import numpy as np
from numpy import *

def zadanie191():

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

def zadanie19212():
	def zapolneniemasvruchnuy12(mas,n):
		for i in range(n):
			mas[i]=int(input("введите элемент массива: "))
		return mas

	def zapolneniemasrandom12(mas,n):
		for i in range(n):
				mas[i]=random.randint(-1000,1000)
		return mas
	n=int(input("введите размерность массива: "))
	mas=[0]*n
	vibor=input("Введите 1 - если хотите сами заполнить массив, 2 - если через функцию рандома ")
	if vibor=='1':
		masnew=zapolneniemasvruchnuy12(mas,n)
	elif vibor=='2':
		masnew=zapolneniemasrandom12(mas,n)
	summa=0
	for i in range(masnew.index(min((masnew))),n):
		summa+=mas[i]
	print(summa)

def zadanie19213():
	def zapolneniemasvruchnuy(mas,n):
		for i in range(n):
			for j in range(n):
				mas[i][j]=int(input("введите элемент массива: "))
		return mas

	def zapolneniemasrandom(mas,n):
		for i in range(n):
			for j in range(n):
				mas[i][j]=random.randint(-1000,1000)
		return mas
	n=int(input("введите размерность матрицы: "))
	mas=np.empty((n,n))
	vibor=input("Введите 1 - если хотите сами заполнить матрицу, 2 - если через функцию рандома ")
	if vibor=='1':
		masnew=zapolneniemasvruchnuy(mas,n)
	elif vibor=='2':
		masnew=zapolneniemasrandom(mas,n)
	kolvostolbcov=0
	stroka=0
	maksimymgl=mas[0][0]
	minimumgl=mas[0][0]
	minimumpb=mas[0][n-1]
	maksimympb=mas[0][n-1]
	maks_igl=0
	maks_ipb=0
	maks_jpb=0
	min_igl=0
	min_ipb=0
	min_jpb=0
	makss='pobochnaya'
	minn='pobochnaya'
	for j in range(n):
		for i in range(n-1):
			for k in range(n-1):
				k=i+1
				if masnew[i][j]!=masnew[k][j]:
					opros=True
				else:
					opros=False
		if opros==True:
			kolvostolbcov+=1

	for i in range(n):
		if masnew[i][i]>maksimymgl:
			maksimymgl=masnew[i][i]
			maks_igl=i
		if masnew[i][i]<maksimymgl:
			minimumgl=masnew[i][i]
			min_igl=i

	for i in range(n):
		for j in range(n):
			if (i+j==n-1):
				if masnew[i][j]>maksimympb:
					maksimympb=masnew[i][j]
					maks_ipb=i
					maks_jpb=j
				if mas[i][j]<minimumpb:
					minimumpb=masnew[i][j]
					min_jpb=j
					min_ipb=i

	if maksimymgl>maksimympb:
		makss='glavnaya'
	if minimumgl>minimumpb:
		minn='glavnaya'

	if makss=='glavnaya' and minn=='glavnaya':
		mas[maks_igl][maks_igl],mas[min_igl][min_igl]=mas[min_igl][min_igl],mas[maks_igl][maks_igl]
	if makss=='glavnaya' and minn=='pobochnaya':
		mas[maks_igl][maks_igl],mas[min_ipb][min_jpb]=mas[min_ipb][min_jpb],mas[maks_igl][maks_igl]
	if makss=='pobochnaya' and minn=='glavnaya':
		mas[maks_ipb][maks_jpb],mas[min_igl][min_igl]=mas[min_igl][min_igl],mas[maks_ipb][maks_jpb]
	if makss=='pobochnaya' and minn=='pobochnaya':
		mas[maks_ipb][maks_jpb],mas[min_ipb][min_jpb]==mas[min_ipb][min_jpb],mas[maks_ipb][maks_jpb]

	print("\tКоличество столбцов заданной матрицы, которые составлены из попарно различных чисел:",kolvostolbcov)
	print("\n",mas)

def zadanie19214():
	def zapolneniemasvruchnuy(mas,n):
		for i in range(n):
			for j in range(n):
				mas[i][j]=int(input("введите элемент массива: "))
		return mas

	def zapolneniemasrandom(mas,n):
		for i in range(n):
			for j in range(n):
				mas[i][j]=random.randint(-1000,1000)
		return mas
	
	n=int(input("Введите размерность массива n: "))
	mas=np.empty((n,n))
	summ=0
	vibor=input("Введите 1 - если хотите сами заполнить матрицу, 2 - если через функцию рандома ")
	if vibor=='1':
		masnew=zapolneniemasvruchnuy(mas,n)
	elif vibor=='2':
		masnew=zapolneniemasrandom(mas,n)
			
	if n%2==0:
		for i in range(n//2+2):
			for j in range(n//2+1):
				if (i>=j and i+j<=n-1):
					summ+=masnew[i][j]
					print(masnew[i][j])
	if n%2!=0:
		for i in range(n//2+2):
			for j in range(n//2+2):
				if (i>=j and i+j<=n-1):
					summ+=masnew[i][j]
	print(mas,summ)

def zadanie19317():
	def strrk2(stroka2,stroka1):
		for i in stroka1:
			if i not in ('0','1','2','3','4','5','6','7','8','9','B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z','A', 'E', 'I', 'O', 'U','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я'):
				stroka2+=i
		return stroka2
	stroka1=str(input("Введите символы и строки: "))
	strokacount=stroka1.count('abc')
	stroka2=''
	stroka2=strrk2(stroka2,stroka1)
	print(strokacount,"- число вхождений подстроки'abc'")
	print(stroka2)

def zadanie19318():
	def func(predlojenie):
		for i in predlojenie.split():
			if i.startswith("pr"):
				print(i)
	predlojenie=input("Введите предложение: ")
	func(predlojenie)
	

vbbr=input("Выберите задание: \n1 - 19.1.1\n2 - 19.2.12\n3 - 19.2.13\n4 - 19.2.13\n5 - 19.3.17\n6 - 19.3.18\n")
if vbbr=='1':
	a=zadanie191()
elif vbbr=='2':
	a=zadanie19212()
elif vbbr=='3':
	a=zadanie19213()
elif vbbr=='4':
	a=zadanie19214()
elif vbbr=='5':
	a=zadanie19317()
elif vbbr=='6':
	a=zadanie19318()