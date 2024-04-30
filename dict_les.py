'==============================Словарь (Dict)====================='
# Словарь- изменяемые, итерируемый, неупорядочный, неиндексируемый тип данных, хранит в парах {ключ: значение} {key: value}

# user = {'name': 'Anton', 'login': 'anton1123', 'password': 12345, 1: 111}
# print(user)
# print(user['name'])
# print(user['login'])
# print(user['password'])
# print(user[1])

#  Ключами в словаре могут быть только неизменяемые типы данных
# Ключи должны быть уникальными, не должны повторятся, если же повторяются то сохранится последний

# dict_ = {1: 'Anton', 2: 'Ainazik', 3: 'Alina', 1: 'Max'}
# print(dict_[1])

# Значения могут быть любые типы данных и могут повторятся
# print(dict_[4]) # KeyError: 4
# print(dict_['anton']) # KeyError: 'anton'

'===========================Создание словарей=============='
# dict_1 = {'1': 'a', '2': 'b', '3': 'c'}
# dict_2 = dict([('1', 'a'), ('2', 'b'), ('3', 'c')])
# print(dict_1)
# print(dict_2)

# dict_1['1'] = 'Anton'
# dict_1['2'] = 'adilet'
# dict_1['3'] = 'adil'
# print(dict_1)

'=====================Методы словарей========='

# get - метод, который возвращает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение

dict_ = {1: 'Anton', 2: 'Ainazik', 3: 'Alina', 3: 'Max'}
# print(dict_.get(5)) # вернет пустоту
# print(dict_.get(1, 'Такого ключа нет!')) # вернет мне дефолтное значение 

# pop - метод, удаляет пару по ключу и возвращает значение 
# remove_element = dict_.pop(1)
# print(remove_element)
# print(dict_)

# popitem - метод, удаляет последнюю пару и возвращает еe
# print(dict_.popitem())
# print(dict_)

# update - метод, который расширяет словарь парами из другого словаря 
dict_3 = {1: 'Akmaral', 4: 'Seit'}
dict_.update(dict_3)
print(dict_)

#clear- очищает словарь 
# dict_.clear()
# print(dict_)

# fromkeys- метод, который создает новый словарь исползуя список ключей 
# dict_1 = dict.fromkeys([1,2,3,4,5], 'name')
# print(dict_1)


#keys, values, items
#keys - метод, который возвращает все ключи 
#values - метод, который возвращает все значения 
#items - метод, который возвращает tuple (ключ, значение)

# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())

'============================Итерирование словарей==========='
# user= {'name': 'Anton', 'login': 'anton123', 'password': 12345}
# for key in user.keys():
#     print(key)
# for values in user.values():
#     print(values)

# for key, value in user.items():
#     print(key, value)

# new_user = {}
# for key, value in user.items():
#     new_user[value] = key
# print(new_user)
# print(user)

# university = {'программирование': 10, 'экономика': 9, 'медицина': 8} 
# university['программирование']= 14
# university['лингвистика'] = 4
# university.update({'дипломатие': 0})
# university.pop('медицина')
# sum_=0
# for value in university.values():
#     sum_+=value
# print(sum_)
# print(sum(university.values()))
# print(university)

# dict_ = {1: 'a', 2: 'b', 3: 'c'}
# new_dict= {}
# for key, value in dict_.items():
#     new_dict[value]= key
# print(new_dict)

# n = int(input ())
# dict_ = {}
# for i in range (1, n+1):
#     x = input('Введите имена гостей:')
#     dict_[i] = x
# print(dict_)

# guest = int(input())
# party = []
# new_dict = {}
# for key in range (1, guest +1):
#     name = input('Введите имя гостя:')
#     party.append(name)
#     new_dict[key]= name
# print(party)
# print(new_dict)

# number = int(input('Введите число: '))
# first = number // 1000 # 1614 // 1000 = 1
# second = number // 100 - (number // 1000 * 10) # 1614 // 100 = 16 1614 // 1000 = 1 * 10 = 10     16 - 10 = 6
# third = (number % 100 - number % 10) / 10 # 1614 % 100 = 14 - 4 = 10 / 10 = 1
# last = number % 10   # 1614 % 10 = 4
# if first + last == second - third:
#     print('ДА')
    
# else:
#     print('НЕТ')
# print(second)

# Исправьте ошибки в коде, чтобы получить требуемый вывод.
# d1 = {"a": 100, "b": 200, "c":300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# print(d1["b"] == d2["b"])

# Выведите значение возраста из словаря person.

# person = {"name": "Kelly", "age":25, "city": "New york"}
# print(person(["age"]))

# Напишите код который добавит все элементы списка в множество
# set1 = {"Yellow", "Orange", "Black"}
# list1 = ["Blue", "Green", "Red"]
# set1.update(list1)
# print(set1)

# set2= set(sample_set)
# set3 = set(sample_list)
# print(set3)


# new_dict={}
# ind=0
# for key in set1: 
#     new_dict[key] = list1[ind]
#     ind +=1
# print(new_dict)

# Set №1
# set1= {6, 4, 2, 5, 7, 8, 10, 9}
# set1.remove('7')
# print(set1)


# Set №2
# set_1= {'Python', 'it', 'c++', 'java', 'programming'}

# Set №3
# set_2= {'html', 'css', 'c++', 'java', 'dart', 'programming'}
# print(set_1.intersection(set_2)) 
# print(set_1.difference(set_2))

# Dictionary 1
# menu = {'manty': 200, 'plov': 150, 'lagman': 130, 'borsh': 100}
# menu['besh_barmak'] = 130
# menu['lagman'] = 135
# menu.pop('borsh')
# menu.update({'drinks': ['Sprite', 'Fanta', 'Cola']})
# print(menu)

# set1 = set(set(dir(set)))
# set2 = set(dir(dict))
# # print(set1.intersection(set2))
# for i in set1.intersection(set2):
#     if i.startswith('__'):
#         continue
#     print(i)

# set1 = set()
# for num in range(10):
#     set1.add(int(input()))
# frozen = frozenset(set1)
# print(frozen)

# suitcase = []
# for i in range(5):
#     suitcase.append(input())
# suitcase.pop()
# print(suitcase)

# Set №4
# ferma1 = {'корова', 'курица', 'овца', 'заяц'}

# # Set №5
# ferma2 = {'корова', 'козел', 'собака', 'заяц'}
# print(ferma2.difference(ferma1))

stroka = input().split()
print(stroka)



# set_stroka = set(''.join(stroka))
# print(set_stroka) 
# print(len(set_stroka))
# for word in stroka: 
#     unic_word = set(word)
#     print(f'В слове{word}, уникальных {len(unic_word)} символов')
