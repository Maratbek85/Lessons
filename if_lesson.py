'=====================Условия==============='
#Логические операторы - это выражения, которые возвращают True, если выражение верно и false - если не верно

# print(55 == 55)

"равенство"               'не равенсво'
5 == 5 # True              4 != 5 True
4 == 5 # False             4 != 4 False


"больше"                   'больше или равно'
5 > 4 # True                5 >= 10 False
5 > 10 # False              5 >= 4 True
5 > 5 # False               5 >= 5 True

"меньше"                    'меньше или равно'
5 < 4 # Falase              5 <= 10 True
5 < 10 # True               5 <= 4 False
5 < 5 # False               5 <= 5 True 

'=======================And, Or, Not=============='
# and = и
# or = или 
# not = нет 

# a = 5 
# b = 6
# # and 
# print (a == 5 and b == 6) #True 
# print (a ==5 and b == 7) # False
# print (a == 1 and b == 1) # False
# # если все выражения возвразщают True, то вернется True
# # если хотябы одно выражение или все выражения возвращат False, то вернется False 

# # OR
# print (a ==5 or b == 6) #True 
# print (a == 5 or b == 2) #True 
# print (a == 1 or b ==1) # False 
# #если хотябы одно выражение возвращает True, то нам вернется True 

#NOT 

not True # False 
not False # True

# При операторе AND OR NOT 
''' 
1 Всегда первым будет выполнятся NOT
2 Вторым по важности будет AND 
3 Последний в приоритете будет OR
'''
# print ((False or not False) and (not False) or False) 

'=======================Boolean Type==========='
# Булевый тип данных имеет только 2 значения: True или False
# print (bool(1)) # True 
# print (bool (0)) # False
# print (bool (), 'пустота') # False
# print (bool ( ), 'пробел') # True
# print (bool ([{}])) # True 
# print (bool ({})) # False

'=======================None Type=============='
# None - это неизменяемый тип данных с одним значением None, который используется для обозначения отсутствия значения, иначе говоря ПУСТОТА
# print (bool (None))
# print (bool ('None'))

'=================Условные операторы============='
# Условные операторы - конструкция, которая используется для того чтобы создать структуру условий для входных данных, для разных событий 

# answer = input ('Какой язык программирования мы изучаем?')
# if answer == 'Python': 
#     print ('Верно! Мы работаем на Python')
#     print ('Отличный язык!')
# else: 
#     print('Не совсем так!')
# Отступ сообщает, где начинается и где заканчивается блок кода 

# number = int(input ('Введите число:'))
# if number == 1:
#     print('Вы ввели число 1')
# elif number == 2:
#     print ("Вы ввели число 2") 
# elif number == 3: 
#     print ( 'Вы ввели число 3')
# else: 
#     print ('Вы ввели число больше 3')

# в одной конструкции может быть только один if
# в одной конструкции момет быть много elif либо же вообще отсутсвовать
# в одной конструкции момет быть лишь один else либо вообще не быть 

# otvet = input ('Какой язык програмирования лучший?')
# if otvet == 'Python':
#     print ('Да')
# else: 
#     print ('Нееееетттт!!!!')

# number = int (input ('Enter number:'))
# if number == 11 or number == 22 or number == 33 or number == 44 or number == 55 or number == 66 or number == 77 or number == 88 or number == 99: 
#     print ('Да')
# else: 
#      print ('Нет')

'===================Вложенный условный оператор=========='
'''
if условия1:
     блок кода 
else: 
     if условия2:
         блок кода 
     else:
         блок кода 
 '''
# grade = int(input ("Введите от 1- 100 :"))
# if grade >= 86:
#     print (5)
# else: 
#     if grade >=75:
#         print (4)
#     else: 
#         if grade >= 66:
#             print (3)
#         else: 
#             if grade >= 50:
#                 print (2)
#             else:
#                 print (1)


# grade = int(input ("Введите от 1- 100 :"))
# if grade >= 86:
#     print (5)
# elif grade >= 76: 
#     print (4)
# elif grade >= 66:
#     print (3)
# elif grade >= 50: 
#     print (2)
# else: 
#     print (1)

'======================Тернарный оператор==========='
# Тернарный оператор - это условия в одну строку
# num = int (input ('Введите число:'))
# result = 'Hello' if num == 5 else 'Bye'
# print (result)

# number = int(input ())
# is_chet = 'Четное' if number % 2 == 0 else 'Нечетное'
# print (is_chet)

# print ('Четное' if int(input('Введите число:')) % 2 == 0 else 'Нечетное') 
# В тернарном операторе нету ключевого слово elif, 
# Выполнится при True- (Любое действие) if УСЛОВИЕ Else (Любое действие) - выполнится при False 