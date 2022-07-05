#Вывести последовательность действительных чисел b1, ..., bnn, получающуюся при чтении заданной квадратной матрицы порядка n по по схеме, которая приведена на рисунке. 

import numpy as np
from numpy import *
n=int(input("Введите размерность массива n: "))
mas=np.empty((n,n))
summ=0

for i in range(n):
	for j in range(n):
		mas[i][j]=int(input("введите элемент массива: "))

for i in range(n):
	if i==1 or i%2!=0:
		print(mas[i][::-1])
	else:
		print(mas[i])