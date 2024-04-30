# 1)Спросите у пользователя 5 чисел добавьте их в SET и  скажите какое самое маленькое число он ввел.
# def number_():
#     set1= min({int(value) for value in input().split()})
#     return set1
# print(number_())


# 2) Вы работаете в Банке и пишите программу которая считает % для кредита. Спросите у пользователя сумму займа(не меньше 100 000) и посчитайте сколько нужно будет вернуть если процент = 7.89, результат округлите до 2 чисел после точки.
# Формула подсчёта переплаты: Сумма * (% / 100)

# def prosent():
#     kredit= int(input())
#     if kredit >= 100000:
#         print(round(kredit * (7.89 / 100),2))
#     else:
#         print('Введите сумму не меньше 10_000')
# prosent()

# 3) Запросите у пользователя ввести текст с цифрами, найти цифры и преобразовать их в целое число и вывести на экран.

# def text_():
#     text1 = input('введите текст с сифрами:')
#     text2 = []
#     for i in text1:
#         if i.isdigit():
#             text2.append(int(i))
#     print(text2)
# text_()

# variantb
# def find_numbers():
#     text = input()
#     numbers = ''.join([i for i in text if i.isdigit()])
#     if numbers:
#         print(int(numbers))
#     else:
#         print('Цифры не было')
# find_numbers()

# 4) Создайте  функцию, которая выполняет следующее действие:
# Пользователь вводит количество месяцев и лет. Вывести на экран количество дней за это время. Считать, что в каждом месяце 30 дней;

# def day_count():
#     month_= int(input())
#     year_ = int(input()) 
#     print(f'количество дней веленных лет и дней равно: {month_* 30 + year_*365} дней')
# day_count()

# 5) Создайте функция, которая возвращает словарь, где  ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб. 

# def slovar():
#     dict1 = {}
#     for i in range(1,11):
#           dict1[i] = i ** 3
#     return dict1
# print(slovar())

# def slovar():
#     dict1 = {i :i **3 for i in range (1, 11)}
#     # for i in range(1,11):
#     #       dict1[i] = i ** 3
#     return dict1
# print(slovar())


# 6)Написать функцию, которая высчитывает сумму чисел от 1 до 50 и возвращает результат. 

# def count_():
#     totals= sum(range(1, 51))
#     return totals()                
# count()

# def num_count():
#     list = [n for n in range (1, 51)]
#     print(sum(list))
#     return list
# num_count()

'''
ТЗ “Угадай число”

Напишите мини-проект “Угадай число”. Для
этого, вам понадобиться стандартный
ввод/вывод данных, тип данных числа и
условные операторы. Также не забудьте
использовать библиотеку random.
Требования:
1. Ваша программа должна запрашивать
имя пользователя. Программа должна
запросить у пользователя хочет ли он
играть или нет. Если ответ будет ‘нет’, то
программа должна завершиться.
2. Далее пользователь должен угадать
число. Также вы должны сделать счетчик
попыток, и показать пользователю сколько
попыток ему потребовалось, чтобы отгадать
число.
3. Если пользователь угадал число,
запросить у него хочет ли он пройти игру
еще раз, если ответ будет “нет”, программа
должна завершиться'''

import random
name = input('Привет! Как тебя зовут?: ') 
print ('Отлично', name,  'отгадай число между 1 и 30. Будешь играть? Если да,то продолжим!') 
otvet = input('Твой ответ?:')
while otvet == 'да':
    number = random.randint(1, 30) 
    print('Отлично, продолжим!')
    guesses = 0  
    while guesses < 4:
        guess = int(input('Введи число: ')) 
        guesses += 1 
        if guess < number:
            print ('Твое число меньше моего,', name, ",Еще попытка?")

        if guess > number:
           print ('Твое число больше моего,', name, ",Еще попытка?")
        if guess == number:
            break
    if guess == number:
        print ('Вау! Ты везунчик. Ты угадал с', (guesses), 'попыток!!!')
        break
    else:
        print ('Ты не угадал,', name, ' Я загадал число',( number))
        idem_dalwe = input('Еще играем?:')
        if idem_dalwe == 'да':
            continue
        else: 
            break 
if otvet == 'нет':
    print("Хорошо", name, "Увидимся")
else:
    print('Не понял твой ответ, попробуй еще раз')


