# # Дан список чисел. Определите, сколько в нем встречается различных чисел.
# lst = [2, 3, 3, 3, 2, 1, 43, 5, 2, 6]
# print(len(set(lst)))
# # Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
# lst1 = [1, 2, 3, 4]
# lst2 = [3, 4, 5, 6]
# print(len(set(lst1) & set(lst2)))
# # Даны два списка чисел. Найдите все числа, которые не содержатся одновременно в этих двух списках.
# lst1 = [1, 2, 3, 4]
# lst2 = [3, 4, 5, 6]
# print(set(lst1) ^ set(lst2))
# # Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке),
# # если это число ранее встречалось в последовательности или NO, если не встречалось.
# s = set()
# for elem in input().split():
#     if elem in s:
#         print('YES')
#         s.add(elem)
#     else:
#         print('NO')
#         s.add(elem)
# # В ходе исследований ученые делают некие замеры, результаты которых заносят в базу данных.
# # Однако для анализа результатов нет необходимости держать в базе "лишние", повторяющиеся данные.
# # Напишите программу, которая выводит максимальное количество записей, после удаления которых анализ результатов будет
# # произведен верно. Список элементов вводится через пробел.
# # Sample Input:
# # 6311 9423 142 142 8654 909 Error 6311 142 909 404 502 828 404 9423
# # Sample Output:
# # 6
# notes = input().split()
# print(len(notes) - len(set(notes)))
# # В первой строке задано n - максимальное число, которое мог загадать Август. Далее каждая строка содержит вопрос Беатрисы
# # (множество чисел, разделенных пробелом) и ответ Августа на этот вопрос. Вы должны вывести через пробел, в порядке возрастания,
# # все числа, которые мог задумать Август.
# # Sample Input:
# # 20
# # Enter guess: 1 2 3 4
# # Enter guess: 5 9 20 11
# # Enter guess: 12 15 10 17 13
# # Enter guess: 10 17
# # Enter guess: 13
# # Sample Output:
# # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# # NO: 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# # NO: 6 7 8 10 12 13 14 15 16 17 18 19
# # YES: 10 12 13 15 17
# # NO: 12 13 15
# # YES: 13 is correct. You answered on the 5th try.
# number = {13}
# count = 0
# set1 = {num for num in range(1, int(input('Введите максимальное число, которое мог загадать Август: ')) + 1)}
# print(*set1)
# while True:
#     s = set(map(int,input('Enter guess: ').split()))
#     if s == number:
#         count += 1
#         print(f'YES: {number} is correct. You answered on the {count}th try.')
#         break
#     if s.issuperset(number):
#         count += 1
#         set1 &= s
#         print('YES:', end=' ')
#         print(*sorted(set1))
#     else:
#         count += 1
#         set1 -= s
#         print('NO:', end=' ')
#         print(*sorted(set1))

