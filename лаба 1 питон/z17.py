# 8.	Определить число вхождений в строку подстроки 'abс'. Вывести символы строки, не являющиеся буквами или цифрами.

stroka1=str(input("Введите символы и строки: "))
strokacount=stroka1.count('abc')
stroka2=''
for i in stroka1:
	if i not in ('0','1','2','3','4','5','6','7','8','9','B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z','A', 'E', 'I', 'O', 'U','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я'):
		stroka2+=i
print(strokacount,"- число вхождений подстроки'abc'")
print(stroka2)