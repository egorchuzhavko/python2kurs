# n=int(input())
# k=1
# summa=0
# number=1
# # while k!=n:
# # 	if (number<10):
# # 		if(isinstance(number%1,int)==True):
# # 			summa+=number
# # 			k=k+1
# # 	if (number<100):
# # 		ch1=number%10
# # 		ch2=number//10
# # 		if(isinstance(number%(ch1+ch2),int)==True):
# # 			summa+=number
# # 			k=k+1
# # 	if (number<1000):
# # 		ch1=number%10
# # 		ch2=(number//10)%10
# # 		ch3=number//100
# # 		if(isinstance(number%(ch1+ch2+ch3),int)==True):
# # 			summa+=number
# # 			k+=1
# # 	if (number<10000):
# # 		ch1=number%10
# # 		ch2=number%100//10
# # 		ch3=number%1000//100
# # 		ch4=number//1000
# # 		if(isinstance(number%(ch1+ch2+ch3+ch4),int)==True):
# # 			summa+=number
# # 			k+=1
# # 	number+=1
# # print(summa)


# while k!=n:
# 	if(number<10):
# 		if isinstance(number%number,int)==True:
# 			summa+=number
# 			k+=1
# 	if(number >10 and number<100):
# 		ch1=number%10
# 		ch2=number//10
# 		if isinstance(number%(ch1+ch2),int) == True:
# 			summa+=number
# 			k+=1
# 	if(number >= 100 and number<1000):
# 		ch1=number%10
# 		ch2=number//10%10
# 		ch3=number//100
# 		if isinstance(number%(ch1+ch2+ch3),int) == True:
# 			summa+=number
# 			k+=1
# 	number+=1
# print(summa)
def summa(x):
	suma=0
	while x>0:
		suma+=x%10
		x//10
	return suma


n=int(input())
suma=0
k=1
c=1
while k<=n:
	while True:
		if(c%summa(c)==0):
			break
		else:
			c+=1
	k+=1
	suma+=c
	c+=1
print(suma)