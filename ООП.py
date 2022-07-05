class Person():
	k=0
	def __init__(self,name,surname,age):
		Person.k=Person.k+1
		self.name=name
		self.surname=surname
		self.age=age
	def __del__(self):
		Person.k-=1	
		print("Удаление: "+self.__str__())
	def display_info(self):
		print(f"Name:{self.name},Surname:{self.surname},Age:{self.age}")
	def year_of_birth(self):
		print(f"Год рождения {self.name} {self.surname} Составляет:{2021-self.age}")


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


person1=Person("Elon","Musk",49)
person2=Person("Mike","Tyson",59)
person1.display_info()
person2.display_info()
person1.year_of_birth()
person2.year_of_birth()
print("Количество объектов класса = ", Person.k)
st1=Student("Sanek", "Yanuwevich", 17, 7.8)
st1.display_info()
st1.study()
st2=Student("Denchik", "Slaziey", 18, 8.1)
st2.display_info()
st2.study()
tchr1=Teacher("Dima", "Pupkin", 21, 30)
tchr1.display_info()
tchr1.teach()
tchr2=Teacher("Petya", "Nepupkin", 27, 22)
tchr2.display_info()
tchr2.teach()
print("Количество объектов Person: ", Person.k)
print("Количество объектов Student: ", Student.k)
del st1
print("Количество объектов Student: ", Student.k)
print("Количество объектов Teacher: ", Teacher.k)
del tchr1
print("Количество объектов Teacher: ", Teacher.k)