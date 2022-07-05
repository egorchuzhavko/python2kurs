import random
import numpy as np
from numpy import *

n=int(input("Введите размерность матрицы n: "))
mas=np.empty((n,n))
for i in range(n):
		for j in range(n):
			mas[i][j]=random.randint(-1000,1000)

print(mas)