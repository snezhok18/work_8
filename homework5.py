# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# a = int(input('Введите число, возводимое в степень: '))
# b = int(input('Введите число, степень: '))



# def func(a, b):
#     if b == 0:
#         return 1

#     return a * func(a, b - 1)


# print(func(a, b))


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))


# def sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return sum(a - 1, b + 1)


# print(sum(a, b))