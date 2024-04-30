'=============================ASCII========================='
#ASCII- Представляет собой набор из 128 цифровых кодов, которые обознают английские буквы. 

'=============================UNICODE======================='
#Unicode- таблица символов  Unicode представляет собой набор цифровых символов, которые включает в себе знаки почти всех письменных языков мира. 
# Первые 128 кодов из таблицы символов Unicode совпадает с ASCII
# Unicode - жто не кодеровка, это таблица символов
# Кодировка на таблице символов unicode - например  UTF -8


'==============================ORD=========================='
# Ord - позволяет определить код некоторого символа в таблице символов Unicode

# ord1 = ord('a')
# ord2 = ord('b')
# ord3 = ord('c')
# ord4 = ord('а')

# print(ord1, ord2, ord3, ord4)

'===============================CHR==========================='
#Chr - позволяет по коду символа определить сам символ 

# chr1 = chr(65)
# chr2 = chr(66)
# chr3 = chr(67)
# print(chr1, chr2, chr3)



# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# list_= [chr(i) for i in range(a, b+1)]
# print(list_)


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


# text1 = input('Введите ваш текст: ')
# text2 = [ord(bukva) for bukva in text1]
# print(text2)

'=========================Декораторы с параметрами=============='

# def repeat(times=2):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @repeat(5)
# def my_func(text): 
#     print(text)

# @repeat(4)
# def my_func1(): 
#     print(4+4)
    
# my_func('Hello, World')
# my_func1()
# from functools import wraps

# def limit_calls(max_calls):
#     def decorator(func):
#         call_count = 0
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal call_count
#             if call_count >= max_calls:
#                 print(f'Функция {func.__name__} достигла лимита вывозв ({max_calls})')
#                 return
#             call_count +=1
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator

# @limit_calls(3)
# def my_function():
#     print('Вызвана функция my_function')

# my_function()
# my_function()
# my_function()
# my_function()


# def make_bold(func):
#     def wrapper (*args, **kwargs):
#         text1= f'<b> {func()}</b>'
#         return text1
#     return wrapper
    
# def make_italis(func):
#     def wrapper (*args, **kwargs):
#         text2 = f'<i> {func()} </i>'
#         return text2
#     return wrapper
    
# def make_underline(func): 
#     def wrapper(*args, **kwargs):
#         text3 = f'<u> {func()} </u>'
#         return text3
#     return wrapper

# @make_bold
# @make_italis
# @make_underline
# def hello():
#     text= 'Hello World'
#     return text
# print(hello())


# Декоратор log, перед вызовом функции выводит имя функции и её аргументы (известно, что аргументы только позиционные), потом вызывается функция, потом в той же строчке дописывает результат. '''
# # func.__name__
# from functools import wraps

# def log_(func):
#     # @wraps
#     def wrapper(*args, **kwargs):
#             print(f'Имя функции: {func.__name__}')
#             print(f'Список аргументов {args}')
#             result = func(*args, **kwargs)
#             return result
#     return wrapper


# @log_
# def sum_numbers(*args):
#     return sum(args)
# print(sum_numbers(1, 2, 3, 4, 5, 6, 7))



# def limit_calls(max_calls):
#     def decorator(func):
#         call_count = 0
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal call_count
#             if call_count >= max_calls:
#                 print(f'Функция {func.__name__} достигла лимита вывозв ({max_calls})')
#                 return
#             call_count +=1
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator