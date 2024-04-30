
# n= int (input ('Enter your number:'))
# a = n // 1000
# b = n // 100 % 10
# c = n // 10 % 10
# d = n % 10
# if a + d == b -c:
#     print (' True ')


# n= int (input ('Enter your number:'))
# n1 = n // 1000 # 1614 // 1000 = 1
# n2 = n // 100 - (n // 1000 * 10) # 1614 // 100 = 16 
# #1614 // 1000 = 1 * 110 = 10   16 - 10 = 6 
# n3 = (n % 100 - n % 10) / 10 # 1614 % 100 = 14 - 4 = 10 / 10 = 1
# n4 = n % 10   # 1614 % 10 = 4


# number = int(input('Напишите любое число:'))
# num10 = number % 10
# num20 = number // 10
# if num10 == num20:
#     print('da')
# else:
#     print('net')

# a = 4
# b = 1
# c = 4

# if a == c == b: #но это не значит что а != c != b 
#     print('числа равны!э')
# if a != b and a !=c and c !=b: 
#     print('числа не равны!')

# password = input ('Введите пароль:')
# parol = input ('Повторите пароль:')
# if password == parol:
#     print ( ' Пароль принят!')
# else: 
#     print ('Пароль не принят!')

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# c = 0

# if num1 % 2 == 0:
#     c = c + 1
# if num2 % 2 == 0:
#     c = c + 1
# if num3 % 2 == 0:
#     c = c + 1 
# print(c)

# num1 = int (input('Enter number:'))
# if num1 % 2 == 0: 
#     print ('Четное число')
# if num1 %2 != 0: 
#     print ('Нечетное число')

#  Создайте 2 переменные со значениями 2**3 и 3**2 и покажите значение переменной в которой значение больше.

# a = 2 ** 3
# b = 3 ** 2
# if a > b:
#     print ('2 ** 3 больше')
# elif a < b: 
#     print ("3 ** 2 больше")

# У нас есть числа от 0 до 100, но не все числа разрешены! Разрешенённые: От 0 до 21 или От 57 до 100. Ввести число и выясните является ли число разрешенным
    
# n = int (input ('Enter your number from 0 to 100:'))
# if 0 <= n <= 21 or 57 <= n <= 100
#         print ('Разрешенные')
# else:
#      print ('Неразрешенные')

#Написать программу которая проверит число на несколько критериев: Чётное ли число? Делится ли число на 3 без остатка? Если возвести его в квадрат, больше ли оно 1000?

# n = int (input (' Enter your number:'))
# if n % 2 == 0: 
#    print (' Число четное')
# else:
#    print ('Нечетное число')

# if n % 3 == 0:
#    print (' Делится без отсатка')
# else:
#    print ( ' Не делиться без остатка')

# if n ** 2 > 100:
#    print (' Число в квадрате больше 1000')
# else: 
#    print (' Число в квадрате меньше 1000')

# if pow (n,2) >= 1000:
#    print (' true')
# else: 
#   print ('False')

# n1 = int (input ('1'))
# n2 = int (input ('2'))
# n3 = int (input ('3'))
# if n1 != n2 or n2 != n3 or n1 != n3 or n1 == n2 == n3:
#    print('true')

# number = input()
# if number or not number: 
#     print (' Sdelano')

#У вас есть переменная а=10//5 и b=10/5 Ровны ли переменные a и b? если они равны выведите их сумму. 
# a = 10 // 5
# b = 10 / 5
# if a == b:
#   print ('Сумма:', a + b)
# else:
#    print ('Неравны')

# # У вас есть переменные a = 10 и b = 5. Напишите условия которое проверяет, являются ли ваши переменные положительными числами (только один if)
# a = 10 
# b = 5
# if a > 0 and b > 0: 
#    print ('Обе переменные положительные числа')

#Для переменных из прошлого задания(6) напишите условие которые выясняет, a больше b, если это так, то выведите a+2 Иначе, b+2
# a = 10 
# b = 5
# if a > b: 
#    print (a + 2)
# else: 
#    print (b + 2)

#Запросить у пользователя ввести любое число и если это число больше 0 вывести сообщение "Положительное число", если меньше 0 вывести сообщение "Отрицательное число" иначе вывести само число.
# n = int (input ('Enter:'))
# if n > 0: 
#    print ('Положительное число')
# elif n < 0:
#    print ('Отрицательное число')
# else: 
#    print (n)

