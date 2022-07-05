def russian():
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
		height=input("Введите свой рост(м): ")
		if height.replace(".","",1).isdigit():
			break
		if not height.replace(".","",1).isdigit():
			print("Вы ввели не то")

	while True:
		weight=input("Введите свой вес(кг): ")
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


print("")

def spanish ():
	print("\nAhora está pasando la prueba de aptitud para el Servicio")
	print("En muchas preguntas, debe responder sí/no, verifique si hay un registro, tenga cuidado")

	surname=input("Su apellido: ")
	name=input("Su nombre: ")
	dadsname=input("Su patronímico: ")

	while True:
		age=input("Introduzca su edad: ")
		if not age.isdigit():
			print("Has introducido lo incorrecto.Has introducido lo incorrecto.")
		else:
			break

	city=input("Ciudad en la que vives: ")
	famstatus=input("Su estado civil: ")
	judicial=input("Antecedentes penales: ")
	education=input("Lugar de estudio (si no, escriba no): ")

	if (education == 'no' or education == 'No' or education =='nO' or education == 'NO'):
		education = "no estoy aprendiendo"
	else:
		education=education
		
	while True:
		height=input("Ingrese su altura (en metros): ")
		if height.replace(".","",1).isdigit():
			break
		if not height.replace(".","",1).isdigit():
			print("Has introducido lo incorrecto.Has introducido lo incorrecto.")

	while True:
		weight=input("Ingrese su peso (en kilogramos): ")
		if weight.replace(".","",1).isdigit():
			break
		if not weight.replace(".","",1).isdigit():
			print("Has introducido lo incorrecto.Has introducido lo incorrecto.")

	imt=float(weight)/(float(height)*float(height))
	badweight=0

	if 18.5<=imt<=37.5:
		imt=imt
	else:
		badweight=badweight+1

	information=[name, surname, dadsname, age, city, famstatus, judicial, education, height, weight, imt]

	print("\n\tAhora habrá una prueba psicológica para responder + o - \n")

	test=[1,2,3,4,5,6,7,8,9,10]
	questionnumber=0
	nomer=-1
	def fortest1(test,nomer,questionnumber):
		for i in range (len(test)):
			test[nomer]=questionnumber

	while True:
		suicide=input("¿Hubo pensamientos suicidas? ")
		if suicide=='+' or suicide=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto.Has introducido lo incorrecto.")

	a1=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Has pensado en el hecho de que no te necesitan? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto.Has introducido lo incorrecto.")

	a2=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Te gusta ayudar a la gente? ")
		if questionnumber =='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto.Has introducido lo incorrecto.")

	a3=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes fobia? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto.Has introducido lo incorrecto.")

	a4=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Sufres de insomnio? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto.")

	a5=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Ha tenido un ataque? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto.")

	a6=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Te gusta trabajar? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto.")

	a7=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes una adicción a los licores? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	a8=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes una adicción a los licores? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	a9=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes malos hábitos? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	a10=fortest1(test,nomer,questionnumber)

	psychologytest=0
	psychologytest=test.count('+')

	bolezni=[1,2,3,4,5,6,7,8,9,10,11,12]
	questionnumber=0
	nomer=-1
	def fortest2(bolezni,nomer,questionnumber):
		for i in range (len(bolezni)):
			bolezni[nomer]=questionnumber

	print("\n\tPreguntas sobre enfermedades graves\n")

	while True:
		questionnumber=input("¿Tienes cáncer? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b1=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tiene una infección por VIH? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b2=fortest2(bolezni,nomer,questionnumber)


	while True:
		questionnumber=input("¿Tienes tuberculosis? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b3=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes sífilis? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b4=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tiene alguna enfermedad de la sangre? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b5=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tiene alguna enfermedad ocular? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b6=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes enfermedades intestinales? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b7=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes enfermedades intestinales? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b8=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes autismo? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b9=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes el síndrome de Tourette? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b10=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes problemas hormonales? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b11=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("¿Tienes problemas para hablar? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("Has introducido lo incorrecto")

	b12=fortest2(bolezni,nomer,questionnumber)
	boleznires=0
	boleznires=bolezni.count('+')

	print(" ")
	print(" ")
	print("\n\t\t\tTarjeta de cuenta del recluta")
	print("\tGenerales")
	#information=[name, surname, dadsname, age, city, famstatus, judicial, education, height, weight, imt]
	print("Fio:",information[0],information[1], information[2])
	print("Edad: ",information[3])
	print("Crecimiento: ",information[8])
	print("Peso: ",information[9])
	print("Índice de masa corporal: ",information[10])
	print("Lugar de educación: ",information[7])
	print("Ciudad de residencia: ",information[4])
	print("Семейное положение: ",information[5])
	print("Estado civil: ",information[6])

	print("\tLa presencia de enfermedades graves: ")

	if boleznires > 0:
		print("Hay enfermedades graves")
	else:
		print("No hay enfermedades graves")

	print("\tEstado psicológico: ")

	if psychologytest>=6:
		print("Enfermo")
	else:
		print("Sano")

	print("\nResultado: ")

	if (psychologytest>=6 or boleznires>=1 or badweight==1):
		print("INSERVIBLE")
	else:
		print("APTO")

def english():
	print("\nyou are currently undergoing a fitness test")
	print("In many questions, you need to answer Yes/no, check the presence of the register, be careful")

	surname=input("Your Surname: ")
	name=input("Your Name: ")
	dadsname=input("Your middle name: ")

	while True:
		age=input("Introduzca su edad: ")
		if not age.isdigit():
			print("You entered the wrong information")
		else:
			break

	city=input("City where you live: ")
	famstatus=input("Your marital status: ")
	judicial=input("Criminal record: ")
	education=input("Place of study (if not, write no): ")

	if (education == 'no' or education == 'No' or education =='nO' or education == 'NO'):
		education = "don't study"
	else:
		education=education
		
	while True:
		height=input("Enter your height (in meters): ")
		if height.replace(".","",1).isdigit():
			break
		if not height.replace(".","",1).isdigit():
			print("You entered the wrong information")

	while True:
		weight=input("Enter your weight (in kilograms): ")
		if weight.replace(".","",1).isdigit():
			break
		if not weight.replace(".","",1).isdigit():
			print("You entered the wrong information")

	imt=float(weight)/(float(height)*float(height))
	badweight=0

	if 18.5<=imt<=37.5:
		imt=imt
	else:
		badweight=badweight+1

	information=[name, surname, dadsname, age, city, famstatus, judicial, education, height, weight, imt]

	print("\n\nNow there will be a psychological test that you need to answer + or - \n")

	test=[1,2,3,4,5,6,7,8,9,10]
	questionnumber=0
	nomer=-1
	def fortest1(test,nomer,questionnumber):
		for i in range (len(test)):
			test[nomer]=questionnumber

	while True:
		suicide=input("Have you ever thought about suicide?")
		if suicide=='+' or suicide=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a1=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Have you thought about the fact that you are not needed? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a2=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Don't you like helping people? ")
		if questionnumber =='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a3=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have a phobia? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a4=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Do you suffer from insomnia? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a5=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Did you have a seizure? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a6=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Don't you like working? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a7=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have an addiction to alcohol? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a8=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have a drug addiction? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a9=fortest1(test,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have any bad habits? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	a10=fortest1(test,nomer,questionnumber)

	psychologytest=0
	psychologytest=test.count('+')

	bolezni=[1,2,3,4,5,6,7,8,9,10,11,12]
	questionnumber=0
	nomer=-1
	def fortest2(bolezni,nomer,questionnumber):
		for i in range (len(bolezni)):
			bolezni[nomer]=questionnumber

	print("\n\tQuestions about serious illnesses\n")

	while True:
		questionnumber=input("Do you have cancer? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b1=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have HIV infection? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b2=fortest2(bolezni,nomer,questionnumber)


	while True:
		questionnumber=input("Do you have tuberculosis? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b3=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have syphilis? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b4=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have a blood disorder? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b5=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have eye diseases? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b6=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have intestinal diseases? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b7=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have down syndrome? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b8=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have autism? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b9=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have Tourette's syndrome? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b10=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have problems with hormones? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b11=fortest2(bolezni,nomer,questionnumber)

	while True:
		questionnumber=input("Do you have speech problems? ")
		if questionnumber=='+' or questionnumber=='-':
			nomer=nomer+1
			break
		else:
			print("You entered the wrong information")

	b12=fortest2(bolezni,nomer,questionnumber)
	boleznires=0
	boleznires=bolezni.count('+')

	print(" ")
	print(" ")
	print("\n\t\t\tRegistration card of the recruit")
	print("\tGeneral information")
	#information=[name, surname, dadsname, age, city, famstatus, judicial, education, height, weight, imt]
	print("FCS:",information[0],information[1], information[2])
	print("Age: ",information[3])
	print("Height: ",information[8])
	print("Weight: ",information[9])
	print("Body mass index: ",information[10])
	print("Place of education: ",information[7])
	print("City of residence: ",information[4])
	print("Marital status: ",information[5])
	print("Criminal record: ",information[6])

	print("\tPresence of serious diseases: ")

	if boleznires > 0:
		print("There are serious diseases")
	else:
		print("There are no serious diseases")

	print("\tPsychological state: ")

	if psychologytest>=6:
		print("Ill")
	else:
		print("Healthy")

	print("\nРезультат: ")

	if (psychologytest>=6 or boleznires>=1 or badweight==1):
		print("fit")
	else:
		print("unfit")

print("Hello!\nBefore you take the test, you must choose which language you will take it in:\n1)English\n2)Русский\n3)Spanish\n")
while True:
	language=input()
	if language=='1':
		l=english()
		break
	elif language=='2':
		l=russian()
		break
	elif language=='3':
		l=spanish()
		break
	else:
		print("wrong, try again")