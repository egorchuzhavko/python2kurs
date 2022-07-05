#Подсчитать количество столбцов заданной матрицы, которые составлены из попарно различных чисел. 
#Найти минимальный и максимальный элементы среди стоящих на главной и побочной диагонали и поменять их местами.

import numpy as np
from numpy import *
n=int(input("Введите размерность матрицы n: "))
mas=np.empty((n,n))

for i in range(0,n):
	for j in range(0,n):
		mas[i][j]=int(input("введите элемент матрицы: "))

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
			if mas[i][j]!=mas[k][j]:
				opros=True
			else:
				opros=False
	if opros==True:
		kolvostolbcov+=1

for i in range(n):
	if mas[i][i]>maksimymgl:
		maksimymgl=mas[i][i]
		maks_igl=i
	if mas[i][i]<maksimymgl:
		minimumgl=mas[i][i]
		min_igl=i

for i in range(n):
	for j in range(n):
		if (i+j==n-1):
			if mas[i][j]>maksimympb:
				maksimympb=mas[i][j]
				maks_ipb=i
				maks_jpb=j
			if mas[i][j]<minimumpb:
				minimumpb=mas[i][j]
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

