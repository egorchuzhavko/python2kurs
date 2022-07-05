import telebot
import settings
import random
import sqlite3
import sys
from telebot import types
from translate import Translator

bot = telebot.TeleBot(settings.token)
translatorToEn = Translator(from_lang="ru", to_lang="en")
translatorToRu = Translator(from_lang="en", to_lang="ru")

try:
	db=sqlite3.connect('DataBaseTgBot.db',check_same_thread = False)
	sql=db.cursor()
	sql2=db.cursor()
	sql3=db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS DataBaseTgBot (
			login TEXT,
			adminstatus INT
		)""")

	db.commit()
	print("БД создана успешно.")
except Exception as er:
	wErorr("BD",er)
	print("Не удалось создать БД.")

@bot.message_handler(commands=['start'])
def begin(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("/help")
	item2=types.KeyboardButton("Орёл или решка")
	item3=types.KeyboardButton("кнб")
	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id,"Привет ☺ Я бот Айсу!\nПриятно с тобой познакомиться, {0.first_name}.\nПропиши /регистрация, чтобы быть крутым челом".format(message.from_user,bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def AnswerForMassage(message):
	if message.text.lower()=="привет":
		bot.send_message(message.from_user.id, "Привет ☺ Я бот Айсу. Напиши /help, чтобы узнать, что я могу 😎")

	elif message.text=="/help":
		bot.send_message(message.from_user.id, "1) Я могу предугадывать возможный исход ситуации, которую ты мне напишешь 😮\n </predict>[пробел]<Текст>\n2) У меня есть возможность зарегистрировать пользователя! 😎\n </регистрация>  \n3) Могу ещё переводить с русского на английский 😱\n</translatetoeng>[пробел]<Текст>\n4) А также с английского на русский 😱 \n </translatetoru>[пробел]<текст>\n5) Можно поиграть в \n<<камень, ножницы, бумага>>\n<кнб>")

	elif "/predict" in message.text:
		if '?' in message.text:
			bot.send_message(message.from_user.id, random.choice(settings.mas))
		else:
			bot.send_message(message.from_user.id,"Чел, ты..\nПиши с вопросом")

	elif message.text=="Орёл или решка":
		if random.randint(1,2)==1:
			photo = open('D:\\study\\питон\\TelegramBot\\pictures\\Орёл.png', 'rb')
			bot.send_photo(message.from_user.id,photo)
		else:
			photo=open('D:\\study\\питон\\TelegramBot\\pictures\\Решка.png', 'rb')
			bot.send_photo(message.from_user.id,photo)

	elif message.text=='/регистрация':
		sql.execute(f"SELECT login FROM DataBaseTgBot WHERE login='{message.from_user.id}'")
		if (sql.fetchone() is None):
			sql.execute("INSERT INTO DataBaseTgBot VALUES (?,?)",(message.from_user.id,0))
			db.commit()
			print("Зарегистрирован новый пользователь ", message.from_user.id, '\n\n')
			bot.send_message(message.from_user.id,"Вы успешно зарегистрировались!")
		else:
			print('Попытка регистрации существующего пользователя!\n\n')
			bot.send_message(message.from_user.id,"Вы уже Зарегистрированы!")

	elif message.text=='/АдминРега 777':
		sql.execute(f"SELECT login FROM DataBaseTgBot WHERE login='{message.from_user.id}'")
		if (sql.fetchone() is None):
			sql.execute("INSERT INTO DataBaseTgBot VALUES (?,?)",(message.from_user.id,1))
			db.commit()
			bot.send_message(message.from_user.id,"Вы зарегистрировались как Администратор!")
			print("Зарегистрирован новый Администратор: "<<message.from_user.id)
		else:
			sql.execute("UPDATE DataBaseTgBot SET adminstatus = 1 WHERE adminstatus = 0")
			db.commit()
			bot.send_message(message.from_user.id,"Вы вошли как Администратор!")
			print("Администратор вошёл в систему\n\n")

	elif message.text=='/ReggedUsers':
		sql.execute(f"SELECT login FROM DataBaseTgBot WHERE adminstatus = ?",(1,))
		aalanguage=sql.fetchall()
		flag=False
		for row in aalanguage:
			if row[0] == str(message.from_user.id):
				flag=True
		if flag==True:
			sql.execute(f"SELECT * FROM DataBaseTgBot")
			aalanguage=sql.fetchall()
			for row in aalanguage:
				bot.send_message(message.from_user.id,row[0])
		else:
			bot.send_message(message.from_user.id,"Вы не имеете прав администратора!")

	elif "/рассылка" in message.text:
		sql.execute(f"SELECT login FROM DataBaseTgBot WHERE adminstatus = ?",(1,))
		aalanguage=sql.fetchall()
		flag=False
		for row in aalanguage:
			if row[0] == str(message.from_user.id):
				flag=True
		if flag==True:
			temp=message.text.split()
			temp.pop(0)
			temp1=""
			for i in range(0,len(temp)):
				temp1=temp1+" "+temp[i]
			sql.execute(f"SELECT login FROM DataBaseTgBot")
			aa=sql.fetchall()
			for row in aa:
				bot.send_message(row[0],temp1)		
		else:
			bot.send_message(message.from_user.id,"Вы не имеете прав администратора!")

	elif message.text=='/оффбота':
		raise SystemExit

	elif message.text=="кнб":
		markup=types.InlineKeyboardMarkup(row_width=2)
		item1=types.InlineKeyboardButton("Камень",callback_data="Камень")
		item2=types.InlineKeyboardButton("Ножницы",callback_data="Ножницы")
		item3=types.InlineKeyboardButton("Бумага",callback_data="Бумага")
		markup.add(item1, item2, item3)

		bot.send_message(message.from_user.id,"Я загадал. Напиши что ты загадал, если не боишься проиграть 😎", reply_markup=markup)

	elif "/translatetoeng" in message.text:
		msg=message.text
		a=msg.split()
		a.pop(0)
		fortranslate=""

		for i in range(0,len(a)):
			fortranslate=fortranslate+" "+a[i]
		translated=translatorToEn.translate(fortranslate)
		bot.send_message(message.from_user.id, translated)

	elif "/translatetoru" in message.text:
		msg=message.text
		a=msg.split()
		a.pop(0)
		fortranslate=""

		for i in range(0,len(a)):
			fortranslate=fortranslate+" "+a[i]
		translated=translatorToRu.translate(fortranslate)
		bot.send_message(message.from_user.id, translated)

	else:
		bot.send_message(message.from_user.id, "Я не понял, что ты написал 😞\n Напиши </help>")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		q=random.choice(settings.knb)
		if call.message:
			if call.data == 'Ножницы' and q == 'Камень':
				bot.send_message(call.message.chat.id,"Опаа, победа за мной, у меня был Камень")
			elif call.data == 'Камень' and q== 'Ножницы':
				bot.send_message(call.message.chat.id, "Повезло повезло, у меня были ножницы..")
			elif call.data == 'Бумага' and q== 'Ножницы':
				bot.send_message(call.message.chat.id, "Иуууу, победа за мной, у меня были ножницы!")
			elif call.data == 'Ножницы' and q == 'Бумага':
				bot.send_message(call.message.chat.id, 'Блин, ты порезал мою бумагу >.<')
			elif call.data == 'Камень' and q == 'Бумага':
				bot.send_message(call.message.chat.id, 'Хехе, победа за мной, у меня была бумага')
			elif (call.data=='Камень' and q=='Камень') or (call.data=='Ножницы' and q=='Ножницы') or (call.data=='Бумага' and q=='Бумага'):
				bot.send_message(call.message.chat.id,'У нас ничья, хмм..')
			else:
				bot.send_message(call.message.chat.id, 'Ля ты жук, у меня был камень.. В этой битве победил ты')

			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="кнб", reply_markup=None)
	except Exception as e:
		print(repr(e))

bot.polling(none_stop=True)