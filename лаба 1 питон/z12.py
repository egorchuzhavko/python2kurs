# Определите сумму элементов массива, расположенных после минимального по модулю значения.
n=int(input("введите размерность массива: "))
mas=[0]*n
for i in range(n):
	mas[i]=int(input("введите элемент массива: "))
summa=0
for i in range(mas.index(min(mas))+1,n):
	summa+=mas[i]
print(summa)