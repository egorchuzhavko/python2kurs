#1 Вариант
import math 

class Triangle():
	figure="..."
	name="..."
	number=0
	a=0
	b=0
	c=0
	point_x1=0
	point_y1=0
	point_x2=0
	point_y2=0
	perimetr=0
	pperimetr=0
	square=0
	def __init__(self,point_x1,point_y1,point_x2,point_y2,a,b,c):
		Triangle.number+=1
		self.figure=figure="Треугольник"
		self.name="object "+ str(Triangle.number)
		self.point_x1=point_x1
		self.point_y1=point_y1
		self.point_x2=point_x2
		self.point_y2=point_y2
		self.a=a
		self.b=b
		self.c=c
		self.perimetr=0
		self.pperimetr=0
		self.square=0
	def Pperimetr(self):
		self.pperimetr=(self.a+self.b+self.c)/2
		return self.pperimetr

	def Square(self):
		self.pperimetr=self.Pperimetr()
		self.square=math.sqrt(self.pperimetr*(self.pperimetr-self.a)*(self.pperimetr-self.b)*(self.pperimetr-self.c))
		return self.square

	def Print(self):
		print(f"Рисую {self.figure}")

	def Perimetr(self):
		self.perimetr=self.a+self.b+self.c
		return self.perimetr

	def Print(self):
		print(f"Рисую {self.figure}")

	def Moving(self,px1,py1,px2,py2):
		self.point_x1+=px1
		self.point_y1+=py1
		self.point_x2+=px2
		self.point_y2+=py2
		print(f"Новые значения: x1={self.point_x1}, y1={self.point_y1}, x2={self.point_x2}, y1={self.point_y2}")

	def Sjatie(self,zn):
		self.a-=zn
		self.b-=zn
		self.c-=zn
		print(f"Новые значения: a={self.a}, b={self.b}, c={self.c}")

	def Rastyajenie(self,zn):
		self.a+=zn
		self.b+=zn
		self.c+=zn
		print(f"Новые значения: a={self.a}, b={self.b}, c={self.c}")


t1=Triangle(3,2,5,3,6,6,10)
t2=Triangle(5,1,3,5,4,2,3)
print(t1.figure,t1.name)
print(t2.figure,t2.name)
t1.Print()
t2.Print()
print("Периметр Треугольника 1 = ",t1.Perimetr())
print("Периметр Треугольника 2 = ",t2.Perimetr())
print("Площадь Треугольника 1 = ",t1.Square())
print("Площадь Треугольника 2 = ",t2.Square())
px1=int(input("Введите значение 1 треугольника для передвижения x1: "))
py1=int(input("Введите значение 1 треугольника для передвижения y1: "))
px2=int(input("Введите значение 1 треугольника для передвижения x2: "))
py2=int(input("Введите значение 1 треугольника для передвижения y2: "))
t1.Moving(px1,py1,px2,py2)
px1=int(input("Введите значение 2 треугольника для передвижения x1: "))
py1=int(input("Введите значение 2 треугольника для передвижения y1: "))
px2=int(input("Введите значение 2 треугольника для передвижения x2: "))
py2=int(input("Введите значение 2 треугольника для передвижения y2: "))
t2.Moving(px1,py1,px2,py2)
zn=int(input("Введите значение для уменьшения стороны треугольника 1: "))
t1.Sjatie(zn)
zn=int(input("Введите значение для уменьшения стороны треугольника 2: "))
t2.Sjatie(zn)
zn=int(input("Введите значение для растяжения стороны треугольника 1: "))
t1.Rastyajenie(zn)
zz=int(input("Введите значение для растяжения стороны треугольника 2: "))
t2.Rastyajenie(zn)