n=int(input("Введите N: "))
m=int(input("Введите M: "))
mas=[]
for i in range(n):
	mas.append([])
	for j in range(m):
		row=input("Введите число: ")
		mas[i].append(row)
print(mas)
proizvedenie=1
naimj=0
naimi=0
naim=mas[0][0]
for i in range(n):
	for j in range(m):
		if mas[i][j]<naim:
			naimj=j
			naimi=i
print("Индекс наименьшего элемента массива: i=",naimi," j=",naimj)
for i in range(m):
	proizvedenie=proizvedenie*int(mas[i][naimj])
print("Произведение= ", proizvedenie)
#istrue=False
# for i in range(n-1):
# 	for j in range(m):
# 		if(int(mas[i][j])>=int(mas[i+1][j])):
# 			istrue=True
# 		else:
# 			istrue=False
# 	if (istrue==True):
# 		for j in range (n):
# 			print(mas[i][j],end="")


# tempmas=mas
# for i in range(n):
# 	tempmas[i].sort(reverse = True)
# 	if(mas[i]==tempmas[i]):
# 		print(mas)
# 		break


