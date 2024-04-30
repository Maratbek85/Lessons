'=================================Try Except================='
# Исключения - это обьекты которые прерывают работу кода, если не были обработаны (связаны с логикой нашей программы
# print(10+ '10') TypeError

# Ошибки - обькты, которые прерывают работу и их нужно обработать (связаны по большей части с разработчиком)

# print( SymtaxError; '(' was never closed

SyntaxError
# ошибка, которая выходит, когда в кодк допущена синтаксическая ошибка 
# '''SyntaxtError : unterminated triple-quoted string literal (detected at line 10)'
# когда мы не закрыли скобку либо кавычки 

# a = 
# 'SyntaxError: invalid syntax'

NameError
#исключение, которые выходит когда мы обращаемся к несуществующей  переменной 
name = 'Anton'
#print(Name)
"NameError: name 'Name' is not defined. Did you mean: 'name'?"

IndexError
#исключение, клтлрые выходит когда мы обращаемся по несуществующему индексу 

# list_= [1, 2, 3]
# print(list_[3])
'IndexError: list index out of range'
# list_.pop(4)
'IndexError: pop index out of range'

KeyError
#исключение, которое выходит когда мы обращаемя по несцществующему ключу
# dict_={'a': 1}
# print(dict_('b'))
"KeyError: 'b'"
# dict_pop.('b')
"KeyError: 'b'"

"ValueError:"
# Исключение, когда мы передаем в функцию не коректный для нее тип данных
# int('12d')

"ValueError: invalid literal for int() with base 10: '12d'"
# когда мы распаковываем итерируемый обьект на несколько переменных и количество переменных не совпадает с количеством элементов внутри итеруемого обьекта
# a,b, c = [1,2]
"ValueError: not enough values to unpack (expected 3, got 2)"

TypeError
# исключение, когда мы пытаемся использовать методы не свойственные какому-либо типу данных или мы пытаемся передать функции больше или менбше аргументов, чем принимает эта функция

# for i in 12345: 
#     print(i)
"TypeError: 'int' object is not iterrable"
# '5'+5# TypeErrorL can only concetenate str (not "int" to str)
# {[1,2,3: 'gel']} #TypeError: unhashable type: 'list'
# input('hello!', 'World') #TypeError: input expected at most 1 argument, got 2

ZeroDivisionError
# выходит при делении на 0

AttributeError
# выходит, когда мы обращаемся к несуществующему методу или атрибуту у обьекта (типа данных)
# [].replace()
"AttributeError: 'list'object has no attribute 'replace"

IndentationError
#выходит, когда мы не правильно используем отступы
        # a = 5
#         'IndentationError: unexpected indent'
# for i in 'abs':
# print(i)

Exception
# исключение, которое мы сами создали чтобы его вызвать
"Вызов исключение происходит с помощью ключевошо слово: raise"
# raise Exception ('Ошибка')

'=============================Обработка исключений======================='
# Чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except и обрабатывать вызванное исключение

# try:
#     # код, который возможно вызовет ошибку
#     num = int(input('Введите число:'))
# except ValueError: # исключение, которое может возникнуть 
#     print(('Вы ввели не число!'))
# else: #код, который отработает только если никакая ошибка не вышла
#     print('Вы ввели число', num)
# finally: # код который отработает в любом случае 
#     print ('До свидание!')


# try: 
#     while True:
#         num = int(input())
#         num2 = int(input())
#         print(num/num2)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя!")
# except ValueError:
#     print("Нужно было ввести число!")

# try:
#     num = int(input('Введите число'))
#     if num == 0:
#         raise ValueError
# except (SyntaxError, NameError, ValueError):
#     print('Вышла какая-та ошибка')

# try:
#     raise Exception
# except: 
#     print("любая ошибка")

# try: 
#     4/0
#     raise TypeError ('Ошибка типа данных')
# except Exception as error: 
#     print(error)

# try:
#     num1 = input()
#     num2 = input()
#     print(int(num1) + int(num2))
# except: 
#     print(num1+num2)

