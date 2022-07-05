def imt_calculator(growth, weight, dis_rez):
	IMT=float(weight)/(float(growth)*float(growth))
	print("Индекс массы тела: " + str(IMT))
	
	if float(IMT) <= 18.5:
		dis_rez=dis_rez+1
		print("Дефицит массы тела")
	elif float(IMT) >=35:
		dis_rez=dis_rez+1
		print("Избыток мыссы тела")
	else:
		print("Вам очень повезло! Продолжаем")

def function(text):
	disease=input(text)
	if disease == "да" or disease == "Да" or disease == "ДА" or disease == "дА":
		if disease == "да":
			return True
def male():
	print ("Добро пожаловать, пожалуйста пройдите тест на годность к военной службе")
	dis_rez=0
	print("Мужитский")
	while True:
		while True:
			surname=input("Введите фамилию: ")
			if surname.isalpha():
				break
			if not surname.isalpha():
				print("Пожалуйста, введите вашу фамилию")
		while True:
			name=input("Введите имя: ")
			if name.isalpha():
				break
			if not name.isalpha():
				print("Пожалуйста, введите ваше имя")
		while True:
			patronymic=input("Введите отчество: ")
			if patronymic.isalpha():
				break
			if not patronymic.isalpha():
				print("Пожалуйста, введите ваше отчество")
		pr = [surname,name,patronymic]
		for cs in pr:
			print(cs,end=' ')
		print("")
		ask=input("Введены правильные данные: ")
		if ask == "да" or ask == "Да" or ask == "ДА" or ask == "дА":
			break
		else:
			print("Пожалуйста, повторите ввод данных")
	print(" ")
	while True:
		age=input("Введите свой возраст: ")
		if age.isdigit():
			if int(age) > 27:
				print ("Ты уже стар...")
				break
			elif int(age) >= 18:
				print ("Поздравляю! Ты нам подходишь")
				break
			else:
				print("Ты еще слишком мал...")
				break
		if not age.isdigit():
			print("Пожалуйста, введите ваш возраст... ")

	while True:
		growth=input("Введите свой рост(м): ")
		if growth.replace(".","").isdigit():
			break
		if not growth.replace(".","").isdigit():
			print("Пожалуйста, введите ваш рост...")

	while True:
		weight=input("Введите свой вес(кг): ")
		if weight.replace(".","").isdigit():
			break
		if not weight.replace(".","").isdigit():
			print("Пожалуйста, введите ваш вес...")

	IMT1=imt_calculator(growth, weight,dis_rez)
	print(" ")
	conviction=input("Есть ли у вас судимость? ")
	if conviction == "да" or conviction == "Да" or conviction == "ДА" or conviction == "дА":
		print("Вы должны исполнить требования суда для её погашения")
	else:
		print("Вы законопослушный гражданин, так держать! Продолжаем дальше")

	city=input("В каком городе вы проживаете? ")

	education=input("Ты сейчас учишься в ВУЗе(колледже)? ")
	if education == "да" or education == "Да" or education == "ДА" or education == "дА":
		print("Вы сможете получить отсрочку по причине получение образования")
	else:
		print("Вы не получите отсрочку")

	wife=input("У вас есть супруга? ")
	if wife == "да" or wife == "Да" or wife == "ДА" or wife == "дА":
		pregnant=input("Ваша супруга беременна? ")
		if pregnant == "да" or pregnant == "Да" or pregnant == "ДА" or pregnant == "дА":
			print("Вы сможете получить отсрочку по данному пункту")
		else:
			child=input("У вас есть дети? ")
			if child == "да" or child == "Да" or child == "ДА" or child == "дА":
				quantity=input("Сколько у вас детей? ")
				if quantity == "":
					print("Вы ввели пустоту, введите число ...")
					exit(0)
				else:
					if int(quantity) >= 2:
						print("Вы сможете получить отсрочку по данному пункту")
					else:
						print("Вы не сможете получить отсрочку по данному пункту")
						child_age=input("У вас есть ребенок, возраст которого - не более 3 лет? ")
						if child_age == "да" or child_age == "Да" or child_age == "ДА" or child_age == "дА":
							print("Вы сможете получить отсрочку по данному пункту")
						else:
							print("Вы не сможете получить отсрочку по данному пункту")
			else:
				print("Вы не сможете получить отсрочку по данному пункту")
	else: 
		print("Вы не сможете получить отсрочку по данному пункту")
		child1=input("У вас есть дети? ")
		if child1 == "да" or child1 == "Да" or child1 == "ДА" or child1 == "дА":
			quantity1=input("Сколько у вас детей? ")
			if quantity1 == "":
				print("Вы ввели пустоту, введите число ...")
				exit(0)
			else:

				if int(quantity1) >= 2:
					print("Вы сможете получить отсрочку по данному пункту")
				else:
					print("Вы не сможете получить отсрочку по данному пункту")
					child_age1=input("У вас есть ребенок, возраст которого - не более 3 лет? ")
					if child_age1 == "да" or child_age1 == "Да" or child_age1 == "ДА" or child_age1 == "дА":
						print("Вы сможете получить отсрочку по данному пункту")
					else:
						print("Вы не сможете получить отсрочку по данному пункту")
		else:
			print("Вы не сможете получить отсрочку по данному пункту")
	print(" ")
	print ("Сейчас будет часть теста, в которой нам нужно узнать о вашем здоровье")
	print ("Это один из самых распространенных вариантов получения отсрочки, поскольку в законодательно")
	print ("утвержденном Расписании болезней содержится более 2000 диагнозов")
	print(" ")
	test=input("Вы хотите продолжить тест? ")
	if (test == 'нет' or test == 'Нет' or test =='нЕт' or test == 'неТ' or test == 'НеТ' or test == 'НЕт' or test == 'нЕТ' or test == 'НЕТ'):
		print("Спасибо, что уделили свое время")
		exit(0)
	else:
		test=test
		print("Продолжаем!")

	disease1=function("У вас есть Туберкулез органов дыхания? ")
	if disease1 == True:
		dis_rez=dis_rez+1
	disease2=function("У вас есть Туберкулез других органов и систем? ")
	if disease2 == True:
		dis_rez=dis_rez+1
	disease3=function("У вас есть Лепра? ")
	if disease3 == True:
		dis_rez=dis_rez+1
	disease4=function("У вас есть Болезнь, вызываемая вирусом иммунодефицита человека? ")
	if disease4 == True:
		dis_rez=dis_rez+1
	disease5=function("У вас есть Сифилис и другие инфекции, передающиеся преимущественно половым путем? ")
	if disease5 == True:
		dis_rez=dis_rez+1
	disease6=function("У вас есть Микозы? ")
	if disease6 == True:
		dis_rez=dis_rez+1
	disease7=function("У вас есть Злокачественные новообразования (кроме опухолей нервной системы, лимфоидной, кроветворной и родственных им тканей)? ")
	if disease7 == True:
		dis_rez=dis_rez+1
	disease8=function("У вас есть Доброкачественные новообразования (кроме опухолей нервной системы)? ")
	if disease8 == True:
		dis_rez=dis_rez+1
	disease9=function("У вас есть Болезни крови и кроветворных органов, иммунодефицитные состояния? ")
	if disease9 == True:
		dis_rez=dis_rez+1
	disease10=function("У вас есть Зоб без нарушения функций щитовидной железы? ")
	if disease10 == True:
		dis_rez=dis_rez+1
	disease11=function("У вас есть Аффективные расстройства (настроения)? ")
	if disease11 == True:
		dis_rez=dis_rez+1
	disease12=function("У вас есть Психические и поведенческие расстройства вследствие принятия психоактивных веществ? ")
	if disease12 == True:
		dis_rez=dis_rez+1
	disease13=function("У вас есть Психические расстройства эндогенной этиологии? ")
	if disease13 == True:
		dis_rez=dis_rez+1
	disease14=function("У вас есть Расстройства личности? ")
	if disease14 == True:
		dis_rez=dis_rez+1
	disease15=function("У вас есть Умственная отсталость? ")
	if disease15 == True:
		dis_rez=dis_rez+1
	disease16=function("У вас есть Недостаточное физическое развитие? ")
	if disease16 == True:
		dis_rez=dis_rez+1
	disease17=function("У вас есть Последствия травм, отравлений и других воздействий внешних факторов? ")
	if disease17 == True:
		dis_rez=dis_rez+1
	disease18=function("У вас есть Врожденные аномалии развития органов и систем? ")
	if disease18 == True:
		dis_rez=dis_rez+1
	disease19=function("У вас есть Хронические заболевания почек? ")
	if disease19 == True:
		dis_rez=dis_rez+1
	disease20=function("У вас есть Хронические воспалительные болезни женских половых органов? ")
	if disease20 == True:
		dis_rez=dis_rez+1
	disease21=function("У вас есть Расстройства овариально-менструальной функции? ")
	if disease21 == True:
		dis_rez=dis_rez+1
	disease22=function("У вас есть Отсутствие конечностей? ")
	if disease22 == True:
		dis_rez=dis_rez+1
	disease23=function("У вас есть Плоскостопие и другие деформации стопы? ")
	if disease23 == True:
		dis_rez=dis_rez+1
	disease24=function("У вас есть Хирургические болезни и поражения крупных суставов, хрящей, остеопатии, хондропатии? ")
	if disease24 == True:
		dis_rez=dis_rez+1
	disease25=function("У вас есть Отсутствие, деформации, дефекты кисти и пальцев? ")
	if disease25 == True:
		dis_rez=dis_rez+1
	disease26=function("У вас есть Болезни кожи и подкожной клетчатки? ")
	if disease26 == True:
		dis_rez=dis_rez+1
	disease27=function("У вас есть Нарушение развития и прорезывания зубов? ")
	if disease27 == True:
		dis_rez=dis_rez+1
	disease28=function("У вас есть Болезни пищевода, желудка, двенадцатиперстной кишки? ")
	if disease28 == True:
		dis_rez=dis_rez+1
	disease29=function("У вас есть Болезни печени, желчевыводящих путей, поджелудочной железы? ")
	if disease29 == True:
		dis_rez=dis_rez+1
	disease30=function("У вас есть Бронхиальная астма? ")
	if disease30 == True:
		dis_rez=dis_rez+1
	disease31=function("У вас есть Другие болезни органов дыхания? ")
	if disease31 == True:
		dis_rez=dis_rez+1
	disease32=function("У вас есть Болезни системы кровообращения? ")
	if disease32 == True:
		dis_rez=dis_rez+1
	disease33=function("У вас есть Болезни уха и сосцевидного отростка? ")
	if disease33 == True:
		dis_rez=dis_rez+1
	disease34=function("У вас есть Болезни глаза и придаточного аппарата? ")
	if disease34 == True:
		dis_rez=dis_rez+1
	disease35=function("У вас есть Болезни нервной системы? ")
	if disease35 == True:
		dis_rez=dis_rez+1
	print(" ")
	print ("Спасибо, что уделили свое время")
	print(" ")
	print(" ")
	if dis_rez > 0:
		print("Вы не годны")
	else:
		print("Вы годны")
	print(" ")
	print(" ")
	test1=input("Вы хотите оценить тест? ")
	if test1 == "да" or test1 == "Да" or test1 == "ДА" or test1 == "дА":
		print("Огромное спасибо!")
	else:
		print("Очень жаль, до скорой встречи в армии, Солдат!!!")
		exit(0)

	while True:
		test2=input("Оцените тест(1-5): ")
		if test2.isdigit():
			if int(test2) == 1 or int(test2) == 2:
				print("Конечно спасибо, но можно было поставить повыше")
				break
			elif int(test2) == 3 or int(test2) == 4:
				print("Спасибо за ваш отзыв, буду стараться улучшать тест")
				break
			elif int(test2) > 5:
				print("Конечно спасибо, но максимальная оценка - 5")
				break
			else:
				print("Огромное спасибо за максимальную оценку, вам обеспечен военный билет ")
				break
		if not test2.isdigit():
			print("Пожалуйста, оцените тест")

