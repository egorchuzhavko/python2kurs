# На поле (k, l) стоит ферзь, на поле (m, n) – пешка. 
while True:
	n=int(input("Введите размерность поля (не больше 8): "))
	if 1<=n<=8:
		break
while True:
	xferz=int(input("введите x ферзя: "))
	if 1<=xferz<=n:
		break
while True:
	yferz=int(input("введите y ферзя: "))
	if 1<=yferz<=n:
		break
while True:
	xpewka=int(input("введите x пешки: "))
	if 1<=xpewka <=n:
		break
while True:
	ypewka=int(input("введите y пешки: "))
	if 1<=ypewka<=n:
		break
biet=True
nebiet=False
print("бьет ли одна фигура другую?")
if(ypewka==yferz) or (xpewka==xferz) or (xferz+yferz==xpewka+ypewka) or (xferz-yferz==xpewka-ypewka):
	print(biet)
else:
	print(nebiet)
print("возможен ли ход какой-либо фигуры, после которого одна из фигур бьет другую?")
if (xpewka+1==xferz) or (xpewka+2==xferz):
	print(biet)
else:
	print(nebiet)