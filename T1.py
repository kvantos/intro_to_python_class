#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from random import randrange as rndrange


def print_result(funct_name):
    print("-----[%s]-----" % funct_name.__name__)
    funct_name()
    print("==============")
    print("")

    
def pp_matrix(mx):
    for i in mx:
        for j in i:
            print(j, end="\t")

        print("")


def transpose_matrix(mx):
    
    transpose_matrix = []

    for j in range(len(mx[0])):
        line = []
        for i in range(len(mx)):
            line.append(mx[i][j])
        
        transpose_matrix.append(line)

    return transpose_matrix


def solution123(a=1, b=2, c=3):
    """
    1. (a + b*c)^2
    2. a - 4*b/c
    3. (a*b + 4)/(c - 1)
    """
    print("(a + b*c)^2 =", (a + b*c)**2)
    print("a - 4*b/c =", a - 4*b/c)
    print("(a*b + 4)/(c - 1) =", (a*b + 4)/(c - 1))


print_result(solution123)


def solution4():
    """
    4. Найти произведение нечетных цифр пятизначного
    целого числа, введенного пользователем с клавиатуры
    """

    print("Hello, please input 5-digit number.")
    number = input("type number: ")

    if len(number) != 5:
        print("Hey, fellow, number should contain 5 digits")
        return None

    product = 1
    for n in number:
        n = int(n)
        if n % 2:
            product *= n

    print("Product of all odd numbers: ", product)


print_result(solution4)
    

def solution5():
    """
    5. Создать программу, выводящую на экран ближайшее к 10
    из двух чисел, введенных пользователем. Например, среди
    чисел 8,5 и 11,45 ближайшее к десяти 11,45.
    """
    print("Hello, please input two numbers separated by space.")
    print("Numbers should not be equal size and 10")
    x1 = float(input("type first number: "))
    x2 = float(input("type second number: "))

    if x1 == x2 or x1 == 10 or x2 == 10:
        print("Man, I told you, not equal size or equal 10")
        return None
    
    a1 = abs(10 - x1)
    a2 = abs(10 - x2)

    if a1 < a2:
        print("Number %.2f is closer to 10" % x1)
    else:
        print("Number %.2f is closer to 10" % x2)


print_result(solution5)

    
def solution6(n=100):
    """
    6. Создать список из 10 любых простых чисел, записанных в
    случайном порядке.
    """
    
    prime_numbers = list(range(2, n+1))

    sqn = math.sqrt(n)
    p = 2
    j = 1
    
    while p < sqn:
        for i in range(j, len(prime_numbers))[::-1]:
            if prime_numbers[i] % p == 0:
                del prime_numbers[i]
                
        p = prime_numbers[j]
        j += 1

    random_primes = [prime_numbers[rndrange(len(prime_numbers))] for i in range(10)]
    
    print(random_primes)


print_result(solution6)


def solution7():
    """
    7. Найти сумму десяти первых чисел ряда Фибоначчи.
    """
        
    fn_list = [0, 1]
    n = 0
    while len(fn_list) < 10:
        fn = fn_list[n+1] + fn_list[n]
        fn_list.append(fn)
        n += 1

    print(sum(fn_list))


print_result(solution7)


def solution8():
    """
    8. В одномерном массиве поменять местами минимальный
    и максимальный элементы. Остальные оставить на своих местах.
    """

    one_set = [rndrange(100) for i in range(10)]
    print(one_set)
    
    max_digit = max(one_set)
    min_digit = min(one_set)
    max_pos = one_set.index(max_digit)
    min_pos = one_set.index(min_digit)

    one_set[max_pos] = min_digit
    one_set[min_pos] = max_digit

    print(one_set)

    
print_result(solution8)


def solution9():
    """
    9. Нормировать одномерный массив случайных чисел. Нормирование
    означает приведение всех значений массива к интервалу [-1;1],
    причем максимальное абсолютное значение элементов после нормирование
    должно быть равно 1. Например, последовательность {-5, 3, 4}
    после нормирование будет выглядеть {-1, 0.6, 0.8}
    """

    rnd_set = [rndrange(-42, 42) for i in range(10)]
    rnd_set.sort()
    x_max = max([abs(i) for i in rnd_set])

    norm_set = [i/x_max for i in rnd_set]
    norm_set.sort()
    print(rnd_set)
    print(norm_set)


print_result(solution9)


def solution10():
    """
    10. Вывести на экран матрицу, транспонированную заданной (3*8)
    """

    matrix = []
    for i in range(3):
        line = []
        for j in range(8):
            rnd_j = rndrange(42)
            line.append(rnd_j)

        matrix.append(line)

    pp_matrix(matrix)

    transpose_matrix = []

    for j in range(len(matrix[0])):
        line = []
        for i in range(len(matrix)):
            line.append(matrix[i][j])
        
        transpose_matrix.append(line)

    pp_matrix(transpose_matrix)


print_result(solution10)

    
def solution11():
    """
    11. В двумерном массиве отсортировать четные столбцы по возрастанию,
    а нечетные - по убыванию
    """
    rows = 5
    columns = 8
    
    matrix = []
    for i in range(rows):
        line = []
        for j in range(columns):
            rnd_j = rndrange(42)
            line.append(rnd_j)

        matrix.append(line)

    print("Original matrix")
    pp_matrix(matrix)
    
    tr_mx = transpose_matrix(matrix)
    for i in range(len(tr_mx)):
        if i % 2:
            tr_mx[i].sort()
        else:
            tr_mx[i].sort(reverse=True)

    sorted_matrix = transpose_matrix(tr_mx)
    print("----------")
    print("Sorted matrix")
    pp_matrix(sorted_matrix)


print_result(solution11)


def solution12():
    """
    12. Для проверки остаточных знаний учеников после летних каникул,
    учитель младших классов решил начинать каждый урок с того, чтобы
    задавать каждому ученику пример из таблицы умножения, но в классе
    15 человек, а примеры среди них не должны повторяться. В помощь
    учителю напишите программу, которая будет выводить на экран 15
    случайных примеров из таблицы умножения (от 2*2 до 9*9, потому
    что задания по умножению на 1 и на 10 — слишком просты).
    При этом среди 15 примеров не должно быть повторяющихся
    (примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)
    """

    multy_table = {}
    for i in range(2, 10):
        for j in range(2, 10):
            example = ("%i*%i" % (i, j))
            example_key = i*j
            multy_table[example_key] = example

    example_list = list(multy_table.values())
    teachers_help = set()

    while len(teachers_help) < 15:
        rnd_index = rndrange(len(example_list))
        teachers_help.add(example_list[rnd_index])

    print(teachers_help)


print_result(solution12)
