mas=input().split()
summa=0
k=0
for i in range(0,len(mas)):
	summa+=int(mas[i])
	k+=1
sr=summa/k
for i in range(0,len(mas)):
	if(int(mas[i])<sr):
		print(mas[i],' ', end='')