'===============================Lambda========================='
# Lambda - анонимная функция с телом, но без имени
# Общий синтаксис: lambda список_параметров: выражение

# hello = lambda: 'hello'
# print(hello())

# sum_kvad = lambda a, b, c: a**2+ b**2+c**2
# print(sum_kvad(1,2,3))


# calc= {
#     '+': lambda n1, n2: n1 + n2,
#     '-': lambda n1, n2: n1 - n2,
#     '*': lambda n1, n2: n1 * n2,
#     '/': lambda n1, n2: n1 / n2,
#     '%': lambda n1, n2: n1 % n2,
#     '//': lambda n1, n2: n1 // n2,
# }

# def main():
#     try:  
#         num1 = int(input(' Введите число:'))
#         num2 = int(input(' Введите число:'))
#         operator = input('Введите оператор (+, -, *, /, %, //)')
#         func_= calc[operator]
#         result = func_(num1, num2)
#         print(result) 
#     except ValueError: 
#         print('Вы ввели не число!')
#         main()
#     except ZeroDivisionError: 
#         print('Делить на ноль нельзя')
#         main()
#     except KeyError:
#         print('Такого оператора нет')
#         main()
# main()

# f1 = lambda x, y, z= 3: sum((x, y, z))
# print(f1(1,2))
# print(f1(1,2, 4))

# f2 = lambda *args: sum(args)
# print(f2(1,1,1,1,1,1,1))
# print(f2(1,1,1,1,1,1,1, 2,2,2,2,2))

# f3 = lambda*args, **kwargs: sum(kwargs.values())
# print(f3(n1 =1, n2 = 2, n3 =3))

# Основные качества lambda
# 1. Однокрвтное использование 
# 2. Передача функций в качестве аргумента другим функциям
# 3. Возвращение только одного значения 


# string = ['a', 'b', 'c', 'd', 'e']
# numbers = [3, 2, 1, 4, 5]
# new_strings = list(map(lambda x, y: x *y, string, numbers))
# print(new_strings)

# numbers = [1, 2, 3, 4, 5]
# num_kvad = list(map(lambda x: x**2, numbers))
# print(num_kvad)

# numbers = [-11, -50, 50, 55, 30, 3, 13, 12]
# positive_numbers = list(filter(lambda x: x>0, numbers))
# large_numbers = list(filter(lambda x: x>30, numbers))
# even_numbers = list(filter(lambda x: x%2==0, numbers))
# print(positive_numbers, large_numbers, even_numbers)

# list1 = [1 ,2, 2, 1]
# list2 = [5, 6, 7, 8]
# target_sum = 9
# filter_zip = list(filter(lambda x: x if sum(x) == target_sum else '', zip(list1, list2)))
# print(filter_zip)

'=============================Рекурсия======================='
# Рекурсивная функция - это функция которая вызывает сама себя, и при каждом вызове использует данные, созданные во время предыдущего вызова

# 1. Граничный случай, при котором функция завершает свою работу и возвращает данные в основную программу
# 2. Рекусивный случай, при котором функция продолжает вызывать себя 

# def greetings(string):
#     print(string)
#     if len(string) ==0:
#         return #Граничный случай
#     else: 
#         greetings(string [:-1]) # Рекурсивный случай
# greetings ('Hello World')

# def factorial(n):
#     if n ==1: 
#         return 1
#     else: 
#         return n * factorial(n-1)
# print(factorial(10))

# def fact(n):
#     factorial = 1
#     for i in range(1, n+1):
#         factorial*=i
#     return factorial
# print(fact(10))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 112,113,119,124]

# def eden_recur(spisok_num):
#     num = spisok_num.pop()
#     if  num%2 == 0:
#         print(num)
#     if len(spisok_num) == 0:
#         return
#     else: 
#         eden_recur(spisok_num)
# eden_recur(numbers)

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# func_= lambda x, y, z: f'Объем коробки:{x*y*y}'
# print(func_(n1, n2, n3))

# n1 = int(input())
# n2 = int(input())
# fun_= lambda x, y: ((x**3) + (y**3))
# print(fun_(n1, n2))

# list1 = [1, 2, 3, 4,  5, 6, 8, 9]
# list2= list(filter(lambda x: x % 2 ==0, list1))
# print(list2)

# 1)Напишите программу которая выводит только нечётные числа с помощью рекурсии.
# def rec(n):
#   list1 = [1, 2, 3, 4,  5, 6, 8, 9]
#   new_list = []
#   if n > 0:
#     rec(n-1)
#     if n % 2: 
#       return rec(n+1)
#     new_list.append(n)
#   else: 
#     n == 0
#     return
# rec()

# 4) Написать lambda которая получает сколько дней ПРОШЛО с нового года как параметр и говорит пользователю сколько дней ОСТАЛОСЬ до нового года. 

# data_new_year = lambda days_pass: 365 - days_pass
# print(data_new_year(43))

# 5) Написать lambda функцию, которая принимает 1 параметр количество лет. Посчитайте количество дней в n лет. 1 год = 365.
# years_in_days = lambda years: years*365
# print(years_in_days(4))

# 6) Напишите функцию которая принимает LIST и рекурсивно удаляет оттуда по одному элементу при запуске.

# spisok = ['ada', 'python', 'course', 1, 3, 4, 5]
# def remove_one(lst):
#     if not lst:
#         return
#     lst.pop()
#     print(lst)
#     remove_one(lst)
# remove_one(spisok)

# 7) Вам дан список [2, 5, 20, 100, 9, 1, 6, 7, 12, 8], выведите квадрат каждого элемента, использовать lambda и map.

# list_=[2, 5, 20, 100, 9, 1, 6, 7, 12, 8]
# squared= list(map(lambda x: x**2, list_))
# print(squared)

# 8) Использовать предыдущий список, вывести элементы кратные 3. Использовать lambda и filter.

# even_list = list(filter(lambda x: x%3 ==0, list_))
# print(even_list)

# 9) Написать рекурсию, которая находит сумму цифр n.
# пример: n = 256
# сумма равна 13    (2+5+6)

# def sum_numbers(n):
#     if n == 0:
#         return 0 
#     else: 
#         return n % 10 +sum_numbers (n // 10)
# print(sum_numbers(256))
