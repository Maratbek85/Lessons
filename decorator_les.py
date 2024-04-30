'==================================Декоратор======================='
# Декоратор - это функция высшего порядка , которая нужна чтобы расширять функционал другой функции не изменяя ее    аргумент (функция обертка)
# Функция высшего порядка - эта та функция которая принимает в аргументы другую функцию, создает внутри себя функцию, вызывает функцию и возвращает функцию 

# def my_func(name):
#     print(f' Hello {name}')
# my_func("ADA")

# def new_func(func):
#     print('Я функция которая принимает другую функцию')
#     func('Phyton')
#     print('Конец функция')
# new_func(my_func)

# def decorator(func):
#     def wrapper():
#         print('Я код, до вызова функции')
#         func()
#         print('Я код, после вызова функции')
#     return wrapper
# @decorator # Третий способ вызова декоратора 
# def hello():
#     print('Hello world')
# decorator(hello)() # первый способ вызова декоратора

# hello_ = decorator(hello) #второй способ вызова 
# hello_()
# hello()

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Я код, до вызова функции')
#         func(*args, **kwargs)
#         print('Я код, после вызова функции')
#     return wrapper

# @decorator
# def my_func(name):
#     print(f' Hello {name}')

# @decorator
# def sum_num(a, b):
#     print(a + b)

# my_func("Marat")
# sum_num(4,5)


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         res= func(*args, **kwargs)
#         print(res *2)
#     return wrapper

# @decorator
# def my_func(name):
#     return f' Hello {name}'

# @decorator
# def sum_num(a, b):
#     return a + b

# my_func("Marat")
# sum_num(4, 4)

# from datetime import datetime
# import time
# def decorator(func):
#     def wrapper (*args, **kwargs):
#         print('start:', datetime.now())
#         func(*args, **kwargs)
#         print('finish:', datetime.now())
#     return wrapper
# @decorator
# def time_10sek():
#     for i in range(10):
#         print(i)
#         time.sleep(1)

# time_10sek()

# def text_decor(func):
#     def wrapper(*args, **kwargs):
#         print('Hello', *args)
#         func(*args, **kwargs)
#         print( 'Goodbye', *args)
#     return wrapper

# @text_decor
# def greetings(name):
#     print('1, 2, 3')

# greetings('Marat')


# def repeater(func):
#     def wrapper(*args, **kwargs):
#         print(func(*args, **kwargs))
#         print(func(*args, **kwargs))
#     return wrapper

# @repeater
# def sum_num(a, b):
#     return a + b
# sum_num ( 4, 9)

# def repeater(func):
#     def wrapper(*args):
#         res = func(*args)
#         print(res ** 2)
#     return wrapper

# @repeater
# def sum_num(a, b):
#     return a * b
# sum_num (4, 9)


# def Upper_case(func):
#     def wrapper(*args, **kwargs):
#         res = func (*args, **kwargs)
#         # print(res)
#         print(res.upper())
#     return wrapper

# @Upper_case
# def spisok(lst):
#     import random
#     list2 = random.choice(lst)
#     return list2
# list1 = ['ada', 'mara', 'sara', 'klara']
# spisok(list1)

# def 

# def copy_delete(func):
#     def wrapper(*args, **kwargs):
#         result = func()
#         print (f'Результат функции с дубликатами равен {len(result)}')
#         new_list = list(set(result))
#         print (f'Результат функции без дубликатов равен {len(new_list)}')
#         return new_list
#     return wrapper

# @copy_delete
# def random():
#     import random
#     list1= [random.randint(10, 50) for i in range(100)]
#     return list1
# print(random())

# 4) Напишите функцию которая спрашивает у пользователя login и password. Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные. (Можете воспользоваться функцией ord и char, можете загуглить...)

# def shifrovka(func):
#     def wrapper():
#         login, parol = func()
#         encrypted_login = ''.join([chr(ord(bukva)+1) for bukva in login])
#         encrypted_parol = ''.join([chr(ord(bukva)+1) for bukva in parol])
#         return encrypted_login, encrypted_parol
#     return wrapper

# @shifrovka
# def login_password():
#     login = input('Введите ваш логин: ')
#     parol = input("Введите ваш паролль:")
#     return (login, parol)

# print(login_password())

# # 5)Создайте декоратор, который записывает значение оборачиваемой функции в файл.  


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         with open('text.txt', 'a') as file:
#             login, parol = func()
#             text = f'Логин:{login}\tПароль:{parol}\n'
#             file.write(text)
#     return wrapper

# @decorator
# def login_password():
#     login = input('Введите ваш логин: ')
#     parol = input("Введите ваш паролль:")
#     return (login, parol)
# login_password()


