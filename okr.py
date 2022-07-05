class Triangle():
	name=".."
	a=0
	b=0
	c=0
	def __init__ (self,a,b,c,name):
		self.a=a
		self.b=b
		self.c=c
		self.name=name
	def displayInfo(self):
		print(f"Треугольник {self.name}\na={self.a}\nb={self.b}\nc={self.c}")
	@property
	def a(self):
		return self._a
	@a.setter
	def a(self,value):
		self._a=value
	@property
	def b(self):
		return self._b
	@b.setter
	def b(self,value):
		self._b=value
	@property
	def c(self):
		return self._c
	@c.setter
	def c(self,value):
		self._c=value
	def triangleType(self):
		if self.a == self.b and self.a == self.c:
			print(f"Треугольник {self.name} является равносторонним треугольником")
		elif (self.a == self.b and self.a != self.c) or (self.a == self.c and self.a != self.b) or (self.b == self.c and self.b != self.a):
			print(f"треугольник {self.name} является равнобедренным")
		elif self.c**2 == ((self.a**2)+(self.b**2)):
			print(f"Треугольник {self.name} является прямоугольным")
	def Square(self):
		import math
		p=(self.a+self.b+self.c)/2
		s=math.sqrt(p*(p-self.a)*(p*self.b)*(p*self.c))
		print(f"площадь Треугольника {self.name} = {s}")
	def perimetr(self):
		print(f"периметр {self.name} = {self.a+self.b+self.c}")
aaa=Triangle(10,13,18,"Первый")
aaa.displayInfo()
aaa.a=13
aaa.displayInfo()
aaa.Square()
aaa.triangleType()
aaa.perimetr()
bbb=Triangle(11,11,11,"Второй")
bbb.displayInfo()
bbb.Square()
bbb.triangleType()
bbb.perimetr()