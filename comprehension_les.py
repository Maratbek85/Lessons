'=================================comperhensions================================='
# comperhensions - с помощью которого мы можем создавать последовательность используя цикл for в одну
# строку так же использую if else 
# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр
# результат if условие else тело for элемент in последовательность
# результат if условие else тело for элемент in последовательность if фильтр
# comperhensions_ = (num for num in range(1, 6))
# print(list(comperhensions_))
# Генератор - это итерируемый обьект, который не хранит в себе полностью всю последовательность данных, а создает
# их когда требуется
# print(next(comperhensions_))
# print(next(comperhensions_))
# print(next(comperhensions_))
# print(next(comperhensions_))
# print(next(comperhensions_))
# next - функция которая запрашивает у генератора текущий элемент и 
# генератор создает ссылку на следующий элемент

'=============================Синтаксический сахар============================'
'list comprehensions'
# list_comp = [i**2 for i in range(1, 6)]
# list_comp2 = [i**2 for i in range(1, 11) if i % 2 ==0]
# print(list_comp2)
# new_list = [1, 'hello', 2, 'string', True, False]
# new = [i for i in new_list if type(i)==str or type(i)==int]
# print(new)

'============================Dict comprehension================================='
# dict_ = dict((i, i *2) for i in range(10))
# print(dict_)
# dict2 = {'a': [1,2,3,4,5,6,7], 'b': [1,2,3,4], 'c': [2,3,4,5,6]}
# new = {key: sum(value) for key, value in dict2.items()}
# print(new)

# example = ['Helloworld' for i in range(5)]
# print(example)

'============================Set comprehension================================='
# set_ = {1,2,3,4,5,10}
# set_1 = {i for i in set_ if i%2 !=0}
# print(set_1)
'============================вложенные comprehension==========================='
# dict_ = {v: [i for i in range(1, v+1)] for v in range(1,6)}
# print(dict_)

# exmaple = [['helloworld'for i in range (5)] for i in range (3)]
# print(exmaple)

'============================random========================================='
import random
a = random.randint(0,10)
b = random.randrange(0,10,2)
print(a)
print(type(b))
again = 'yes'
while again.lower() == 'yes':
    print('brosaem kubiki....')
    print('znachenie granei')
    print(random.randint(1,6))
    print(random.randint(1,6))
    again = input("brosit' kubiki ewe raz? yes or no")