# try: 
#     age= int(input('введите ваш возраст'))
#     if age > 0:
#         print(age)
#     else: 
#         raise Exception
# except:
#     print('ваш возраст должен быть больше нуля')


# 1) Напишите код который обрабатывает исключение TypeError

# try: 
#     list= [1, 2, 3, 4, 'a', 'b']
#     dic ={'a': 1, 'b': 2}

#     print(list+dic)
# except TypeError:
#     print(TypeError)
# else: 
#     print('Удачно')



    
# 2) Создайте файл который содержит цифры в одной строчке. Напишите программу которая открывает файл и преобразовывает каждую цифру в целое число. Обработайте случай если в файле будет символ, который нельзя преобразовать в целое число.


# try: 
#     with open ('Files/test.txt') as file: 
#         content = file.read().replace('\n', '')
#         numbers = [int(i) for i in content]
#         # print(sum(numbers))
# except ValueError:
#     print('Невозмодно преобращовать букву в цифру')
# except FileNotFoundError: 
#     print('Такого файла не существует')
# else: 
#     print(f'Сумма всех цифр {sum(numbers)}')


# 3) Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in. Предусмотреть момент не существования файла и обработать.

# try: 
#     with open('Files/test2.txt') as file:
#         content = file.read ()
#         if 'w' in content:
#             print('В тексте есть буква "w"')
#         else: 
#             print( 'В тексте нет буквы "w"')
# except FileNotFoundError:
#     print('Такого файла не существует')



# # 4) Попросите пользователя ввести имя, страну, год рождения. Запишите все данные файл, однако год рождения преобразовать в целое число. 

# try:
#     name = input('Введите ваше имя:')
#     birthday = int(input('Введите год рождения:'))
#     country = input('Введите строну: ')
#     with open ('Files/test.txt''w') as file: 
#         file.write (f'Name: {name}\nBirthday:{birthday}\nCountry:{country}')
#         print('ok')
# except Exception as error: 
#     print(error)



# 5) Создайте функцию которая принимает произвольные аргументы (*args, **kwargs). Данная функция из kwargs берет ключи "name", "age" и выводит на экран. Вызовите функцию внутри try и обработайте конкретное исключение, какое именно исключение найти самостоятельно.

# def name_age(*args, **kwargs):
#     name = kwargs['name']
#     age = kwargs['age']
#     print(f'Name:{age}, age: {age}')

# try: 
#     name_age(name = 'Anton', age = 25)
#     name_age (name = 'Denis')
# except KeyError as error:
#     print('Такого ключа нет',error)

# 6) Создать 4 функции add(), subtract(), multiply(), divide(), каждая принимает два обязательных аргумента.Попросите пользователя ввести два числа и вызовите все 4 функции для двух чисел. Обработайте возможные ошибки.

# def add(a, b):
#     return a + b
# def substract(a, b):
#     return a - b
# def multi(a, b):
#     return a * b
# def divide(a, b):
#     return a / b
# try: 
#     num1 = int(input('Введите число:'))
#     num2 = int(input('Введите число:'))
#     print(add(num1, num2))
#     print(substract(num1, num2))
#     print(multi(num1, num2))
#     print(divide(num1, num2))
# except ValueError: 
#     print('Введите число!')
# except ZeroDivisionError: 
#     print('деление нв ноль звапрещено!')


# 7) Создайте два списка с целыми числами, написать программу, которая проходит по всем элементам первого списка и каждый элемент это доступ по индексу второго списка.

# l1 = [2, 3, 0, 1]
# l2 = [10,20,30,40]
# try: 
#     result = []
#     for ind in l1:
#         elem = l2[ind]
#         result.append(elem)
# except IndexError as error:
#     print(error)
# else: 
#     print(result)

# try: 
#     spisok= input('Введите строку:')
#     index = int(input('Введите индекс строки:'))
#     print(spisok[index])
# except IndexError as error:
#     print ('Ошибка индекса:', error)
# except Exception as error:
#     print('Какая-то ошибка', error)

    
