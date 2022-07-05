x = float(input("Введите х: "))
y = float(input("Введите у: "))

R=(x*x+y*y)**(1/2)

if ((x<=0 and x >=-1 and y>=-1 and y<=1) or (R<=1 and x>=0 and x<=2)):
	print("Принадлежит")
else:
	print("Не принадлежит")
