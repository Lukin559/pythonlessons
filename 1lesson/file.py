age = 20 #int (Integer) целое число
name = "Ilya" #str (String) строка, любой набор символов в кавычках 
pi = 3.14 #float число с плавающей точкой 

print(age - 21)
print(age / 10)
print(age + 21)
print(age * pi)

var3 = name + " Lukin"
print(var3)

var1 = age + age / pi
print(var1)

var4 = var3[3:5]
print(var4)

var5 = age > pi #True/False - логический тип данных
print(var5)
var2 = age < pi
print(var2)
if age > pi:
    print("Условие верно")
else:
    print("Условие неверно")