#Спросить у пользователя его возраст, если значение больше или равно 18 вывести сообщение "Совершеннолетний", если меньше или равно 4 вывести "Ребенок" иначе "Несовершеннолетий". Если значение меньше 0 и больше 120 вывести сообщение "Недопустимый возраст!" 

# age= int (input ('Your age:'))
# if age >= 18 and age <=119: 
#    print ('Совершеннолетний')
# elif age <= 4 and age >= 1: 
#    print ('Ребенок')
# elif age <= 0  or age >= 120: 
#    print ('Недопустимый возраст!')
# else: 
# #     print ('Несовершеннолетий')

#Создайте 2 переменные со значениями 45 и 6, проверить делится ли первое число на второе, если делится вывести соответствующее сообщение.
# a = 45
# b = 6
# if a % b == 0: 
#    print("Delitsya") 
# else: 
#    print ('Delitsya s ostatkom')

#Написать программу где надо ввести любой год и вывести сообщение "Текущий год" если это текущий год, если будущий год вывести "Год еще не наступил" иначе "Год прошел".
#Создайте условие которое определит самое большое и самое маленькое число из трёх.
# year = int (input ('Enter number:'))
# current_year = 2024
# if year > current_year: 
#    print ('Год еще не наступил')
# elif  current_year > year: 
#    print ('Год прошел')
# elif year == current_year:
#    print ('Текущий год') 

# num1 = int (input ('1'))
# num2 = int (input ('2'))
# num3 = int (input ('3'))
# if num1 > num2 and num1 > num3 and num2 < num3:
#     print('Cамое большое ', num1)
#     print('Самое мальнькое', num2)
# elif num1 > num2 and num1 > num3 and num2 > num3:
#     print('Cамое большое ', num1)
#     print('Самое мальнькое', num3)
# elif num2 > num1 and num2 > num3 and num1 < num3:
#     print('Cамое большое ', num2)
#     print('Самое мальнькое', num1)
# elif num2 > num1 and num2 > num3 and num1 > num3:
#     print('Cамое большое ', num2)
#     print('Самое мальнькое', num3)
# else:
#     if num1 < num2:
#         print('Cамое большое ', num3)
#         print('Самое маленькое', num1)
#     else:
#         print('Cамое большое ', num3)
#         print('Самое маленькое', num2)

# min_number = min (num1, num2, num3)
# max_number = max (num1, num2, num3)
# print('Самое наименьшее число', min_number)
# print('Самое наибольшее число', max_number)




#Есть три числа 17391, 546, 934. Если каждое из них поделить на 17 по модулю, где остаток меньше всего?
# num1 = 17391 % 17
# num2 = 546 % 17
# num3 = 934 % 17
# min_number = 'num1 'if num1 < num2 and num1 < num3 else 'num2' if num2 < num1 and num2 < num3 else 'num3'
# print (min_number)

# if a > b >c: 
#    print ('a')
# elif  b > a > c:
#    print ('b')
# elif c > b > a: 
#    print ('c')

# Есть переменная x = 13. Нужно возвести её в квадрат и сравнить с числом 172. Если x всё ещё меньше возвести в квадрат ещё раз.
# x = 13 
# x2 = x ** 2
# if x2 < 172:
#     x3 = x2 ** 2
#     print (x3)
# print (x2)

# Напишите код где где после ввода числа, на экран выводится делиться оно на 6 или нет.
 
# print ('Делится'if int(input ('Введите число:')) % 6 == 0 else 'Не делится')

#  Пользователь вводит три числа. Если все числа больше 10, то вывести на экран "yes", иначе "no"
# number1 = int (input (' Введите 1-число:'))
# number2 = int (input (' Введите 2-число:'))
# number3 = int (input (' Введите 3-число:'))
# if (number1 > 10, number2 > 10, number3 > 10):
#     print ('yes')
# else:
#     print ('No')

# Напишите код авторизации где юзер вводит логин и пароль. Если логин и пароль совпадают, то печатает: "Вы успешно вошли в систему" Если не совпадают то печатает: "Не правильно ввели логин или пароль"

