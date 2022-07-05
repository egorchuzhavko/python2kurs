print("\nСейчас вы проходите тест на пригодность к службе")
print("Во многих вопросах нужно отвечать да/нет, проверяйте наличие регистра, будьте аккуратны")

surname=input("Ваша фамилия: ")
name=input("Ваше имя: ")
dadsname=input("Ваше отчество: ")

while True:
	age=input("Введите ваш возраст: ")
	if not age.isdigit():
		print("Вы ввели не то что нужно")
	else:
		break

city=input("Город, в каком вы проживаете: ")
famstatus=input("Ваше семейное положение: ")
judicial=input("Наличие судимости: ")
education=input("Место учёбы (Если нет - напишите нет): ")

if (education == 'нет' or education == 'Нет' or education =='нЕт' or education == 'неТ' or education == 'НеТ' or education == 'НЕт' or education == 'нЕТ' or education == 'НЕТ' or education==''):
	education = "не имеется"
else:
	education=education
	
while True:
	height=input("Введите свой рост (в метрах): ")
	if height.replace(".","",1).isdigit():
		break
	if not height.replace(".","",1).isdigit():
		print("Вы ввели не то")

while True:
	weight=input("Введите свой вес (в килограммах): ")
	if weight.replace(".","",1).isdigit():
		break
	if not weight.replace(".","",1).isdigit():
		print("Вы ввели не то")

imt=float(weight)/(float(height)*float(height))
badweight=0

if 18.5<=imt<=37.5:
	imt=imt
else:
	badweight=badweight+1

information=[name, surname, dadsname, age, city, famstatus, judicial, education, height, weight, imt]

print("\n\tСейчас будет психологический тест, на который нужно отвечать + или - \n")

test=[1,2,3,4,5,6,7,8,9,10]
questionnumber=0
nomer=-1
def fortest1(test,nomer,questionnumber):
	for i in range (len(test)):
		test[nomer]=questionnumber

while True:
	suicide=input("Были ли мысли о суициде? ")
	if suicide=='+' or suicide=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a1=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Думали ли вы о том, что вы ненужны? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a2=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Любите ли вы помагать людям? ")
	if questionnumber =='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a3=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас фобия? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a4=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Страдаете ли вы от бессонницы? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a5=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Был ли у вас приступ? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a6=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Любите ли вы работать? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a7=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас зависимость от спиртных напитков? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a8=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас зависимость от наркотиков? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a9=fortest1(test,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас вредные привычки? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

a10=fortest1(test,nomer,questionnumber)

psychologytest=0
psychologytest=test.count('+')

bolezni=[1,2,3,4,5,6,7,8,9,10,11,12]
questionnumber=0
nomer=-1
def fortest2(bolezni,nomer,questionnumber):
	for i in range (len(bolezni)):
		bolezni[nomer]=questionnumber

print("\n\tОпрос о серьёзных болезнях\n")

while True:
	questionnumber=input("Есть ли у вас раковые заболевания? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b1=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас вич инфекция? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b2=fortest2(bolezni,nomer,questionnumber)


while True:
	questionnumber=input("Есть ли у вас туберкулез? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b3=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас сифилис? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b4=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас заболевания крови? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b5=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас болезни глаз? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b6=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас кишечные заболевания? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b7=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас синдром Дауна? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b8=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас аутизм? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b9=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас синдром Туретта? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b10=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас проблемы с гармонами? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b11=fortest2(bolezni,nomer,questionnumber)

while True:
	questionnumber=input("Есть ли у вас проблемы с речью? ")
	if questionnumber=='+' or questionnumber=='-':
		nomer=nomer+1
		break
	else:
		print("Вы ввели не то")

b12=fortest2(bolezni,nomer,questionnumber)
boleznires=0
boleznires=bolezni.count('+')

print(" ")
print(" ")
print("\n\t\t\tУчётная карта призывника")
print("\tОбщие сведения")
#information=[name, surname, dadsname, age, city, famstatus, judicial, education, height, weight, imt]
print("ФИО:",information[0],information[1], information[2])
print("Возраст: ",information[3])
print("Рост: ",information[8])
print("Вес: ",information[9])
print("Индекс массы тела: ",information[10])
print("Место образования: ",information[7])
print("Город проживания: ",information[4])
print("Семейное положение: ",information[5])
print("Наличие судимости: ",information[6])

print("\tНаличие серьёзных заболеваний: ")

if boleznires > 0:
	print("Имеются серьёзные заболевания")
else:
	print("Серьёзных заболеваний нет")

print("\tПсихологическое состояние: ")

if psychologytest>=6:
	print("Болен")
else:
	print("Здоров")

print("\nРезультат: ")

if (psychologytest>=6 or boleznires>=1 or badweight==1):
	print("НЕ ГОДЕН")
else:
	print("ГОДЕН")
