'=================Переменная(Variable)=================='
#Переменная- это хранилища данных. В переменную можно положить любое значение. 
#Значение присваиваются с помощью знака равенства <<=>>

name = 'ADAcourse'
age = 20
is_active = True

#Название переменных не могут начинаться с цифр и символов, кроме символа _

# 1_ada = 'test' #SyntaxError
'=======================Числа тип(integer)=========================='
#Основные операции с числами
'''
В языке Python, как и в матиматике, над числами можно совершать арифметические операции:
Операторы.........Описание
.........+........Сложение
.........-........Вычитание
.........*........Умножение
........./........Деление
.........//.......Деление без остатка
........%.........Деление, остаток от деление
........**........Ввозведение в степень
........25 ** 0,5..Нахождение квадратного корня числа
'''
# a=5
# b=1
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# print(a+b * a-b)
# print((a+b)*(a-b))

# num1= 2+3 * 4
# num2 = (2+3)*4
# print( num1, num2)
#Последовательность вычислений придерживается математическим правилам

'====================================Численные типы данных==========='
# int - целое число
# float - вещественное число
# decimal - более точное вещественное число
# bin - бинарное число
# complex - комплексное число

from decimal import Decimal
x1 = 0.1
x2 = Decimal('0.1')

print(x1+x1+x1+x1+x1+x1+x1+x1+x1+x1)
print(x2 + x2 + x2 +x2 +x2 +x2 +x2 + x2 +x2 +x2)

# модуль числа  = положительное число |-5 | | 5 | = 5

print(abs(5), abs (-5))

# round  - округление числа 
print(round (5.5))
print(round(5.4))
print(round(5.432, 2))

from math import sqrt

print(sqrt (25)) #получим корень числа 25

#pow
# 1. Возводит в степень
# 2. Находит остаток от деления на третье число
print (pow(2,3)) #2**3=8
print (pow (2,3,3)) #2 ** 3 %3 =2

'''Написать программу, в которой рассчитывается сумма и произведение цифр положительного трехзначного числа'''

a = 34 ** 2
b = 26 * 3
c = 17 * 33
# e = 4394 * 4
# print(a , b ,c, e)
# print(17925 >= a)
# print(17925 >= b)
# print(17925 >= c)
# print(17925 >= e)


# print(17 * 3 >= 12*5)
# print(12 ** 3 >= 13*7)
# print(4 ** 5 >= 512+512)

# a=25
# b=45
# print((( a + b)*5)**2)
# c = ((( a + b)*5)**2)
# print(193432-c)

# a = 5.5
# b = 5.5
# c = 5.5
# print((a + b) *c)

# a = 20
# b = 13
# c = 8/2
# d = 7
# e = 5

# print((a-e**(b-d))%c)

# a = 25
# b = 20
# c = 30

# print(7 % 3 * 4.8)

# print(25-5 == 15+5)
# print(15+5 == 35-5)

# print(-21//10)

# a = 1985
# b = 2023
# print(b-a)
# print(2025-a)


numbers = [10, 15, 75, 20]
average = sum(numbers) / len(numbers)
print(average)

sum_= 10+ 15 + 70 +20 
arif = sum_ / 4
print("Среднее арифметическое =", arif)  

multi = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 *10
print(multi)

seconds_in_minuts = 60 * 60 
minuts_in_hour = seconds_in_minuts * 60
hour_in_day = minuts_in_hour * 24
year_in_day = hour_in_day * 365 
print(year_in_day)

num_1= 10, 12, 13, 100, 134567
num_2 = 12
num_3 = 13
num_4 = 100
num_5 = 134567


ves_2020 = 75
ves_2021 = 80
ves_2022 = 90
ves_2023 = 70
print(ves_2021 - ves_2020)
print(ves_2022 - ves_2021)
print(ves_2022 - ves_2021)
print(abs (ves_2023 - ves_2021))