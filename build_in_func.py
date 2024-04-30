'===========================Встроенные функции================'
# map, filter, reduce, zip, enumerate, all, any

#zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)
# from itertools import zip_longest

# list_ = [1, 2, 3, 4]
# string_= 'abcsd'
# set_ = {1.5, 2.5, 3.5, 5.5}
# zipped = zip(list_, string_, set_)
# zipped = zip_longest(list_, string_, set_)
# print(zipped)
# print(list(zipped))

# names = ['Anton', 'Dima', 'Max']
# age = [20, 18, 12]
# people = dict(zip(names, age))
# # print(people)
# for i, j in zip(names, age):
#     print(i, j)

#enumarate - нумерует последовательсть (по дефолту начиная с 0), тоже получем генератор

# names = ['Anton', 'Dima', 'Max']
# enumerated = enumerate(names)
# print(next(enumerated))
# print(next(enumerated))
# print(next(enumerated))

# enum_list = list(enumerated)
# print(enum_list)

# enum_string = 'hello world'
# enum_str = enumerate(enum_string, start=1)
# print(list(enum_str))


# names = ['Anton', 'Dima', 'Max']
# dict_names= dict(enumerate(names, start=1))
# print(dict_names)
# print(dict_names[3])

#map- функция высшего порядка, принимает другую функцию и итерируемый обьект, выполняет заданную функцию на каждый элемени последовательности
# spisok = input('Введите число через пробел:').split()
# print(spisok)
# nums = [int(num) for num in spisok]
# nums = list(map(int, spisok))
# print(sum(nums))
# print(nums)


# spisok = input('Введите число через пробел:').split()
# print(spisok)
# def quad(x):
#     try:
#         x = int(x)
#         return x **2
#     except:
#         return 0
# quad_list = list(map(quad, spisok))
# print(quad_list)

# filter - функция высшего порядка, возвращающий генератор, с элементами прощедщими фильт (какое-то условие), принимает функции и последовательность (func, iterable)

# people = [
#     ('John', 22),
#     ('Adrian', 14),
#     ('Adam', 12),
#     ('Mark', 19),
#     ('Sam', 18)
# ]

# def age_control(person):
#     return person[1] >= 18
# filtered= list(filter(age_control, people))
# print(filtered)

'=============================Lambda==================='
# Lambda - анонимная функция с телом, но без имени
# Общий синтаксис: lambda список_параметров: выражение

# nums= [1, 2, 3, 4, 5]
# quadra_nums = list(map(lambda x: x**2, nums))
# print(quadra_nums)
# print(sum(quadra_nums))

# people = [
#     ('John', 22),
#     ('Adrian', 14),
#     ('Adam', 12),
#     ('Mark', 19),
#     ('Sam', 18)
# ]
# filtered = list(filter(lambda person: person[1] >=18, people))
# print(filtered)

'=============================Reduce================='
#reduce- функция высщего порядка, которая принимает другую функцию и последовательность, возвращает один элемент 

# from functools import reduce
# list_= [1, 2, 3, 4, 5]
# sum_numbers = reduce(lambda x, y: x + y, list_)
# print(sum_numbers)


# string = 'hello'
# print(reduce(lambda x, y: x +'|' +y, string))

# list_= [1, 2, 3, 4, 5]
# min_numbers = reduce(lambda x, y: x if x < y else y, list_)
# max_numbers = reduce(lambda x, y: x if x > y else y, list_)
# print(min_numbers, max_numbers)


# users = [
#     {'name': 'Anton', 'age': 19},
#     {'name': 'Alina', 'age': 20},
#     {'name': 'Adilet', 'age': 12},
#     {'name': 'Max', 'age': 15},
#     {'name': 'Kristina', 'age': 30},

# ]

# max_person = reduce(lambda x, y: x if x ['age']> y['age'] else y, users)
# min_person = reduce(lambda x, y: x if x ['age'] < y['age'] else y, users)
# print(f'Самый взрослый человек: {max_person["name"]}')
# print(f'Самый молодой человек: {min_person["name"]}')

'=============================All================'
#all- функция которая итерируемый обьект и возвращает True, если все элементы последовательности True иначе False
# spisok = [True, 1, {'name': 'anton'}, 'hello']
# print(all(spisok))

# my_list = [ 8, 6, 14, 2, 10, 12, 4]
# result = all( x % 2 ==0 for x in my_list)
# print(result)

'===========================Any================='
#Any- Функция которая принимает последовательность и возвращает True, если хотя бы один элемент был истиной (True) иначе False


# my_list = [ 8, 6, 11, 2, 10, 1, 4]
# result = any( x % 2 ==0 for x in my_list)
# print(result)

# my_list = ['abc', 'def123', 'gfy']
# result = all([x.isalpha() for x in my_list])
# result1 = all(map(str.isalpha,my_list))
# print(result)
# print(result1)

# def calculate_factorial(n):
#     if n == 1:
#         return n 
#     else:
#         return n * calculate_factorial (n-1)
# result=  calculate_factorial (5)
# print(result)


# 1) Написать lambda функцию, которая принимает 3 параметра и умножает все параметры между собой. Функция должна вернуть строку: "Объём коробки " и значение которое получилось.

# def count_(num1, num2, num3):
#     num1
#     list_1= map(lambda: num1 * num2 *num3)
#     print('Объем коробки ', list_1)
# count_(num1 =, num2= num3= int(input('Введите число после пробелов')))

