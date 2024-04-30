'===========================Циклы============================='
# Циклы - это блок кода, который отрабатывает несколько раз
# 1. For - цикл, который работает до конца итерируемого обьекта
# 2. While - цикл, который работает пока условие истина (True)

# "FOR"
# stroka = 'hello world'
# for i in stroka:
#     print(i)

# list_ = [1, 2, 3 , 4, 5]
# for i in list_:
#     print(i)

# range - диапазон числе range(start, end, step)
# for i in range(1,11):
#     print(i)


# text = """Пробелы - самый предпочтительный метод отступов.
# # Табуляция должна использова2ться только для поддержки кода, написанного с отступами с помощью табуляции.
# # Python 3 запрещает смешивание табуляции и пробелов в отступах.
# # Python 2 пытается преобразовать табуляцию в пробелы."""

# text1 = text.replace('.', '').replace(',', '')
# text2 = text1.split()
# counter = 0
# for word in text2:
#     if word.isalpha() and len(word) > 3:
#         counter += 1

# print(f'Слов в нашем тексте: {counter}')

#WHILE

# count = 1
# while count<=10:
#     print('hello world')
#     count +=1
# print(1)
# text = print(f'Введите какой-либо текст, если хотите закончить введите выход: ')
# active = True
# while active:
#     message = input()
#     if message == 'выход':
#         active = False
#     else:
#         print(message)

'============================Breake and continue======================='
# breake - оператор, который остнавливает цикл(выходит из цикла)
# continue - оператор, который переходит к следующей итерации

# for i in range(1, 10):
#     print(i)
#     if i ==3:
#         break
# for i in range(10):
#     if i==3:
#         continue
#     print(i)

# for i in range (1, 21):
#     if i % 2 > 0:
#         print (i)

# counter = 1
# while counter:
#     if counter == 11:
#         break
#     print (counter)
#     counter +=1

# for i in range (1,11):
#     print(i)

# counter = 1
# while counter: 
#     if counter == 21:
#         break
#     if counter % 2 == 0:
#         print (counter)

# for i in range (1, 21):
#     if i % 2 == 0:
#         print (i)

# for i in range(0, 21, 2):
#     if i == 0:
#         continue
#     print (i)

# for i in range (1, 101):
#     if i % 3 == 0:
#         print (f'Само число: {i}\nРезультат деления на 3:{i/3}')

# counter = 1
# while counter:
#     if counter == 101:
#         break
#     if counter % 3 == 0:
#         print (counter, counter/3)
#     counter +=1

# for i in range (1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print (f'Само число: {i}')

# counter = 1
# while counter:
#     if counter == 101:
#         break
#     if counter % 3 == 0 and counter % 5 == 0:
#         print (counter)
#     counter +=1

# for i in range (1, 101):
#     if i % 2 == 0 and i % 3 == 0 and i % 9 ==0:
#         print (f'Само число: {i}')

# counter = 1
# while counter:
#     if counter == 301 and counter == 237:
#         break
#     if counter % 2 == 0:
#         print (counter)
#     counter +=1

# for i in range (1, 301):
#     if i == 301:
#         break
#     if i % 2 == 0:
        # print (i)

# counter = 1
# while counter:
#     if counter == 101:
#         break
#     if counter % 2 == 0 and counter % 3 == 0 and counter % 9 ==0:
#         print (counter)
#     counter +=1

# my_string = "Ботнет IPStorm, в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем" 
# for number in my_string: 
#     if number.isdigit():
#         print(int(number)*2)

# my_string = "20210419-2021071914424/..H/][[102e//==::'/:13-=---1234l][23-13lo31w323'/.,,o32r;;ld"
# for bukva in my_string: 
#     if bukva.isalpha():
#         print (bukva, end = '')

# for i in range (5, 0, -1):
    # print (i)

# counter = 5
# while counter > 0:
#     print (counter)
#     counter -= 1

# for i in range (1, 51):
#     num = i **2
#     if num < 50:
#         print (i, num)

# summa_number = 0
# for i in range (1, 31):
#     print (f'{summa_number}, мы прибавляем {i}')
#     summa_number += i 
# print (summa_number)

'==================================Вложенные циклы======================='
# Вложенный цикл расположен еще в одном цикле, т.е внутри тело другого цикла

# import time
# for hours in range(24):
#     for minutes in range (60):
#         for seconds in range(60):
#             print (f'{hours}:{minutes}:{seconds}')
#             time.sleep(1)

# Вложенный цикл выполняет все свои итерации для каждой отдельной итерации внешнего цикла
# Вложенные циклы завершают свои итерации быстрее, чем внешние циклы
# print (24 * 60 * 60)

# for i in range(8):
#     for j in range(i+1):
#         print ('*', end = '')
#     print()

# n = int(input())
# for i in range(1, n):
#     for j in range (1,4):  
#         print(n, end=' ')  
#     print() 
# for i in range (n):
#     print (n, n, n)

n = int(input())
# for i in range(1, n, n):
#     for j in range (sum(i+1)):  
#         print(i, end=' ')  


# for i in range (1, n+1):
#     print ((str(i)+ ' ')* n)

# n = int(input())
# for i in range (1, n+1):
#     for j in range (1, 10):
#         print (f'{i} + {j} = {i+j}' )
#     print () 

# n = int(input ())
# m = int(input ())
# if n < m:
#     for i in range (n, m +1):
#         print (i)
# else:
#     for i in range (n, m -1, -1):
#         print (i)

# n = int(input ())
# m = int(input ())
# if n < m:
#     for i in range (n, m+1):
#         if i % 17 == 0 or str(i).endswith('9') or (i % 3 == 0 and i %5 == 0):
#             print(i)

# n = int(input ())
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break

# n = int(input ())
# print(next(i for i in range(2, n + 1) if n % i == 0))

'''На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» (без кавычек). При этом само слово «КОНЕЦ» не входит в последовательность, лишь символизируя её окончание. Напишите программу, которая выводит члены данной последовательности.
Формат входных данных
На вход программе подается последовательность слов, каждое слово на отдельной строке.
Формат выходных данных
Программа должна вывести члены данной последовательности.'''
