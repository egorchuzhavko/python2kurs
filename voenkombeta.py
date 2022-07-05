
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
	height=input("Ваш рост (в метрах): ")
	if height=='':
		print("Вы ничего не ввели, начните заново программу")
		input("Нажмите на Enter для окончания программы")
		exit(0)
	else:
		break


weight=input("Ваш вес (в килограммах): ")
if weight=='':
	print("Вы ничего не ввели, начните заново программу")
	input("Нажмите на Enter для окончания программы")
	exit(0)
else:
	weight=weight

imt=float(weight)/(float(height)*float(height))
badweight=0

if 18.5<=imt<=37.5:
	imt=imt
else:
	badweight=badweight+1

print("\t\t\tСейчас будет психологический тест, на который нужно отвечать + или - ")

psychologytest=0
psychogood=0
psychonormal=0
psychobad=0
psychodurka=0

pstest=[1,2,3,4,5,6,7,8,9,10]

while True:
	suicide=input("Были ли мысли о суициде? ")
	if suicide=='+' or suicide=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if suicide=='+'
		pstest[0]=suicide
	else:
		pstest=pstest

while True:
	loneliness=input("Думали ли вы о том, что вы ненужны? ")
	if loneliness=='+' or loneliness=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if loneliness=='+'
		pstest[1]=loneliness
	else:
		pstest=pstest


while True:
	helpfull=input("Любите ли вы помагать людям? ")
	if helpfull =='+' or helpfull=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if helpfull=='-'
		pstest[2]='+'
	else:
		pstest=pstest


while True:
	phobia=input("Есть ли у вас фобия? ")
	if phobia=='+' or phobia=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if phobia=='+'
		pstest[3]=phobia
	else:
		pstest=pstest

while True:
	insomnia=input("Страдаете ли вы от бессонницы? ")
	if insomnia=='+' or insomnia=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if insomnia=='+'
		pstest[4]=insomnia
	else:
		pstest=pstest

while True:
	seizure=input("Был ли у вас приступ? ")
	if seizure=='+' or seizure=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if seizure=='+'
		pstest[5]=seizure
	else:
		pstest=pstest

while True:
	work=input("Любите ли вы работать? ")
	if work=='+' or work=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if work=='-'
		pstest[6]='+'
	else:
		pstest=pstest	

while True:
	addictionbuhlo=input("Есть ли у вас зависимость от спиртных напитков? ")
	if addictionbuhlo=='+' or addictionbuhlo=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if addictionbuhlo=='+'
		pstest[7]=addictionbuhlo
	else:
		pstest=pstest

while True:
	addictiondrugs=input("Есть ли у вас зависимость от наркотиков? ")
	if addictiondrugs=='+' or addictiondrugs=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if suicide=='+'
		addictiondrugs[8]=addictiondrugs
	else:
		pstest=pstest

while True:
	badhabits=input("Есть ли у вас вредные привычки? ")
	if badhabits=='+' or badhabits=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(pstest)):
	if badhabits=='+'
		pstest[9]=badhabits
	else:
		pstest=pstest

psychologytest=pstest.count('+')

if 1<=psychologytest<=4:
	psychonormal=psychonormal+1
	print("У тебя есть некоторые проблемы, но ты всё ещё можешь служить родине))")
	print("Сейчас будут вопросы про ваше здоровье")	
elif 5<=psychologytest<=7:
	psychobad=psychobad+1
	print("Сейчас будут вопросы про ваше здоровье")	
elif 8<=psychologytest<=10:
	psychodurka+psychodurka+1
	print("Тебе стоит сходить к психологу и лучше лечь в дурку..")
	print("Сейчас будут вопросы про ваше здоровье")
else:
	psychogood=psychogood+1
	print("С головой у вас всё хорошо, но что насчёт заболеваний?")

bolezni=[1,2,3,4,5,6,7,8,9,10,11,12]

print("Тут также нужно отвечать либо +, либо -")

while True:
	canser=input("Есть ли у вас раковые заболевания? ")
	if canser=='+' or canser=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if canser=='+'
		bolezni[0]=bolezni
	else:
		bolezni=bolezni

while True:
	hiv=input("Есть ли у вас вич инфекция? ")
	if hiv=='+' or hiv=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if hiv=='+'
		bolezni[1]=hiv
	else:
		bolezni=bolezni

while True:
	tuberculosis=input("Есть ли у вас туберкулез? ")
	if tuberculosis=='+' or tuberculosis=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if canser=='+'
		bolezni[2]=canser
	else:
		bolezni=bolezni

while True:
	sifilis=input("Есть ли у вас сифилис? ")
	if sifilis=='+' or sifilis=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if sifilis=='+'
		bolezni[3]=sifilis
	else:
		bolezni=bolezni

while True:
	blood=input("Есть ли у вас заболевания крови? ")
	if blood=='+' or blood=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if blood=='+'
		bolezni[4]=blood
	else:
		bolezni=bolezni

while True:
	eyes=input("Есть ли у вас болезни глаз? ")
	if eyes=='+' or eyes=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if eyes=='+'
		bolezni[5]=eyes
	else:
		bolezni=bolezni

while True:
	gut=input("Есть ли у вас кишечные заболевания? ")
	if gut=='+' or gut=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if gut=='+'
		bolezni[6]=gut
	else:
		bolezni=bolezni

while True:
	daun=input("Есть ли у вас синдром Дауна? ")
	if daun=='+' or daun=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if daun=='+'
		bolezni[7]=daun
	else:
		bolezni=bolezni

while True:
	autist=input("Есть ли у вас аутизм? ")
	if autist=='+' or autist=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if autist=='+'
		bolezni[8]=autist
	else:
		bolezni=bolezni

while True:
	turetta=input("Есть ли у вас синдром Туретта? ")
	if turetta=='+' or turetta=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if turetta=='+'
		bolezni[9]=turetta
	else:
		bolezni=bolezni

while True:
	gormoni=input("Есть ли у вас проблемы с гармонами? ")
	if gormoni=='+' or gormoni=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if gormoni=='+'
		bolezni[10]=gormoni
	else:
		bolezni=bolezni

while True:
	rech=input("Есть ли у вас проблемы с речью? ")
	if rech=='+' or rech=='-':
		break
	else:
		print("Вы ввели не то")

for i in range (len(bolezni)):
	if rech=='+'
		bolezni[11]=rech
	else:
		bolezni=bolezni

print(" ")
print(" ")
print("\n\t\t\tУчётная карта призывника")

print("\tОбщие сведения")

print("Фамилия: ",surname)
print("Собственное имя: ",name)
print("Отчество: ",dadsname)
print("Возраст: ",age)
print("Рост: ",height)
print("Вес: ",weight)
print("Индекс массы тела: ",imt)
print("Место образования: ",education)
print("Город проживания: ",city)
print("Семейное положение: ",famstatus)
print("Наличие судимости: ",judicial)

print("\tНаличие заболеваний: ")

boleznires=0

boleznires=bolezni.count('+')

if boleznires > 0:
	print("Имеются серьёзные заболевания")
else:
	print("Серьёзных заболеваний нет")

if psychogood==1:
	print("Здоров")
elif psychonormal==1:
	print("Здоров")
elif psychobad==1:
	print("Болен")
else:
	print("Болен")

print("\nРезультат: ")

if (psychobad==1 or psychodurka==1 or boleznires>=1 or badweight==1):
	print("НЕ ГОДЕН")
else:
	print("ГОДЕН")
