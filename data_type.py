'==================Типы данных=========='
# Переменная - это ссылки на ячейки памяти, где храняться эти данные для дальнейшего использования этих данных

num1 = 4
num2 = 3

# правила по наименованию переменных
number = 5 # название переменных, нужно записывать осмысленное 
a = 5 # так можно, но нету логического смысла
NUMBER = 10 # Переменные в верхнем регистре называют константы

# 1num = 10 так нельзя начинать название переменного с числа
# num-df@ = 12 нельзя использовать символы в название, кроме _ 
# print = 10 нельзя называть вситроенными функциями python
# if = 12 нельзя называть переменные ключевыми словами

# Snake case - python стиль наименования
my_name = 'Marat'

#Camel Case - стиль других языков програмирования

'=====================Ввод и Вывод данных========='
# print - функция для вывода данных
# # input - функция для ввода данных
# print('Мы изучаем язык Python') 
# print("'Python'") # можно использовать двойные и одинарные кавычки
# print('"Python"')
# # То что мы пишем в круглыз скобках у команлы print называют аргументами команды

# print( 'Скоро я', "пойду", 'завтракать') #каждый аргумент разделен межу друг другом пробелом
# print( 'Какой хороший день!') #последующая команда print выводит текст с новой строки
# "Необязательные параметры команды print: sep and end"
# # sep (separator- разделитель)
# # end (окончание)
# print( 1, 2, 3, 4, 5) #sep =''
# print(1, 2, 3, 4, 5, sep= '(<_>)')
# print( 'Python course', end = '\n') #\n - переводит текст на новую строку
# print(1, 2, 3, 4, 5, sep = '(<_>)', end = "^_^")
# print( 'Я остался на предыдущей строке')

# '=====================Input()=================='
# # input()- втсроенная функция, для считывания данных, с клавиатуры
# print( 'Как тебя зовут?') # вывод текста на экран
# name = input() #ввод текста и запись в переменную, записывает строковое значение
# print (' Привет', name) #вывод тескта на экран
# print (input() + input ())

# day = input(" Какой сегодня день?")
# print('Сегодня:', day)

'===========================Типы данных================'
# В Python типы данных относят к двум категориям: изменяемые и неизменяемые
'''
Изменяемые: list (список), dict(словарь), set(множества)
Неизменяемые: int (целые 1, 2, 3), float (с точкой 2,5), complex, decimal, str (строка), tuple (кортеж), bool (булевые), None (пустота), frozenset (неизменяемое множества)
'''
list_= [1 , 2, 3, 'Anton', 'a', True]
dict_ ={'Anton' : 20, 'Maks' :22}
set_= {1, 1, 1, 1, 2, 2, 3} # уникальные значения (не повторяются)
# print (set_)

int_ = 10
float_ = 0.5
complex_ = 1j #больше типы данных
str_ = 'Marat'
tuple_ = (1, 2, 3, 'abc')
bool_1 = True
bool_0 = False
none_ = None

'====================Преобразование типова данных======='
number1 = '4'
number2 = 11
number3 = 3.12

# print (int(number3)) # с округлением в стронору нуля
# print (int(number1) + number2 + int(number3))
# print ( float (number1) + float (number2) + float(number3))
# print (12 + 2.4)
# print (number1 + str(number2) + str (number3))

# number1 = int(input ('Первая:')) 
# number2 = int (input('Вторая:'))
# print((number1) + (number2))

# age= int (input('Date of Birth:'))
# today= 2024
# print(today - age)

# age= int (input('Date of Birth:'))
# today= 2024
# seconds_in_minute = 60  
# minutes_in_hours = 60 * seconds_in_minute
# hours_in_day = 24 * minutes_in_hours
# days_in_year = 365 * hours_in_day 
# print((today-age) * days_in_year)

# cost1 = int(input ('chocolate:'))
# cost2 = int(input ('Milk:'))
# cost3 = int(input ('Cofee:'))
# quantity = int(input ('Quantity in a pack:'))
# print((cost1 *quantity)+(cost2 * quantity) +(cost3 * quantity))

# a= int (input ('Сторона прямоугольника А:'))
# b= int (input ('Сторона прямоуголтника В:'))
# print("Периметр прямоугольника:", a * b)

# Celcium = int (input ('Temperature in Celciums:'))
# print((Celcium * (9 / 5) + 32))  

# # Напишите программу, которая находит возведение числа в степень. Само число и степень спросить у пользователя.
# number1 = int (input ('number to be multiplied:'))
# number2 = int (input ( 'times to be multipled:'))
# print(pow (number1, number2))

#Сделайте калькулятор стоимости компьютера со скидкой. Запросите стоимость компьютера и скидку  в %, выведите стоимость компьютера со скидкой.

# Cost = int (input ('Cost of the Computer:'))
# Discount = int (input ('Discount offered:'))
# print(Cost - (Discount * Cost / 100))

# V1 = int(input ('Speen of 1st lady:'))
# V2 = int (input ('Speed of 2nd lady:'))
# S = int (input ('S:'))
# print(S/(V1+ V2))

# x = float(input ())
# if x == 0:
#     print('Обратного числа не существует')
# else:
#     print( 1 / x)

# #Пример 232114.921 Вывод 9
# a = float(input('Задайте число:'))
# a *= 10 # a = a + 1
# print(int (a % 10))

# Дано положительное действительное число. Выведите его дробную часть
# 4.25 ==> 0.25
# b = float( input('Задайте число:'))
# b_int = int(b)
# print(b - b_int)
