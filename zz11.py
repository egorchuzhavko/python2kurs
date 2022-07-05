#x1>x2<=x3<x4>=x5>x6

x1=int(input("x1: "))
x2=int(input("x2: "))
x3=int(input("x3: "))
x4=int(input("x4: "))
x5=int(input("x5: "))
x6=int(input("x6: "))

# if x1<x2:
# 	x1,x2=x2,x1
# if x1==x2:
# 	x1,x3=x3,x1
# if x2>=x3:
# 	x2,x3=x3,x2
# if x3>x4:
# 	x3,x4=x4,x3
# if x3==x4:
# 	x3,x5=x5,x3
# if x4<=x5:
# 	x4,x5=x5,x4
# if x5<x6:
# 	x5,x6=x6,x5
# if x4<=x5:
# 	x4,x5=x5,x4
for i in range(0,777):
	if x1<x2:
		x1,x2=x2,x1
	if x1==x2:
		x1,x3=x3,x1
	if x2>=x3:
		x2,x3=x3,x2
	if x3>x4:
		x3,x4=x4,x3
	if x3==x4:
		x3,x5=x5,x3
	if x4<=x5:
		x4,x5=x5,x4
	if x5<x6:
		x5,x6=x6,x5
	if x4<=x5:
		x4,x5=x5,x4
	if x5==x6:
		x5,x6,x2,x3=x2,x3,x5,x6
	if x4==x1:
		x5,x1=x1,x5
print(x1,'>',x2, '<=',x3, '<',x4, '>=',x5, '>',x6)