import math
class Romb(object):
	objnum = 1
	name = ""
	nameobj = "obj"
	place = ""
	countab = 4
	perimt = 0
	ploshad = 0
	def __init__(self, sizestoron, ugol, x1 , y1, x2, y2):
		self.name = "Ромб"
		self.nameobj =  "obj"+str(Romb.objnum)
		self.sizestoron=sizestoron
		self.ugol=ugol
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2
		Romb.objnum+=1

	def disp_inf(self):
		print(f"Name = {self.name}, Name object = {self.nameobj}, Size storon = {self.sizestoron}, Maliy ugol = {self.ugol}, x1 = {self.x1}, y1 = {self.y1}, x2 = {self.x2}, y2 = {self.y2}")
	
	def perim(self):
		self.perim = 0

	def Plosh(self):
		self.ploshad = self.sizestoron * self.sizestoron * math.sin(self.ugol)
		print (f"S = {self.ploshad}")

	def draw(self):
		print (f" ромб от точки ({self.x1},{self.y1}) до точки ({self.x2} {self.y2})")

	def sdvig(self, right, up):
		self.x1 += right
		self.y1 += up
		self.x2 += right
		self.y2 += up 
	def sizedown(self):
		print("krja")

	def sizeup(self):
		print("ne krja")

r1=Romb(14,30,12,14,42,56)
r2=Romb(40, 45, 30, 20, 20, 10)
r1.Plosh()
r1.disp_inf()


