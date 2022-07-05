import sqlite3

try:
	db=sqlite3.connect('DataBaseTgBot.db')
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

# sql.execute(f"SELECT * FROM DataBaseTgBot")
# aalanguage=sql.fetchall()

sql.execute(f"SELECT login FROM DataBaseTgBot WHERE adminstatus = ?",(1,))
aalanguage=sql.fetchall()
print(aalanguage)
for row in aalanguage:
	print ("ID: ", row[0])
	#print("IsAdmin: ", row[1])
	print("\n\n")



for row in aalanguage:
	if row[0] == str(893846755):
		print(1)