from random import randint

def game():
    start = input("Начать игру?(да/нет)     ")
    attempts = 0
    while start == "да":
        attempts += 1
        num = int(input("Загадай число от 1 до 5   "))
        if num == randint(1, 6):
            print(f"Угадал, количество попыток:{attempts}")
            cont = input("Хотите продолжить?(да/нет)    ")
            if cont == "да":
                attempts = 0
                continue
            else:
                break
        else:
            print("Не угадал")
            cont = input("Хотите продолжить?(да/нет)    ")
            if cont == "да":
                continue
            else:
                break
print(game())

# 1) Все задания из предыдущей темы выполнить с помощью функции с аргументами.




# 2) Создайте функцию которая  берёт лист делит его пополам и обе стороны разворачивает в противоположную сторону. Пример: Оригинальный Лист:
# Оригинальный Лист:
#      list_1 = ['python', 'Django', '3.11', '4']
# Изменённый Лист:
#      list_1 = ['Django', 'python', '4', '3.11']


# def perevernem():
#     list_1 = ['python', 'Django', '3.11', '4']
#     list_1.pop(-2)
#     list_1.pop(-1)
#     list_1.reverse()
#     list_1.append('4')
#     list_1.append('3.11')
#     return list_1
# print(perevernem())

# def razdelenie():
#     list_= ['python', 'Django', '3.11', '4']
# # list_.reverse()
#     list2 = list_[1], list_[0], list_[3], list_[2]
#     print(list_,list2)
     
# razdelenie()

# def new_func(firth):
#     middle_index = len(firth) // 2
#     list1 = firth[:middle_index]
#     list2 = firth[middle_index:]
#     list1_reversed = list1[::-1]
#     list2_reversed = list2[::-1]
#     list3 = list1_reversed + list2_reversed
#     return list3


# list_1 = ['python', 'Django', '3.11', '4']
# change_list = new_func(list_1)
# print(change_list)

# def new_func(firth):
#     middle_index = len(firth)//2
#     firth[:middle_index] = reversed([firth[:middle_index]])
#     firth[middle_index:] = reversed(firth[middle_index:])
#     return firth


# list_1 = ['python', 'Django', '3.11', '4']
# change_list = new_func(list_1)
# print(change_list)

# 3)Создайте функцию gen_number() которая генерирует телефонный номер с кодом 0888 _ _ _ _ _ _. Номера которые вы можете генерировать могут содержать в себе только числа 5, 6, 8, 0, 3, 4. Пример: 0444506345

# import random
# def gen_number(num):     
#     for k in range(num):
#         numbers = []  
#         for i in range(9):     
#             j = random.randint(0, 9)        
#             numbers.append(j)       
#     return numbers
# # print(gen_number())
 

# def gen_number(kod):
#     import random
#     string_ = ''
#     numbers2 = 5, 6, 8, 0, 3, 4
#     for i in range(6):
#         gen_number = str(random.choice(numbers2))
#         string_ += gen_number
#         finish = kod + string_
#     return finish


# numbers = ('0888')
# full_numbers = (gen_number(numbers))
# print(full_numbers)

# 4) Создайте 4 функции: add(), substract(), multiply(), divide() которые будут принимать по 2 аргумента и возвращать результат: сложения, вычитания, умножения и деления.

# def math_solution(num1, num2):
#         print(num1 + num2)
#         print(num1 - num2)
#         print(num1 * num2)
#         print(num1 / num2)
# math_solution(num1=int(input('Первое число:')), num2 =int(input('Второе число:')))

# def add(a, b):
#     return a + b
# def substract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     if b == 0:
#         print("na nol' delit' nel'zya")
#     else:
#          return a / b


# numbers = 2, 3
# rewenie = add(*numbers)
# rewenie2 = substract(4, 6)
# rewenie3 = multiply(*numbers)
# rewenie4 = divide(*numbers)
# print(add(*numbers))
# print(substract(4, 5))
# print(multiply(numbers))
# print(divide(numbers))

# 5) Написать Функцию которая принимает предложение как аргумент, считает количество букв и возвращает сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ функцию len()

# def text_count(text):
#     simvol = 0
#     for i in text:
#         if i != '':
#             simvol +=1
#     return simvol

# print(text_count(text =input('Введите ваш текст:')))