# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А
# в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('Введите число a '))
b = int(input('Введите число b '))
def powerr(m,n):
    if n==0:
        return 1
    else:
        return m*powerr(m,n-1)
print(f'{a} в степени {b} равна {powerr(a,b)}')



# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

a = int(input('Введите число a '))
b = int(input('Введите число b '))
def summ(m,n):
    if n!=0:
        m=summ(m+1,n-1)
    return m
print(f'Сумма чисел {a} и {b} равна {summ(a,b)}')
