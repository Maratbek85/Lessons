'========================двумерные списки=============='
matrix = [['django', 'python', 'js'], 
          [   1,      2,        3],
          ['Beka', 'Almaz', 'Alisher']]         

# n = 3
# m = 4
# array = []
# i = 0
# while i < n:
#     array.append([])
#     j = 0
#     while j < m:
#         array[i].append(0)
#         j +=1
#     i += 1
# print(array)

# n = 3
# m = 4
# array = []
# for i in range(n):
#     array.append([1])
#     for j in range(m):
#         array[i].append(1)
# print(array)

# n = 3
# m = 5
# array = list(range(n))
# print(array)
# for i in range(n):
#     array[i] = list(range(1, m+1))
# print(array)

# array = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
# n = len(array)
# m = len(array[0])
# i = 0
# while i < n:
#     j = 0
#     while j < m:
#         print(array[i][j], end= ' ')
#         j += 1
#     print()
#     i += 1

# array = [[1, 2, 3, 4, 5], 
#          [1, 2, 3, 4, 5], 
#          [1, 2, 3, 4, 5]]
# n = len(array)
# m = len(array[0])
# for i in range(n):
#     for j in range(m):
#         print(array[i][j], end = ' ')
#     print()

# n = 3
# m = 3
# array = list(range(n))
# for i in range(n):
#     array[i]= list(range(m))
#     for j in range(m):
#         text = f'Введите элемент в {i}x{j} позицию:'
#         el = input(text)
#         array[i][j]= el
# print(array)

# n = int(input())
# x = [[i*1 for i in range(n)] for j in range (n)]
# for i in range(n):
#     for j in range(n):
#         print(x[i][j], end= ' ')
#     print()



# n = 3
# m = 4
# array = []
# for i in range(n):
#     array.append([0])
#     for j in range(m):
#         array[i].append(0)
# print(array)

# Создайте двумерный список размера 3x4 с помощью вложенных циклов заполните единицами

# n = 3
# m = 4
# array =[]
# i = 0
# while i < 3:
#       array.append([])
#       j = 0
#       while j < m:
#             array[i].append(1)
#             j +=1
#       i += 1
# print(array)

# for i in range (n):
#     array.append([])
#     for j in range(m):
#         array[i].append(1)
# print(array)


# Создайте двумерный список размера 3x3 с помощью вложенных циклов заполните числами от 1 до 9.

# n = 3
# m = 3
# for i in range(n): # n = rows
#         for j in range(1,m+1): # m= columns 
#             print((m * i) + j, end= ' ')
#         print()

# Запросите у пользователя элементы двумерного списка размера 2x3 и выведите матрицу(красиво).
# n, m = int(input()), int(input())
# array=[]
# for i in range(n):
#     array.append([])
#     for j in range(m):
#         array[i].append('красиво')
# print(array)
'==========================Comprehensions========='
# Comprehensions - с помощью которого мы можем создать последовальность использую цикл for в одну строку, такжу использую if else 
# Результат for элемент in последовательность
# Результат for элемент in последовательност if фильтр
# Результат if условие else тело for элемент in последовательность 
# Результат if условие else тело for элемент in последовательность if фильтр

# comprehensions = (i for i in range(1, 6))
# print(comprehensions)


# Генератор - это итерируемый обьект, который не хранит себе полнсотью всю последовательность данных, а создает их когда требуется 
# print(next(comprehensions))
# print(next(comprehensions))
# print(next(comprehensions))
# print(next(comprehensions))
# print(next(comprehensions))
# print(next(comprehensions))# StopIterationn
# next- функция, которая запрашивает у генератора текущий элемент и генератор создает ссылку на следующий элемент

'===========================Синтаксический сахар============'
# list_comp = [i ** 2 for i in range(1, 6)]
# print(list_comp)
# list_comp1 = [i**2 for i in range(1, 11) if i % 2 == 0]
# print(list_comp1)
# list_comp2 = ['Это число четное' + str(i), i for  i in range (1, 6), if i %2 ==0]
# new_list =[1, 'hello', 2, 'string', True, False]
# new = [i for i in new_list if type(i) == str]
# print(new)

'===========================Dict comprehension==========='
# dict_= dict(((i, i * 2) for i in range(10)))
# print(dict_)
# dict_ = {'a': [1,2,3,4,5,11], 'b': [1,2,3,], 'c': [2,3,4,5]}
# new = {key: sum(value) for key, value in dict_.items()}
# print(new)
# example = ['Helloworld' for i in range(5)]
# print(example)

'=====================Set Comprehension=================='
# set_= {1,2,3,4,5,1}
# set_1 = {i for i in set_ if i % 2 != 0}
# print(set_1)
# '=====================Вложенные comprehension============'
# dict_= {v: [i for i in range (1, v+1)] for v in range (1, 6)}
# print(dict_)
# example= [['helloworld' for i in range(5)] for i in range(3)]
# print(example)

'==========================Random=============='
# import random
# a = random.randint(0, 10)
# b = random.randrange(0,10,2)
# print(a)
# print(type(b))

# again= 'yes'
# while again.lower() == 'yes':
#     print("Бросаем кубики......")
#     print("Значеие граней......")
#     print(random.randint(1 ,6))
#     print(random.randint(1 ,6))
#     again = input("Бросить кубики еще раз? yes or no")

