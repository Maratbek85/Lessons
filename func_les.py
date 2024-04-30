'==========================Функция======================='
#Функция - это именованный блок кода, который вызывается множество раз в других частях программы
# Они создают благодаря ключевому слову  def
# При наименовании функции придерживаются стилю Snake_case

# def name_of_functions(a, b - параметры функции, их может быть сколько угодно):
# <body> код, который имеет некую логику
# return оператор, который возвращает результат выполнения функции 

# def my_func():
#     a = 4
#     b = 5
#     print(a + b)
#     return a + b

# print(my_func())

# list_numbers = [1,2,22,33,12,13,15,2,6,7]
# def find_even():
#     # for el in list_numbers:
#     #     if el % 2 == 0:
#     #         print(f'четное число: {el}')
#     [print (f'четное число: {el}') for el in list_numbers if el % 2 == 0]
# find_even()

# def say_hello_world():
#     print(f'{input("Введите свое имя:")} говорит helloworld')
#     # name = input('Введите свое имя:')
#     # print(name, 'говорит helloworld')

# say_hello_world()  

# def summa_n():
#     t = int(input())
#     # s = sum(range(1, t+1))
#     print(f"Я знаю, что сумма чисел от 1 до,{t} равна {sum(range(1,t+1))}")
          
# summa_n()

# def exponentiation_():
#     n = int(input('Введите ваше число:'))
#     print(f'Квадрат вашего числа: {n **2}\nКуб вашего числа: {n ** 3}')
# exponentiation_()

# def sum_num():
#     stroka= input()
#     # spisok = []
#     # for i in stroka:
#     #     if i.isdigit():
#     #         spisok.append(int(i))
#     # print(sum(spisok))
#     result = sum([int(num) for num in stroka if num.isdigit()])
#     print(result)

# sum_num()

# def add(a, b):
#     return a + b
# def substract(a, b):
#     return a - b
# def multi(a, b):
#     return a * b
# def divide(a, b):
#     return a / b


# def hello(name):
#     print(f'Hello {name}')

# if __name__ == '__main__':
#     hello('Marat')

# '===========================Функции======================'
# Функция - это именованный блок кода, который может принимать агрументы и возращать результат, функции можно использовать многократно

# Параметры функции - это переменные, которые будут принимать наша функция, для того чтобы мы смогли работать с данными, которые попадают в нашу функцию через аргументы
# Аргументы функции - это данные, которые мы передаем для параметров при вызове функции.
# return - это оператор, который нужен, чтобы функция возращала результат(по умолчанию возращает None)

# string = '1234abs'
# def our_len(stroka):
#     count = 0
#     for _ in stroka:
#         count += 1
#     return count
# print(our_len(string))
# print(our_len('123'))
# print(our_len(input()))

'==========================Виды Аргументов======================'
# 1. Позиционные (по позиции)
# 2. Именованные( по названию параметра-значение)

# def add(num1, num2):
#     return num1 + num2

# print(add(1,2))
# print(add(num1=5, num2=6))
# print(add(num2=5, num1=6))
# print(add(5, num2=3))

'=========================Виды Параметров========================='
# 1. Обязательные
# 2. Необязательные:
    # с дефолтным значением(с значением по умолочанию, которые передается при создании функции)
    # args (все позиционные аргументы, которые не попали в обязательные параметры или с дефолтом)
    # kwargs (все лишние именованные параметры)

# def greet(name1, name2, *args):
#     print(type(args))
#     print(*args)
#     # for name in args:
#     #     print(f'Привет {name}')
# greet('Антон', "Рашид", "Фархад", "Кирилл")
# def my_greet(name1=None, name2=None, **kwargs):
#     print(type(kwargs))
#     print(kwargs)
    # name = kwargs.get('name')
    # age = kwargs.get('age')
    # print(f'Привет {name}, твой возраст {age}')

# my_greet(age1='12', name='Anton')

# Чем хороши функции?
'''
1. Помогают избегать повторения одинаковых фрагментов кода
2. Упрощают внесение изменений в повторяемых блоках кода
3. Позваляет разбить задачу на подзадачи
Функции соблюдают принцип DRY (don't repeat yourself)
'''

'=========================Register, Login======================'
database = [
    {'name': 'user1', 'password': 12345},
    {'name': 'user2', 'password': 12345},
    {'name': 'user3', 'password': 12345},
]

def in_database(name):
    for user in database:
        if user['name'] == name:
            return True
    return False

def register_database(name, password1, password2):
    if in_database(name):
        return 'Юзер с таким именем уже существует'
    if password1 != password2:
        return "Пароли не совпали"
    user = {'name': name, 'password': password1}
    database.append(user)
    return 'Вы успешно зарегистрировались!'

def login_database(name, password):
    if not in_database(name):
        return 'Пользователь не найден'
    for user in database:
        if user['name'] == name:
            if user['password'] != password:
                return "Пароль не верный"
            return 'Вы успешно вошли'

def main():
    print('Добро пожаловать')
    while True:
        action = input('Введите что-то из этого --> register: 1\nlogin:2\nexit:3')
        if action == '3':
            break
        elif action == '1':
            name = input('Введите имя пользователя: ')
            password1 = input('Введите пароль: ')
            password2 = input('Введите пароль повторно: ')
            print(register_database(name,password1,password2))
        elif action == '2':
            name = input('Введите имя пользователя: ')
            password1 = input('Введите пароль: ')
            print(login_database(name, password1))
        else:
            print('Не корректный выбор')

# main()

'''
Напишите функцию count_letter(text, letter), которая принимает два параметра:
text – текст, в котором нужно посчитать сколько раз появилась буква letter, учитывая регистр буквы;
letter – буква, количество которой мы должны посчитать в text.
'''
# def count_letter(text, letter):
    # print(text.count(letter))
    # count=0
    # for simvol in text: 
    #     if simvol == letter:
    #         count += 1
    # print(count)
    # count= sum([1 for i in text if i == letter])
    # print(count)
# count_letter('asdfsdsdvdcaehagd', 'a')

'''
Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:
name – имя человека;
surname – фамилия человека;
patronymic – отчество человека;
а затем выводит на печать ФИО человека.
Ввод данных:
Александр
Пушкин
Сергеевич
Вывод:
ПАС
'''


# def print_fio(name, surname, patronymic):
#     fio = surname[0] + name[0] + patronymic[0]
    # print(fio)

# print_fio('Александр','Пушкин','Сергеевич')

'''
Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.
12345
15
'''
# def print_digit_sum(number):
#     result= sum([int(num) for num in str(number)])
#     print(result)
# print_digit_sum(12345)

# def print_digit_sum(number):
#     result = sum([int(num) for num in str(number)])
#     print(result)

# print_digit_sum(12345)

def greet(name, age):
    print(f'Привет, меня зовут{name}, и мне {age} лет')

person = {'name': 'Marat', 'age': 39}
greet(**person)
person1 = {'name': 'Alica', 'age':30}
person3 = {**person, **person1}
print(person3)