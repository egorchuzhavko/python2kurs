import random
chislo1=random.randint(0,99)
chislo2=random.randint(0,99)
chislo3=chislo1+chislo2
print("Введите ответ выражения: ",chislo1,"+",chislo2)
otvet=int(input())
if otvet==chislo3:
	print("Правильно, вы угадали")
else:
	print("Неправильно, вы неугадали")