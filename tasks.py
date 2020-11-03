a = int
a = input("insert the number : ")
if a <= 1000 or a != 1000:
    while a < 1000 or a <= 1000:
        print(a+1)
        a += 100
        if a == 1000:
            break
if a >= 1000:
    while a > 1000 or a >= 1000:
        print(a+1)
        a -= 100
        if a == 1000:
            break

#https://acmp.ru/index.asp?main=task&id_task=529 длина отрезка это   -   корень(x^2+y^2)
import math
x1 = int
x1 = input("insert the number: ")
y1 = int
y1 = input("insert the number: ")
x2 = int
x2 = input("insert the number: ")
y2 = int
y2 = input("insert the number: ")
l = int
l = math.sqrt((x2-x1)^2+(y2-y1)^2)
print(l)


# https://acmp.ru/index.asp?main=task&id_task=819 паралм
a = int
a = input("Введите положительное число:")
b = int
b = input("Введите положительное число:")
h = int
h = input("Введите положительное число:")
if a < 0 or b < 0 or h < 0:
    print("Введите положительное числа:")
if a >= 0 or b >= 0 or h >= 0:
    S = int
    V = int
    S = 2*(a*b + b*h + a*h)
    V = a*b*h
print(S, V)