def female():
	test120=input("Девушкам необязательно проходить военную службу, хотите ли вы пройти тест?")
	if test120 == "да" or test120 == "Да" or test120 == "ДА" or test120 == "дА":
		print ("Добро пожаловать, пожалуйста пройдите тест на годность к военной службе")
		dis_rez=0
		while True:
			while True:
				surname=input("Введите фамилию: ")
				if surname.isalpha():
					break
				if not surname.isalpha():
					print("Пожалуйста, введите вашу фамилию")
			while True:
				name=input("Введите имя: ")
				if name.isalpha():
					break
				if not name.isalpha():
					print("Пожалуйста, введите ваше имя")
			while True:
				patronymic=input("Введите отчество: ")
				if patronymic.isalpha():
					break
				if not patronymic.isalpha():
					print("Пожалуйста, введите ваше отчество")
			pr = [surname,name,patronymic]
			for cs in pr:
				print(cs,end=' ')
			print("")
			ask=input("Введены правильные данные: ")
			if ask == "да" or ask == "Да" or ask == "ДА" or ask == "дА":
				break
			else:
				print("Пожалуйста, повторите ввод данных")
		print(" ")
		while True:
			age=input("Введите свой возраст: ")
			if age.isdigit():
				if int(age) > 27:
					print ("Ты уже старa...")
					break
				elif int(age) >= 18:
					print ("Поздравляю! Ты нам подходишь")
					break
				else:
					print("Ты еще слишком малa...")
					break
			if not age.isdigit():
				print("Пожалуйста, введите ваш возраст... ")

		while True:
			growth=input("Введите свой рост(м): ")
			if growth.replace(".","").isdigit():
				break
			if not growth.replace(".","").isdigit():
				print("Пожалуйста, введите ваш рост...")

		while True:
			weight=input("Введите свой вес(кг): ")
			if weight.replace(".","").isdigit():
				break
			if not weight.replace(".","").isdigit():
				print("Пожалуйста, введите ваш вес...")

		conviction=input("Есть ли у вас судимость? ")
		if conviction == "да" or conviction == "Да" or conviction == "ДА" or conviction == "дА":
			print("Вы должны исполнить требования суда для её погашения")
		else:
			print("Вы законопослушный гражданин, так держать! Продолжаем дальше")

		city=input("В каком городе вы проживаете? ")

		education=input("Ты сейчас учишься в ВУЗе(колледже)? ")
		if education == "да" or education == "Да" or education == "ДА" or education == "дА":
			print("Вы сможете получить отсрочку по причине получение образования")
		else:
			print("Вы не получите отсрочку")

		husband=input("У вас есть муж? ")
		if husband == "да" or husband == "Да" or husband == "ДА" or husband == "дА":
			child=input("У вас есть дети? ")
			if child == "да" or child == "Да" or child == "ДА" or child == "дА":
				print("Вы сможете получить отсрочку по данному пункту")
			else:
				print("Вы не сможете получить отсрочку по данному пункту")
		else: 
			print("Вы не сможете получить отсрочку по данному пункту")
			child1=input("У вас есть дети? ")
			if child1 == "да" or child1 == "Да" or child1 == "ДА" or child1 == "дА":
				print("Вы сможете получить отсрочку по данному пункту")
			else:
				print("Вы не сможете получить отсрочку по данному пункту")
		print(" ")
		print ("Сейчас будет часть теста, в которой нам нужно узнать о вашем здоровье")
		print ("Это один из самых распространенных вариантов получения отсрочки, поскольку в законодательно")
		print ("утвержденном Расписании болезней содержится более 2000 диагнозов")
		print(" ")
		test=input("Вы хотите продолжить тест? ")
		if (test == 'нет' or test == 'Нет' or test =='нЕт' or test == 'неТ' or test == 'НеТ' or test == 'НЕт' or test == 'нЕТ' or test == 'НЕТ'):
			print("Спасибо, что уделили свое время")
			exit(0)
		else:
			test=test
			print("Продолжаем!")

		disease1=function("У вас есть Туберкулез органов дыхания? ")
		if disease1 == True:
			dis_rez=dis_rez+1
		disease2=function("У вас есть Туберкулез других органов и систем? ")
		if disease2 == True:
			dis_rez=dis_rez+1
		disease3=function("У вас есть Лепра? ")
		if disease3 == True:
			dis_rez=dis_rez+1
		disease4=function("У вас есть Болезнь, вызываемая вирусом иммунодефицита человека? ")
		if disease4 == True:
			dis_rez=dis_rez+1
		disease5=function("У вас есть Сифилис и другие инфекции, передающиеся преимущественно половым путем? ")
		if disease5 == True:
			dis_rez=dis_rez+1
		disease6=function("У вас есть Микозы? ")
		if disease6 == True:
			dis_rez=dis_rez+1
		disease7=function("У вас есть Злокачественные новообразования (кроме опухолей нервной системы, лимфоидной, кроветворной и родственных им тканей)? ")
		if disease7 == True:
			dis_rez=dis_rez+1
		disease8=function("У вас есть Доброкачественные новообразования (кроме опухолей нервной системы)? ")
		if disease8 == True:
			dis_rez=dis_rez+1
		disease9=function("У вас есть Болезни крови и кроветворных органов, иммунодефицитные состояния? ")
		if disease9 == True:
			dis_rez=dis_rez+1
		disease10=function("У вас есть Зоб без нарушения функций щитовидной железы? ")
		if disease10 == True:
			dis_rez=dis_rez+1
		disease11=function("У вас есть Аффективные расстройства (настроения)? ")
		if disease11 == True:
			dis_rez=dis_rez+1
		disease12=function("У вас есть Психические и поведенческие расстройства вследствие принятия психоактивных веществ? ")
		if disease12 == True:
			dis_rez=dis_rez+1
		disease13=function("У вас есть Психические расстройства эндогенной этиологии? ")
		if disease13 == True:
			dis_rez=dis_rez+1
		disease14=function("У вас есть Расстройства личности? ")
		if disease14 == True:
			dis_rez=dis_rez+1
		disease15=function("У вас есть Умственная отсталость? ")
		if disease15 == True:
			dis_rez=dis_rez+1
		disease16=function("У вас есть Недостаточное физическое развитие? ")
		if disease16 == True:
			dis_rez=dis_rez+1
		disease17=function("У вас есть Последствия травм, отравлений и других воздействий внешних факторов? ")
		if disease17 == True:
			dis_rez=dis_rez+1
		disease18=function("У вас есть Врожденные аномалии развития органов и систем? ")
		if disease18 == True:
			dis_rez=dis_rez+1
		disease19=function("У вас есть Хронические заболевания почек? ")
		if disease19 == True:
			dis_rez=dis_rez+1
		disease20=function("У вас есть Хронические воспалительные болезни женских половых органов? ")
		if disease20 == True:
			dis_rez=dis_rez+1
		disease21=function("У вас есть Расстройства овариально-менструальной функции? ")
		if disease21 == True:
			dis_rez=dis_rez+1
		disease22=function("У вас есть Отсутствие конечностей? ")
		if disease22 == True:
			dis_rez=dis_rez+1
		disease23=function("У вас есть Плоскостопие и другие деформации стопы? ")
		if disease23 == True:
			dis_rez=dis_rez+1
		disease24=function("У вас есть Хирургические болезни и поражения крупных суставов, хрящей, остеопатии, хондропатии? ")
		if disease24 == True:
			dis_rez=dis_rez+1
		disease25=function("У вас есть Отсутствие, деформации, дефекты кисти и пальцев? ")
		if disease25 == True:
			dis_rez=dis_rez+1
		disease26=function("У вас есть Болезни кожи и подкожной клетчатки? ")
		if disease26 == True:
			dis_rez=dis_rez+1
		disease27=function("У вас есть Нарушение развития и прорезывания зубов? ")
		if disease27 == True:
			dis_rez=dis_rez+1
		disease28=function("У вас есть Болезни пищевода, желудка, двенадцатиперстной кишки? ")
		if disease28 == True:
			dis_rez=dis_rez+1
		disease29=function("У вас есть Болезни печени, желчевыводящих путей, поджелудочной железы? ")
		if disease29 == True:
			dis_rez=dis_rez+1
		disease30=function("У вас есть Бронхиальная астма? ")
		if disease30 == True:
			dis_rez=dis_rez+1
		disease31=function("У вас есть Другие болезни органов дыхания? ")
		if disease31 == True:
			dis_rez=dis_rez+1
		disease32=function("У вас есть Болезни системы кровообращения? ")
		if disease32 == True:
			dis_rez=dis_rez+1
		disease33=function("У вас есть Болезни уха и сосцевидного отростка? ")
		if disease33 == True:
			dis_rez=dis_rez+1
		disease34=function("У вас есть Болезни глаза и придаточного аппарата? ")
		if disease34 == True:
			dis_rez=dis_rez+1
		disease35=function("У вас есть Болезни нервной системы? ")
		if disease35 == True:
			dis_rez=dis_rez+1
		print(" ")
		print ("Спасибо, что уделили свое время")
		print(" ")
		print(" ")
		if dis_rez > 0:
			print("Вы не годны")
		else:
			print("Вы годны")
		print(" ")
		print(" ")
		test1=input("Вы хотите оценить тест? ")
		if test1 == "да" or test1 == "Да" or test1 == "ДА" or test1 == "дА":
			print("Огромное спасибо!")
		else:
			print("Очень жаль, до скорой встречи в армии, Солдат!!!")
			exit(0)

		while True:
			test2=input("Оцените тест(1-5): ")
			if test2.isdigit():
				if int(test2) == 1 or int(test2) == 2:
					print("Конечно спасибо, но можно было поставить повыше")
					break
				elif int(test2) == 3 or int(test2) == 4:
					print("Спасибо за ваш отзыв, буду стараться улучшать тест")
					break
				elif int(test2) > 5:
					print("Конечно спасибо, но максимальная оценка - 5")
					break
				else:
					print("Огромное спасибо за максимальную оценку, вам обеспечен военный билет ")
					break
			if not test2.isdigit():
				print("Пожалуйста, оцените тест")
	else:
		print("Всего хорошего !!!")

print("Пожалуйста, выберете свой пол:\n 1)Мужчина\n 2)Женщина")
print(" ")
while True:
	gender=input()
	if gender =='1':
		a=male()
		break
	elif gender =='2':
		a=female()
		break
	else:
		print("Ошибка, повторите снова")