'==============================Множество(Set)============'
#Множество- это изменяемый, нупорядочный, итерируемый, неиндексируемый, предназначен для хранения уникальных значений (нельзя хранить изменямые типы данных), даже нельзя в tuple ([1, 2, 3,])

# set1 = {2,1, 3, 5,6, 'a', 'b', 'c'}
# print(set1)

# set1= {1,1, 1, 1,1 }
# print(set1)

set1 = {[1,2,3], {1,,1,}, {'a', :1}} # такие типы данных нельзя хранить
# set2 = {1,2,3, (1,2[1,2,3])} даже так


'==========================Методы множества=========================='
# set1 = {'a', 'b', 3, 4, 5}

# # add - добавляет элемент в множество
# set1.add(33)
# print(set1)

# # pop - удаляет случайный элемент из множество
# popped = set1.pop()
# print(popped)
# print(set1)

# # remove - удаляет элемент по значение из множества, если не найдет значение выводит ошибку keyerror
# set1.remove('a')
# # set1.remove('c')
# print(set1)

# difference - находит различия между множеством и другой колеекцией
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.difference(set2)) # {1, 2}
# print(set2.difference(set1)) # {4, 5}

# # symmetric_difference - находит только разные значения в множествах
# print(set1.symmetric_difference(set2)) # {1, 2, 4, 5}

# # intersection - выводит одинаковые значения коллекций
# print(set1.intersection(set2)) # {3}

'========================Множества(set)===================='
# # Множество - это изменяемый, неупорядочный, итерируемый, неиндексируемый, предназначен для хранения уникальных значений (нельзя хранить изменемые типы данных), даже нельзя в tuple([1,2,3])

# # set1 ={2,1,3,5,6, 'a', 'b', 'c'}
# # print(set1)
# # set1 = {1,1,1,1,1,1,1,1,1}
# # print(set1)

# # # set1 = {[1,2,3], {1,1,1}, {'a':1}} такие типы данных нельзя хранить
# # set2 = {1,2,3, (1,2,[1,2,3])} даже внутри tuple
# # print(set2)

# # set3 = {1,True,0, False}
# # print(set3)

# '==========================Методы множества=========================='
# set1 = {'a', 'b', 3, 4, 5}

# # add - добавляет элемент в множество
# set1.add(33)
# print(set1)

# # pop - удаляет случайный элемент из множество
# popped = set1.pop()
# print(popped)
# print(set1)

# # remove - удаляет элемент по значение из множества, если не найдет значение выводит ошибку keyerror
# set1.remove('a')
# # set1.remove('c')
# print(set1)

# difference - находит различия между множеством и другой коллекцией
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.difference(set2)) # {1, 2}
# print(set2.difference(set1)) # {4, 5}

# # symmetric_difference - находит только разные значения в множествах
# print(set1.symmetric_difference(set2)) # {1, 2, 4, 5}

# # intersection - выводит одинаковые значения коллекций
# print(set1.intersection(set2)) # {3}

'''
На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая создает из указанных строк список и выводит его.
n = int(input())
ada
courses
hello
Вывод:
['ada', 'courses', hello]
'''
# spisok = []
# n = int(input())
# for _ in range(n):
#     word = input('Напишите слово:')
#     spisok.append(word)
# print(spisok)

# ; На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список их кубов.
# ; n = 5
# ; 1
# ; 2
# ; 3
# ; 4
# ; 5
# ; Вывод: [1, 8, 27, 64, 125]

# n = int(input())
# s=[]
# for _ in range (n):
#     x = int (input ())
#     s.append(x**3)
# print(s)

# На вход программе подается натуральное число n. Напишите программу, которая создает список, состоящий из делителей введенного числа.

# num = int (input())
# spisok= []
# for i in range (1, num +1):
#     if num % i == 0:
#         spisok.append(i)
# print(spisok)


# alphabet = 'abcdefghijklmnoprqstuvwyz'
# step = int(input ('Введите число сдвига:'))
# stroka = input('Введите сообщение:')
# # bwfusvfupdbftbs
# new_stroka = ''
# for simvol in stroka: 
#     ind = alphabet.find(simvol)
#     new_simvol = alphabet[ind - step]
#     new_stroka += new_simvol
#     print(f'Изначальная буква: {simvol} и Расшифрованная: {new_simvol}')
# print(new_stroka)
    

# n = int (input('Введите число:'))
# numbers=[]
# for i in range (n):
#     num = int(input())
#     numbers.append(num)
# print(numbers)

# sum_num = []
# for i in range(n-1):
#     sum_element = numbers[i] + numbers [i+1]
#     sum_num.append(sum_element)
# print(sum_num)
