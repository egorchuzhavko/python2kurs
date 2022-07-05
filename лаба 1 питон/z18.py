# Вывести слова, начинающиеся с букв 'pr'.

predlojenie=input("Введите предложение: ")
for i in predlojenie.split():
	if i.startswith("pr"):
		print(i)