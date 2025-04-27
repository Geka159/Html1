# # Задание 1
# # Пользователь вводит с клавиатуры три числа.
# # В зависимости от выбора пользователя программа выводит
# # на экран сумму трёх чисел или произведение трёх чисел.
#
# value1 = int(input("Введите число 1: "))
# value2 = int(input("Введите число 2: "))
# value3 = int(input("Введите число 3: "))
# summ3 = value1 + value2 + value3
# proz3 = value1 * value2 * value3
# userchoise = int(input("Выберите 1 или 2: "))
# if userchoise == 1:
#     print ('summ:', summ3 )
# else:
#     print ('proz:', proz3 )
#
# # Задание 2
# # Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# # на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.
# value1 = int(input("Введите число 1: "))
# value2 = int(input("Введите число 2: "))
# value3 = int(input("Введите число 3: "))
# maks = max(value1, value2, value3)
# mins = min(value1, value2, value3)
# sr = (value1 + value2 + value3) /3
# userchoise = int(input("Выберите 1, 2 или 3: "))
# if userchoise == 1:
#     print ('maks', maks)
# if userchoise == 2:
#     print('mins', mins)
# if userchoise == 3:
#     print ('sr', sr)

# Задание 3
# Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа
# переводит метры в мили, дюймы или ярды.

value = int(input("Введите количество метров: "))
userchoise = int(input("Выберите 1, 2 или 3: "))
if userchoise == 1:
    print (1609.34*value)
if userchoise == 2:
    print (39.3701*value)
if userchoise == 3:
    print (1.09361*value)





