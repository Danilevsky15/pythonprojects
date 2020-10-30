#бисер https://acmp.ru/index.asp?main=task&id_task=903
a = int(input("рандомное число:"))
print(a+1)

# https://acmp.ru/index.asp?main=task&id_task=942
a = (1)
b = (2)
c = (3)
print("Победил " + str(a) + "-ый школьник ")

# https://acmp.ru/index.asp?main=task&id_task=25
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
if a > b :
    print(">")
if a < b :
    print("<")
if a == b :
    print("=")

# https://acmp.ru/index.asp?main=task&id_task=766
n = int(input("Введите число: "))
m = int(input("Введите число: "))
k = int(input("Введите число: "))
if n + m < k :
    print("no")
if n + m > k :
    print("yes")

# https://acmp.ru/index.asp?main=task&id_task=195 элия
a = int( input("Введите число: "))
b = int( input("Введите число: "))
n = int( input("Введите число: "))
c = (a * b * n) * 2
print("Понадобится " + str(c) + " грамм наносульфида")

# https://acmp.ru/index.asp?main=task&id_task=773 гулливер
k = int(input("Введите число: "))
m = int(input("Введите число: "))
a = k * k * m
print(a)

# https://acmp.ru/index.asp?main=task&id_task=33 два бандита
a = int(input("Введите число: "))
b = int(input("Введите число: "))
if a < 10 :
    c = 10 - a
    print(c)
# я хз пока как ставить ограничение до того или иного числа,поэтому ,говорю, что пользователь пж выбери до 10
if a > 10 :
    print("Введите число до 10")
if b < 10 :
    e = 10 - b
    print(e)
if b > 10 :
    print("Введите число до 10")

# https://acmp.ru/index.asp?main=task&id_task=21 зарплата
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
if a < b and a < c :
    n = a
if b < a and b < c :
    n = b
if c < a and c < b :
    n = c
if a > b and a > c :
    m = a
if b > a and b > c :
    m = b
if c > a and c > b :
    m = c
r = m - n
print("Разница между максимальным и минимальным - " + str(r))

# https://acmp.ru/index.asp?main=task&id_task=4 игра
a = int(input("Введите первую цифру сотни числа: "))
b = int(input("Введите первую цифру десятка числа: "))
с = int(input("Введите единицу числа: "))
e = a + b + c       # хз я не понял как это делать
f = c + b + a
i = e - f
print(i)

# https://acmp.ru/index.asp?main=task&id_task=8 арифметика
a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
if a * b == c :
    print("yes")
if a * b != c :
    print("no")

# https://acmp.ru/index.asp?main=task&id_task=61 баскетбол
a0 = int(input("Введите первой команды число: "))
a1 = int(input("Введите первой команды число: "))
a2 = int(input("Введите первой команды число: "))
a3 = int(input("Введите первой команды число: "))
b0 = int(input("Введите второй команды число: "))
b1 = int(input("Введите второй команды число: "))
b2 = int(input("Введите второй команды число: "))
b3 = int(input("Введите второй команды число: "))
a = a0 + a1 + a2 + a3
b = b0 + b1 + b2 + b3
if a == b :
    print("DRAW")
if a > b :
    print(1)
if a < b :
    print(2)

# https://acmp.ru/index.asp?main=task&id_task=755 земляника
x = int(input("Введите число ягод собранных Мише: "))
y = int(input("Введите число ягод собранных Машей: "))
z = int(input("Введите число сьеденных: "))
a = x + y - z
if a > z :
    print(a)
if a < z :
    print("Impossible")
if a == z :
    print("Impossible")

# https://acmp.ru/index.asp?main=task&id_task=539 торт
n = input("Введите число: ")
a = n//2        # ВЕРНУТЬСЯ УТРОМ!# ВЕРНУТЬСЯ УТРОМ!# ВЕРНУТЬСЯ УТРОМ!# ВЕРНУТЬСЯ УТРОМ!# ВЕРНУТЬСЯ УТРОМ!# ВЕРНУТЬСЯ УТРОМ!
if a == int :
    n = n//2
    print(n + " минимальное число разрезов торта")
if a == float :
    n = (n+1)//2
    print(str(n) + " минимальное число разрезов торта")
