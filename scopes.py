'=============================Области видимости================================'
# LEGB - Local Enclosed Global Build-in

# a = 5
# def func(a):
#     b = 10
#     print(a)
# func(1)
# print(b)

'=================================BUILD IN======================'
# Встроенное пространство имен (list, sum, print, input, max...........)

# our_len = len 
# print(our_len('123456'))

'================================Globals============================'
# Все переменные, которые мы создали внутри одного файла (модуля) чтобы посмотреть переменные можно использовать функцию globals
# a = 5
# b = 6
# c = 1


'=============================ENCLOSED (Non Local)============================'
# Замкнутое пространство - локальное простарнство, у которого есть внутреннее локальное простпранствою 


# var = 'globals'

# def func():
#     var = 'enclosed'
#     def inner_func():
#         var = 'local'
#         print(var)
#     print(var)
#     inner_func()
# print(var)
# func()


'=================================Local=================================='
#ЛОкальное пространство имен - переменные, созданные внутри функции (можно посмотреть с функции local())

# a = 10
# b = 1
# def func(a, b):
#     print('Globals': globals())
#     print('Locals:', locals())
#     print(a, b)
# func(a, b)

# count = 1
# def count_():
#     print(count)
#     count +=1
# count_() 
# UnboundLocalError: local variable 'count' referenced before assignment

# count = 1
# def count_():
#     global count # доступ на изменение глобального 
#     print(count)
#     count +=1
#     print(count)
# count_() 


# count = 1
# def count_():
#     count2 = 0
#     def inner_func():
#         nonlocal count2
#         global count
#         count2 = 10
#         count =100
#     inner_func()
#     print(count2)
# count_()


# matreshka = 100

# def func(matreshka_2):
#     global matreshka
#     matreshka = matreshka + matreshka_2
#     def inner_func(matreshka_3):
#         global matreshka
#         matreshka = matreshka + matreshka_3
#     inner_func(1)
# func(10)
# print(100)

# num = 3
# def mul():
#     global num 
#     num = num **2
# mul()
# mul()
# mul()
# print(num)


# list_= []

# def add():
#     global list 
#     name = input('Введите имя:')
#     list_.append(name)
#     print(f'user with name - {name}, was added')
#     return list_

# def remove():
#     global list_
#     if len(list_) > 0:
#         ind = int(input(" Введите номе юзера которого нужно удалить"))
#         user = list_.pop(ind)
#         print(f' Usser was deleted - {user}')

# def random_fun(number): 
#     import random
#     for i in range (number):
#         ran = random.randint(0, 1)
#         if ran == 0: 
#             add()
#         else:
#             remove() 
#     return list_
# print(random_fun(10)) 