# login = str(input ('Введите логин:'))
# password = str (input ('Введите пароль:')) 
# # print ('Вы успешно вошли в систему' if login == password else ' не правильно ввели логин или пароль')
# if login == 'admin' and password == 'admin':
#     print ('Вы успешно вошли в систему')
# else:
#     print ('Не правильно ввели логин и пароль')

# Напишите код программу, которая проверяет то, как вы умеете умножать в уме. Программа принимает два числа для умножения и число которое вы предполагаете равняется произведению этих чисел. Программа должна вывести на экран произведение этих чисел и является ли ваш ответ верным или нет.

# num1 = int (input ('Введите 1-ое число:'))
# num2 = int (input ('Введите 2-ое число:'))
# result = int (input (' Введите ваше предпологаемое произведение: '))
# res = num1 * num2
# print ('Произвеление чисел', num1, 'и', num2, 'равно', res)
# if res == result:
#     print ('Ващ ответ верный!')
# else:
#     print ('Ваш ответ не верный')
#     # comp = num1 * num2
# # guess = int (input ('Введите ваш ответ:'))

# print (' Ваш ответ правильный' if comp == guess else 'Вы продули')

# Напишите код который принимает число месяца, а выводит описание сезона. А в случае неверного ввода месяца выводить ошибку.

# В качестве описания событий будет характеристика сезона:
# month = int (input ('Введите номер месяца: (1-12)'))
# if month in (1, 2, 12):
#     print ('За окном падал белый снег')
# elif month in (3, 4, 5):
#     print ('Птицы пели прекрасные песни')
# elif month in (6, 7, 8):
#     print ('Солнце светило ярче чем когда-либо')
# elif month in (9, 10, 11):
#     print ('Урожай был невероятным')
# else:
#     print ('Такого месяца не существует')


# Для зимы: За окном падал белый снег
# Для весны: Птицы пели прекрасные песни
# Для лета: Солнце светило ярче чем когда-либо
# Для осени: Урожай был невероятным
# Для ошибка: Такого месяца не существует

# if number >= 112 and number<= 2902:
#     print ('Зима-За окном падал белый снег' )
# elif number >= 103 and number <= 3105: 
# #     print ( 'Весна- Птицы пели прекрасные песни')
# # elif number >= 106 and number <= 3108:
# #     print ('Лето- Солнце светило ярче чем когда-либо')
# # elif number >= 109 and number <= 3112: 
#     print ( 'Осень-Урожай был невероятным')

# number = int (input ('Введите число месяца в следующем порядке: число месяц (12.12- 12-декабря)'))
# zima = [zima for zima in range (0112, 0103)]
# vesna = [vesna for vesna in range (0103, 0106)]
# leto = [ leto for leto in range (0106, 0109)]
# osen = [osen for osen in range (0109, 0101)]
# if [number for number in range ( 01.12, 29.02)]:
#     print ('Зима- за окном падал белый снег')
# elif [number for number in range (01.03, 31.05)]:
#     print ( 'Весна- птицы пели прекрасные песни')
# elif [number for number in range (01.06, 31.08)]:
#     print ('Лето- солнце светило ярче чем когда-либо')
# elif [number for number in range (01.09, 31.12)]:
#     print ( 'Осень-урожай был невероятным')
# else: 
#     print ('Ошибка. Такого месяца не существует')


# # Если переменная a больше нуля и меньше 5-ти, то выведите 'Верно', иначе выведите 'Неверно'. Значение "a" ввести с терминала
# a = int (input ('Введите число:'))
# print ('Верно' if 0 < a < 5  else 'Неверно')

# # Если переменная a равна или меньше 1, а переменная b больше или равна 3, то выведите сумму этих переменных, иначе выведите их разность (результат вычитания). a и b ввести с терминала.

# a = int (input ('Введите число: '))
# b = int (input ('Введите число: '))
# if a <= 1 and b >=3:
#     print (a+b)
# else:
#     print (a-b)

# Если переменная a больше 2-х и меньше 11-ти, или переменная b больше или равна 6-ти и меньше 14-ти, то выведите 'Верно', в противном случае выведите 'Неверно'.

# a = int (input (' Введите число а:'))
# b = int (input ('Введите число b:'))
# if a > 2 and a < 11 and b >= 6 and b > 14:
#     print ('Верно') 
# else: 
#     print (' Неверно')

