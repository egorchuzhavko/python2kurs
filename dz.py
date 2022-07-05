def decor_fullName(method_to_decor):
	def wrapper(self,ot4estvo):
		self.fullname=self.fullname+" "+ot4estvo
		return method_to_decor(self,ot4estvo)
	return wrapper

class Person():
	k=0
	name="..."
	surname="..."
	fullname="..."
	age=0
	def __init__(self,name,surname,age):
		Person.k=Person.k+1
		self.name=name
		self.surname=surname
		self.age=age
		self.fullname=name+" "+surname
	def __del__(self):
		Person.k-=1	
		print("Удаление: "+self.__str__())
	def display_info(self):
		print(f"Name:{self.name},Surname:{self.surname},Age:{self.age}, fullname:{self.fullName}")	
	def year_of_birth(self):
		print(f"Год рождения {self.name} {self.surname} Составляет:{2021-self.age}")
	
	@decor_fullName
	def fullName(self,ot4estvo):
		print(f"Моё полное имя {self.fullname}")

	@property
	def age(self):
		print("Getting..")
		return self._age

	@age.setter
	def age(self,value):
		print("Setting..")
		self._age=value
	

class Student(Person):
	k=0
	def __init__(self,name,surname,age,avg):
		Student.k=Student.k+1
		super().__init__(name,surname,age)
		self.avg=avg
	def study(self):
		print(f"{self.name} {self.surname} is studying")
	def display_info(self):
		print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Avg: {self.avg}")
	def __del__(self):
		Student.k-=1	
		print("Удаление: "+self.__str__())

	@decor_fullName
	def fullName(self,ot4estvo):
		print(f"Моё полное имя {self.fullname}")

	@property
	def age(self):
		print("Getting..")
		return self._age

	@age.setter
	def age(self,value):
		print("Setting..")
		self._age=value


class Teacher(Person):
	k=0
	def __init__(self,name,surname,age,workingtime):
		Teacher.k=Teacher.k+1
		super().__init__(name,surname,age)
		self.workingtime=workingtime
	def display_info(self):
		print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Working time: {self.workingtime}")
	def teach(self):
		print(f"{self.name} {self.surname} is teaching")
	def __del__(self):
		Teacher.k-=1	
		print("Удаление: "+self.__str__())

	@decor_fullName
	def fullName(self,ot4estvo):
		print(f"Моё полное имя {self.fullname}")

	@property
	def age(self):
		print("Getting..")
		return self._age

	@age.setter
	def age(self,value):
		print("Setting..")
		self._age=value


person1=Person("Elon","Musk",49)
person1.display_info()
print("\n\n\n")
person1.fullName("Anatoliev")
print("\n\n\n")         
person1.age = 10
person1.display_info()
print("\n\n\n")
person1.year_of_birth()
print("Количество объектов класса = ", Person.k)
st1=Student("Sanek", "Yanuwevich", 17 , 7.8)
st1.display_info()
print("\n\n\n")
st1.fullName("Vasiliev")
print("\n\n\n")
st1.study()
st1.age = 22
st1.display_info()
tchr1=Teacher("Dima", "Pupkin",  21, 30)
tchr1.display_info()
print("\n\n\n")
tchr1.fullName("Andreevich")
print("\n\n\n")
tchr1.teach()
tchr1.age = 11
tchr1.display_info()
print("Количество объектов Person: ", Person.k)
del person1
print("Количество объектов Person: ", Person.k)
print("Количество объектов Student: ", Student.k)
del st1
print("Количество объектов Student: ", Student.k)
print("Количество объектов Teacher: ", Teacher.k)
del tchr1
print("Количество объектов Teacher: ", Teacher.k)