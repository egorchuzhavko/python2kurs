# Найдите сумму первых n натуральных чисел, которые делятся на 9

n=int(input("Введите число: "))
summa=0
dlina=n*9
for nomer in range(dlina):
	if nomer%9==0:
		summa=summa+nomer
print(summa)