#  В переменной month(Ввод с терминала) лежит какое-то число из интервала от 1 до 12. Определите в какую пору года попадает этот месяц (зима, лето, весна, осень)

# month = int (input (' Введите число:'))
# if month in list ( 1, 2, 12):
#     print ('Зима')
# elif month in range ( 3, 6):
#     print (' Весна')
# elif month in range ( 6, 9):
#     print (' Лето')
# elif month in range ( 9, 12):
#     print (' Осень')


# В первом подъезде квартиры с 1 по 20. Во втором с 21 по 48. В третьем с 49 по 90. Пользователь вводит номер квартиры. Программа должна указать в каком подъезде находится данная квартира.

# num = int (input ('Введите номер квартиры:'))
# if num in range (1, 21):
#     print ('1-й подъезд')
# elif num in range ( 21, 49):
#     print (' 2-й подъезд')
# elif num in range (49, 91):
#     print ('3 -й подъезд')

# if 1 <= num <=20:
#     print ('1-й подъезд')
# elif 21 <= num <=48:
#     print (' 2-й подъезд')
# elif 49 <= num <= 90:
#     print ('3 -й подъезд')
# else:
#     print ('Такой квартиры нет в доме')
    



# Пользователь вводит порядковый номер пальца руки. Необходимо показать его название на экран.

# x = int (input ('номер пальца:'))
# if x == 1:
#     print ('Большой')
# elif x == 2: 
#     print ('Указательный')
# elif x == 3: 
#     print ('Средний')
# elif x == 4: 
#     print ('Безымянный')
# elif x == 5:
#     print ('Пальчик')
# else:
#     print ('Такого пальца нет')

# Программа принимает положительное число, проверить делится ли число на 2, 4 и на 6

# num = int (input ('Введите число:'))
# print ('Делится' if num % 2 == 0 and num % 4 ==0 and num % 6 ==0 else 'Не делится')

# Пользователь вводит углы треугольника, проверить является ли треугольник валидным.
# print("Стороны:")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
# if a + b + c ==180:
#     if a > 0 and b > 0 and c > 0:
#         print("Треугольник валидный")
#     else: 
#         print ("Треугольник не валидный")
# else: 
#     print ("Треугольник не валидный")

# if a + b > c and a + c > b and b + c > a:
#     print("Треугольник валидный")
# else:
#     print("Треугольник не валидный")

# if a + b > c:
#     if a + c > b:
#         if b + c > a:
#             print("Треугольник валидный")
#         else:
#             print("Треугольник не валидный")

# Найти корни квадратного уравнения ax^2+bx+c=0. Значения a, b и с ввести с терминала

# a = int (input ('a ='))
# b = int (input ('b ='))
# c = int (input ('c ='))
# D = b2 - 4ac
# Discr = b ** 2 - 4 * a * c
# print ((ax**2)+(bx)+c=0)

# Составить программу, определяющую результат гадания на ромашке — «любит—не любит», количество лепестков ввести с терминала.
# num = int (input ('Введите свое число:'))
# print ('Любит' if num % 2 == 0 else 'Не любит')

# Вывести на экран сообщение выбора операции:

# Введите 1 для конвертации Фаренгейта в Цельсий
# Введите 2 для конвертации Цельсии в Фарангейт
# В зависимости от выбора операции пользователем вывести соответсвующее сообщение для ввода значения, далее результат конвертации. 

# num = int (input ('Ввыбор операции: '))
# if num == 1:
#     print ('Конвертация Фаренгейта в Цельсий: ')
# a = int (input ('Введите число: '))
# print ((a - 32) / 1.8 ) 
# if num == 2: 
#     print ('конвертации Цельсии в Фарангейт: ')
# b = int (input ('Введите ваше число:'))
# print ((b*1.8+32))

# counter = 0
# while True:
#     word = input()
#     if word == 'стоп' or word == "хватит" or word == "достаточно":
#         break
#     if not word:
#         continue
#     counter += 1
#     print (counter)

# counter = 0
# while True:
#     word = input()
#     if word == 'стоп' or word == "хватит" or word == "достаточно":
#         break
#     if not word:
#         continue
#     counter +=1
# print(counter)

