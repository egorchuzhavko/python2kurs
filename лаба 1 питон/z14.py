import numpy as np
from numpy import *
n=int(input("Введите размерность массива n: "))
mas=np.empty((n,n))
summ=0

for i in range(0,n):
	for j in range(0,n):
		mas[i][j]=int(input("введите элемент массива: "))
		
if n%2==0:
	for i in range(n//2+2):
		for j in range(n//2+1):
			if (i>=j and i+j<=n-1):
				summ+=mas[i][j]
				print(mas[i][j])
if n%2!=0:
	for i in range(n//2+2):
		for j in range(n//2+2):
			if (i>=j and i+j<=n-1):
				summ+=mas[i][j]
print(mas,summ)