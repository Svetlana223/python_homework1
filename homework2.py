# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

# count_1 = 0
# count_0 = 0
# number_coins = int(input('Введите количество монет: '))
# for _ in range(number_coins):
#     side_coins = int(input('Введите стророну где 1 это решка, 0 это орел: '))
#     if 0 < side_coins > 1:
#         print('error')
#         break
#     elif side_coins == 0:
#         count_0 += 1
#     elif side_coins == 1:
#         count_1 +=1
# if count_1 >= count_0:
#     print(f'Переверните {count_0} орла')
# else:
#     print(f'Переверните {count_1} решки')
    


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3
# s = int(input('Введите сумму 2-х загаданных чисел: '))
# p = int(input('Введите произведение 2-х загаданных чисел: '))
# for i in range(0,s):
#     for j in range(0,p):
#         if i * j == p:
#             if i + j == s:
#                 print(i, j)
#             else:
#                 print('error')



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
# пользователь будет вводить каждое число на новой строке для задач 10, 12.
# n = int(input('Введите число N: '))
# i = 1
# while i < n:
#     print(i, end=' ')
#     i *= 2