# numbers = [1, 10, 4, 5, 6]
# letters = ('a', 'b', 'c', 'd')

# list1 = [1, 2, 3, 'hello', [1, 2, 3], None, True]
# list1[1] #2
# list1[3] # hello
# list1[4] #
# list1[4][0] #1
# # print(list1[4])

# list2 = list('ada') # ['a', 'b', 'a']
# list3 = list(range(1,11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_sum= list2+list3 #['a', 'd', 'a', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list4= list2 * 4 #['a', 'd', 'a', 'a', 'd', 'a', 'a', 'd', 'a', 'a', 'd', 'a']

# list1 = [1, 2, 4, 11, 22,  333, -1,]
# list1.sort()
# list1.reverse()
# print(list1)


# numbers[-2] = -2
# # print(min(numbers))

# if 'a' in 'abc':
    # print ('Yes')

# print (dir(list))
# name= 'Marat'
# list1 = [- 123 ]
# list1.append(name)
# list1.append('ada')
# list1.append(2)
# list1.append(2/2)
# list1.append((1,2, 3,4))
# print(list1)

# list1 = [-123, 'Marat', 'ada', 2, 1, 1, 0, (1, 2, 3, 4)]
# pop_elemenent1 = list1.pop(1) #1

# list1.remove('ada')

# # print(list1.count(1))

# list3= 'helloworld'
# list4 = list('helloworld')
# # print(list3, list4)
# list1= list('helloworld')
# print (list1)
# list2= '-'.join(list1)
# print(list2)
# print(*list1)

# number= int(input())
# print(list(range(1,number+1)))

# Создать список из 5 вложенных кортежей.
# tuple_1 = (1, 2, 3, 4, 5)
# tuple_2 = ('spring',1,'summer',2, 'autumn', 'winter',3)
# tuple_3 = (1, 'hero', 22, 'coward', 33, 'normal')
# tuple_4 = ('senario', 101, 'action', 202, 'conclusion', 303)
# tuple_5 = ('never', 'say', 555, 'never', 606, 'again')

# list1 = [(), (), (), (),()]
# for i in list1:
#     print(type(i))

# # print(tuple_3.index('coward'))

# tuple_= (1, 2, 3)
# for i in range(3):
#     print(tuple_[i])


# list1 = []
# list1.append(str)
# list1.append(float)
# list1.append(int)
# list1.append(list)
# list1.append(tuple)
# print(list1)



# list1 = ['Elnura', 'Yabiga', 'Eliyana', 'Eldemar', 'Zuhra']
# print(''.join(list1))

# spisok_name = ['Yabiga', 'Eliyana', 'Eldemar', 'Zuhra']
# spisok_surname = ['Tashtemirova', 'Tashtemirova', 'Kydyeva', 'Toktasinova']
# spisok_name.extend(spisok_surname)
# print(spisok_name)
# spisok3= spisok_name+spisok_surname
# print(spisok3)

# list1 = [1, 2, 3, 4]
# list2 = [4, 5, 6, 7]
# list3 = [list2 + list1]
# print(list3)

# list = ['Sanjar', 'Tilek', 'Kalys', 'Eldar', 'Elina', 'Beka', 'Elzar', 'Bael', 'Atajan', 'Emir', 'Mamed', 'Beka']
# print(list.count('Beka'))

# list1 = list.remove('Elina')
# print(list)

# list123 = [] 
# list123.insert(0, 'Maratbek')
# list123.insert(1, '02.04.1985')
# list123.insert(2, 'Python')
# print(list123)

# # List №2
# l = ['integer', 'float', 'string', 'list', 'loop', 'tuple', 'while', 'for']
# index_ = l.index('loop')
# print(l.pop(index_))
# print(l)


# List №3
# import math 
# l = [1, 2, 5, 3]
# math.prod([l])
# print(l)


# l = [1, 2, 5, 3]
# l2 = l[0] * l[1] *l[2]*l[3]
# print(l2)

# count= 1
# l = [1, 2, 5, 3]
# for num in l:
#     count *= num
# print(count)

# Взять строку №1 создать два списка numbers и letters, пройтись по каждому элементу строки No1 и в numbers добавлять только числа, а в letters буквы.

# numbers = []
# letters = []
# s = 'Integers 1,2,3 Floats 44 Strings 5 Lists 10Tuples'
# for elm in s:
#     if elm.isalpha():
#         letters.append(elm)
#     elif elm.isdigit():
#         numbers.append(elm)
# print(numbers)
# print(''.join(letters))

# Дополните приведенный код так, чтобы он вывел среднее арифметическое элементов списка evens.
# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# srednee = sum(evens) / len(evens)
# print(srednee)


# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# change= rainbow.index('Green')
# print(change)
# rainbow[3] = ('Зеленый')
# print(rainbow)
# rainbow[rainbow.index('Green')]= 'Зеленый'
# rainbow[rainbow.index('Violet')] = 'Фиолетовый'
# print(rainbow)


# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# languages.reverse()
# print(languages)

# word = []
# num = int(input())
# for num in range(1, num+1):
#     word = input('Введите ваше слово:')
#     word.append(word)
# print(word)


# spisok= []
# n = int(input())
# for _ in range(n):
#     spisok.append(word)
# print(spisok)
             
# list1= [1,2,3,4]
# list2= [3, 4, 5, 6]
# set1 = set(list1)
# set2 = set(list2)
# print(list(set1.intersection(set2)))


# def count_letters(text, letters):
#     text =[]
#     for _ in text:
#         if text.islower('a'):
#             print(text.count(text))
#     for i in letters:
#         print(len(text))

# count_letters('asdfsdsdvdcaehagd', 'f')


'==============================Game==========================='

import random

def privetstvie():
    name = input('Привет! Как тебя зовут? ')
    otvet = input(f'{name} хочешь сыграть в камень-ножницы? (да\нет) ')
    if otvet == 'да':
        return (True, name)
    else:
        return (False, name)

def igra(name):
    play_list = ['камень', 'ножницы', 'бумага']
    c_ochko = 0
    g_ochko = 0
    while True:
        if g_ochko == 2 or c_ochko == 2:
            return g_ochko, c_ochko
        compt = random.choice(play_list)
        guess = (input(f'Твой выбор: камень/ножницы/бумага?, {name}'))
        if guess =='бумага' and compt == 'бумага':
           print('ничья')
        elif guess == 'бумага' and compt == 'ножницы':
            print(f'Ты проиграл!, {name}')
            c_ochko +=1
        elif guess == 'бумага' and compt == 'камень':
            print(f'Тебе 1 очко, {name}')
            g_ochko += 1
        elif guess == 'камень' and compt == 'камень':
            print('ничья')
        elif guess == 'камень' and compt =='бумага':
            print(f'Ты проиграл!,{name}')
            c_ochko +=1
        elif guess == 'камень' and compt == 'ножницы':
            print(f'Тебе очко, {name}')
            g_ochko += 1
        elif guess =='ножницы' and compt == 'ножницы':
            print('Ничья!')
        elif guess == 'ножницы' and compt == 'бумага':
            print(f'Тебе очко, {name}')
            g_ochko += 1
        elif guess == 'ножницы' and compt == 'камень':
            print(f'Ты проиграл, {name}')
            c_ochko += 1

def champ():
    while True:
        game, name = privetstvie()
        if not game:
            print('Poka')
            break
        g_ochko, c_ochko = igra(name)
        if c_ochko == 2:
            print(f'Ты профукал, {name}')
            break
        if g_ochko == 2:
            print (f'Ты выиграл, {name}')
            break

champ()
        
import random
def det_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    elif (player_choice == 'камень' and computer_choice == 'ножницы') or (player_choice == 'ножницы' and computer_choice == 'бумага') or (player_choice == 'бумага' and computer_choice == 'камень'):
        print("Победа в раунде за вами")
        return 1
    else:
        print("Победа в раунде за компьютером")
        return 2

def play_game():
    player = 0
    computer = 0
    while True:
        if player == 2 or computer == 2:
            if player == 2:
                print("Вы победили!")
                break
            else:
                print("Вы проиграли!")
                break
        player_choice = input("Выберите камень, ножницы или бумагу: ")
        choices = ['камень', 'ножницы', 'бумага']
        computer_choice = random.choice(choices)
        print(f"Ваш выбор: {player_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        result = det_winner(player_choice, computer_choice)
        if result:
            if result == 1:
                player += 1
            else:
                computer += 1
play_game()

    
